class BotId:

    def __init__(self,message):
        self.message=message
        global content
        self.content=self.message.content.lower()

    