class Result(object):

    @staticmethod
    def result_data(result_code, result_data):
        final_result = ""
        if result_code == 200:
            final_result = "Status: " + str(result_code) + ", Body: " + str(result_data)
            return final_result
        else:
            final_result = "Status: " + str(result_code) + " Bad request" + ", Body :" + str(result_data)

        return final_result
