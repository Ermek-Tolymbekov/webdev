let i = 0;
let tasks = document.getElementById('task_list');

document.getElementById('add').addEventListener('click',
function (){
    let task = document.getElementById('newtask').value;
    document.getElementById('newtask').value = "";
    let li = document.createElement('li');
    let task_id = 'task' + i;
    li.id = task_id;
    li.className = 'tasks';
    li.innerHTML = `
    <form>
        <input type="checkbox" id="check${i}" onclick=taskDone(${i})>
        <span id="txt${i}">${task}</span>
        <input type="button" id="deleteButton" onclick = deleteTask(${task_id}) value="Delete">
    <form>
    `
    tasks.appendChild(li); 
    i++;
});

function deleteTask(task){
    task.parentNode.removeChild(task);
}

function taskDone(id){
    let checkBox = document.getElementById('check'+id);
    let task = document.getElementById('txt'+id);
    if(checkBox.checked == true){
        task.style.textDecoration = 'line-through';
    } else{
        task.style.textDecoration = 'none';
    }
}