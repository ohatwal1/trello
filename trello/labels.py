import requests
import trello as t


class Labels(object):

    def __init__(self, key, token, board_id):
        self.key = key
        self.token = token
        self.board_id = board_id

    def new_label(self, name, color):
        resp = requests.post("https://trello.com/1/labels".format(), params={"key": self.key, "token": self.token},
                             data={"name": name, "color": color, "idBoard": self.board_id})

        response = t.Response()
        response.handle_response(resp, "name: " + name + " color: " + color)
        return response

    # Valid values: yellow, purple, blue, red, green, orange, black, sky, pink, lime

    def create_labels(self, labels_to_create):
        process_result = []
        for l in labels_to_create:
            label_name, label_color = l.split(':')
            response_ = self.new_label(label_name, label_color)
            process_result += [response_]
        return process_result