from flask import Flask, request, jsonify

app=Flask(__name__)

# http://127.0.0.1:5002/index
@app.route("/index", methods=["POST","GET"])
def index():
    # method = "GET"
    age=request.args.get("age")
    pwd=request.args.get("pwd")
    print(age,pwd)

    # method = "POST", xx=123&yy=999
    xx=request.form.get("xx")
    yy=request.form.get("yy")
    print(xx,yy)

    # method = "POST", {"uu":321, "vv":111}
    uu=request.json.get("uu",None)
    vv=request.json.get("vv",None)
    print(request.json)
    print(uu,vv)
    return jsonify({"status":True, 'data':{"uu":uu,"vv":vv}, "caller":"v1.index"})

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)


