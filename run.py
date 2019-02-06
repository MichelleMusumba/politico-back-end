from flask import Flask,jsonify,make_response
app = Flask(__name__)

office_list=[]


@app.route('/offices',methods=['GET'])
def offices():
    return make_response(jsonify({
        "offices":office_list,
        "status":"200"
    }), 200)


if __name__=='__main__':
    app.run()