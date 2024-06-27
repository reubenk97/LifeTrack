const currAddress = document.querySelector('.address')
const addCategoryForm = document.querySelector('#add-category-form')
const addCategoryErrorField = document.querySelector('#add-cat-error-field')
const categoryList = document.querySelector('#category-list')

function addCategory(event) {
    event.preventDefault();
    console.log('Attempting to add new Activity.');
    let categoryFormData = new FormData(addCategoryForm)
    fetch ('/categories/add', { method: 'post', body: categoryFormData })
    .then(res => res.json())
    .then(data => {
        console.log(data)
        addCategoryErrorField.innerHTML = ""
        if (data.hasOwnProperty('errors')) {
            console.log('errors found', data.errors)
            for (let error of data.errors){
                addCategoryErrorField.innerHTML += `<p class='text-danger'>${error}</p>`
            }
        } 
        else {
            categoryList.innerHTML += `
            <div class="d-flex justify-content-between border rounded py-3 px-5 mb-3">
            <h6>${data.title}</h6>
            <h6>Edit</h6>
            </div>
            `;
            addCategoryForm.title.value = "";
        }
    })
    .catch(err => console.log(err));
}

function getAddress(event) {
    event.preventDefault()
    console.log('Searching API...');
    let mapSearch = document.querySelector('#map-search')
    let mapArea = document.querySelector('iframe')
    // mapArea.src = `/https://www.google.com/maps/embed/v1/place?key=${key}&q=${mapSearch}`;
    fetch(`/lifetrack/search/${mapSearch.value}`)
        .then(res => res.json())
        .then(data => {
            location.reload();
            console.log(data);
        })
        .catch(err => console.log(err))
}

// let mapSearch = document.querySelector('#map-search')
// mapSearch.addEventListener("keypress", function(event) {
//     // If the user presses the "Enter" key on the keyboard
//     if (event.key === "Enter") {
//       // Cancel the default action, if needed
//       event.preventDefault();
//       // Trigger the button element with a click
//       document.getElementById("myBtn").click();
//     }
//   });