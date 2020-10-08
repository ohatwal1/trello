import requests
import json
import trello as t


class Lists(object):

    def __init__(self, key, token, board_id):
        self.key = key
        self.token = token
        self.board_id = board_id

    def new_list(self, name, idListSource=None, pos=None):
        """

        :param string name: column name
        :param string idListSource: optional
        :param [string] pos: optional
        :return: response payload json
        """
        resp = requests.post("https://trello.com/1/lists".format(), params={"key": self.key, "token": self.token},
                             data={"name": name, "idBoard": self.board_id, "idListSource": idListSource, "pos": pos})

        response = t.Response()
        response.handle_response(resp, "list name: " + name)
        return response

        # return json.loads(resp.text)

    def create_list(self, column):
        """

        :param string column: column id
        :return: response payload in json
        """
        response_ = self.new_list(column)
        return response_
