import requests
import json
import trello


class Labels(object):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def new_label(self, name, color, idBoard):
        resp = requests.post("https://trello.com/1/labels".format(), params={"key": self.key, "token": self.token},
                             data={"name": name, "color": color, "idBoard": idBoard})

        result = trello.Result()
        result_code = resp.status_code
        result_data = resp.text

        display_result = result.result_data(result_code, json.loads(result_data))
        return display_result

    # Valid values: yellow, purple, blue, red, green, orange, black, sky, pink, lime
