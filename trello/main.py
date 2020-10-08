from trello import boards, message, lists, labels, util, message_processor

key = "1e6831b1f78b8934adc4a3da342be951"
token = "d787b3d2d19cb3428058f6e9556035bf2516360b605253483708a9a0732ca322"


def get_available_lists_and_labels(board_id):
    """

    :param board_id: string
    :return: list of available labels and columns
    """
    board = boards.Boards(key, token)
    get_labels = board.get_label(board_id)
    get_lists = board.get_list(board_id)

    available_lists = util.Util.available_lists(get_lists)
    available_labels = util.Util.available_labels(get_labels)
    return available_labels, available_lists


def get_inputs(board_id):
    """

    :param string board_id: id of board on which card is going to add
    :return: message attributes including name, label, column, board id, key, token
    """
    name_for_card = input("Enter card name: ")
    label = input("Enter label for new card: ")
    # label = "".join(label.split())
    label_data = set(map(lambda s: s.strip(), label.split(",")))

    column = input("Enter column for new card: ")

    message_ = message.Message().set_card_name(name_for_card).set_labels(label_data) \
        .set_columns(column) \
        .set_board_id(board_id) \
        .set_key(key) \
        .set_token(token)

    return message_


def main():
    board_id = "5f741bd3fc46e569b4b65c2f"
    available_labels, available_columns = get_available_lists_and_labels(board_id)

    input_message = get_inputs(board_id)

    processor = message_processor.MessageProcessor(available_labels, available_columns)
    response = processor.process(input_message)

    print(response)


if __name__ == "__main__":
    main()
