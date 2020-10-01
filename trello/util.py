import pandas as pd


class Util(object):

    @staticmethod
    def available_labels(get_labels):

        labels_dict = {}
        for data in get_labels:
            labels_dict[data["color"]] = data["id"]

        labels_ = list(labels_dict.keys())
        print("|    Available Labels    |")
        s = '    |    '.join(labels_)
        print("-" * (len(s) + 10))
        print("|    " + s + "    |")
        print("-" * (len(s) + 10))

        return labels_dict

    @staticmethod
    def available_lists(get_lists):

        lists_dict = {}
        for data in get_lists:
            lists_dict[data["name"]] = data["id"]

        lists_ = list(lists_dict.keys())

        print("|    Available Lists    |")
        s = '    |    '.join(lists_)
        print("-" * (len(s) + 10))
        print("|    " + s + "    |")
        print("-" * (len(s) + 10))

        return lists_dict
