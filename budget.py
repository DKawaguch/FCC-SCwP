from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Dict,
    List,
    Union,
)

@dataclass
class Category:

    categorie: str
    ledger: List[Dict[str, Union[str, int, float]]] = field(default_factory=list)
    # like double entry bookkeeping
    spent: float = 0.0
    income: float = 0.0

    def deposit(self, amount: Union[int, float], description: str = "") -> None:
     
        self.ledger.append(
            {"amount": round(float(amount), 2), "description": description}
        )
        self.income += amount

    def withdraw(self, amount: Union[int, float], description: str = "") -> bool:
       
        if self.check_funds(amount):
            self.ledger.append(
                {
                    "amount": round(float(-amount), 2),
                    "description": description,
                }
            )
            self.spent += amount
            self.income -= amount

            return True
        else:
            return False

    def get_balance(self) -> float:
       
        return round(float(self.income), 2)

    def transfer(self, amount: Union[int, float], categorie_obj) -> bool:
      
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {categorie_obj.categorie}")
            categorie_obj.deposit(amount, f"Transfer from {self.categorie}")

            return True
        else:
            return False

    def check_funds(self, amount: Union[int, float]) -> bool:
    
        if self.income >= round(float(amount), 2):
            return True
        else:
            return False

    def __str__(self):
       
        titel_row: str = self.categorie.center(30, "*") + "\n"
        items: str = ""

        for entry in self.ledger:
            
            items += (
                f"{entry.get('description')[0:23]:23}"
                + f"{entry.get('amount'):>7.2f}"
                + "\n"
            )

        return titel_row + items + "Total: " + f"{self.income:.2f}"

def create_spend_chart(categories: List) -> str:
   
    plot: str = "Percentage spent by category\n"
    # calculate the total of everything spent in all categories
    total_spent: float = sum(x.spent for x in categories)
   
    percentages: List[float] = [(x.spent / total_spent) // 0.01 for x in categories]

    for p_value in range(100, -10, -10):
        plot += str(p_value).rjust(3, " ") + "|"
        for percentage in percentages:
            
            if percentage >= p_value:
                plot += " o "
            else:
                plot += " " * 3
        plot += " \n"

    # build the x axis
    plot += " " * 4 + "-" * 3 * len(percentages) + "-\n"
    # calculate the length of the longest categorie
    longest_name: int = max(len(x.categorie) for x in categories)

    for char in range(longest_name):
        # prepend 4 spaces before every row
        plot += " " * 4
        # for every name
        for name in categories:
            # append the char to the row
            if char < len(name.categorie):
                plot += " " + name.categorie[char] + " "
            else:
                # or if no char append 3 spaces
                plot += " " * 3

        plot += " \n"

    plot = plot.rstrip() + " " * 2

    return plot
