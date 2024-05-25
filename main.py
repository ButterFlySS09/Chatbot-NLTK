from nlp_pipeline.chatbot import chatbot
import numpy as np

class ChatBot():
  def __init__(self):
    print(" Warming up ")

  # Sets Name of chatbot
  def set_name(self, name):
    self.name = name

  # Retuens Name of chatbot
  def get_name(self):
    return self.name

  # Returns NLP response
  def chat(self, text):
    chat = chatbot(text)
    return chat


if __name__ == "__main__":
  ai = ChatBot()

  while True:
    print("Do you want to chat with me?")
    action = int(input("(1 to chat) \nMe -> "))

    # User chooses to chat
    if action == 1:
      inp = input("AI -> What do you want to call me?\nMe -> ")
      ai.set_name(name=inp)
      print("AI -> Great what's on your mind?")
      while True:
        inp = input("Me ->")
        if any(i in inp for i in ["quit", "exit", "close", "shut down", "bye"]):
          break
        elif any(i in inp for i in ["your name", "who are you"]):
          print("AI -> I'm " + ai.get_name())
        else:
          output = ai.chat(inp)
          print("AI ->", output)

    # Exit program
    else:
      break

  res = np.random.choice(["Tata", "Have a good day", "Bye", "Goodbye", "Hope to meet soon", "peace out!"])
  ai.text_to_speech(res)
