import requests
import json
import trello


class Cards(object):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def new_card(self, card_name, column_id, label_ids, boardId, desc=None, pos=None, due=None, dueComplete=None,
                 idMembers=None,
                 urlSource=None, fileSource=None, idCardSource=None, keepFromSource=None):
        resp = requests.post("https://trello.com/1/cards".format(), params={"key": self.key, "token": self.token},
                             data={"name": card_name, "idList": column_id, "desc": desc, "pos": pos, "due": due,
                                   "dueComplete": dueComplete, "idMembers": idMembers,
                                   "idLabels": label_ids,
                                   "urlSource": urlSource, "fileSource": fileSource, "idCardSource": idCardSource,
                                   "keepFromSource": keepFromSource})

        result_code = resp.status_code
        # result_data = resp.text

        display_result = trello.Result().result_data(result_code, json.loads(resp.text))
        return display_result

        # return json.loads(resp.text)
