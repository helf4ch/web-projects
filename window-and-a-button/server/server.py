import websockets
import asyncio
import json


IP = "185.242.106.198"
PORT = 8080


connected = set()


# jsons:
# requests:
# {
#       "from": "ButtonApp",
#       "type": "changeImage",
# }

# answers:
# {
#       "type": "changeImage",
# }


async def onChangeImage(websocket):
    for conn in connected:
        if connected != websocket:
            await conn.send(json.dumps( { "type": "changeImage" } ))


async def messageHandler(websocket, message_parsed):
    type = message_parsed["type"]
    
    if type == "changeImage":
        await onChangeImage(websocket)
    
    else:
        pass


def messageParse(message):
    return json.loads(message)


async def handler(websocket):
    print("A client just connected.")
    connected.add(websocket)
    try:
        async for message in websocket:
            await messageHandler(websocket, messageParse(message))
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected.")
    finally:
        connected.remove(websocket)



async def main():
    async with websockets.serve(handler, IP, PORT):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
