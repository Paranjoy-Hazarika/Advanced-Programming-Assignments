# Assignment 8: [Course Enrollment Dashboard]

This branch contains the solutions for the assignment 8.

## Problem Statement
Develop a course enrollment dashboard in reactjs:

You are building a React component that displays enrolled students.

Each student:
{
  id: number,
  name: string,
  enrolledCourses: Set<string>,
  gpa: number
}

You must: 

1. Maintain students in state.

2. Implement the following features:
a. Add new student
b. Remove student by ID
c. Display students sorted by GPA (descending)
d. Display all unique courses across students
e. Filter students enrolled in a specific course

3. Use the followings
a. Use useState
b. Use Map internally for id to student mapping
c. Use Set for course uniqueness
d. Use map, filter, and reduce
e. Do not mutate state directly
f. Use spread operator for updates
g. Convert Set to array before rendering

4. Compute time complexity of filtering students by course

**🔗 Live Demo**: https://csb24017-todo-app.netlify.app/

## Time Complexity: Filtering by Course

Filtering students by course is **O(n)** where n is the number of students.

Each student's `enrolledCourses` is a `Set`, so the `.has()` lookup is O(1).
This makes the overall filter linear — we check each student once.

## Features
- Add a new student via a modal form (ID, name, courses, CGPA)
- Remove a student by ID
- Students are sorted by GPA in descending order
- Filter students by course name (case-insensitive)
- Sidebar displays all unique courses across all students

## Tech Used
- React (Vite)
- CSS (no libraries)

## How to run locally
```bash
git clone https://github.com/Paranjoy-Hazarika/Advanced-Programming-Assignments.git
git checkout assignment-8

npm install
npm run dev
```
 
## Key Decisions
Students are stored in a `Map` (id → student object) in state, with courses stored as a `Set` per student. A new `Map` is created on every update to avoid direct state mutation. `reduce` is used to compute unique courses across all students, and `Set` lookup makes course filtering O(1) per student, giving an overall filter time complexity of **O(n)** where n is the number of students.