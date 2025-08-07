'''
What is the Abstract Factory Pattern?
	•	It is an extension of the Factory Pattern.
	•	Instead of a single factory method, it provides a factory for related objects.
	•	It ensures that related objects are created together.

⸻

✅ Example: Abstract Factory Pattern in Python

Let’s create an abstract factory that creates different types of UI elements
(WindowsButton, MacButton, WindowsCheckbox, MacCheckbox).
'''

from abc import ABC, abstractmethod

# Step 1: Abstract Products (Interfaces)
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

# Step 2: Concrete Implementations
class WindowsButton(Button):
    def click(self):
        return "Clicked Windows Button"

class MacButton(Button):
    def click(self):
        return "Clicked Mac Button"

class WindowsCheckbox(Checkbox):
    def check(self):
        return "Checked Windows Checkbox"

class MacCheckbox(Checkbox):
    def check(self):
        return "Checked Mac Checkbox"

# Step 3: Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Step 4: Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# ✅ Example Usage
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.click())   # ✅ Output depends on factory
    print(checkbox.check()) # ✅ Output depends on factory

# Create Windows UI
windows_factory = WindowsFactory()
client_code(windows_factory)

# Create Mac UI
mac_factory = MacFactory()
client_code(mac_factory)



'''
🔥 When to Use Abstract Factory Pattern?

✔️ When you need to create families of related objects.
✔️ When object creation needs to be decoupled from implementation.
✔️ Example: Cross-platform UI libraries (Windows, Mac, Linux).

'''
