const http = require('http');
const url = require('url');

const server = http.createServer((req, res) => {
  const queryObject = url.parse(req.url, true).query;
  const name = queryObject.name || 'Guest';
  const age = queryObject.age || 'Not provided';

  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end(`<h2>Hello, ${name}!</h2><p>Age: ${age}</p>`);
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
