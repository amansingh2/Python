'''
What is the Facade Pattern?
	•	Provides a simplified interface to a complex system.
	•	Hides the underlying complexity by providing a unified API.
	•	Example: Instead of interacting with multiple subsystems separately, you call a single function to perform an operation.

	✅ Example: Facade Pattern in Python

Let’s implement a home automation system where different subsystems (Lights, TV, AC) are controlled using a single facade class.
'''

# Subsystems (Complex System)
class Lights:
    def turn_on(self):
        return "Lights are ON"

    def turn_off(self):
        return "Lights are OFF"

class TV:
    def turn_on(self):
        return "TV is ON"

    def turn_off(self):
        return "TV is OFF"

class AC:
    def turn_on(self):
        return "AC is ON"

    def turn_off(self):
        return "AC is OFF"

# Facade (Simplifies interaction)
class HomeAutomationFacade:
    def __init__(self):
        self.lights = Lights()
        self.tv = TV()
        self.ac = AC()

    def activate_home_mode(self):
        return f"{self.lights.turn_on()}, {self.tv.turn_on()}, {self.ac.turn_on()}"

    def activate_night_mode(self):
        return f"{self.lights.turn_off()}, {self.tv.turn_off()}, {self.ac.turn_on()}"

# Example Usage
home = HomeAutomationFacade()
print(home.activate_home_mode())  #  Turns ON all devices
print(home.activate_night_mode())  # Turns OFF lights & TV, keeps AC ON