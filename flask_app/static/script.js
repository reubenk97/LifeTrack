const todoForm = document.querySelector('#todo-form');
const errorField = document.querySelector('#error-field');
const todosTable = document.querySelector('#todos-table');

function addTodo(event) {
    event.preventDefault();
    console.log('Attempting to add new Todo.');
    let todoFormData = new FormData(todoForm)
    fetch ('/todos/add', { method: 'post', body: todoFormData })
        .then(res => res.json())
        .then(data => {
            console.log(data)
            errorField.innerHTML = ""
            if (data.hasOwnProperty('errors')) {
                console.log('errors found', data.errors)
                for (let error of data.errors){
                    errorField.innerHTML += `<p class='text-danger'>${error}</p>`
                }
            } 
            else {
                todosTable.innerHTML += `
                <tr>
                    <td>${data.title}</td>
                    <td>${data.date}</td>
                    <td><a>Edit</a> | <a>Delete</a></td>
                </tr>
                `;
                todoForm.title.value = "";
                todoForm.description.value = "";
                todoForm.date.value = "";
                todoForm.location.value = "";
            }
        })
        .catch(err => console.log(err));
}