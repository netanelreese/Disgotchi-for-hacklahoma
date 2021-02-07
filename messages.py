class M_handler:

    def __init__(self,message):
        self.message=message
        global content
        self.content=self.message.content.lower()


    async def send(self,content):
        print("sending")
        await self.message.channel.send(content)
        print("sent")
