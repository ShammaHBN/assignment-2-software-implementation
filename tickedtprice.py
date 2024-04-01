class TicketPrice:
    """
    TicketPrice class representing the price and VAT for tickets.
    """
    def __init__(self, regular_price=63, vat_percent=0.05):
        self.regular_price = regular_price  # Regular price of a ticket
        self.vat_percent = vat_percent      # VAT percentage

    # Method to calculate ticket price based on visitor's age
    def get_price_for_visitor(self, visitor_age):
        if 18 <= visitor_age <= 60:
            ticket_price = self.regular_price  # Regular price for adults
        else:
            ticket_price = 0  # Free ticket for children, teachers/students, and seniors
        return ticket_price

    # Method to apply VAT to the ticket price
    def apply_vat(self, ticket_price):
        return ticket_price * (1 + self.vat_percent)

    # Method to calculate group discount
    def get_group_discount(self, ticket_price):
        return ticket_price * 0.5

    # Method to calculate the total price for a group of visitors
    def get_total_price_for_visitors(self, visitors):
        total_price = 0
        for visitor in visitors:
            ticket_price = self.get_price_for_visitor(visitor.age)
            total_price += ticket_price
        if len(visitors) >= 15:
            total_price = self.get_group_discount(total_price)
        total_price = self.apply_vat(total_price)
        return total_price