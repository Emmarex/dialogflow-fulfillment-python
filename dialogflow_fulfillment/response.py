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

class Permissions:

    DEVICE_PRECISE_LOCATION = "DEVICE_PRECISE_LOCATION" # Ask for user's precise location, lat/lng and formatted address
    DEVICE_COARSE_LOCATION = "DEVICE_COARSE_LOCATION" # Ask for user's coarse location, zip code, city and country code. Works only from Google Home devices
    UPDATE = "UPDATE" # Ask for permissions to send updates
    NAME = "NAME" # Ask for user's first and last name

class AskPermission:

    def __init__(self,permission_list,opt_context):
        self.response = OrderedDict()
        self.response["intent"] = "actions.intent.PERMISSION"
        permission_data = OrderedDict()
        permission_data["@type"] = 'type.googleapis.com/google.actions.v2.PermissionValueSpec'
        permission_data["optContext"] = opt_context
        permission_data["permissions"] = [permission for permission in permission_list]
        self.response["data"] = permission_data

