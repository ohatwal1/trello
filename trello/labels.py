import requests
import trello as t


class Labels(object):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def new_label(self, name, color, idBoard):
        resp = requests.post("https://trello.com/1/labels".format(), params={"key": self.key, "token": self.token},
                             data={"name": name, "color": color, "idBoard": idBoard})

        response = t.Response()
        response.handle_response(resp, name, color)
        return response

    # Valid values: yellow, purple, blue, red, green, orange, black, sky, pink, lime
