import websockets
import asyncio
import json


IP = "localhost" # args parser 
PORT = 80


connected = {}

# connected:
# {
#       websocket:
#           {
#               "type": "ButtonApp" / "ImageApp"
#           }
# }


# jsons:
# requests:
# {
#       "from": "ButtonApp" / "ImageApp",
#       "type": "connect",
# }

# {
#       "from": "ButtonApp",
#       "type": "changeImage",
# }

# answers:
# {
#       "type": "changeImage",
# }


async def onConnect(websocket, type):
    connected[websocket]["type"] = type


async def onChangeImage(websocket):
    async for conn in connected[websocket]:
        if conn["type"] == "ImageApp":
            await conn.send(json.dumps( { "type": "changeImage" } ))


async def messageHandler(websocket, message_parsed):
    type = message_parsed["type"]
    
    if type == "connect":
        await onConnect(websocket, message_parsed["from"])
    
    elif type == "changeImage":
        await onChangeImage(websocket)
    
    else:
        pass


async def messageParse(message):
    return json.loads(message)


async def handler(websocket):
    print("A client just connected.")
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
