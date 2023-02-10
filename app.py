from flask import Flask, request, make_response, jsonify
from dbhelpers import run_statement
from helpers import check_data

app = Flask(__name__)

@app.get('/api/item')
def get_items():
    result = run_statement('CALL get_items()')
    if(type(result) == list):
        return make_response(jsonify(result), 200)
    else:
        return make_response(jsonify(result), 400)

# keys = ["name", "price"]
# values = (("Jellycat Butterfly", "26.99"), ("Jellycat Picnic Basket", "59.99"))
# result = []
# for item in values:
    # zipped = zip(keys, item)
    # result.append(dict(zipped))

app.run(debug = True)