let catData = [];
const catNameInput = document.querySelector('input[aria-label="cat-name"]');
const catAgeInput = document.querySelector('input[aria-label="cat-age"]');
const catBreedInput = document.querySelector('select[aria-label="cat-breeds"]');

let msg = document.getElementById("msg");

// Load cat data from local storage
document.addEventListener('DOMContentLoaded', function () {
    if (localStorage.getItem('catData')) {
        catData = JSON.parse(localStorage.getItem('catData'));
        displayCatList();
    }
});

const searchForm = document.querySelector('.form-inline');
const searchInput = document.querySelector('.form-control');

searchForm.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission

    const searchText = searchInput.value.toLowerCase();
    const filteredCats = catData.filter(function (cat) {
        return cat.name.toLowerCase().includes(searchText);
    });
    displayCatList(filteredCats);

    searchInput.blur(); // Remove focus from the search input field
});

const submitButton = document.querySelector('button.btn-primary');
submitButton.addEventListener('click', function (event) {
    event.preventDefault(); // Prevent form submission

    const catName = catNameInput.value;
    const catAge = catAgeInput.value;
    const catBreed = catBreedInput.value;

    if (!catName || !catAge || !catBreed) {
        // Display tooltip indicating null data
        msg.textContent = 'Please fill in all fields';
        return;
    }

    const newCat = {
        name: catName,
        age: catAge,
        breed: catBreed
    };

    catData.push(newCat);
    saveCatDataToLocalStorage(); // Save cat data to local storage

    // Clear input fields
    catNameInput.value = '';
    catAgeInput.value = '';
    catBreedInput.value = '';
    msg.textContent = ''; // Clear error message

    displayCatList();
});

function saveCatDataToLocalStorage() {
    const filteredCats = searchBox.value ? catData.filter(function (cat) {
        return cat.name.toLowerCase().includes(searchBox.value.toLowerCase());
    }) : null;
    localStorage.setItem('catData', JSON.stringify(filteredCats || catData));
}


function displayCat(cat) {
    const catElement = document.createElement('div');
    catElement.classList.add('cat-item');

    const catNameElement = document.createElement('h4');
    catNameElement.textContent = cat.name;
    catElement.appendChild(catNameElement);

    const catAgeElement = document.createElement('p');
    if (cat.age > 1) {
        catAgeElement.textContent = `${cat.breed} - ${cat.age} months old`;
    } else {
        catAgeElement.textContent = `${cat.breed} - ${cat.age} month old`;
    }
    catElement.appendChild(catAgeElement);

    const editIcon = document.createElement('i');
    editIcon.classList.add('fas', 'fa-edit');
    editIcon.addEventListener('click', function () {
        editCat(cat);
    });
    catElement.appendChild(editIcon);

    const gapElement = document.createElement('span');
    gapElement.style.marginRight = '16px';
    catElement.appendChild(gapElement);

    const deleteIcon = document.createElement('i');
    deleteIcon.classList.add('fas', 'fa-trash-alt');
    deleteIcon.addEventListener('click', function () {
        deleteCat(cat);
    });
    catElement.appendChild(deleteIcon);

    const shownCat = document.getElementById('shownCat');
    shownCat.appendChild(catElement);
}

function displayCatList(filteredCats) {
    const shownCat = document.getElementById('shownCat');
    shownCat.innerHTML = ''; // Clear existing cat list

    const catsToDisplay = filteredCats || catData;

    catsToDisplay.forEach(function (cat) {
        displayCat(cat);
    });

    const displayFilter = document.getElementById('displayFilter');
    const searchResultCount = document.getElementById('searchResultCount');
    const searchText = searchInput.value;
    if (searchText) {
        displayFilter.textContent = 'Display search filter for: ' + searchText;
        searchResultCount.textContent = 'Search results: ' + catsToDisplay.length;
    } else {
        displayFilter.textContent = '';
        searchResultCount.textContent = '';
    }
}


function editCat(cat) {
    const catNameInput = document.getElementById('catName');
    const catAgeInput = document.getElementById('catAge');
    const catBreedInput = document.getElementById('catBreed');

    catNameInput.value = cat.name;
    catAgeInput.value = cat.age;
    catBreedInput.value = cat.breed;

    const saveChangesButton = document.getElementById('saveCatChanges');

    saveChangesButton.addEventListener('click', function () {
        const updatedName = catNameInput.value;
        const updatedAge = catAgeInput.value;
        const updatedBreed = catBreedInput.value;

        if (updatedName && updatedAge && updatedBreed) {
            cat.name = updatedName;
            cat.age = updatedAge;
            cat.breed = updatedBreed;

            saveCatDataToLocalStorage();
            displayCatList();

            showSuccessMessage();
            $('#editCatModal').modal('hide'); // Hide the modal
        } else {
            const msg = document.getElementById('msg');
            msg.textContent = 'Please fill in all fields';
        }
    });

    $('#editCatModal').modal('show'); // Show the modal
}

// Function to show success message
// Function to show success message
function showSuccessMessage() {
    const successMessage = document.createElement('div');
    successMessage.classList.add('alert', 'alert-success');
    successMessage.textContent = 'Cat data successfully updated';

    const modalBody = document.querySelector('.modal-body');
    modalBody.appendChild(successMessage);

    // Remove the success message after 3 seconds
    setTimeout(function () {
        modalBody.removeChild(successMessage);
    }, 3000);
}


function deleteCat(cat) {
    const index = catData.indexOf(cat);
    if (index > -1) {
        catData.splice(index, 1);
        saveCatDataToLocalStorage(); // Save cat data to local storage
        displayCatList();
    }
}

function deleteCatData() {
    deleteCookie('catData');
    localStorage.removeItem('catData');
}

function deleteCookie(cookieName) {
    document.cookie = cookieName + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
}

// Usage: Call deleteCatData() when the "Clear Cookie" button is clicked.
const clearCookiesButton = document.getElementById('clearCookies');
clearCookiesButton.addEventListener('click', function () {
    // Remove the catData cookie
    document.cookie = 'catData=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
    // Clear the catData records
    deleteCatData()
    catData = [];
    // Clear the displayed cat list
    displayCatList();
});