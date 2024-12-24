import random
from tabulate import tabulate
from colorama import Fore, Style, init

class Grid:
    @staticmethod
    def start_game():
        # Initialize colorama
        init()

        # Initialize the table and called numbers
        table = [[0 for _ in range(10)] for _ in range(9)]  # A 9x10 table for 1-90
        called_numbers = []

        h = input('Click Enter to start and aything else to quit: ')
        while h == '':
            i = random.randint(1, 90)
            if i in called_numbers:
                continue
            
            called_numbers.append(i)

            # Update board
            row_index = (i - 1) // 10
            column_index = (i - 1) % 10
            table[row_index][column_index] = i

            # Print the table with the last number in blue
            styled_table = []
            for row in table:
                styled_row = []
                for num in row:
                    if num == i:
                        styled_row.append(Fore.BLUE + str(num) + Style.RESET_ALL)
                    elif num != 0:
                        styled_row.append(Fore.WHITE + str(num) + Style.RESET_ALL)
                    else:
                        styled_row.append("")
                styled_table.append(styled_row)

            print(tabulate(styled_table, headers=['.' for _ in range(10)], tablefmt="fancy_grid"))

            if len(called_numbers) == 90:
                print("GRID COMPLETED\n")
                exit(0)
            h=input("ENTER :")
