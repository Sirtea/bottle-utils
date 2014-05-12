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
