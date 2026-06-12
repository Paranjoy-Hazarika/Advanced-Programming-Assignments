# Assignment 5: []

Live Demo: https://csb24017-todo-app.netlify.app/

## 1. Features — bullet list of what it does:

Add and delete tasks
Mark tasks as complete with a checkbox
Long task names truncate with ... (hover to see full text)
Tasks persist on page refresh via localStorage

## 2. Tech used

React (Vite)
CSS (no libraries)

## 3. How to run locally
```bash
git clone <repo-url>
git checkout <branch-name>
npm install
npm run dev
```

## 4. Brief explanation of key decisions — this is what makes it stand out for grading. One short paragraph, e.g.:

Tasks are stored as objects { text, done } rather than plain strings to support the toggle feature. localStorage is synced via useEffect so state persists across sessions.