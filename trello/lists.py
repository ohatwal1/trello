import requests
import json
import trello as t


class Lists(object):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def new_list(self, name, idBoard, idListSource=None, pos=None):
        resp = requests.post("https://trello.com/1/lists".format(), params={"key": self.key, "token": self.token},
                             data={"name": name, "idBoard": idBoard, "idListSource": idListSource, "pos": pos})

        response = t.Response()
        response.handle_response(resp, "list name: " + name)
        return response

        # return json.loads(resp.text)
