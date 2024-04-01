class Exhibition:
    def __init__(self, title, location, duration, artworks):
        self.title = title
        self.location = location
        self.duration = duration
        self.artworks = artworks

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_duration(self, duration):
        self.duration = duration

    def get_duration(self):
        return self.duration

    def set_artworks(self, artworks):
        self.artworks = artworks

    def get_artworks(self):
        return self.artworks

