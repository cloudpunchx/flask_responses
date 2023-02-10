from flask import Flask, request, make_response, jsonify
from dbhelpers import run_statement
from helpers import check_data

app = Flask(__name__)

@app.get('/api/item')
def get_items():
    keys = ["itemId","itemName", "itemPrice"]
    result = run_statement('CALL get_items()')
    items = []
    if(type(result) == list):
        for item in result:
            zipped = zip(keys, item)
            items.append(dict(zipped))
        return make_response(jsonify(items), 200)
    else:
        # Mark chose 500 since it's a GET and there was no error from client input so server error is ok
        return make_response(jsonify(result), 500)



app.run(debug = True)