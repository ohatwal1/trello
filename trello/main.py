from trello import *
from trello.constants import *

key = "1e6831b1f78b8934adc4a3da342be951"
token = "d787b3d2d19cb3428058f6e9556035bf2516360b605253483708a9a0732ca322"
boardId = "5f741bd3fc46e569b4b65c2f"


def get_available_lists_and_labels():
    board = Boards(key, token)
    get_labels = board.get_label(boardId)
    get_lists = board.get_list(boardId)

    available_lists = Util.available_lists(get_lists)
    available_labels = Util.available_labels(get_labels)
    return available_labels, available_lists


def get_inputs():
    name_for_card = input("Enter card name: ")
    label = input("Enter label for new card: ")
    label = "".join(label.split())
    label_data = set(label.split(","))

    column = input("Enter list for new card: ")
    return name_for_card, label_data, column


def process_input(name_of_card, label_ids, column_id):
    card = Cards(key, token)
    new_card = card.new_card(name_of_card, column_id, label_ids, boardId)
    return new_card


def create_column(column):
    list_ = Lists(key, token)
    new_list = list_.new_list(column, boardId)
    return new_list.get(COLUMN_ID)


def create_label(labels_to_create):
    process_result = []
    labels_ = Labels(key, token)
    for l in labels_to_create:
        label_name, label_color = l.split(':')
        response_ = labels_.new_label(label_name, label_color, boardId)
        process_result += [response_]
    return process_result


def validate_inputs(available_columns, available_labels, input_column, input_labels):
    label_ids = []
    failed_labels = []
    if input_column not in available_columns:
        column_id = create_column(input_column)
    else:
        column_id = available_columns[input_column]

    input_not_available_labels = set(filter(lambda x: ':' in x, input_labels))
    process_result = create_label(input_not_available_labels)
    for r in process_result:
        if r.created:
            label_ids += [r.id]
        else:
            failed_labels += [r.error_messages]

    input_available_labels = input_labels - input_not_available_labels
    for input_available_label in input_available_labels:
        if available_labels.get(input_available_label) is not None:
            label_ids += [available_labels[input_available_label]]
        else:
            failed_labels += ['Invalid label name: ' + input_available_label]

    label_validation_result = {True: label_ids, False: failed_labels}
    return column_id, label_validation_result


def main():
    available_labels, available_columns = get_available_lists_and_labels()

    name_for_card, input_labels, input_column = get_inputs()

    column_id, label_validation_result = validate_inputs(available_columns, available_labels, input_column,
                                                         input_labels)
    if label_validation_result[False] is None or len(label_validation_result[False]) == 0:
        new_card = process_input(name_for_card, label_validation_result[True], column_id)
    else:
        new_card = "Card not created"
        print(label_validation_result[False])

    print(new_card)


main()
