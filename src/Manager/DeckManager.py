from src.Model.Deck import Deck
from src.Model.Card import Card
from src.CardTable.CardTable import CardTable

class DeckManager:
    def __init__(self, topic):
        cardTable = CardTable()
        allCards = cardTable.getEverything()
        self.cards = []
        self.setRelevantCards(topic, allCards)

        if len(self.cards) == 0:
            raise Exception("No relevant cards")

        self.deck = Deck(self.cards)

    def setRelevantCards(self, topic, allCards):
        if topic == "everything":
            for i in allCards:
                self.cards.append(Card(i))
        else:
            for i in allCards:
                if i["Topics"] == topic:
                    self.cards.append(Card(i))

    def getNextCard(self):
        return self.deck.getNextCard()