'''
What is the Strategy Pattern?
	•	Allows selecting an algorithm at runtime.
	•	Encapsulates different strategies (algorithms) and allows switching dynamically.
	•	Example: Payment processing where a user can pay via Credit Card, PayPal, or Bitcoin.

	Example: Strategy Pattern in Python

Let’s create a payment system where users can select different payment strategies dynamically.

'''

from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"Paid ${amount} using Credit Card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"Paid ${amount} using PayPal"

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"Paid ${amount} using Bitcoin"

# Context (Uses a strategy)
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy  # Change strategy dynamically

    def process_payment(self, amount: float):
        return self.strategy.pay(amount)

# ✅ Example Usage
payment = PaymentContext(CreditCardPayment())
print(payment.process_payment(100))  # ✅ Paid $100 using Credit Card

payment.set_strategy(PayPalPayment())
print(payment.process_payment(200))  # ✅ Paid $200 using PayPal

'''
🔥 When to Use Strategy Pattern?

✔️ When you need to switch between multiple algorithms dynamically.
✔️ When you want to decouple algorithms from the main class for better maintainability.

'''
