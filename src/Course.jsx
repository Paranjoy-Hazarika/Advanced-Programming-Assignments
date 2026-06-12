import React, { useState } from "react";
import './Course.css'

function EnrollmentDashboard() {
  const [showModal, setShowModal] = useState(false);

  const [students, setStudents] = useState(new Map());

  const [filterCourse, setFilterCourse] = useState("");

  const [newStudent, setNewStudent] = useState({
    id: "",
    name: "",
    courses: "",
    gpa: ""
  });

  const addStudent = () => {
    if (!newStudent.id || !newStudent.name || !newStudent.gpa) return;

    const courseSet = new Set(
      newStudent.courses.split(",").map(c => c.trim())
    );

    const student = {
      id: Number(newStudent.id),
      name: newStudent.name,
      enrolledCourses: courseSet,
      gpa: Number(newStudent.gpa)
    };

    const newMap = new Map(students);

    newMap.set(student.id, student);
    
    setStudents(newMap);
    setNewStudent({ id: "", name: "", courses: "", gpa: "" });
  };

  const removeStudent = (id) => {
    const newMap = new Map(students);

    newMap.delete(id);
    setStudents(newMap);
  };

  const studentArray = [...students.values()];
  const sortedStudents = [...studentArray].sort(
    (a, b) => b.gpa - a.gpa
  );

  const uniqueCourses = studentArray.reduce((acc, student) => {
    student.enrolledCourses.forEach(course => acc.add(course));

    return acc;
  }, new Set());

  const filteredStudents = filterCourse
    ? sortedStudents.filter(student =>
        [...student.enrolledCourses].some(c =>
          c.toLowerCase() === filterCourse.toLowerCase()
        )
      )
    : sortedStudents;

  return (
    <div className="dashboard">
      <h2 id="main-heading">Course Enrollment Dashboard</h2>
      <div className="header-row">
        <input
          placeholder="Filter by course"
          value={filterCourse}
          onChange={e => setFilterCourse(e.target.value)}
        />

        <button onClick={() => setShowModal(true)}>
          Add Student
        </button>
      </div>

      {showModal && (
        <div className="modal-overlay">
          <dialog open className="modal">
            <h3>Add Student</h3>
            <div className="inputFields">

              <input
                placeholder="ID"
                value={newStudent.id}
                onChange={e =>
                  setNewStudent({ ...newStudent, id: e.target.value })
                }
              />

              <input
                placeholder="Name"
                value={newStudent.name}
                onChange={e =>
                  setNewStudent({ ...newStudent, name: e.target.value })
                }
              />

              <input
                placeholder="Courses (comma separated)"
                value={newStudent.courses}
                onChange={e =>
                  setNewStudent({ ...newStudent, courses: e.target.value })
                }
              />

              <input
                placeholder="CGPA"
                value={newStudent.gpa}
                onChange={e =>
                  setNewStudent({ ...newStudent, gpa: e.target.value })
                }
              />

              <div className="modal-buttons">
                <button
                  onClick={() => {
                    addStudent();
                    setShowModal(false);
                  }}
                >
                  Add Student
                </button>

                <button onClick={() => setShowModal(false)}>
                  Cancel
                </button>
              </div>
            </div>
          </dialog>
        </div>
      )}

      <div className="main-content">
        <div className="students-section">
          <h3>Students (Sorted by GPA)</h3>
          <div className="students-grid">

            {filteredStudents.map(student => (
              <div key={student.id} className="student-card">

                <div className="card-content">
                  <h4>{student.name}</h4>
                  <hr />

                  <p>ID: {student.id}</p>
                  <p>CGPA: {student.gpa}</p>

                  <p>Courses:</p>

                  <ul>
                    {[...student.enrolledCourses].map((course, i) => (
                      <li key={i}>{course}</li>
                    ))}
                  </ul>
                </div>

                <button onClick={() => removeStudent(student.id)}>
                  Remove
                </button>

              </div>
            ))}
          </div>
        </div>

        <div className="courses-sidebar">
          <h3>Unique Courses</h3>
          <ul>
            {[...uniqueCourses].map((course, index) => (
              <li key={index}>{course}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default EnrollmentDashboard