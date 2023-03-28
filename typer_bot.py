from pynput.keyboard import Key, Controller
import time

keyboard = Controller()



while True:
    
    user_input = input("Text: ")
    time.sleep(5)
    

    
    for x in user_input:
        time.sleep(0.00000005)
        keyboard.type(x)
