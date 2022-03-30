import websockets
import asyncio
import json


IP = "185.242.106.198"
PORT = 8080


async def handler(websocket):
    pass


async def main():
    async with websockets.serve(handler, IP, PORT):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())