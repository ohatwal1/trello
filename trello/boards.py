import requests
import json


class Boards(object):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def get_board(self, board_id, fields=None):
        """

        :param string board_id: required field
        :param string fields: optional
        :return: response payload in json, payload
        """
        resp = requests.get("https://trello.com/1/boards/{}".format(board_id),
                            params={"key": self.key, "token": self.token, "fields": fields}, data=None)

        return json.loads(resp.text)

    def get_label(self, board_id, fields=None, limit=None):
        """

        :param string board_id: required field
        :param string fields: optional
        :param string limit: optional
        :return: response payload in json format
        """
        resp = requests.get("https://trello.com/1/boards/{}/labels".format(board_id),
                            params={"key": self.key, "token": self.token, "fields": fields, "limit": limit},
                            data=None)

        return json.loads(resp.text)

    def get_list(self, board_id, cards=None, card_fields=None, filter=None, fields=None):
        """

        :param string board_id: required field
        :param string cards: optional
        :param string card_fields: optional
        :param string filter: optional
        :param string fields: optional
        :return: response payload in json format
        """
        resp = requests.get("https://trello.com/1/boards/{}/lists".format(board_id),
                            params={"key": self.key, "token": self.token, "cards": cards,
                                    "card_fields": card_fields, "filter": filter, "fields": fields}, data=None)

        return json.loads(resp.text)
