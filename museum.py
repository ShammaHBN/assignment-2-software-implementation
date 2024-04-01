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