class Message:
    def __init__(self):
        self.__labels = []
        self.__columns = ''
        self.__card_name = ''
        self.__board_id = ''
        self.__key = ''
        self.__token = ''

    def get_labels(self):
        return self.__labels

    def get_columns(self):
        return self.__columns

    def get_card_name(self):
        return self.__card_name

    def get_board_id(self):
        return self.__board_id

    def get_key(self):
        return self.__key

    def get_token(self):
        return self.__token

    def set_labels(self, labels):
        self.__labels = labels
        return self

    def set_columns(self, columns):
        self.__columns = columns
        return self

    def set_card_name(self, card_name):
        self.__card_name = card_name
        return self

    def set_board_id(self, board_id):
        self.__board_id = board_id
        return self

    def set_key(self, key):
        self.__key = key
        return self

    def set_token(self, token):
        self.__token = token
        return self
