<h1>Response</h1>

### Simple fulfilment text

```python
from pydialogflow_fulfillment import DialogflowResponse

dialogflow_response = DialogflowResponse("This is a text response")
```

### Simple Response

```python
from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import SimpleResponse

dialogflow_response = DialogflowResponse("This is a text response")
dialogflow_response.add(SimpleResponse("This is a simple text response","This is a simple text response"))
```

### Confirmation

```python
from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import SimpleResponse, Confirmation

dialogflow_response = DialogflowResponse("This is a simple text response")
dialogflow_response.add(SimpleResponse("This is a simple text response","This is a simple text response"))
dialogflow_response.add(Confirmation("Are you sure u wanna do this?"))
```

### Suggestions

```python
from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import SimpleResponse, Suggestions

dialogflow_response = DialogflowResponse("This is a text response")
dialogflow_response.add(Suggestions(["Help","About","Sync"]))
```

You could combine a `SimpleResponse` and `Suggestions`

```python
from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import SimpleResponse, Suggestions

dialogflow_response = DialogflowResponse("This is a text response")
dialogflow_response.add(SimpleResponse("This is a simple text response","This is a simple text response"))
dialogflow_response.add(Suggestions(["Help","About","Sync"]))
```

### SystemIntent

```python
from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import SystemIntent

dialogflow_response = DialogflowResponse("This is a text response")
dialogflow_response.add(SystemIntent("another_dialogflow_intent_name"))
```

### LinkOutSuggestion

```python
from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import LinkOutSuggestion

dialogflow_response = DialogflowResponse("This is a text response")
dialogflow_response.add(LinkOutSuggestion("DialogFlow Website","http://dialogflow.com"))
```

### Expect user response

```python
from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import LinkOutSuggestion

dialogflow_response = DialogflowResponse("Goodbye !!!")
dialogflow_response.expect_user_response = False
```

```python
from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import LinkOutSuggestion

dialogflow_response = DialogflowResponse("This is a simple text response")
dialogflow_response.add(SimpleResponse("This is a simple text response","This is a simple text response"))
dialogflow_response.add(Suggestions(["Help","About","Sync"]))
dialogflow_response.expect_user_response = True
```

### Google Assistant Signin

```python
from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import AskForSignin

dialogflow_response = DialogflowResponse("PLACEHOLDER_FOR_SIGN_IN")
dialogflow_response.add(AskForSignin())
```

### Permissions

* DEVICE_PRECISE_LOCATION - Ask for user's precise location, lat/lng and formatted address
* DEVICE_COARSE_LOCATION - Ask for user's coarse location, zip code, city and country code. Works only from Google Home devices
* UPDATE - Ask for permissions to send updates
* NAME -  Ask for user's first and last name

```python
from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import AskPermission, Permissions

dialogflow_response = DialogflowResponse("PLACEHOLDER_FOR_PERMISSION")
dialogflow_response.add(AskPermission([Permissions.DEVICE_COARSE_LOCATION, Permissions.NAME],"To just know better"))
```

### RegisterUpdate

```python
from pydialogflow_fulfillment import DialogflowResponse, RegisterUpdate, Frequency

dialogflow_response = DialogflowResponse()

sample_arguments =  { 
                        "name": "category",
                        "textValue": "tipCategory"
                    }
dialogflow_response.add(RegisterUpdate("INTENT_NAME",sample_arguments,Frequency.ROUTINES))
```

### DateTime

```python
from pydialogflow_fulfillment import DialogflowResponse, DateTime

dialogflow_response = DialogflowResponse()
dialogflow_response.add(DateTime("When would you like to schedule the appoinment?","What day was that?","What time?"))
```

### DeliveryAddress

```python
from pydialogflow_fulfillment import DialogflowResponse, DeliveryAddress

dialogflow_response = DialogflowResponse()
dialogflow_response.add(DeliveryAddress("Just so we could know where to deliver the product to"))
```

### Set OuputContext

```python
from pydialogflow_fulfillment import DialogflowResponse, OutputContexts

dialogflow_response = DialogflowResponse()
dialogflow_response.add(OutputContexts("sample-project-12","88d13aa8-2999-4f71-b233-39cbf3a824a0","context_name",200,{"user_name":"rex_2019"}))
dialogflow_response.add(OutputContexts("sample-project-12","88d13aa8-2999-4f71-b233-39cbf3a824a0","context_name",200,{}))
```