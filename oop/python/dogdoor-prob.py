import time
from threading import Timer

# 1. DogDoor Class: Represents the physical hardware.
# It only manages the state and provides open/close operations.
class DogDoor:
    def __init__(self):
        self.is_open = False

    def open(self):
        self.is_open = True
        print("The dog door opens.")

    def close(self):
        self.is_open = False
        print("The dog door closes.")

    def is_open(self):
        return self.is_open

# 2. Remote Class: Controls the door. This is the problematic class.
class Remote:
    def __init__(self, door):
        self.door = door
        
    def pressButton(self):
        print("Pressing the remote control button...")
        
        if self.door.is_open:
            # If open, close immediately
            self.door.close()
        else:
            # If closed, open the door
            self.door.open()
            
            # PROBLEM CODE: The automatic closing logic (timer) is located here.
            # This logic must close the door after a few seconds .
            print("Scheduling automatic closing...")
            # We schedule a function that calls close() on the door object
            
            # The lambda function defines what happens when the timer runs out.
            t = Timer(5.0, self.door.close) 
            t.start()


# --- Test Drive Scenario (Simulating Todd and Gina using the remote) ---
dog_door = DogDoor()
remote = Remote(dog_door)

print("Fido barks to go outside...")
remote.pressButton() 
# Door opens, timer starts (In a real application, this waits 5 seconds before closing)
time.sleep(6) 
# Wait 6 seconds to ensure timer fires
print("Fido has done his business and the door closed automatically.")

# Fido is now back inside and the door is closed.



"""Description of the Problem
The code above satisfies the requirement that the dog door closes automatically after being opened . However, this implementation creates a maintenance and flexibility problem that Chapter 2 (and later Chapter 8) addresses:

1. Violation of DRY (Don't Repeat Yourself) Principle: The single requirement, "Once the dog door has opened, it should close automatically" , is currently implemented entirely within the Remote.pressButton() method. The sources emphasize that the Don't Repeat Yourself Principle (DRY) is about having each piece of information and behavior in your system in a single, sensible place .

2. Lack of Cohesion and Tight Coupling: The Remote class now has multiple responsibilities: controlling the toggle logic and managing the timing/scheduling of the door closure. Good design strives for high cohesion, meaning each class should focus on doing one thing really well .

3. Resistance to Change (The Enhancement Goal): If Todd and Gina later add a new feature, such as a BarkRecognizer that can open the door when Fido barks , that new BarkRecognizer class would also need to contain the exact same timer scheduling logic to ensure the door closes automatically . This duplication of complex timing code is prone to errors if the closure time or logic changes later .

The goal of the OOP solution will be to move the responsibility for automatic closing out of the initiating classes (like Remote or future BarkRecognizer) and into the DogDoor class itself, ensuring the automatic closing functionality is encapsulated in only one place .
"""

