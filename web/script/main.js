let catData = [];
const catNameInput = document.querySelector('input[aria-label="cat-name"]');
const catAgeInput = document.querySelector('input[aria-label="cat-age"]');
const catBreedInput = document.querySelector('select[aria-label="cat-breeds"]');

let msg = document.getElementById("msg");

// Load cat data from local storage
if (localStorage.getItem('catData')) {
    catData = JSON.parse(localStorage.getItem('catData'));
    displayCatList();
}

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

    displayCat(newCat);
});

function saveCatDataToLocalStorage() {
    localStorage.setItem('catData', JSON.stringify(catData));
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

function displayCatList() {
    const shownCat = document.getElementById('shownCat');
    shownCat.innerHTML = ''; // Clear existing cat list

    catData.forEach(function (cat) {
        displayCat(cat);
    });
}

function editCat(cat) {
    const updatedName = prompt('Enter the updated cat name:', cat.name);
    const updatedAge = prompt('Enter the updated cat age:', cat.age);
    const updatedBreed = prompt('Please select cats breed:', cat.breed);
    if (updatedName && updatedAge && updatedBreed) {
        cat.name = updatedName;
        cat.age = updatedAge;
        cat.breed = updatedBreed;

        saveCatDataToLocalStorage(); // Save cat data to local storage
        displayCatList();
    } else {
        // Display tooltip indicating null data
        msg.textContent = 'Please fill in all fields';
    }
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