import requests
import json
import trello


class Lists(object):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def new_list(self, name, idBoard, idListSource=None, pos=None):
        resp = requests.post("https://trello.com/1/lists".format(), params={"key": self.key, "token": self.token},
                             data={"name": name, "idBoard": idBoard, "idListSource": idListSource, "pos": pos})

        result = trello.Result()
        result_code = resp.status_code
        result_data = resp.text

        display_result = result.result_data(result_code, json.loads(result_data))
        return display_result

        # return json.loads(resp.text)
