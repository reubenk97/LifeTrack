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
    let mapSearch = document.querySelector('#map-search');
    let formAddress = document.querySelector('#address-on-form');
    let googleAddress = document.querySelector('iframe html body div#mapDiv.address')
    fetch(`/lifetrack/search/${mapSearch.value}`)
        .then(res => res.json())
        .then(data => {
            console.log(googleAddress.innerHTML);
            location.reload();
            formAddress.value = googleAddress.innerHTML;
        })
        .catch(err => console.log(err));
}