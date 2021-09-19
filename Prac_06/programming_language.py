class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year


def __str__(self):
    """Returns a string for ProgrammingLanguage"""
    return "{}, {} Typing, Reflection={}, First appeared in {}".format(
        self.name, self.typing, self.reflection, self.year)


 def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"