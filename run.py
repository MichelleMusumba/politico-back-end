from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

office_list = []
party_list = []


@app.route('/offices', methods=['GET'])
def offices():
    return make_response(jsonify({
        "offices": office_list,
        "status": "200"
    })), 200


@app.route('/parties', methods=['POST'])
def party():
    data = request.get_json()
    party_name = data['name']
    party_address = data['hqAddress']
    party_logo = data['logoUrl']

    new_party = {
        "id": len(party_list) + 1,
        "name": party_name,
        "hqAddress": party_address,
        "logoUrl": party_logo
    }
    party_list.append(new_party)

    return make_response(jsonify({"status": 201, "data": [new_party]}), 201)


if __name__ == '__main__':
    app.run()
