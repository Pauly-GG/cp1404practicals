CURRENT_YEAR = 2021
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string for printing guitar class"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Gets the age of a guitar from the year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Shows whether the guitar is vintage or not"""
        return self.get_age() >= VINTAGE_AGE