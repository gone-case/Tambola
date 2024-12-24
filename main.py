from grid import Grid 
from ticket_generator import TicketGenerator, TicketFormatter

def main():
    # Generate Tambola tickets
    generator = TicketGenerator()
    formatter = TicketFormatter()

    number_of_players = int(input("Enter the number of players: "))
    tickets = []

    for i in range(number_of_players):
        ticket = generator.generate_ticket()
        tickets.append(ticket)
        print(f"\nTambola Ticket {i + 1}:")
        print(formatter.format_ticket(ticket))

    # Start the number-calling game
    print("\nAll tickets are generated! Starting the number-calling grid game...\n")
    Grid.start_game()  

if __name__ == "__main__":
    main()
