const http = require('http');

const PORT = 3000;

const server = http.createServer((req, res) => {
  // Set response headers for HTML content
  res.writeHead(200, { 'Content-Type': 'text/html' });
  
  // Send the Hello World markup
  res.end('<h1>Hello World!</h1>');
});

server.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
