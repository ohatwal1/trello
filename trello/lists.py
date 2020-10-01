import requests
import json


class Lists(object):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def new_list(self, name, idBoard, idListSource=None, pos=None):
        resp = requests.post("https://trello.com/1/lists".format(), params={"key": self.key, "token": self.token},
                             data={"name": name, "idBoard": idBoard, "idListSource": idListSource, "pos": pos})
        resp.raise_for_status()
        return json.loads(resp.text)
