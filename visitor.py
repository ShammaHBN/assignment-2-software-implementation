class Visitor:
    def __init__(self, name, age, is_teacher_student=False, is_senior=False, is_group=False):
        self.name = name
        self.age = age
        self.is_teacher_student = is_teacher_student
        self.is_senior = is_senior
        self.is_group = is_group
        self.tickets_purchased = []

    # Method to buy a ticket for an event
    def buy_ticket(self, event, ticket_price):
        if self.age < 18 or self.age >= 60:  # Check if visitor is under 18 or over 60
            ticket_price = 0  # Free ticket for children and seniors
        elif self.is_group:
            ticket_price *= 0.5  # Apply 50% discount for groups

        ticket = {
            "ticket_type": event.capitalize(),
            "location": self._get_ticket_location(event),
            "price": ticket_price
        }
        self.tickets_purchased.append(ticket)
        return "Ticket purchased successfully"

    # Method to get the location for the ticket
    def _get_ticket_location(self, event):
        if event == "exhibition":
            return "Exhibition Halls"
        elif event == "tour":
            return "Main Galleries"
        elif event == "special_event":
            return "Outdoor Areas"
        else:
            return "Unknown Location"

    # Method to display purchased tickets
    def display_purchased_tickets(self):
        print("Purchased Tickets:")
        for ticket in self.tickets_purchased:
            print(f"Type: {ticket['ticket_type']}, Location: {ticket['location']}, Price: {ticket['price']} AED")