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
