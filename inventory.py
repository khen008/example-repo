# inventary.py
# Nike Stock Storage Manager
# Author: Matthew.
# Date: 11/11/2025

from tabulate import tabulate

class Shoe:
    """Object that keeps infomation of a single shoe."""

    def __init__(self, cntry, code, prod, cost, qty):
        self.cntry = cntry
        self.code = code
        self.prod = prod
        self.cost = float(cost)
        self.qty = int(qty)

    def get_cost(self):
        return self.cost

    def get_qty(self):
        return self.qty

    def __str__(self):
        return (f"Country:{self.cntry} | Code:{self.code} | "
                f"Product:{self.prod} | Cost:R{self.cost:.2f} | Qty:{self.qty}")


shoe_items = []


def read_shoes_file():
    """Loads data from the text file into the program."""
    try:
        with open("inventory.txt", "r", encoding="utf-8") as file:
            next(file)
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    shoe = Shoe(*parts)
                    shoe_items.append(shoe)
    except FileNotFoundError:
        print("inventory.txt file missing, making new one...")
        with open("inventory.txt", "w", encoding="utf-8") as newfile:
            newfile.write("Country,Code,Product,Cost,Quantity\n")
    except Exception as err:
        print("Somthing went wrong while reading file:", err)


def add_shoe():
    """Let user add a new shoe into the list."""
    try:
        cntry = input("Enter country: ").strip()
        code = input("Enter shoe code: ").strip()
        prod = input("Enter shoe name: ").strip()
        cost = float(input("Enter cost R"))
        qty = int(input("Enter quantity: "))

        if any(s.code.lower() == code.lower() for s in shoe_items):
            print("That code already exist, not adding again!\n")
            return

        new_shoe = Shoe(cntry, code, prod, cost, qty)
        shoe_items.append(new_shoe)

        with open("inventory.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{cntry},{code},{prod},{cost:.2f},{qty}")

        print("Shoe captured sucesfully!\n")

    except ValueError:
        print("Invalid input, please enter numbers for cost or qty.\n")
    except Exception as e:
        print("Error while saving shoe:", e)


def show_all():
    """Display all items nicely in a table."""
    if not shoe_items:
        print("No items to show yet.\n")
        return

    tab = [[s.cntry, s.code, s.prod, s.cost, s.qty] for s in shoe_items]
    print(tabulate(tab, headers=["Country", "Code", "Product", "Cost", "Qty"], tablefmt="fancy_grid"))
    print(f"Total shoes: {len(shoe_items)}\n")


def restock_shoe():
    """Find item with smallest stock and offer restocking."""
    if len(shoe_items) == 0:
        print("Nothing in stock to restock.\n")
        return

    low = min(shoe_items, key=lambda x: x.qty)
    print(f"Lowest stock item:\n{low}\n")

    ans = input("Do you want to restok this shoe? (y/n): ").lower()
    if ans == "y":
        try:
            addnum = int(input("Enter how many to add: "))
            low.qty += addnum
            write_inventory()
            print("Updated! New qty:", low.qty, "\n")
        except ValueError:
            print("Invalid number enterd.\n")
    else:
        print("Restock canceled.\n")


def find_shoe():
    """Search for shoe by code."""
    c = input("Type shoe code to search: ").strip()
    for s in shoe_items:
        if s.code.lower() == c.lower():
            print("Shoe found:\n", s, "\n")
            return
    print("Not found.\n")


def show_value():
    """Show total value per product."""
    rows = []
    for s in shoe_items:
        total = s.cost * s.qty
        rows.append([s.prod, f"R{s.cost:.2f}", s.qty, f"R{total:.2f}"])
    print(tabulate(rows, headers=["Product", "Cost", "Qty", "Total Value"], tablefmt="grid"))
    print()


def top_stock():
    """Show product with biggest stock."""
    if not shoe_items:
        print("No info loaded.\n")
        return

    big = max(shoe_items, key=lambda s: s.qty)
    print("Top stock item:\n", big, "\n")


def write_inventory():
    """Rewrite the inventory file with updated data."""
    try:
        with open("inventory.txt", "w", encoding="utf-8") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for s in shoe_items:
                file.write(f"{s.cntry},{s.code},{s.prod},{s.cost},{s.qty}\n")
    except Exception as e:
        print("Problem updating file:", e)


def main():
    print("Loading data from file...")
    read_shoes_file()
    print("Data load completed!\n")

    while True:
        print("====== NIKE STOCK MENU ======")
        print("1 - View all shoes")
        print("2 - Add new shoe")
        print("3 - Restock lowest item")
        print("4 - Search shoe by code")
        print("5 - See total value of items")
        print("6 - Show highest stock")
        print("7 - Exit\n")

        pick = input("Choose option: ")

        if pick == "1":
            show_all()
        elif pick == "2":
            add_shoe()
        elif pick == "3":
            restock_shoe()
        elif pick == "4":
            find_shoe()
        elif pick == "5":
            show_value()
        elif pick == "6":
            top_stock()
        elif pick == "7":
            print("Bye bye!")
            break
        else:
            print("Wrong choice, try again.\n")


if __name__ == "__main__":
    main()
