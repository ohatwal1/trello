class ValidateResult():
    def __init__(self):
        self.error_list = []
        self.validated_data_map = {}
        self.valid = False

    def get_error_list(self):
        return self.error_list

    def get_validated_list(self):
        return self.validated_data_map

    def is_valid(self):
        return self.valid

    def set_error_list(self, error_list):
        self.error_list += error_list

    def set_validated_data_map(self, data_type, data):
        self.validated_data_map[data_type] = data

    def set_valid(self, valid):
        self.valid = valid