class Message:
    def __init__(self, labels, columns, card_name, board_id):
        self._labels = labels
        self._columns = columns
        self._card_name = card_name
        self._board_id = board_id

    def get_labels(self):
        return