class Category:

    def __init__(self, category: str):
        self.category = category
        self.ledger = list()

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
        if not self.check_funds(amount): return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self) -> float:
        """
        Returns the current balance of the budget category based on the deposits and withdrawals
        that have occurred.
        """
        return round(sum([moves.get("amount", 0) for moves in self.ledger]), 2)

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

    def formatted_str_return(self):
        str_ret = f"{self.category.center(30, '*')}\n"
        for led in self.ledger:
            descr = led['description'] if len(led['description']) + len(str(led['amount']))+1 <= 30 else \
                    led['description'][:30-len(format(led['amount'], '.2f'))-1]
            str_ret += f"{descr}{' ' * (30 - len(descr) - len(format(led['amount'], '.2f')))}" \
                       f"{led['amount']:.2f}\n"
        str_ret += f"Total: {self.get_balance()}"
        return str_ret

    def __repr__(self) -> str:
        """
        -A title line of 30 characters where the name of the category is centered in a line of * characters.
        -A list of the items in the ledger.
         Each line should show the description and amount.
         The first 23 characters of the description should be displayed, then the amount.
         The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
        -A line displaying the category total.
        """
        return self.formatted_str_return()


def create_spend_chart(categories: list) -> str:
    """
    Takes a list of categories as an argument. It should return a string that is a bar chart.
    :param categories:
    :return:
    """
    pass


if __name__ == "__main__":
    # This is for testing purposes
    food = Category("Food")
    food.deposit(900, "deposit")
    food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
    print(food)