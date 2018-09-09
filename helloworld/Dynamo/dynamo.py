import boto3

class DynamoTable:
    def __init__(self, tableName):
        self.tableName = tableName

        self.dynamodb = boto3.resource('dynamodb',region_name='ap-southeast-2')
        self.table = self.dynamodb.Table(tableName)

    def getEverything(self):
        return self.table.scan()

    def getItems(self):
        return self.table.scan()["Items"]

    def insertItem(self, item):
        self.dynamodb.put_item(TableName=self.tableName, Item=item)