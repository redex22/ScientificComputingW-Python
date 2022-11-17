class Category:
    ledger = list()

    def __init__(self, category: str):
        self.category = category

    def deposit(self, amount: float, description: str = "") -> None:
        """
        Accepts an amount and description.
        If no description is given, it should default to an empty string.
        The method should append an object to the ledger list in the form of:
        {"amount": amount, "description": description}.
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        """
        Similar to the deposit method,
        but the amount passed in should be stored in the ledger as a negative number.
        If there are not enough funds, nothing should be added to the ledger.
        This method should return True if the withdrawal took place, and False otherwise.
        """
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self) -> float:
        """
        Returns the current balance of the budget category based on the deposits and withdrawals
        that have occurred.
        """
        return sum([moves.get("amount", 0) for moves in self.ledger])

    def transfer(self, amount: float, budget) -> bool:
        """
        Accepts an amount and another budget category as arguments.
        The method should add a withdrawal with the amount and the description:
        "Transfer to [Destination Budget Category]".
        The method should then add a deposit to the other budget category with the amount and the description:
        "Transfer from [Source Budget Category]".
        If there are not enough funds, nothing should be added to either ledgers.
        This method should return True if the transfer took place, and False otherwise.
        :param amount:
        :param budget:
        :return:
        """
        pass

    def check_funds(self, amount: float) -> bool:
        """
        Accepts an amount as an argument.
        It returns False if the amount is greater than the balance of the budget category
        and returns True otherwise.
        This method should be used by both the withdraw method and transfer method.
        :param amount:
        :return:
        """
        return not amount > self.get_balance()

    def __repr__(self) -> str:
        """
        -A title line of 30 characters where the name of the category is centered in a line of * characters.
        -A list of the items in the ledger.
         Each line should show the description and amount.
         The first 23 characters of the description should be displayed, then the amount.
         The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
        -A line displaying the category total.
        """
        return "hola soy una prueba"


def create_spend_chart(categories: list) -> str:
    """
    Takes a list of categories as an argument. It should return a string that is a bar chart.
    :param categories:
    :return:
    """
    pass


if __name__ == "__main__":
    # This is for testing purposes
    t1 = Category("food")
    t1.deposit(900, "deposit")
    print(t1.ledger[0]) # -> {'amount': 900, 'description': 'deposit'}
    print(t1.get_balance())
    print(t1.check_funds(899.01))
    print(t1.withdraw(100, "debt with a friend"))
    print(t1.get_balance())
