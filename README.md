# Assignment 5: [To-Do List]

This branch contains the solutions for the assignment 5.

## Problem Statement
Create a simple React component that maintains a list of todos using useState.
Allow the user to add a todo and display all added todos on the screen.

**🔗 Live Demo**: https://csb24017-todo-app.netlify.app/

## Features — bullet list of what it does:

- Add and delete tasks
- Mark tasks as complete with a checkbox
- Long task names truncate with ... (hover to see full text)
- Tasks persist on page refresh via localStorage

## Tech used

- React (Vite)
- CSS (no libraries)

## How to run locally
```bash
git clone https://github.com/Paranjoy-Hazarika/Advanced-Programming-Assignments.git
git checkout assignment-5

npm install
npm run dev
```

## Key Decision

Tasks are stored as objects { text, done } rather than plain strings to support the toggle feature. localStorage is synced via useEffect so state persists across sessions.