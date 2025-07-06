import hashlib
from flask import Flask, request, jsonify
import os

print(os.getcwd())

app=Flask(__name__)

def get_user_dict():
    user_dict={}
    with open("FullstackTest/db.txt",mode="r",encoding='utf-8') as f:
        for line in f:
            line=line.strip()
            token,name=line.split(",")
            user_dict[token]=name
    return user_dict


# http://127.0.0.1:5002/bili
@app.route("/bili", methods=["POST"])
def bili():
    """
    :params:
    data={"ordered_string":"...."}
    :return: 
    """
    token=request.args.get("token")
    if not token:
        return jsonify({"status":False,'error':'missing token'})
    user_dict=get_user_dict()
    if token not in user_dict:
        return jsonify({"status":False,'error':'not user'})
        

    ordered_string=request.json.get("ordered_string")
    if not ordered_string:
        return jsonify({"status":True,'error':'wrong args'})
    encrypt_string=ordered_string+'asdlkfjaskdfaskdflaik'
    return jsonify({"status":True, 'data':encrypt_string, "caller":"v2.bili"})

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)


