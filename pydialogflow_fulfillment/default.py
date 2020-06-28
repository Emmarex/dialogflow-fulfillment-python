from collections import OrderedDict


class TextResponse:
    def __init__(self, message):
        self.response = OrderedDict()
        simple_reponse = OrderedDict()
        responses_list = []
        responses_list.append(message)
        simple_reponse["text"] = responses_list
        self.response["text"] = simple_reponse
        self.response["platform"] = "DEFAULT"


class CustomPayloadResponse:
    def __init__(self, payload):
        self.response = OrderedDict()
        self.response["payload"] = payload
        self.response["platform"] = "DEFAULT"
