from flask import Flask, jsonify, make_response
app = Flask(__name__)

office_list = []


@app.route('/offices', methods = ['GET'])
def offices():
    return make_response(jsonify({
        "offices": office_list,
        "status": "200"
    })), 200


party_list = []


@app.route('/parties', methods=['GET'])
def parties():
    return make_response(jsonify({
        "parties": party_list,
        "status": "200"
    }), 200)



@app.route('/parties', methods=['GET'])
def parties():
    return make_response(jsonify({
        "parties": party_list,
        "status": "200"
    }), 200)



if __name__ == '__main__':
    app.run()