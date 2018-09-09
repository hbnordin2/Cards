
class Deck:
    def __init__(self, cards):
        cards.sort(key=lambda x: int(x.lastSeen), reverse=True)
        self.cards = cards

    def getNextCard(self):
        return self.cards[0]
