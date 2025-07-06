import hashlib
from flask import Flask, request, jsonify


app=Flask(__name__)

# http://127.0.0.1:5002/index
@app.route("/bili", methods=["POST"])
def bili():
    """
    :params:
    data={"ordered_string":"...."}
    :return: 
    """
    ordered_string=request.json.get("ordered_string")
    if not ordered_string:
        return jsonify({"status":True,'error':'wrong args'})
    encrypt_string=ordered_string+'asdlkfjaskdfaskdflaik'
    return jsonify({"status":True, 'data':{encrypt_string}, "caller":"v2.bili"})

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)


