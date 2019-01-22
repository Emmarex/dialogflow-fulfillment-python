from flask import Flask
from flask import request, abort
from pydialogflow_fulfillment import DialogflowResponse, DialogflowRequest, SimpleResponse, Suggestions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'POST':
        dialogflow_request = DialogflowRequest(request.data)
        if dialogflow_request.get_intent_displayName() == "welcome_intent":
            dialogflow_response = DialogflowResponse("Welcome to my test dialogflow webhook")
            dialogflow_response.add(SimpleResponse("Welcome to my test dialogflow webhook","Welcome to my test dialogflow webhook"))
            response = app.response_class(
                response=dialogflow_response.get_final_response(),
                mimetype='application/json'
            )
        else:
            dialogflow_response = DialogflowResponse("Now that you are here. What can I help you with ?")
            dialogflow_response.add(Suggestions(["About","Sync","More info"]))
            response = app.response_class(
                response=dialogflow_response.get_final_response(),
                mimetype='application/json'
            )
        return response
    else:
        abort(404)