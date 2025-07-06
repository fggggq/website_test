import hashlib
import uuid
from flask import Flask, request, jsonify
import os

print(os.getcwd())

app=Flask(__name__)

@app.route("/task",methods=["POST"])
def task():
    ordered_string=request.json.get("ordered_string")
    if not ordered_string:
        return jsonify({"status":False,'error':'wrong args'})
    tid=str(uuid.uuid4())

    task_dict={'tid':tid,'data':ordered_string}
    REDIS_CONN_PARAMS={
        "host":'127.0.0.1',
        "password":'qwe123',
        "port":6379,
        "encoding":'utf-8'
    }
    conn=redis.Redis()

    # put the task into a queue


if __name__=="__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)


