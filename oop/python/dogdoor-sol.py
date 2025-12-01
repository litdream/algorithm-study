import time
from threading import Timer

# 1. DogDoor Class: Now holds the full responsibility for timing and state management.
class DogDoor:
    def __init__(self):
        self.is_open = False
        self.timer = None
        
    def open(self):
        # Only open if currently closed
        if not self.is_open:
            self.is_open = True
            print("The dog door opens.")
            
            # Encapsulating the automatic closing logic here (DRY principle applied)
            # The door now takes care of closing itself.
            print("Dog door scheduling automatic closing...")

            # Schedule the closing function (time in seconds)
            # We use lambda to ensure we cancel any existing timer, though
            # in this basic model, we only schedule when opening.
            self.timer = Timer(5.0, self.close) 
            self.timer.start()

    def close(self):
        if self.is_open:
            self.is_open = False
            print("The dog door closes.")
            if self.timer:
                # Cancel the timer just in case it was interrupted or called manually
                self.timer.cancel()
                self.timer = None

    def is_open(self):
        return self.is_open

# 2. Remote Class: Responsibility simplified. It only initiates the open/close request.
class Remote:
    def __init__(self, door):
        self.door = door
        
    def pressButton(self):
        print("Pressing the remote control button...")
        
        # The Remote no longer contains any timing logic, fulfilling the goal of
        # simplifying this initiator class.
        if self.door.is_open:
            self.door.close()
        else:
            self.door.open()

# 3. BarkRecognizer Class (Future Feature Simulation):
# If this class were introduced, it simply calls open() on the door, proving the DRY solution works.
class BarkRecognizer:
    def __init__(self, door):
        self.door = door

    def recognize(self, bark):
        print(f"BarkRecognizer: Heard a '{bark}'")
        # Since DogDoor handles the timer, we only call open()
        self.door.open()

# --- Test Drive Scenario (Demonstrating Flexibility) ---
print("--- Scenario: Remote Button Test ---")
door = DogDoor()
remote = Remote(door)

remote.pressButton() # Opens door and starts timer (output: 'The dog door opens.' and 'Dog door scheduling...')
time.sleep(2)
print("Fido is going outside quickly (Door still open)...")
time.sleep(3.5) # Total time elapsed > 5.0 seconds
# Door closes automatically (output: 'The dog door closes.')

print("\n--- Scenario: Bark Recognizer Test (New Feature) ---")
door2 = DogDoor()
recognizer = BarkRecognizer(door2)

recognizer.recognize("Woof") # Opens door and starts timer
time.sleep(5.5)
# Door closes automatically due to logic in DogDoor, not BarkRecognizer
print("End of test.")

