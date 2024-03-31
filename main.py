# Define the TicketPrice class representing ticket prices and VAT
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


# Define the Museum class
class Museum:
    def __init__(self, location, ticket_price_calculator):
        self.location = location
        self.ticket_price = ticket_price_calculator  # Initialize TicketPrice instance
        self.artworks = []  # List to store artworks
        self.exhibitions = []  # List to store exhibitions
        self.special_events = []  # List to store special events
        self.tours = []  # List to store tours

    # Method to add artwork to the museum
    def add_artwork(self, title, artist, date, historical_significance, location, Artwork):
        artwork = Artwork(title, artist, date, historical_significance, location)
        self.artworks.append(artwork)

    # Method to add multiple artworks to the museum
    def add_artworks(self, artworks):
        for artwork in artworks:
            self.artworks.append(artwork)

    # Method to create an exhibition
    def create_exhibition(self, title, location, duration, artworks, Exhibition):
        exhibition = Exhibition(title, location, duration, artworks)
        self.exhibitions.append(exhibition)
        return exhibition

    # Method to create a special event
    def create_special_event(self, title, location, duration, ticket_price, SpecialEvent):
        special_event = SpecialEvent(title, location, duration, ticket_price)
        self.special_events.append(special_event)
        return special_event

    # Method to create a tour
    def create_tour(self, title, date, capacity, guide, location, Tour):
        tour = Tour(title, date, capacity, guide, location)
        self.tours.append(tour)
        return tour


# Define the Exhibition_Location class
class Exhibition_Location:
    def __init__(self, name):
        self.name = name


# Define the Artwork class
class Artwork:
    def __init__(self, title, artist, date, historical_significance, location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date
        self.historical_significance = historical_significance
        self.location = location

    # Method to submit artwork
    def submit_artwork(self):
        pass

    # Method to display artwork in a specific location
    def display_artwork(self, location):
        if isinstance(location, Location):
            print(f"Displaying '{self.title}' by {self.artist} in {location.name}")
        else:
            print("Invalid location provided.")

    # Method to display information about the artwork
    def display_info(self):
        print("Artwork Information:")
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Date of Creation: {self.date_of_creation}")
        print(f"Historical Significance: {self.historical_significance}")
        print(f"Location: {self.location}")


# Define the SpecialEvent class
class SpecialEvent:
    def __init__(self, title, location, duration, ticket_price):
        self.title = title
        self.location = location
        self.duration = duration
        self.ticket_price = ticket_price


# Define the Tour class
class Tour:
    def __init__(self, title, date, capacity, guide, location):
        self.title = title
        self.date = date
        self.capacity = capacity
        self.guide = guide
        self.location = location


# Define the Exhibition class
class Exhibition:
    def __init__(self, title, location, duration, artworks):
        self.title = title
        self.location = location
        self.duration = duration
        self.artworks = artworks


# Define the Visitor class
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


# Create an instance of TicketPrice with default values
ticket_price_calculator = TicketPrice(regular_price=63, vat_percent=0.05)
ticket_price_calculator = TicketPrice(regular_price=70, vat_percent=0.08)
# Define the Louvre Museum instance
louvre_museum = Museum("Louvre Abu Dhabi", ticket_price_calculator)

# Add artworks to the Louvre Museum
louvre_museum.add_artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Renaissance masterpiece", "Main Galleries", Artwork)
louvre_museum.add_artwork("Starry Night", "Vincent van Gogh", "1889", "Post-Impressionist masterpiece", "Gallery 5", Artwork)
louvre_museum.add_artwork("Venus de Milo", "Alexandros of Antioch", "c. 100 BC", "Ancient Greek sculpture", "Gallery 12", Artwork)
louvre_museum.add_artwork("Rosetta Stone", "Unknown", "196 BC", "Ancient Egyptian artifact", "Egyptian Antiquities", Artwork)
# Display information about artworks
for artwork in louvre_museum.artworks:
    artwork.display_info()
    print()  # Add a blank line for clarity

# Create an instance of Exhibition at the Louvre Museum
exhibition1 = louvre_museum.create_exhibition("Impressionism Masterpieces", "Exhibition Halls", "3 months", [Artwork("Water Lilies", "Claude Monet", "1919", "Series of approximately 250 oil paintings", "Gallery 2")], Exhibition)

# Create an instance of SpecialEvent at the Louvre Museum
special_event1 = louvre_museum.create_special_event("Music in the Museum", "Outdoor Areas", "1 night", 100, SpecialEvent)

# Create an instance of Tour at the Louvre Museum
tour1 = louvre_museum.create_tour("Renaissance Art Tour", "2024-04-15", 25, "John Smith", "Main Galleries", Tour)

# Create an instance of Visitor
visitor1 = Visitor("Alice", 25)
visitor2 = Visitor("Bob", 55, is_group=True)
visitor3 = Visitor("Charlie", 16)
visitor4 = Visitor("David", 10, is_group=True)
visitor5 = Visitor("Emma", 70)

# Visitor buys tickets
visitor1.buy_ticket("exhibition", 63)  # Buy exhibition ticket
visitor1.buy_ticket("tour", 100)  # Buy tour ticket
visitor2.buy_ticket("special_event", 75)  # Buy special event ticket with group discount
visitor3.buy_ticket("exhibition", 70)  # Buy exhibition ticket
visitor4.buy_ticket("special_event", 120)  # Buy special event ticket with group discount
visitor5.buy_ticket("tour", 100)  # Buy tour ticket

# Display purchased tickets for visitors
visitor1.display_purchased_tickets()
visitor2.display_purchased_tickets()
visitor3.display_purchased_tickets()
visitor4.display_purchased_tickets()
visitor5.display_purchased_tickets()
