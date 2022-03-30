import websockets
import asyncio
import json


IP = "localhost" # args parser 
PORT = 8080


connected = {}

# connected:
# {
#       websocket:
#           {
#               "type": "ButtonApp" / "ImageApp"
#               "status": "onRoomList" / "inRoom" 
#               "roomName": "roomName"
#           }
# }


def getNewConnection():
    return { "type": None, "status": None, "roomName": None }


rooms = {} 

# rooms:
# { 
#       "roomName":  
#           {
#               "capacity": 3,
#               "usersIn": 0,
#               "buttonApps":
#                   [
#                       websocket
#                   ],
#               "imageApps":
#                   [
#                       websocket
#                   ],
#           }, 
# }


def getNewRoom():
    return { "capacity": 0, "usersIn": 0, "buttonApps": [], "imageApps": [] }


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


# {
#       "from": "ButtonApp" / "ImageApp",
#       "type": "createRoom",
#       "info": 
#           {
#               "roomName": "name",
#               "capacity": 2
#           },
# }


# {
#       "from": "ButtonApp" / "ImageApp",
#       "type": "joinRoom",
#       "info": 
#           {
#               "roomName": "name",
#           },
# }


# answers:
# {
#       "type": "changeImage",
# }


# {
#       "type": "updateRoomList",
#       "roomList": 
#           [
#               "roomName" ...
#           ],
# }


async def updateRoomList():
    answer = { "type": "updateRoomList", "roomList": rooms }
    async for conn in connected:
        if conn["status"] == "onRoomList":
            await conn.send(json.dumps(answer))


# errors:
# {
#       "type": "error",
#       "error": "Room already exists." / "Room doesn't exist." / "Room is already full.",
# }


async def onConnect(websocket, type):
    connected[websocket] = getNewConnection()
    connected[websocket]["type"] = type
    connected[websocket]["status"] = "onRoomList"
    await updateRoomList()


async def onChangeImage(websocket):
    async for conn in rooms[connected[websocket]["roomName"]]["imageApps"]:
        await conn.send(json.dumps( { "type": "changeImage" } ))


async def onCreateRoom(websocket, info):
    if rooms.get(info["roomName"]) != None:
        await websocket.send(json.dumps( { "error": "Room already exists." } ))
        return
    
    rooms[info["roomName"]] = getNewRoom()
    rooms[info["roomName"]]["capacity"] = info["capacity"]
    await updateRoomList()


async def onJoinRoom(websocket, type, info):
    if rooms.get(info["roomName"]) == None:
        await websocket.send(json.dumps( { "error": "Room doesn't exist." } ))
        return
        
    if rooms[info["roomName"]]["usersIn"] >= rooms[info["roomName"]]["capacity"]:
        await websocket.send(json.dumps( { "error": "Room is already full." } ))
        return
        
    connected[websocket]["status"] = "inRoom"
    connected[websocket]["roomName"] = "roomName"
    
    rooms[info["roomName"]]["usersIn"] += 1
    if type == "ButtonApp":
        rooms[info["roomName"]]["ButtonApp"].append(type)
    
    else:
        rooms[info["roomName"]]["ImageApp"].append(type)


async def messageHandler(websocket, message_parsed):
    type = message_parsed["type"]
    
    if type == "connect":
        await onConnect(websocket, message_parsed["from"])
    
    elif type == "changeImage":
        await onChangeImage()
    
    elif type == "createRoom":
        await onCreateRoom(websocket, message_parsed["info"])
    
    elif type == "joinRoom":
        await onJoinRoom(websocket, message_parsed["from"], message_parsed["info"])
    
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
