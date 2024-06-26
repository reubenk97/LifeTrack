const todoForm = document.querySelector('#todo-form');
const todoErrorField = document.querySelector('#todo-error-field');
const goalForm = document.querySelector('#goal-form');
const goalErrorField = document.querySelector('#goal-error-field');
const todosTable = document.querySelector('#todos-table');
const goalsTable = document.querySelector('#goals-table tbody');

function addTodo(event) {
    event.preventDefault();
    console.log('Attempting to add new Todo.');
    let todoFormData = new FormData(todoForm)
    fetch ('/todos/add', { method: 'post', body: todoFormData })
        .then(res => res.json())
        .then(data => {
            console.log(data)
            todoErrorField.innerHTML = ""
            if (data.hasOwnProperty('errors')) {
                console.log('errors found', data.errors)
                for (let error of data.errors){
                    todoErrorField.innerHTML += `<p class='text-danger'>${error}</p>`
                }
            } 
            else {
                let todoFillerRow = document.querySelector('#todo-filler-row')
                if (!todoFillerRow.classList.contains("d-none"))
                    todoFillerRow.classList.add("d-none")

                todosTable.innerHTML = `
                <tr>
                    <td>${data.title}</td>
                    <td>${data.date}</td>
                    <td><a onclick="showEditTodo()" class="link-underline link-underline-opacity-0 text-success">Edit</a> | <a href="todos/${data.id}/delete" class="link-underline link-underline-opacity-0 text-success">Delete</a></td>
                    <td><input type="checkbox" name="${data.title}-check" class="form-check-input"></td>
                </tr>
                ` + todosTable.innerHTML;
                todoForm.title.value = "";
                todoForm.description.value = "";
                todoForm.date.value = "";
                todoForm.location.value = "";
            }
        })
        .catch(err => console.log(err));
}

// Needs to be fixed after MVP
function editTodo(event, id) {
    event.preventDefault();
    console.log('Attempting to edit Todo.');
    const editTodoForm = document.querySelector('#edit-todo-form')
    const editTodoErrorField = document.querySelector('#edit-todo-error-field');
    let editTodoFormData = new FormData(editTodoForm)
    let thisRow = document.querySelector(`#${id}-row`)
    fetch (`/todos/${id}/edit`, { method: 'post', body: editTodoFormData })
        .then(res => res.json())
        .then(data => {
            console.log(data)
            editTodoErrorField.innerHTML = ""
            if (data.hasOwnProperty('errors')) {
                console.log('errors found', data.errors)
                for (let error of data.errors){
                    editTodoErrorField.innerHTML += `<p class='text-danger'>${error}</p>`
                }
            } 
            else {
                thisRow.innerHTML = `
                    <td>${data.title}</td>
                    <td>${data.date}</td>
                    <td><a onclick="showEdit()" class="link-underline link-underline-opacity-0 text-success">Edit</a> | <a href="todos/{{todo.id}}/delete" class="link-underline link-underline-opacity-0 text-success">Delete</a></td>
                    <td><input type="checkbox" name="{{ todo.title }}-check" class="form-check-input"></td>
                `;
                editTodoForm.title.value = "";
                editTodoForm.description.value = "";
                editTodoForm.date.value = "";
                editTodoForm.location.value = "";
            }
        })
        .catch(err => console.log(err));
}

function showAddTodo() {
    todoForm.classList.toggle("d-none");
}

// Needs to be fixed after MVP
function showEditTodo() {
    editTodoForm.classList.toggle("d-none");
}

function addGoal(event) {
    event.preventDefault();
    console.log('Attempting to add new Goal.');
    let goalFormData = new FormData(goalForm)
    fetch ('/goals/add', { method: 'post', body: goalFormData })
        .then(res => res.json())
        .then(data => {
            console.log(data)
            goalErrorField.innerHTML = ""
            if (data.hasOwnProperty('errors')) {
                console.log('errors found', data.errors)
                for (let error of data.errors){
                    goalErrorField.innerHTML += `<p class='text-danger'>${error}</p>`
                }
            } 
            else {
                let goalFillerRow = document.querySelector('#goal-filler-row')
                if (!goalFillerRow.classList.contains("d-none"))
                    goalFillerRow.classList.add("d-none")

                goalsTable.innerHTML = `
                <tr id="${data.id}-row">
                    <td>${data.title}</td>
                    <td>Progression: 0% </td>
                    <td><a onclick="showEditGoal()" class="link-underline link-underline-opacity-0 text-success">Edit</a> | <a href="goals/{{todo.id}}/delete" class="link-underline link-underline-opacity-0 text-success">Delete</a></td>
                    <td><input type="checkbox" name="${data.title}-check" class="form-check-input"></td>
                </tr>
                ` + goalsTable.innerHTML;
                goalForm.title.value = "";
                goalForm.description.value = "";
                goalForm.date.value = "";
                goalForm.location.value = "";
            }
        })
        .catch(err => console.log(err));
}

function editGoal() {

}

function showAddGoal() {
    goalForm.classList.toggle("d-none");
}

function showEditGoal() {

}