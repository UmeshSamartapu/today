const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const app = express();
const PORT = 3000;

app.use(cors());
app.use(bodyParser.json());

let students = [
  { id: 1, name: "Alice", course: "Computer Science" },
  { id: 2, name: "Bob", course: "Mechanical Engineering" },
  { id: 3, name: "Charlie", course: "Electrical Engineering" }
];

app.get('/students', (req, res) => {
  res.json(students);
});

app.post('/students', (req, res) => {
  const newStudent = req.body;
  newStudent.id = students.length + 1;
  students.push(newStudent);
  res.json({ message: "Student added successfully!", students });
});

app.delete('/students/:id', (req, res) => {
  const studentId = parseInt(req.params.id);
  students = students.filter(student => student.id !== studentId);
  res.json({ message: "Student deleted successfully!", students });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
