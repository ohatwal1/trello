import requests
import json


class Labels(object):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def new_label(self, name, color, idBoard):
        resp = requests.post("https://trello.com/1/labels".format(), params={"key": self.key, "token": self.token},
                             data={"name": name, "color": color, "idBoard": idBoard})
        resp.raise_for_status()
        return json.loads(resp.text)

    # Valid values: yellow, purple, blue, red, green, orange, black, sky, pink, lime