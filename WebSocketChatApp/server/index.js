import { createServer } from "http"
import { Server } from "socket.io"

const myServer = createServer()

const io = new Server(myServer, {
  cors: {
    origin: process.env.NODE_ENV === "production" ? false : ["http://localhost:5500","http://127.0.0.1:5500"]
  }
})

io.on('connection', socket => {
  console.log(`USER ${socket.id} CONNECTED`)
  socket.on('message', data => {
    console.log(data)
    io.emit('message', `${socket.id.substring(0,5)}: ${data}`)
  })
})

myServer.listen(3500, () => {console.log("listening on port 3500")})