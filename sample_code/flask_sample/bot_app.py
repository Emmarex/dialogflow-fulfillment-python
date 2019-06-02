from flask import Flask, request, abort, jsonify
from pydialogflow_fulfillment import DialogflowResponse, DialogflowRequest, SimpleResponse, Suggestions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'POST':
        print('post')
        dialogflow_request = DialogflowRequest(request.data)
        if dialogflow_request.get_intent_displayName() == "welcome_intent":
            dialogflow_response = DialogflowResponse("Welcome to my test dialogflow webhook")
            dialogflow_response.add(SimpleResponse("Welcome to my test dialogflow webhook","Welcome to my test dialogflow webhook"))
            response = jsonify(dialogflow_response.get_final_response())
        else:
            dialogflow_response = DialogflowResponse()
            dialogflow_response.add(SimpleResponse("Welcome to my test dialogflow webhook","Welcome to my test dialogflow webhook"))
            dialogflow_response.add(Suggestions(["About","Sync","More info"]))
            response = jsonify(dialogflow_response.get_final_response())
            print(dialogflow_response.get_final_response())
        return response
    else:
        print('404')
        abort(404)