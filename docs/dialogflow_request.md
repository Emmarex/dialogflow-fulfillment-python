<h1>Requests</h1>

### Get Intent Name

```python
from pydialogflow_fulfillment import DialogflowRequest

dialog_fulfillment = DialogflowRequest(request.body) # for Django

# dialog_fulfillment = DialogflowRequest(request.data) for Flask

print(dialog_fulfillment.get_intent_name())
```

### Get Intent Display Name

```python
from pydialogflow_fulfillment import DialogflowRequest

dialog_fulfillment = DialogflowRequest(request.body) # for Django

# dialog_fulfillment = DialogflowRequest(request.data) for Flask

print(dialog_fulfillment.get_intent_displayName())
```

### Get Project ID

```python
from pydialogflow_fulfillment import DialogflowRequest

dialog_fulfillment = DialogflowRequest(request.body) # for Django

# dialog_fulfillment = DialogflowRequest(request.data) for Flask

print(dialog_fulfillment.get_project_id())
```

### Get Single Paramter

```python
from pydialogflow_fulfillment import DialogflowRequest

dialog_fulfillment = DialogflowRequest(request.body) # for Django

# dialog_fulfillment = DialogflowRequest(request.data) for Flask

print(dialog_fulfillment.get_parameter("param"))
```

### Get Request Parameters

```python
from pydialogflow_fulfillment import DialogflowRequest

dialog_fulfillment = DialogflowRequest(request.body) # for Django

# dialog_fulfillment = DialogflowRequest(request.data) for Flask

print(dialog_fulfillment.get_parameters())
```

### Get Session

```python
from pydialogflow_fulfillment import DialogflowRequest

dialog_fulfillment = DialogflowRequest(request.body) # for Django

# dialog_fulfillment = DialogflowRequest(request.data) for Flask

print(dialog_fulfillment.get_session())
```

### Get Response ID

```python
from pydialogflow_fulfillment import DialogflowRequest

dialog_fulfillment = DialogflowRequest(request.body) # for Django

# dialog_fulfillment = DialogflowRequest(request.data) for Flask

print(dialog_fulfillment.get_response_id())
```

### Get all OuputContext

```python
from pydialogflow_fulfillment import DialogflowRequest

dialog_fulfillment = DialogflowRequest(request.body) # for Django

# dialog_fulfillment = DialogflowRequest(request.data) for Flask

print(dialog_fulfillment.get_ouputcontext_list())
```

### Get Single OuputContext

```python
from pydialogflow_fulfillment import DialogflowRequest

dialog_fulfillment = DialogflowRequest(request.body) # for Django

# dialog_fulfillment = DialogflowRequest(request.data) for Flask

print(dialog_fulfillment.get_single_ouputcontext())
```