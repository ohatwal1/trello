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


def create_label(label_name, label_color):
    label = Labels(key, token)
    response = label.new_label(label_name, label_color, boardId)
    return response.get(LABEL_ID)


def create_label(labels_to_create):
    created_labels = []
    labels_ = Labels(key, token)
    for l in labels_to_create:
        label_name, label_color = l.split(':')
        response = labels_.new_label(label_name, label_color, boardId)
        created_labels += [response.get(LABEL_ID)]
    return created_labels


def validate_inputs(available_columns, available_labels, input_column, input_labels):
    label_ids = []
    if input_column not in available_columns:
        column_id = create_column(input_column)
    else:
        column_id = available_columns[input_column]

    if len(input_labels) == 1:
        temp = list(input_labels)
        check = temp[0].split(":")
        if len(check) == 1:
            if check[0] in available_labels:
                label_ids.append(available_labels.get(check[0]))
                return column_id, label_ids
            else:
                label_ids.append(0)
                return column_id, label_ids

    input_not_available_labels = set(filter(lambda x: ':' in x, input_labels))
    input_available_labels = input_labels - input_not_available_labels
    label_ids += create_label(input_not_available_labels)
    label_ids += list(map(lambda x: available_labels[x], input_available_labels))

    return column_id, label_ids


def main():
    available_labels, available_columns = get_available_lists_and_labels()

    name_for_card, input_labels, input_column = get_inputs()

    column_id, label_ids = validate_inputs(available_columns, available_labels, input_column, input_labels)

    new_card = process_input(name_for_card, label_ids, column_id)

    print(new_card)


main()
