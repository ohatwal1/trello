import requests
import json
from trello import *



class Cards(object):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def new_card(self, card_name, column_id, label_ids, boardId, desc=None, pos=None, due=None, dueComplete=None,
                 idMembers=None,
                 urlSource=None, fileSource=None, idCardSource=None, keepFromSource=None):


        # if idLabels not in label_dict:
        #     # Labels(self.key,self.token).new_label(label_name, idLabels, )
        #
        #     return "invalid id label: " + idLabels
        # if column_name not in list_dict:
        #     list = Lists(self)
        #     custom_list = list.new_list(column_name, boardId)


        resp = requests.post("https://trello.com/1/cards".format(), params={"key": self.key, "token": self.token},
                             data={"name": card_name, "idList": column_id, "desc": desc, "pos": pos, "due": due,
                                   "dueComplete": dueComplete, "idMembers": idMembers,
                                   "idLabels": label_ids,
                                   "urlSource": urlSource, "fileSource": fileSource, "idCardSource": idCardSource,
                                   "keepFromSource": keepFromSource})
        resp.raise_for_status()
        return json.loads(resp.text)
