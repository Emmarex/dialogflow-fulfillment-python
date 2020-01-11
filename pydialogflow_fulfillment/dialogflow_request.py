import json

class DialogflowRequest:

    def __init__(self, webhook_request):
        """
        webhook_request: str, bytes containing Json
        """
        self.request_data = json.loads(webhook_request)

    def get_response_id(self):
        """
        Get the current response ID

        returns str
        """
        return self.request_data["responseId"]

    def get_session(self):
        """
        Get the current session

        returns a str

        e.g 'projects/pyconafrica2019-axsuml/agent/environments/__aog-7/users/-/sessions/ABwppHHEDZveVRxc8W_xk_TZdo4JT2onlvWKBehKW_PYDh2Eznhl7DsX8972SQJTBqKLgBCzyzq3dedjiqkSQ6wm5v57Rg'
        """
        return self.request_data["session"]

    def get_session_id(self):
        """
        Get the current session ID

        returns a str

        e.g 'ABwppHHEDZveVRxc8W_xk_TZdo4JT2onlvWKBehKW_PYDh2Eznhl7DsX8972SQJTBqKLgBCzyzq3dedjiqkSQ6wm5v57Rg'
        """
        return self.request_data["session"].split('/')[-1]

    def get_action(self):
        return self.request_data["queryResult"]["action"]

    def get_intent_name(self):
        """
        Get the name of the current intent

        returns a str

        e.g: 'projects/pyconafrica2019-axsuml/agent/intents/02001f63-cac8-418a-8ee7-ec1a45c4d49f'
        """
        return self.request_data["queryResult"]["intent"]["name"]

    def get_intent_displayName(self):
        """
        Get the display name of the current intent

        returns a str
        e.g 'Default Welcome Intent'
        """
        return self.request_data["queryResult"]["intent"]["displayName"]

    def get_parameters(self):
        """
        Get all parameters sent from dialogflow

        returns a dict
        """
        return self.request_data["queryResult"]["parameters"]

    def get_parameter(self, param_key):
        """
        Get a single parameter value sent from dialogflow
        param_key: str
        """
        return self.request_data["queryResult"]["parameters"][param_key]

    def get_project_id(self):
        """
        Get the current project ID

        returns the project ID as a string
        """
        return self.request_data["session"].split('/')[1]
    
    def get_ouputcontext_list(self):
        """
        Get list of output contexts

        returns a list of output contexts
        """
        return self.request_data["queryResult"]["outputContexts"]

    def get_single_ouputcontext(self, context_name):
        """
        Get a single output context

        required:
        context_name: str

        returns a dict
        """
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
        e.g google, telegram, facebook

        returns a string
        """
        return self.request_data['originalDetectIntentRequest']['source']

    def get_chat_platform_payload(self):
        """
        Get the data been sent from the chat platform

        returns a dict
        """
        return self.request_data['originalDetectIntentRequest']['payload']