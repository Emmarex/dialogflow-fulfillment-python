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