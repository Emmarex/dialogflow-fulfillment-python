# Dialogflow Fulfillment Python

[![PyPI version](https://badge.fury.io/py/pydialogflow-fulfillment.svg)](https://badge.fury.io/py/pydialogflow-fulfillment)

The <a href="https://dialogflow.com/docs/fulfillment" target="_blank">Dialogflow Fulfillment Library</a> allows you to connect natural language understanding and processing to your own systems, APIs, and databases. Using Fulfillment, you can surface commands and information from your services to your users through a natural conversational interface.

This Library makes creating fulfillment for Dialogflow v2 agents with <a href="https://www.djangoproject.com" target="_blank">Django</a> or <a href="http://flask.pocoo.org" target="_blank">Flask</a> easy and simple.

## Supported Features

<ol>
    <li>Simple Response</li>
    <li>System Intent</li>
    <li>Suggestions</li>
    <li>Link out Suggestion</li>
    <li>Google Assistant Signin</li>
    <li>Permissions</li>
</ol>

## Quick Start

1. <a href="https://console.dialogflow.com/api-client/#/login" target="_blank">Login or Create a Dialogflow Account</a>
2. Create a Dialogflow agent or import samples
3. Setup your Django or Flask API</a>
4. Install this library from Pip using `pip install pydialogflow-fulfillment`
5. Go to <b>Fulfillment > Enable Webhook > Enter the url for your API > Enable webhook for all domains</b> 

## Examples

### Dialogflow Request

```
from pydialogflow_fulfillment import DialogflowRequest

dialog_fulfillment = DialogflowRequest(request.body)

# get intent name
print(dialog_fulfillment.get_intent_name())
# get intent display name
print(dialog_fulfillment.get_intent_displayName())

# get a parameter from Google Assistant request 
print(dialog_fulfillment.get_paramter("param")) # single parameter
print(dialog_fulfillment.get_paramters()) # all parameters

```

### Dialogflow Response

```
from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import SimpleResponse, Suggestions, SystemIntent

dialogflow_response = DialogflowResponse("This is a text response")
dialogflow_response.add(SimpleResponse("This is a simple text response","This is a simple text response"))
dialogflow_response.add(Suggestions(["Help","About","Sync"]))
dialogflow_response.add(SystemIntent("another_dialogflow_intent_name"))

dialogflow_response.add(LinkOutSuggestion("DialogFlow Website","http://dialogflow.com"))

dialogflow_response.expect_user_response = False

print(dialogflow_response)
```

### Google Assistant Signin

```
dialogflow_response = DialogflowResponse("PLACEHOLDER_FOR_SIGN_IN")
dialogflow_response.add(AskForSignin())

print(dialogflow_response)
```

### Permissions

```
dialogflow_response = DialogflowResponse("PLACEHOLDER_FOR_PERMISSION")
dialogflow_response.add(AskPermission(["DEVICE_PRECISE_LOCATION","NAME"],"To just know better"))

print(dialogflow_response)
```



## License
See LICENSE.md.