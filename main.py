from pynput.keyboard import Key, Listener, KeyCode
import time
import threading
import keyboard
import mouse
from colorama import Fore

class Logger:
    def __init__(self) -> None:
        self.is_active = False # Don't touch this!
        self.thread = None # Don't touch this!
        self.activate_button = Key.f6 # For enable/disable script. Put here only F button and other. Letters don't support.
        self.exit_button = Key.f7 # For exit from script. Put here only F button and other. Letters don't support.
        
        self.press_button = 'e' # Change for your letter on keyboard | Изменить клавишу нажатия, обязательно в кавычках
        
        self.wait_seconds = 1 # Float number for waiting | Время ожидания в секундах, можно с точкой (0.001)
        
        self.colors = {
            'enabled': Fore.GREEN, # Color for Enabled Status
            'disabled': Fore.BLUE, # Color for Disabled Status
            'message': Fore.CYAN # Color for Message
        }    


    def pressed(self, key):
        if key == self.activate_button:
            self.is_active = not self.is_active
            if self.is_active:
                if not self.thread or not self.thread.is_alive():
                    print(self.colors['enabled'] + '[*] Activation Status: Enabled')
                    self.thread = threading.Thread(target=self.run)
                    self.thread.start()
            else:
                print(self.colors['disabled'] + '[*] Activation Disabled: Disabled')
                
        elif key == self.exit_button:
            print(self.colors['message'] + '[*] Good Bye')
            return False
    
    
    def run(self):
        while self.is_active:
            # Method
            keyboard.press_and_release(self.press_button) # Pressing your button
            # mouse.click(button='left')
            
            # print(self.colors['message'] + '[*] Clicked') # Print function
            time.sleep(self.wait_seconds)
    
if __name__ == '__main__':
    
    logger = Logger()
    
    print(Fore.CYAN + '[*] Started!')

    with Listener(on_press=logger.pressed) as listener:
        listener.join()
