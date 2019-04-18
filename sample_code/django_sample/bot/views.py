from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from pydialogflow_fulfillment import DialogflowResponse, DialogflowRequest, SimpleResponse, Suggestions

@csrf_exempt
def index_function(request):
    if request.method == "POST":
        if request.body:
            dialogflow_request = DialogflowRequest(request.body)
            if dialogflow_request.get_intent_displayName() == "welcome_intent":
                dialogflow_response = DialogflowResponse("Welcome to my test dialogflow webhook")
                dialogflow_response.add(SimpleResponse("Welcome to my test dialogflow webhook","Welcome to my test dialogflow webhook"))
                response = dialogflow_response.get_final_response()
            else:
                dialogflow_response = DialogflowResponse("Now that you are here. What can I help you with ?")
                dialogflow_response.add(Suggestions(["About","Sync","More info"]))
                response = dialogflow_response.get_final_response()
        else :
            response = {
                "error" : "1",
                "message" : "An error occurred."
            }
        return HttpResponse(response, content_type='application/json; charset=utf-8')
    else:
        raise Http404()