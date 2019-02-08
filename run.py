from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

office_list = []
party_list = []


@app.route('/offices', methods=['GET'])
def offices():
    return make_response(jsonify({
        "offices": office_list,
        "status": "200"
    }), 200)


@app.route('/parties', methods=['GET'])
def parties_g():
    return make_response(jsonify({
        "parties": party_list,
        "status": "200"
    }), 200)


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


@app.route('/offices', methods=['POST'])
def create_office():
    data = request.get_json()
    office_name = data['name']
    office_type = data['type']

    new_office = {
        "id": len(office_list) + 1,
        "name": office_name,
        "type": office_type,

    }
    office_list.append(new_office)

    return make_response(jsonify({"status": 201, "data": [new_office]}), 201)


@app.route('/parties/<party_id>', methods=['GET'])
def get_party(party_id):
    for party_item in party_list:
        if party_item['id'] == party_id:
            return make_response(jsonify({"status": 200, "data": [party]}), 200)
        return make_response(jsonify({"status": 404, "error": 'Party not found'}), 404)


@app.route('/parties/<party_id>/name', methods=['PATCH'])
def edit_party(party_id):
    data = request.get_json()
    party_item_name = ['name']
    for party_item in party_list:
        if party_item['id'] == party_id:
            party_item_name = ['name']
            return make_response(jsonify({"status": 200, "data": [party]}), 200)
        return make_response(jsonify({"status": 404, "error": 'Party not found'}), 404)


if __name__ == '__main__':
    app.run()
