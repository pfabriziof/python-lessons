import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    """Custom deck of cards class.

    A custom deck of cards class implementing special methods like
    __len__ and __getitem__, so this class behaves as a normal
    Python sequence.
    """
    ranks = [str(n) for n in range (2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __steitem__(self):
        # will be implemented on chapter 13
        return

if __name__ == "__main__":
    deck = FrenchDeck()
    print(len(deck))

    print(deck[0])
    print(deck[-1])

    # No need to create a method to pick a random card,
    # python already has a function to get random item form a sequence
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))

    # but it gets better...
    print("\nSlicing the deck because __getitem__ delegates to the [] operator")
    print(deck[:3])
    print(deck[12::13])

    print("\n__getitem__ also allows us to iterate over the deck")
    for card in deck:
        # print(card)
        continue

    # iterating over it in reverse
    for card in reversed(deck):
        # print(card)
        continue
    # Iterator is often implicit. If a collection has no __contains__ method, the
    # in operator does a sequential scan.


    # How about sorting?
    print("\nHow about sorting? Let's rank the card system with aces being the highest")
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    for card in sorted(deck, key=spades_high):
        print(card)
