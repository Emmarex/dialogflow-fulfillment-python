import json

class DialogflowRequest:

    def __init__(self,webhook_request):
        self.request_data = json.loads(webhook_request)

    def get_response_id(self):
        return self.request_data["responseId"]

    def get_session(self):
        return self.request_data["session"]

    def get_session_id(self):
        return self.request_data["session"].split('/')[-1]

    def get_action(self):
        return self.request_data["queryResult"]["action"]

    def get_intent_name(self):
        return self.request_data["queryResult"]["intent"]["name"]

    def get_intent_displayName(self):
        return self.request_data["queryResult"]["intent"]["displayName"]

    def get_parameters(self):
        return self.request_data["queryResult"]["parameters"]

    def get_parameter(self,param_key):
        return self.request_data["queryResult"]["parameters"][param_key]

    def get_project_id(self):
        return self.request_data["session"].split('/')[1]
    
    def get_ouputcontext_list(self):
        return self.request_data["queryResult"]["outputContexts"]

    def get_single_ouputcontext(self,context_name):
        output_contexts = self.request_data["queryResult"]["outputContexts"]
        for context in output_contexts:
            if context["name"].split('/')[-1] == context_name:
                return context
        return dict()

    def get_user_token(self):
        return self.request_data['originalDetectIntentRequest']['payload']['user']['idToken']

    def get_chat_source(self):
        """
        Get the platform from which the user is interacting from
        """
        return self.request_data['originalDetectIntentRequest']['source']

    def get_chat_platform_payload(self):
        """
        Get the data been sent from the chat platform
        """
        return self.request_data['originalDetectIntentRequest']['payload']