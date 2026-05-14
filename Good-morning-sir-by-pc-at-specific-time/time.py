import time

name = input("Enter your name: ")
recent_time = time.strftime("%H:%M:%S")

Recent_time = int(time.strftime("%H"))

c = name.capitalize()
if 4 <= Recent_time <12:
    print(f"GOOD MORNING! {c}. Its {recent_time} time.")
elif 12 <= Recent_time < 17:
    print(f"GOOD AFTERNOON! {c}. Its {recent_time} time.")
elif  17 <= Recent_time < 20:
    print(f"GOOD EVENING! {c}. Its {recent_time} time.")
else:
    print(f"GOOD NIGHT! {c}. Its {recent_time} time.")