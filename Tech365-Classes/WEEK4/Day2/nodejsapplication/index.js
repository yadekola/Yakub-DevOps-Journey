const express = require("express");

const app = express();

app.use(express.json());

const PORT = process.env.PORT || 3000;

let students = [
  {
    id: 1,
    name: "Wale Olajumoke",
    course: "DevOps Engineering",
  },
  {
    id: 2,
    name: "Sarah James",
    course: "Data Engineering",
  },
];

// Home
app.get("/", (req, res) => {
  res.json({
    message: "Welcome to the Student API",
    environment: process.env.NODE_ENV || "development",
  });
});

// Health check
app.get("/health", (req, res) => {
  res.json({
    status: "healthy",
  });
});

// Get all students
app.get("/students", (req, res) => {
  res.json(students);
});

// Get one student
app.get("/students/:id", (req, res) => {
  const student = students.find((s) => s.id === parseInt(req.params.id));

  if (!student) {
    return res.status(404).json({
      message: "Student not found",
    });
  }

  res.json(student);
});

// Create student
app.post("/students", (req, res) => {
  const student = {
    id: students.length + 1,
    name: req.body.name,
    course: req.body.course,
  };

  students.push(student);

  res.status(201).json(student);
});

// Delete student
app.delete("/students/:id", (req, res) => {
  const id = parseInt(req.params.id);

  students = students.filter((student) => student.id !== id);

  res.json({
    message: "Student deleted",
  });
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Student API running on port ${PORT}`);
});
