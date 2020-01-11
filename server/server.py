import eventlet
import socketio

sio = socketio.Server(async_mode='eventlet')
app = socketio.WSGIApp(sio)

@sio.on('message')
async def print_message(sid, message):
    print("Socket ID: " , sid)
    print(message)
    await sio.emit('message', message[::-1])

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)