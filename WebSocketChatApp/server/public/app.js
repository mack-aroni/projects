const socket = io('ws://localhost:3500')

// sends message over socket
function sendMessage(e) {
  e.preventDefault()
  const input = document.querySelector('input')
  if (input.value) {
    socket.emit('message', input.value)
    input.value = ""
  }
  input.focus()
}

document.querySelector('form').addEventListener('submit', sendMessage)

// listen for message over sockets
socket.on('message', (data) => {
  const li = document.createElement('li')
  li.textContent = data
  document.querySelector('ul').appendChild(li)
})