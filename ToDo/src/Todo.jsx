import { useState } from 'react'
import './Todo.css'

function Todo() {
  const [tasks, setTasks] = useState([]);

  function addTask(e) {
    e.preventDefault();

    const input = e.target.elements.taskInput.value;
    if (input.trim() === "") return;
    
    setTasks([...tasks, input]);
    e.target.elements.taskInput.value = "";
  }

  function deleteTask(index) {
    setTasks(tasks.filter((_, i) => i !== index));
  }

  return (
    <div className="container">
      <h1 className="header">To-Do List</h1>
      <form onSubmit={addTask} className="todo-form">
        <input type="text" name="taskInput" placeholder="Enter your task..." />
        <button type="submit">Add</button>
      </form>

    {tasks.map((task, i) => (
      <div key={i} className="task">
        <p>{i+1}. {task}</p>
        <button onClick={() => deleteTask(i)}>Del</button>
      </div>
    ))}
    </div>
  );
}

export default Todo
