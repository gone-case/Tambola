import random
from tabulate import tabulate

class TicketValidator:
    @staticmethod
    def validate_row_count(ticket):
        """Validate each row has exactly 5 numbers."""
        return all(sum(1 for num in row if num != 0) == 5 for row in ticket)

    @staticmethod
    def validate_subgrid_count(ticket):
        """Validate no 3x3 subgrid has more than 6 numbers."""
        for start_col in range(0, 7):
            numbers_count = sum(1 for row in ticket 
                              for col in range(start_col, min(start_col + 3, 9))
                              if row[col] != 0)
            if numbers_count > 6:
                return False
        return True

    @classmethod
    def validate_ticket(cls, ticket):
        """Validate all ticket rules."""
        return cls.validate_row_count(ticket) and cls.validate_subgrid_count(ticket)

class TicketGenerator:
    @staticmethod
    def get_column_ranges():
        """Get the valid number ranges for each column."""
        return [(1,10), (11,20), (21,30), (31,40), (41,50),
                (51,60), (61,70), (71,80), (81,90)]

    @staticmethod
    def initialize_ticket():
        """Create empty ticket grid."""
        return [[0 for _ in range(9)] for _ in range(3)]

    def generate_ticket(self):
        """Generate a valid Tambola ticket."""
        while True:
            ticket = self.initialize_ticket()
            ranges = self.get_column_ranges()
            
            # First, ensure each column has at least one number
            for col in range(9):
                row = random.randint(0, 2)
                start, end = ranges[col]
                ticket[row][col] = random.randint(start, end)
            
            numbers_placed = 9
            
            # Add remaining numbers until we reach 15
            attempts = 0
            while numbers_placed < 15 and attempts < 100:
                row = random.randint(0, 2)
                col = random.randint(0, 8)
                
                if ticket[row][col] == 0:
                    temp_ticket = [row[:] for row in ticket]
                    start, end = ranges[col]
                    col_numbers = [ticket[r][col] for r in range(3) if ticket[r][col] != 0]
                    available = [n for n in range(start, end + 1) if n not in col_numbers]
                    
                    if available:
                        num = random.choice(available)
                        temp_ticket[row][col] = num
                        
                        if TicketValidator.validate_subgrid_count(temp_ticket):
                            ticket[row][col] = num
                            numbers_placed += 1
                
                attempts += 1
            
            if TicketValidator.validate_ticket(ticket):
                return ticket

class TicketFormatter:
    @staticmethod
    def format_ticket(ticket):
        """Format the ticket for display."""
        formatted = [['' if cell == 0 else cell for cell in row] for row in ticket]
        return tabulate(formatted, tablefmt='fancy_grid')

