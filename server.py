from aiohttp import web
import socketio
from quantomoku import process_board
sio = socketio.AsyncServer(cors_allowed_origins="*")
app = web.Application()
sio.attach(app)

@sio.on('message')
async def print_message(sid, message):
    # When we receive a new event of type
    # 'message' through a socket.io connection
    # we print the socket ID and the message
    print("Socket ID: " , sid)
    print("Message {}".format(message))
    stuff= process_board(message)
    print("Stuff {}".format(stuff))
    #do things with stuff
    await sio.emit('message', stuff)

# We bind our aiohttp endpoint to our app
# router
#app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app, port=8000)