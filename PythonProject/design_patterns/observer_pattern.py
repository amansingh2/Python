'''
What is the Observer Pattern?
	•	Defines a one-to-many dependency between objects.
	•	When one object changes state, all its dependent (observer) objects are notified automatically.
	•	Used in event-driven applications (e.g., UI listeners, stock price updates, notifications).

	Example: Observer Pattern in Python

Let’s create a weather station where multiple displays (MobileDisplay, WebDisplay) subscribe to weather updates.
'''

from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass

# Concrete Observers
class MobileDisplay(Observer):
    def update(self, temperature: float):
        print(f"📱 Mobile Display: Temperature is {temperature}°C")

class WebDisplay(Observer):
    def update(self, temperature: float):
        print(f"💻 Web Display: Temperature is {temperature}°C")

# Subject (Observable)
class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0.0

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def set_temperature(self, temperature: float):
        self.temperature = temperature
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)

# Example Usage
weather_station = WeatherStation()
mobile = MobileDisplay()
web = WebDisplay()

weather_station.add_observer(mobile)
weather_station.add_observer(web)

weather_station.set_temperature(25)  # Notifies all displays
weather_station.set_temperature(30)  # Notifies all displays

'''
When to Use Observer Pattern?
✔️ When an object’s state change needs to notify multiple dependents (e.g., Event Listeners, Pub-Sub).
✔️ When you want to decouple objects by using a subscription mechanism.
'''
