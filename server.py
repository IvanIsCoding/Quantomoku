from aiohttp import web
import socketio
from quantomoku import process_board

sio = socketio.AsyncServer(cors_allowed_origins="*")
app = web.Application()
sio.attach(app)


@sio.on("message")
async def process_message(sid, message):
    print("Message received by Socket ID: ", sid)
    answer = process_board(message)
    await sio.emit("message", answer)


# Start server
if __name__ == "__main__":
    web.run_app(app, port=8000)
