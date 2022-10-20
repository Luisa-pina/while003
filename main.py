import gtts
from playsound import playsound
said_the_right_thing = False
while not said_the_right_thing:
    question = input("Won't you take me with you")
    good_answers = ["yes", "ok", "yeah", "yup", "fine", "YES"]
    if question.lower() in good_answers:
        said_the_right_thing = True

celebrate = "Hooray, You will take me with you today! and forever"
speaker = gtts.gTTS(celebrate)
speaker.save("speech1.mp3")
playsound("speech1.mp3")
creepy = "and ever!"
speaker2 = gtts.gTTS(creepy)
speaker2.save("creepy.mp3")
for repeat in range(10):
    playsound("creepy.mp3")
