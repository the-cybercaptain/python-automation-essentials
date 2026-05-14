import pyttsx3 as py

names =[]

while True:
    name = input("Enter your name or quit to exit: ")

    if name.lower() == "quit":
        break
    names.append(name)

for name in names:
    engine = py.init()
    py.speak(f"Hello! How are you?, {name}")
    engine.runAndWait()
