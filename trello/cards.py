import requests
import json


class Cards(object):

    def __init__(self, key, token):
        self.key = key
        self.token = token

    def new_card(self, name, idList, idLabels, label_dict, list_dict, desc=None, pos=None, due=None, dueComplete=None,
                 idMembers=None,
                 urlSource=None, fileSource=None, idCardSource=None, keepFromSource=None):

        if idLabels not in label_dict:
            return "invalid id label: " + idLabels
        if idList not in list_dict:
            return "invalid id list: " + idList
        else:
            resp = requests.post("https://trello.com/1/cards".format(), params={"key": self.key, "token": self.token},
                                 data={"name": name, "idList": list_dict[idList], "desc": desc, "pos": pos, "due": due,
                                       "dueComplete": dueComplete, "idMembers": idMembers,
                                       "idLabels": label_dict[idLabels],
                                       "urlSource": urlSource, "fileSource": fileSource, "idCardSource": idCardSource,
                                       "keepFromSource": keepFromSource})
            resp.raise_for_status()
            return json.loads(resp.text)
