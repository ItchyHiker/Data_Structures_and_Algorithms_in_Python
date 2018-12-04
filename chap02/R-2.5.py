"""test the make_payment() method of CreditCard Class"""
class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance
        The initial balance is zero
        customer: the name of the customer
        bank: the name of the bank
        acnt: the acount identifier
        limit: credit limit
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer()
    def get_account(self):
        return self._bank
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a number of int or float!")
        self._balance -= amount

if __name__ == "__main__":
    c1 = CreditCard('Andy', "CNBC", 10001, 1000)
    c1.charge(100)
    print(c1.get_balance())
    c1.make_payment("100")
