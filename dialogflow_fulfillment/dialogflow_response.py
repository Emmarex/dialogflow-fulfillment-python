from collections import OrderedDict
import json
from response import SimpleResponse, Suggestions, SystemIntent

class DialogflowResponse:

    def __init__(self, fulfillment_message, webhook_source="webhook"):
        self.dialogflow_response = OrderedDict()
        self.response_payload = OrderedDict()
        self.rich_response = OrderedDict()
        self.google_payload = OrderedDict()
        self.expect_user_response = True
        self.dialogflow_response["fulfillmentText"] = fulfillment_message
        self.dialogflow_response["source"] = webhook_source

    def __str__(self):
        self.response_payload["google"] = self.google_payload
        self.dialogflow_response["payload"] = self.response_payload
        return json.dumps(self.dialogflow_response)

    def add(self, dialog_response):
        if isinstance(dialog_response, SimpleResponse):
            self.rich_response["items"] = dialog_response.response
        elif isinstance(dialog_response, Suggestions):
            self.rich_response["suggestions"] = dialog_response.response
        elif isinstance(dialog_response, SystemIntent):
            self.rich_response["systemIntent"] = dialog_response.response
        
        self.google_payload["richResponse"] = self.rich_response
        self.google_payload["expectUserResponse"] = self.expect_user_response