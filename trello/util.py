class Util(object):

    @staticmethod
    def available_labels(get_labels):
        """

        :param list get_labels: available labels
        :return: dict with mapping of key:name of label and value:id of label
        """

        labels_dict = {}
        for data in get_labels:
            if data.get('name') is not None and data.get('name') != '':
                labels_dict[data["name"]] = data['id']
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
        """

        :param list get_lists:available lists
        :return: dict with mapping of key:name of list and value:id of list
        """
        lists_dict = {}
        for data in get_lists:
            lists_dict[data["name"]] = data["id"]

        lists_ = list(lists_dict.keys())
        print("")
        a = '|    Available Lists    |'
        print("-" * len(a))
        print(a)
        s = '    |    '.join(lists_)
        print("-" * (len(s) + 10))
        print("|    " + s + "    |")
        print("-" * (len(s) + 10))

        return lists_dict
