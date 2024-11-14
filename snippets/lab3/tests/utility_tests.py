from snippets.lab3.utility import *

def test_message():
    username="Username"
    message="Message"
    timestamp="01/01/2000 8:00AM"
    id=1
    m=Message(username, message, timestamp, id)
    m2=Message(username=username, message=message, timestamp=timestamp, id=2)
    print(m.id==id)
    print(m.message==message)
    print(m.timestamp==timestamp)
    print(m.id==id)
    print((m==m2)==False)
    print(m==m)

def test_messageList():
    username="Username"
    message="Message"
    timestamp="01/01/2000 8:00AM"
    id=1
    m=Message(username=username, message=message, timestamp=timestamp, id=id)
    ml=MessageList()
    print(ml.isMessagePresent(m.id)==False)
    print(ml.getMessage(m.id)==None)
    print(len(ml.getAllMessagesIds())==0)
    ml.addMessage(m)
    print(ml.isMessagePresent(m.id)==True)
    print(ml.getMessage(m.id)==m)
    print(len(ml.getAllMessagesIds())==1)
    m2=Message(username=username, message=message, timestamp=timestamp, id=2)
    print(ml.isMessagePresent(m2.id)==False)
    print(ml.getMessage(m2.id)==None)
    ml.addMessage(m2)
    print(ml.isMessagePresent(m2.id)==True)
    print(ml.getMessage(m2.id)==m2)
    print(len(ml.getAllMessagesIds())==2)

    

