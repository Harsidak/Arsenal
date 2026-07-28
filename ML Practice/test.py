import collections
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDesk:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]  
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDesk()
print(choice(deck))