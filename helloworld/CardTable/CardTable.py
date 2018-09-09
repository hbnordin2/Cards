from helloworld.Dynamo.dynamo import DynamoTable

class CardTable(DynamoTable):
    def __init__(self):
        self.table = DynamoTable("Cards")

    def getEverything(self):
        return self.table.getItems()

    def insertCard(self, card):
        self.table.insertItem(card.dictionary)
        return card

    def helloWorld(self):
        print("Hello world")
