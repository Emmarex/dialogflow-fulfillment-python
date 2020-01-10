from collections import OrderedDict
import json

class TelegramSimpleResponse:

    def __init__(self, message):
        self.response = OrderedDict()
        simple_reponse = OrderedDict()
        responses_list = []
        responses_list.append(message)
        simple_reponse["text"] = responses_list
        self.response["text"] = simple_reponse
        self.response["platform"] = "TELEGRAM"