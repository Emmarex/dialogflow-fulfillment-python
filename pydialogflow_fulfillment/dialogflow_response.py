from collections import OrderedDict
import json
from pydialogflow_fulfillment.response import *

class DialogflowResponse:

    def __init__(self, fulfillment_message="", webhook_source="webhook"):
        self.dialogflow_response = OrderedDict()
        self.response_payload = OrderedDict()
        self.rich_response = OrderedDict()
        self.google_payload = OrderedDict()
        self.expect_user_response = True
        self.output_contexts = []
        self.dialogflow_response["fulfillmentText"] = fulfillment_message
        self.dialogflow_response["source"] = webhook_source

    def __str__(self):
        self.response_payload["google"] = self.google_payload
        self.dialogflow_response["outputContexts"] = self.output_contexts
        self.dialogflow_response["payload"] = self.response_payload
        return json.dumps(self.dialogflow_response)

    def get_final_response(self):
        self.response_payload["google"] = self.google_payload
        self.dialogflow_response["outputContexts"] = self.output_contexts
        self.dialogflow_response["payload"] = self.response_payload
        return json.dumps(self.dialogflow_response)

    def add(self, dialog_response):
        if isinstance(dialog_response, SimpleResponse):
            self.rich_response["items"] = dialog_response.response
        elif isinstance(dialog_response, Suggestions):
            self.rich_response["suggestions"] = dialog_response.response
        elif isinstance(dialog_response, SystemIntent):
            self.rich_response["systemIntent"] = dialog_response.response
        elif isinstance(dialog_response, LinkOutSuggestion):
            self.rich_response["linkOutSuggestion"] = dialog_response.response
        elif isinstance(dialog_response, AskForSignin):
            self.google_payload["systemIntent"] = dialog_response.response
            self.google_payload["expectUserResponse"] = self.expect_user_response
            fulfillment_message = OrderedDict()
            fulfillment_message["displayText"] = "PLACEHOLDER_FOR_SIGN_IN"
            fulfillment_message["textToSpeech"] = "PLACEHOLDER_FOR_SIGN_IN"
            self.dialogflow_response["fulfillmentText"] = fulfillment_message
        elif isinstance(dialog_response, AskPermission):
            self.google_payload["systemIntent"] = dialog_response.response
            self.google_payload["expectUserResponse"] = self.expect_user_response
            fulfillment_message = OrderedDict()
            fulfillment_message["displayText"] = "PLACEHOLDER_FOR_PERMISSION"
            fulfillment_message["textToSpeech"] = "PLACEHOLDER_FOR_PERMISSION"
            self.dialogflow_response["fulfillmentText"] = fulfillment_message
        elif isinstance(dialog_response, Confirmation):
            self.google_payload["systemIntent"] = dialog_response.response
            self.google_payload["expectUserResponse"] = self.expect_user_response
        elif isinstance(dialog_response, RegisterUpdate):
            self.add(SimpleResponse("PLACEHOLDER","PLACEHOLDER"))
            self.google_payload["systemIntent"] = dialog_response.response
            self.google_payload["expectUserResponse"] = self.expect_user_response
        elif isinstance(dialog_response, DateTime):
            self.add(SimpleResponse("PLACEHOLDER","PLACEHOLDER"))
            self.google_payload["systemIntent"] = dialog_response.response
            self.google_payload["expectUserResponse"] = self.expect_user_response
        elif isinstance(dialog_response, DeliveryAddress):
            self.add(SimpleResponse("PLACEHOLDER","PLACEHOLDER"))
            self.google_payload["systemIntent"] = dialog_response.response
            self.google_payload["expectUserResponse"] = self.expect_user_response
        elif isinstance(dialog_response, OutputContexts):
            self.output_contexts.append(dialog_response.response)
        
        self.google_payload["richResponse"] = self.rich_response
        self.google_payload["expectUserResponse"] = self.expect_user_response