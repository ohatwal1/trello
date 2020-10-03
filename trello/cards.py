import requests
import trello as t


class Cards(object):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def new_card(self, input_message, column_id, label_ids, desc=None, pos=None, due=None, dueComplete=None,
                 idMembers=None,
                 urlSource=None, fileSource=None, idCardSource=None, keepFromSource=None):
        resp = requests.post("https://trello.com/1/cards".format(), params={"key": self.key, "token": self.token},
                             data={"name": input_message.get_card_name(), "idList": column_id, "desc": desc, "pos": pos, "due": due,
                                   "dueComplete": dueComplete, "idMembers": idMembers,
                                   "idLabels": label_ids,
                                   "urlSource": urlSource, "fileSource": fileSource, "idCardSource": idCardSource,
                                   "keepFromSource": keepFromSource})

        response_ = t.Response()
        response_.handle_response(resp, input_message.get_card_name())
        return response_

