
class Message:
    def __init__(self, username:str, message:str, timestamp, id:str):
        self.id=id
        self.username=username
        self.message=message
        self.timestamp=timestamp
        pass
    
    def __str__(self):
        return f"{self.username}: {self.message} ({self.timestamp})"
    
    def __eq__(self, other):
        if not isinstance(other, Message):
            return False
        else:
            return self.id==other.id and self.message==other.message and self.timestamp==other.timestamp and self.username==other.username
    
class MessageList:
    def __init__(self):
        self.__dict={}
        pass

    def addMessage(self, message: Message):
        self.__dict.__setitem__(message.id, message)
        return
    
    def getMessage(self, messageId:str)->Message:
        return self.__dict.get(messageId)
    
    def isMessagePresent(self, messageId:str)->bool:
        if messageId in self.__dict:
            return True
        else:
            return False
        
    def getAllMessagesIds(self):
        return self.__dict.keys()
    

