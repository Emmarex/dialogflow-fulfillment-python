# Dialogflow Fulfillment Python


The <a href="">Dialogflow Fulfillment Library</a> allows you to connect natural language understanding and processing to your own systems, APIs, and databases. Using Fulfillment, you can surface commands and information from your services to your users through a natural conversational interface.

This Library makes creating fulfillment for Dialogflow v2 agents with <a href="">Django</a> or <a href="">Flask</a> easy and simple.

## Supported Features

<ol>
    <li>Simple Response</li>
    <li>System Intent</li>
    <li>Suggestions</li>
    <li>Cards</li>
</ol>

## Quick Start

1. <a href="https://console.dialogflow.com/api-client/#/login">Login or Create a Dialogflow Account</a>
2. Create a Dialogflow agent or import samples
3. Setup your Django or Flask API</a>
4. Install this library from Pip using `pip install dialogflow_fulfillment`
5. Go to <b>Fulfillment > Enable Webhook > Enter the url for your API > Enable webhook for all domains</b> 

## Examples

```
from dialogflow_fulfillment import DialogflowResponse
from dialogflow_fulfillment import SimpleResponse, Suggestions, SystemIntent

dialogflow_response = DialogflowResponse("This is a text response")
dialogflow_response.add(SimpleResponse("This is a simple text response","This is a simple text response"))
dialogflow_response.add(Suggestions(["Help","About","Sync"]))
dialogflow_response.add(SystemIntent("actions.intent.SIGN_IN"))

print(dialogflow_response)
```

## License
See LICENSE.md.