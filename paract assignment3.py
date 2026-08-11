from abc import ABC, abstractmethod
from typing import Dict, Type


# --- 1. Decorator for Transaction Logging ---
def log_transaction(func):
    """Decorator to log payment attempt prior to processing."""
    def wrapper(self, amount: float):
        print(f"\n[LOG] Attempting transaction of ${amount:.2f} using strategy: {self.strategy.__class__.__name__}")
        return func(self, amount)
    return wrapper


# --- 2. Abstract Base Class (Strategy Interface) ---
class PaymentStrategy(ABC):
    
    @abstractmethod
    def validate(self) -> bool:
        """Validate payment details."""
        pass

    @abstractmethod
    def pay(self, amount: float) -> bool:
        """Process the payment for the given amount."""
        pass


# --- 3. Concrete Payment Strategies ---
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv

    def validate(self) -> bool:
        # Simple validation rule example
        return len(self.card_number) == 16 and len(self.cvv) == 3

    def pay(self, amount: float) -> bool:
        print(f"Charging ${amount:.2f} to Credit Card ending in {self.card_number[-4:]}")
        return True


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def validate(self) -> bool:
        return "@" in self.email

    def pay(self, amount: float) -> bool:
        print(f"Charging ${amount:.2f} to PayPal account {self.email}")
        return True


class UPIPayment(PaymentStrategy):
    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def validate(self) -> bool:
        return "@" in self.upi_id

    def pay(self, amount: float) -> bool:
        print(f"Charging ${amount:.2f} to UPI ID {self.upi_id}")
        return True


class NetBankingPayment(PaymentStrategy):
    def __init__(self, bank_code: str, account_number: str):
        self.bank_code = bank_code
        self.account_number = account_number

    def validate(self) -> bool:
        return bool(self.bank_code and self.account_number)

    def pay(self, amount: float) -> bool:
        print(f"Charging ${amount:.2f} via NetBanking ({self.bank_code})")
        return True


# --- 4. Receipt Class ---
class Receipt:
    def __init__(self, status: str, amount: float, method_name: str):
        self.status = status
        self.amount = amount
        self.method_name = method_name

    def __str__(self) -> str:
        return (
            f"\n--------------------\n"
            f"RECEIPT [{self.status}]\n"
            f"Method: {self.method_name}\n"
            f"Amount: ${self.amount:.2f}\n"
            f"--------------------"
        )


# --- 5. PaymentProcessor (Context Class) ---
class PaymentProcessor:
    _registry: Dict[str, Type[PaymentStrategy]] = {}

    def __init__(self, strategy: PaymentStrategy = None):
        self.strategy = strategy

    @classmethod
    def register_strategy(cls, name: str, strategy_cls: Type[PaymentStrategy]):
        """Register strategy implementations dynamically."""
        cls._registry[name.lower()] = strategy_cls

    @classmethod
    def create(cls, name: str, **kwargs) -> PaymentStrategy:
        """Factory method to instantiate registered strategies."""
        strategy_cls = cls._registry.get(name.lower())
        if not strategy_cls:
            raise ValueError(f"Strategy '{name}' is not registered.")
        return strategy_cls(**kwargs)

    def set_strategy(self, strategy: PaymentStrategy):
        """Switch payment strategy dynamically."""
        self.strategy = strategy

    @log_transaction
    def process_payment(self, amount: float) -> Receipt:
        """Delegates payment logic to strategy & generates receipt."""
        if not self.strategy:
            raise RuntimeError("No payment strategy selected.")

        # Delegate validation step
        if self.strategy.validate():
            # Process payment
            self.strategy.pay(amount)
            return Receipt(status="SUCCESS", amount=amount, method_name=self.strategy.__class__.__name__)
        else:
            # Skip processing if validation fails
            print("Validation failed for the selected payment method.")
            return Receipt(status="FAILED", amount=amount, method_name=self.strategy.__class__.__name__)


# --- Execution Example matching the Flowchart ---
if __name__ == "__main__":
    # Step 1: Register strategies in registry
    PaymentProcessor.register_strategy("credit_card", CreditCardPayment)
    PaymentProcessor.register_strategy("paypal", PayPalPayment)
    PaymentProcessor.register_strategy("upi", UPIPayment)
    PaymentProcessor.register_strategy("netbanking", NetBankingPayment)

    # Instantiate Context Class
    processor = PaymentProcessor()

    # --- Scenario 1: Initial Payment Attempt (Invalid Details) ---
    print("\n--- Attempt 1: Failed Credit Card Transaction ---")
    # User selects/configures strategy with invalid card number length
    invalid_card = PaymentProcessor.create("credit_card", card_number="1234", cvv="999")
    processor.set_strategy(invalid_card)

    # Process Payment & Print Receipt (__str__)
    receipt = processor.process_payment(150.00)
    print(receipt)

    # --- Scenario 2: Switch Payment Strategy (Valid Details) ---
    print("\n--- Switch Strategy: Successful PayPal Transaction ---")
    # User switches to PayPal strategy
    paypal_strat = PaymentProcessor.create("paypal", email="user@example.com")
    processor.set_strategy(paypal_strat)

    # Process Payment & Print Receipt (__str__)
    receipt = processor.process_payment(150.00)
    print(receipt)