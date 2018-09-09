#!flask/bin/python
import json
from flask import Flask, Response, request
from helloworld.CardTable.cardtable import CardTable
from helloworld.flaskrun import flaskrun

application = Flask(__name__)


@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)


@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)


@application.route('/getcard/<topic>', methods=['GET'])
def getCardWithTopic(topic):
    flashCardTable = CardTable()
    return Response(json.dumps({'Topic': flashCardTable.getCard("foo")}), mimetype='application/json', status=200)


@application.route('/makecard', methods=['POST'])
def makeCard():
    flashCardTable = CardTable()
    print(flashCardTable.getCard("foo"))
    flashCardTable.helloWorld()
    flashCardTable.insertCard(request.form["frontText"], request.form["backText"], request.form["topic"])


if __name__ == '__main__':
    flaskrun(application)
