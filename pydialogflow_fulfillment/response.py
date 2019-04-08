from collections import OrderedDict
import json

class SimpleResponse:

    def __init__(self,display_text,text_to_speech):
        self.response = []
        single_simple_response = OrderedDict()
        simple_reponse = OrderedDict()
        simple_reponse["displayText"] = display_text
        simple_reponse["textToSpeech"] = text_to_speech
        single_simple_response["simpleResponse"] = simple_reponse
        self.response.append(single_simple_response)

class Suggestions:

    def __init__(self,suggestion_titles):
        self.response = []
        for item in range(0,len(suggestion_titles)):
            suggestion_dict = dict()
            suggestion_dict["title"] = suggestion_titles[item]
            self.response.append(suggestion_dict)

class SystemIntent:

    def __init__(self,intent):
        self.response = OrderedDict()
        self.response["intent"] = intent

class LinkOutSuggestion:

    def __init__(self,destination_name,destination_url):
        self.response = OrderedDict()
        self.response["destinationName"] = destination_name
        linkoutSuggestion_inner = dict()
        linkoutSuggestion_inner["url"] = destination_url
        self.response["openUrlAction"] = linkoutSuggestion_inner

class AskForSignin:

    def __init__(self):
        self.response = OrderedDict()
        self.response["intent"] = "actions.intent.SIGN_IN"
        self.response["inputValueData"] = dict()

class AskPermission:

    def __init__(self,permission_list,opt_context):
        self.response = OrderedDict()
        self.response["intent"] = "actions.intent.PERMISSION"
        permission_data = OrderedDict()
        permission_data["@type"] = "type.googleapis.com/google.actions.v2.PermissionValueSpec"
        permission_data["optContext"] = opt_context
        permission_data["permissions"] = [permission for permission in permission_list]
        self.response["data"] = permission_data

class Confirmation:

    def __init__(self,confirmation_text):
        self.response = OrderedDict()
        self.response["intent"] = "actions.intent.CONFIRMATION"
        confirmation_data = OrderedDict()
        confirmation_data["@type"] = "type.googleapis.com/google.actions.v2.ConfirmationValueSpec"
        dialog_spec = dict()
        dialog_spec["requestConfirmationText"] = confirmation_text
        confirmation_data["dialogSpec"] = dialog_spec
        self.response["data"] = confirmation_data

class RegisterUpdate:

    def __init__(self,intent_name,arguments,update_frequency):
        self.response = OrderedDict()
        self.response["intent"] = "actions.intent.REGISTER_UPDATE"
        register_update_data = OrderedDict()
        register_update_data["@type"] = "type.googleapis.com/google.actions.v2.RegisterUpdateValueSpec"
        register_update_data["intent"] = intent_name
        time_context = dict()
        time_context["frequency"] = update_frequency
        trigger_context = dict()
        trigger_context["timeContext"] = time_context
        register_update_data["triggerContext"] = trigger_context
        register_update_data["arguments"] = [arguments]
        self.response["data"] = register_update_data

class DateTime:

    def __init__(self,request_datetime_text,request_date_text,request_time_text):
        self.response = OrderedDict()
        self.response["intent"] = "actions.intent.DATETIME"
        date_time_data = OrderedDict()
        date_time_data["@type"] = "type.googleapis.com/google.actions.v2.DateTimeValueSpec"
        dialog_spec = dict()
        dialog_spec["requestDatetimeText"] = request_datetime_text
        dialog_spec["requestDateText"] = request_date_text
        dialog_spec["requestTimeText"] = request_time_text
        date_time_data["dialogSpec"] = dialog_spec
        self.response["data"] = date_time_data

class DeliveryAddress:

    def __init__(self,address_prompt_reason):
        self.response = OrderedDict()
        self.response["intent"] = "actions.intent.DELIVERY_ADDRESS"
        delivery_address_data = OrderedDict()
        delivery_address_data["@type"] = "type.googleapis.com/google.actions.v2.DeliveryAddressValueSpec"
        address_options = dict()
        address_options["reason"] = address_prompt_reason
        delivery_address_data["addressOptions"] = address_options
        self.response["data"] = delivery_address_data

class OutputContexts:
    def __init__(self,project_id,session_id,context_name,context_life_span, context_parameters):
        self.response = OrderedDict()
        self.response["name"] = f'projects/{project_id}/agent/sessions/{session_id}/contexts/{context_name}'
        self.response["lifespanCount"] = str(context_life_span)
        self.response["parameters"] = context_parameters

class Permissions:

    DEVICE_PRECISE_LOCATION = "DEVICE_PRECISE_LOCATION" # Ask for user"s precise location, lat/lng and formatted address
    DEVICE_COARSE_LOCATION = "DEVICE_COARSE_LOCATION" # Ask for user"s coarse location, zip code, city and country code. Works only from Google Home devices
    UPDATE = "UPDATE" # Ask for permissions to send updates
    NAME = "NAME" # Ask for user"s first and last name
    
class Frequency:
    ROUTINES = "ROUTINES"
    DAILY = "DAILY"