import os
from flask import Flask, redirect, url_for, request, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.universitiesdb


@app.route('/')
def universities():

    _items = db.universitiesdb.find()
    items = [item for item in _items]

    return render_template('universities.html', items=items)

@app.route('/status/')
def testStatus():
    return jsonify({
    'status':'OK'
    })


@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name': request.form['name'],
        'description': request.form['description'],
        'numplaces': request.form['numplaces']
    }
    db.universitiesdb.insert_one(item_doc)

    return redirect(url_for('universities'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
