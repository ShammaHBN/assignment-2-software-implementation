class Ticket(TicketPrice):
    def __init__(self, regular_price=63, vat_percent=0.05, ticket_type=None, location=None, price=None):
        super().__init__(regular_price, vat_percent)
        self.ticket_type = ticket_type
        self.location = location
        self.price = price

    # Method to display ticket information
    def display_ticket_info(self):
        print("Ticket Information:")
        print(f"Ticket Type: {self.ticket_type}")
        print(f"Location: {self.location}")
        print(f"Price: {self.price} AED")
        print(f"VAT: {self.vat_percent * 100}%")
        print(f"Total Price (including VAT): {self.apply_vat(self.price)} AED")