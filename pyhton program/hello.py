print("Namaste! Welcome to your chatbot")
print("you can ask me basic question, Type 'bye' to exit from the bot")


responses ={
    "hello":" Hi, welcome. How can I help you?",
    "how are you":"I am very fine. Thank you",
    "who are you":"I am smart AI chatbot",
    "motivate me":"Keep going. Evary bug of youur project makes you a better developer",
    "happy":"Great to hear that",
}


def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    
    return "I am not able to tell that yet. Mai Jaldi hi ye sikh lunga"

while True:
    userInput=input("please ask your question:")
    reply= getResponseOfBot(userInput)
    print("Bot Responce :",reply)

    if "bye" in userInput.lower():
        break

 


        
    