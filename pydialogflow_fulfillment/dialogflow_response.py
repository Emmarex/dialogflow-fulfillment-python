from collections import OrderedDict
import json
from pydialogflow_fulfillment.response import *
from pydialogflow_fulfillment.telegram_response import *
from pydialogflow_fulfillment.default import *

class DialogflowResponse:

    def __init__(self, fulfillment_message="", webhook_source="webhook"):
        self.dialogflow_response = OrderedDict()
        self.response_payload = OrderedDict()
        self.rich_response = OrderedDict()
        self.google_payload = OrderedDict()
        self.fulfillment_messages = []
        self.expect_user_response = True
        self.output_contexts = []
        self.dialogflow_response["fulfillmentText"] = fulfillment_message
        self.dialogflow_response["fulfillmentMessages"] = self.fulfillment_messages
        self.dialogflow_response["source"] = webhook_source

    def __str__(self):
        self.response_payload["google"] = self.google_payload
        self.dialogflow_response["fulfillmentMessages"] = self.fulfillment_messages
        self.dialogflow_response["outputContexts"] = self.output_contexts
        self.dialogflow_response["payload"] = self.response_payload
        return json.dumps(self.dialogflow_response)

    def get_final_response(self):
        self.response_payload["google"] = self.google_payload
        self.dialogflow_response["fulfillmentMessages"] = self.fulfillment_messages
        self.dialogflow_response["outputContexts"] = self.output_contexts
        self.dialogflow_response["payload"] = self.response_payload
        return json.dumps(self.dialogflow_response)

    def add(self, dialog_response):
        """
        Add a response to a dialogflow response
        """
        if isinstance(dialog_response, SimpleResponse):
            if 'items' in self.rich_response.keys():
                self.rich_response['items'] += dialog_response.response
            else:
                self.rich_response["items"] = dialog_response.response
        elif isinstance(dialog_response, Suggestions):
            self.rich_response["suggestions"] = dialog_response.response
        elif isinstance(dialog_response, SystemIntent):
            self.rich_response["systemIntent"] = dialog_response.response
        elif isinstance(dialog_response, LinkOutSuggestion):
            self.rich_response["linkOutSuggestion"] = dialog_response.response
        elif isinstance(dialog_response, AskForSignin):
            self.add(SimpleResponse("PLACEHOLDER","PLACEHOLDER"))
            self.google_payload["systemIntent"] = dialog_response.response
            self.google_payload["expectUserResponse"] = self.expect_user_response
            fulfillment_message = OrderedDict()
            fulfillment_message["displayText"] = "PLACEHOLDER"
            fulfillment_message["textToSpeech"] = "PLACEHOLDER"
            self.dialogflow_response["fulfillmentText"] = fulfillment_message
        elif isinstance(dialog_response, AskPermission):
            self.add(SimpleResponse("PLACEHOLDER","PLACEHOLDER"))
            self.google_payload["systemIntent"] = dialog_response.response
            self.google_payload["expectUserResponse"] = self.expect_user_response
            fulfillment_message = OrderedDict()
            fulfillment_message["displayText"] = "PLACEHOLDER_FOR_PERMISSION"
            fulfillment_message["textToSpeech"] = "PLACEHOLDER_FOR_PERMISSION"
            self.dialogflow_response["fulfillmentText"] = fulfillment_message
        elif isinstance(dialog_response, Confirmation):
            self.add(SimpleResponse("PLACEHOLDER","PLACEHOLDER"))
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
        elif isinstance(dialog_response, Table):
            self.rich_response['items'].append(dialog_response.response)
        elif isinstance(dialog_response, UserStorage):
            self.google_payload['userStorage'] = str(dialog_response.response)
        # telegram responses
        elif isinstance(dialog_response, TelegramSimpleResponse):
            self.fulfillment_messages.append(dialog_response.response) 
        elif isinstance(dialog_response, TelegramKeyboardButtonResponse):
            self.fulfillment_messages.append(dialog_response.response)
        elif isinstance(dialog_response, TelegramMessageResponse):
            self.fulfillment_messages.append(dialog_response.response)
        # default responses
        elif isinstance(dialog_response, TextResponse):
            self.fulfillment_messages.append(dialog_response.response)
        elif isinstance(dialog_response, CustomPayloadResponse):
            self.fulfillment_messages.append(dialog_response.response)
        
        self.google_payload["richResponse"] = self.rich_response
        self.google_payload["expectUserResponse"] = self.expect_user_response