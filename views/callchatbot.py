#load_models()
from chatbot import requested


def chat_response_message(msg):
    #done = False
    #while not done:
    #message = input("Enter a message: ")
    #if message == "STOP" or message =="stop" or message =="end" or message =="END" or message =="BYE" :
    #    done = True
    #else:
    #print(requested(message))
    resp = requested(msg)
    #print(resp)
    return resp