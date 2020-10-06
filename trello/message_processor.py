from trello import cards
from trello import validation


class MessageProcessor:

    def __init__(self, available_labels, available_columns):
        self.available_labels = available_labels
        self.available_columns = available_columns

    def process(self, input_message):
        validator = validation.Validation()
        validation_result = validator.validate(self.available_columns, self.available_labels, input_message)
        if validation_result.valid:
            response = self.process_input(input_message, validation_result.get_validated_list()).get_response()
        else:
            response = "Card not created"
            print(validation_result.get_error_list())

        return response

    def process_input(self, input_message, validated_data):
        card = cards.Cards(input_message.get_key(), input_message.get_token())
        label_ids, column_id = validated_data.get('label_ids'), validated_data.get('column_id')
        response = card.new_card(input_message, column_id, label_ids)
        return response

