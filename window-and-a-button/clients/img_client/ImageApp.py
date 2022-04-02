from tkinter import Tk
import threading
import websockets
import asyncio
import json
import argparse

from ImageFrame import ImageFrame
from SetupWindow import SetupWindow

parser = argparse.ArgumentParser()

parser.add_argument("--ip", default="127.0.0.1")
parser.add_argument("--port", default=80)

args = parser.parse_args()

URL = "ws://" + args.ip + ":" + f"{args.port}"


class ImageApp(Tk):

    def __init__(self, filepaths):
        super().__init__()
        self.title("Image App")
        self.initUI(filepaths)
        self.recieveThreadOpen()

    def initUI(self, filepaths):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.imageFrame = ImageFrame(self, filepaths[0], filepaths[1])
        self.imageFrame.grid(row=0, column=0, padx=5, pady=5)

    def recieveThreadOpen(self):
        self.send = threading.Thread(target=self.runRecieveMessage)
        self.send.start()

    def runRecieveMessage(self):
        asyncio.run(self.recieveMessage())

    async def recieveMessage(self):
        async with websockets.connect(URL) as websocket:
            while True:
                message = await websocket.recv()

                if json.loads(message) == {"type": "changeImage"}:
                    self.imageFrame.changeImage()
                else:
                    pass


def main():
    setupWindow = SetupWindow()
    setupWindow.mainloop()

    imageApp = ImageApp(setupWindow.getImagesPaths())
    imageApp.mainloop()


if __name__ == "__main__":
    main()
