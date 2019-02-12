from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

office_list = []
party_list = []


@app.route('/offices', methods=['GET'])
def get_all_offices():
    return make_response(jsonify({
        "offices": office_list,
        "status": "200"
    }), 200)


@app.route('/parties', methods=['GET'])
def get_all_parties():
    return make_response(jsonify({
        "parties": party_list,
        "status": "200"
    }), 200)


@app.route('/parties', methods=['POST'])
def create_party():
    data = request.get_json(force=True)
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
    data = request.get_json(force=True)
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
def get_a_specific_party(party_id):
    for party in party_list:
        if party['id'] == int(party_id):
            return make_response(jsonify({"status": 200, "data": [party]}), 200)
        return make_response(jsonify({"status": 404, "error": 'Party not found'}), 404)
    return make_response(jsonify({"status": 404, "error": 'Party not found'}), 404)


@app.route('/parties/<party_id>/name', methods=['PATCH'])
def edit_party(party_id):
    data = request.get_json(force=True)
    party_item_name = data['name']
    for party in party_list:
        if party['id'] == int(party_id):
            party['name'] = party_item_name
            return make_response(jsonify({"status": 200, "data": [party]}), 200)
        return make_response(jsonify({"status": 404, "error": 'Party not found'}), 404)


@app.route('/parties/<party_id>', methods=['DELETE'])
def delete_party(party_id):
    for party_item in party_list:
        if party_item['id'] == int(party_id):
            party_list.remove(party_item)
            return make_response(jsonify({"status": 200, "message": "deleted successfully"}), 200)
        return make_response(jsonify({"status": 404, "error": 'Party not found'}), 404)


@app.route('/offices/<office_id>', methods=['GET'])
def get_a_specific_office(office_id):
    if not len(office_list) > 0:
        return make_response(jsonify({"status": 400, "error": "No Data In List"}), 400)
    for office_item in office_list:
        if office_item['id'] == int(office_id):
            return make_response(jsonify({"status": 200, "data": [office_item]}), 200)
        return make_response(jsonify({"status": 404, "error": 'office not found'}), 404)


if __name__ == '__main__':
    app.run()
