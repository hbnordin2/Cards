from helloworld.Dynamo.dynamo import DynamoTable

class CardTable(DynamoTable):
    def __init__(self):
        self.table = DynamoTable("Cards")

    def getCard(self, topic):
        return self.table.getItems()

    def insertCard(self, frontText, backText, topic):
        self.table.insertItem({"cardId":hash(frontText + backText + topic), "frontText":frontText, "backText":backText})

    def helloWorld(self):
        print("Hello world")
