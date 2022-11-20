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
        if not self.withdraw(amount, description=f"Transfer to {budget.category}"): return False
        budget.deposit(amount, description=f"Transfer from {self.category}")
        return True

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
            amount = format(led['amount'], '.2f')
            descr = led['description'] if len(led['description']) + len(amount) + 1 < 30 else \
                led['description'][:29 - len(amount)]
            str_ret += f"{descr}{' ' * (30 - len(descr) - len(amount))}" \
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


def calculate_percentage_spend(budgets: list[Category]) -> list:
    """
    Takes a list  of Category objects and calculates the percentages for each withdraw of the accounts
    """
    withdraws = [trans['amount'] for budget in budgets for trans in budget.ledger if trans['amount'] < 0]
    total = sum(withdraws)
    withdraws_percentages = [int(round((withdraw*100)/total, 0)) for withdraw in withdraws]
    return withdraws_percentages


def create_barchart(percentages: list[int]) -> str:
    """
    Takes a list of percentages rounded to 0 extra digits and creates a barchart returning it as a string
    """
    barchart = ""
    for percentage in range(100, -10, -10):
        barchart += str(percentage).rjust(3)+"|"
        for balance in percentages:
            text = "   "
            if percentage <= balance:
                text = " o "
            barchart += text
        barchart += " \n"
    return barchart


def get_categories_names(categories: list[Category]) -> list[str]:
    """
    Takes a list of Category objects and returns a list with the names of each Category object
    """
    return [category.category for category in categories]


def get_longest_name(names: list[str]) -> int:
    """
    Takes a list of names and returns the longest name
    """
    return len(max(names, key=len))


def create_bottom_barchart(stop: int, names: list[str]) -> str:
    """
    Takes a list of names and the longest of them returning the xlab of the barchart with the names vertically sided
    """
    bottom = ""
    for index in range(stop):
        bottom += f"{' '*5}"
        for name in names:
            text = f"{' '* 3}"
            if len(name) > index:
                text = f"{name[index]}  "
            bottom += text
        if index != stop-1:
            bottom += "\n"
    return bottom


def create_spend_chart(categories: list) -> str:
    """
    Takes a list of categories as an argument. It should return a string that is a bar chart.
    param categories:
    :return:
    """
    header = "Percentage spent by category\n"
    balances_percentages = calculate_percentage_spend(categories)
    header += create_barchart(balances_percentages)
    header += f"{' '*4}{'-'*(len(categories)*3)}-\n"
    names = get_categories_names(categories)
    longest_name = get_longest_name(names)
    header += create_bottom_barchart(longest_name, names)
    return header


if __name__ == "__main__":
    # This is for testing purposes
    food = Category("Food")
    business = Category("Business")
    entertainment = Category("Entertainment")
    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    actual = create_spend_chart([business, food, entertainment])
    expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
    print(expected)
    print(actual, actual == expected)
