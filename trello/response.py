import json


class Response:

    def __init__(self):
        self.id = ''
        self.error_messages = ''
        self.response_body = {}
        self.response_status_code = ''
        self.created = False

    def set_id(self, valid_ids):
        self.id = valid_ids

    def set_error_messages(self, error_messages):
        self.error_messages = error_messages

    def handle_response(self, response, input_):
        """

        :param response: json payload
        :param string input_: card name
        :return: response
        """
        self.response_status_code = str(response.status_code)
        self.response_body = json.loads(response.text)
        if self.response_status_code == '200':
            self.id = self.response_body.get('id')
            self.created = True
        else:
            self.error_messages = "Status: " + self.response_status_code + " " + self.response_body.get('message') + \
                                  " with input: " + input_
            self.created = False

    def set_response(self, response):
        self.response_status_code = str(response.status_code)
        self.response_body = json.loads(response.text)

    def get_response(self):
        return "Status: " + self.response_status_code + ", Body: " + str(self.response_body)