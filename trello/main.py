from trello import *

key = "1e6831b1f78b8934adc4a3da342be951"
token = "d787b3d2d19cb3428058f6e9556035bf2516360b605253483708a9a0732ca322"
boardId = "vEZnT5OC"


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
    column = input("Enter list for new card: ")
    return name_for_card, label, column


def main():
    available_labels, available_lists = get_available_lists_and_labels()

    name_for_card, label, column = get_inputs()

    card = Cards(key, token)
    new_card = card.new_card(name_for_card, column, label, available_labels, available_lists)

    print(new_card)


main()
