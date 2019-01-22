import json

class DialogflowRequest:

    def __init__(self,webhook_request):
        self.request_data = json.loads(webhook_request)

    def get_response_id(self):
        return self.request_data["responseId"]

    def get_session(self):
        return self.request_data["session"]

    def get_intent_name(self):
        return self.request_data["queryResult"]["intent"]["name"]

    def get_intent_displayName(self):
        return self.request_data["queryResult"]["intent"]["displayName"]

    def get_paramters(self):
        return self.request_data["queryResult"]["parameters"]

    def get_paramter(self,param_key):
        return self.request_data["queryResult"]["parameters"][param_key]