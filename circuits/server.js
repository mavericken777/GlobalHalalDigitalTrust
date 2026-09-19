const http = require("http");
const server = http.createServer((req, res) => {
  res.setHeader("content-type", "application/json");
  if (req.url === "/health") {
    res.end(JSON.stringify({ status: "SPEC_ONLY", compiled: false, proving: false }));
    return;
  }
  res.statusCode = 501;
  res.end(JSON.stringify({ error: "zkp_not_implemented", verified: false }));
});
server.listen(5005, "0.0.0.0");
