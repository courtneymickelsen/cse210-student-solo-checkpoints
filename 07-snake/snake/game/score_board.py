import random
from game.actor import Actor
from game.point import Point

class ScoreBoard(Actor):
    """Points earned. The responsibility of the ScoreBoard is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self._score = 0
        position = Point(1, 0)
        self.set_position(position)
        self.set_text(f"Score: {self._score}")

    def calculate_points(word):
        """Calculates the amount of points for each given word.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The amount of points for the given word.
        """
        points = 0

        for i in range(len(word)):
            points+= 1

        return points
    
    def add_points(self, word):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        points = self.calculate_points(word)
        self._score += points
        self.set_text(f"Score: {self._score}")

    def subtract_points(self, word):
        """Subtracts the given points from the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        points = self.calculate_points(word)
        self._score -= points
        self.set_text(f"Score: {self._score}")
 