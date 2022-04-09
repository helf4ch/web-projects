import websockets
import asyncio
import json
import argparse

from ButtonFrame import ButtonFrame
from tkinter import Tk

parser = argparse.ArgumentParser()

parser.add_argument("--ip", default="127.0.0.1")
parser.add_argument("--port", default=80)

args = parser.parse_args()

URL = "ws://" + args.ip + ":" + f"{args.port}"


class ButtonApp(Tk):

    def __init__(self):
        super().__init__()
        self.title("Button App")
        self.initUI()

    def initUI(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        button = ButtonFrame(self, self.runSendMessage)
        button.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

    def runSendMessage(self):
        asyncio.run(self.sendMessage())

    async def sendMessage(self):
        async with websockets.connect(URL) as websocket:
            await websocket.send(
                json.dumps({
                    "from": "ButtonApp",
                    "type": "changeImage"
                }))


def main():
    buttonApp = ButtonApp()
    buttonApp.mainloop()


if __name__ == "__main__":
    main()
