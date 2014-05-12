json-plugin
===========

This is a plugin for the framework bottle that aims to create easily REST json web services.
The objective is to reduce the amount of code spent in parsing the request body, filling the content_type and setting the html error status.
It also manages the conversion of the output to JSON.

## How to use json-plugin

Just download a copy of json_plugin.py and import the JsonPlugin object.
Instantiate a copy of the plugin, with the body keyword, and install.
If the controller function includes the keyword parameter, the request body will be parsed and placed on this parameter.

```python
from bottle import Bottle
from json_plugin import JsonPlugin

app = Bottle()
app.install(JsonPlugin('data'))

items = []


@app.get('/items')
def get_items():
    return items, 200


@app.post('/items')
def new_item(data):
    items.append(data)
    return None, 201
```
