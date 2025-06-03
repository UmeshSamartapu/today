const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// Middleware to parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

// Dummy user for authentication
const user = {
  username: 'admin',
  password: 'password123'
};

// Serve login form
app.get('/', (req, res) => {
  res.send(`
    <form method="POST" action="/login">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required>
      <br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required>
      <br>
      <button type="submit">Login</button>
    </form>
  `);
});

// Handle login
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  // Basic credential check
  if (username === user.username && password === user.password) {
    res.send(`<h2>Welcome, ${username}!</h2>`);
  } else {
    res.send('<h2>Invalid username or password. Try again!</h2>');
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
