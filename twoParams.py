import gtts
from playsound import playsound

def say_greeting(greeting, name):
    spoken_name = gtts.gTTS(f"{greeting}, {name}, Nice to meet you")
    spoken_name.save("hello.mp3")
    playsound("hello.mp3")

def main():
    your_name = input("What is your name")
    greet = "How’s it going"
    say_greeting(greet, your_name)

main()