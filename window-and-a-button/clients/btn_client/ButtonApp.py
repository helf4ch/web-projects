from ButtonFrame import ButtonFrame
from tkinter import Tk 
import websockets
import asyncio
import json


URL = "ws://185.242.106.198:8080"


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
            await websocket.send(json.dumps({ "from": "ButtonApp", "type": "changeImage" }))
        

def main():
    buttonApp = ButtonApp()
    buttonApp.mainloop()


if __name__ == "__main__":
    main()
        
