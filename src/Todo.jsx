import { useState, useEffect } from 'react'
import TrashIcon from './assets/trash-can-regular-full.svg'
import PlusIcon from './assets/plus-solid-full.svg'

import './Todo.css'

function Todo() {
  const [tasks, setTasks] = useState(() => {
    const saved = localStorage.getItem('tasks');
    return saved ? JSON.parse(saved) : [];
  });

  useEffect(() => {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  }, [tasks]);

  function addTask(e) {
    e.preventDefault();
    const input = e.target.elements.taskInput.value;
    if (input.trim() === "") return;
    setTasks([...tasks, { text: input, done: false }]);
    e.target.elements.taskInput.value = "";
  }

  function toggleTask(index) {
    setTasks(tasks.map((task, i) =>
      i === index ? { ...task, done: !task.done } : task
    ));
  }

  function deleteTask(index) {
    setTasks(tasks.filter((_, i) => i !== index));
  }

  return (
    <div className="container">
      <h1 className="header">To-Do List</h1>
      <form onSubmit={addTask} className="todo-form">
        <input type="text" name="taskInput" placeholder="Enter your task..." />
        <button type="submit">
          <img src={PlusIcon} alt="add-icon" id='plus-icon'/>
          <span className='extra-text'>Add</span>
        </button>
      </form>

    {tasks.map((task, i) => (
      <div key={i} className={`task ${task.done ? 'done' : ''}`}>
        <p>
          <span className='id-num'>{i + 1}</span>
          <input type="checkbox" checked={task.done} onChange={() => toggleTask(i)} />
          <span className='inp-task' title={task.text}>{task.text}</span>
        </p>
        <button onClick={() => deleteTask(i)}>
          <img src={TrashIcon} alt='delete' id='trash-can'/>
          <span className='extra-text'>Del</span>
        </button>
      </div>
    ))}
    </div>
  );
}

export default Todo