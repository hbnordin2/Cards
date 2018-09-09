#!flask/bin/python
import json
from flask import Flask, Response, request

from helloworld.Manager.DeckManager import DeckManager
from helloworld.Model.Card import Card
from helloworld.CardTable.CardTable import CardTable
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
    return Response(json.dumps({'Topic': flashCardTable.getCard("everything")}), mimetype='application/json', status=200)

@application.route('/getanycard', methods=['GET'])
def getAnyCard():
    deckManager = DeckManager("everything")
    return Response(json.dumps(deckManager.getNextCard().dictionary), status=200)

@application.route('/makecard', methods=['POST'])
def makeCard():
    try:
        flashCardTable = CardTable()
        card = Card(request.form)
        flashCardTable.insertCard(card)
        return Response(json.dumps(card.dictionary), status=200)
    except:
        return Response("Invalid Card", status=422)



if __name__ == '__main__':
    flaskrun(application)
