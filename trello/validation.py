from trello import validation_result
from trello import lists, labels


class Validation():

    def validate(self, available_columns, available_labels, input_message):
        result = validation_result.ValidateResult()

        result = self.__validate_column(input_message, available_columns, result)
        result = self.__validate_label(input_message, available_labels, result)
        return result

    def __validate_column(self, input_message, available_columns, result):
        input_column = input_message.get_columns()
        if input_column not in available_columns:
            list_ = lists.Lists(input_message.get_key(), input_message.get_token(), input_message.get_board_id())
            column_response = list_.create_list(input_message.get_columns())
            if column_response.created:
                column_id = column_response.id
            else:
                column_id = ''
                result.set_valid(False)
                result.set_error_list(column_response.error_messages)
        else:
            column_id = available_columns[input_column]

        result.set_validated_data_map('column_id', column_id)
        return result

    def __validate_label(self, input_message, available_labels, result):
        input_labels = input_message.get_labels()
        board_id = input_message.get_board_id()

        label_ids = []
        input_not_available_labels = set(filter(lambda x: ':' in x, input_labels))
        labels_ = labels.Labels(input_message.get_key(), input_message.get_token(), board_id)
        process_result = labels_.create_labels(input_not_available_labels)
        for r in process_result:
            if r.created:
                label_ids += [r.id]
            else:
                result.set_error_list([r.error_messages])
        result.set_valid(all(map(lambda r: r.created, process_result)))

        input_available_labels = input_labels - input_not_available_labels
        for input_available_label in input_available_labels:
            if available_labels.get(input_available_label) is not None:
                label_ids += [available_labels[input_available_label]]
            else:
                result.set_error_list(['Invalid label name: ' + input_available_label])
                result.set_valid(False)

        result.set_validated_data_map('label_ids', label_ids)
        return result
