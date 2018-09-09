import boto3

class DynamoTable:
    def __init__(self, tableName):
        self.tableName = tableName

        dynamodb = boto3.resource('dynamodb',region_name='ap-southeast-2')
        self.table = dynamodb.Table(tableName)

    def getEverything(self):
        return self.table.scan()

    def getItems(self):
        return self.table.scan()["Items"]