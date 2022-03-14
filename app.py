#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
app = Flask(__name__,template_folder = 'templates')
#create chatbot
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
chatbot = ChatBot("Always")
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english") #train the chatter bot for english
conversation = [
    "Hi mona",
    "Hi Srushu. I love you.",
    "Will I be able to do it?",
    "You are the most amazing girl I have ever met and you can definitely do it.",
    "What if something wrong happens?",
    "You just have to learn from the mistakes and keep pushing forward like you always have. You are an inspiration, definitely stronger than this.",
    "I just dont want to talk to anyone",
    "Then dont talk to anyone. You deserve some privacy and you should take it.",
    "I miss you",
    "I miss you too",
    "Read me a note from 9 mar",
    "It read : We had a very heavy convo today. You cried because you were afraid of what will happen in the future, afraid of hurting me eventually, but trust me honey, we should not worry about the future when we dont need to. Let me have my hope, let me give it all, whatever happens, happens. I love you.",
    "Am I looking good?",
    "Ofcourse, you are absolutely gorgeous srushaa. You are my Andromeda, and I can stare at you without getting tired, or bored, because it probably is the best view in this entire world, or even afar.",
    "What about 5 mar?",
    "Let me give you a memory that you hopefully wont forget, ever. Now Long Way Home will make sense to me. I guess this is what it feels like. Nasik Shebang checked."
   
    
]
trainer = ListTrainer(chatbot)

trainer.train(conversation)
trainer.train(conversation)
trainer.train(conversation)
trainer.train(conversation)
trainer.train(conversation)
trainer.train(conversation)
trainer.train(conversation)
trainer.train(conversation)
#define app routes
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))

if __name__ == "__main__":
    app.run()
