import random
import time

from src.Model.Constants import NEEDED_CARD_FIELDS


class Card:
    def __init__(self, form):
        self.cardId = None
        self.level = None
        self.front = None
        self.back = None
        self.lastSeen = None
        self.topics = None
        self.apply(form)
        self.dictionary = self.makeDictionary()

    def apply(self, form):
        for i in NEEDED_CARD_FIELDS:
            if i not in form.keys():
                raise Exception(i + " not in form")
        if "CardId" not in form.keys():
            self.cardId = str(hash(form['Front'] + form['Back'] + str(random.random())))
        else:
            self.cardId = form['CardId']
        if "Level" not in form.keys():
            self.level = str(5)
        else:
            self.level = form['Level']
        if "LastSeen" not in form.keys():
            self.lastSeen = str(int(time.time()))
        else:
            self.lastSeen = form['LastSeen']
        self.front = form['Front']
        self.back = form['Back']
        self.topics = form['Topics']

    def makeDictionary(self):
        return {"Level": self.level,
                "CardId": self.cardId,
                "Front": self.front,
                "Back": self.back,
                "LastSeen": self.lastSeen,
                "Topics": self.topics}