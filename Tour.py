class Tour:
    def __init__(self, title, date, capacity, guide, location):
        self.title = title
        self.date = date
        self.capacity = capacity
        self.guide = guide
        self.location = location

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity

    def set_guide(self, guide):
        self.guide = guide

    def get_guide(self):
        return self.guide

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location