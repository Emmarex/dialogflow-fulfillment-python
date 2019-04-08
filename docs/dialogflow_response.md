<h1>Dialogflow Response</h1>


### Add Response

The ``.add()`` function allows you add various Dialogflow Responses in the [Response](response.md) class to your dialogflow response.

Usage Example

```python
from pydialogflow_fulfillment import DialogflowResponse

from pydialogflow_fulfillment.response import SimpleResponse, OutputContexts

dialogflow_response = DialogflowResponse()
dialogflow_response.add(SimpleResponse("This is a simple text response","This is a simple text response"))

dialogflow_response.add(OutputContexts("sample-project-12","88d13aa8-2999-4f71-b233-39cbf3a824a0","context_name",200,{"user_name":"user001"}))
```

### Get Final Response

``.get_final_response()`` gives you a string output of your ``DialogflowResponse``.

Usage Example 

```python
from pydialogflow_fulfillment import DialogflowResponse

from pydialogflow_fulfillment.response import SimpleResponse, OutputContexts

dialogflow_response = DialogflowResponse()
dialogflow_response.add(SimpleResponse("This is a simple text response","This is a simple text response"))
print(dialogflow_response.get_final_response())
```
**The same output can be achieved by using ``print(dialogflow_response)``**

Ouput
```json
{
    "fulfillmentText": "", 
    "source": "webhook", 
    "outputContexts": [], 
    "payload": {
        "google": {
            "richResponse": {
                "items": [
                    {
                        "simpleResponse": {
                            "displayText": "This is a simple text response", 
                            "textToSpeech": "This is a simple text response"
                        }
                    }
                ]
            }, 
            "expectUserResponse": true
        }
    }
}
```