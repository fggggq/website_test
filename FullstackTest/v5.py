import hashlib
import pymysql
import os
from flask import Flask, request, jsonify
from dbutils.pooled_db import PooledDB

print(os.getcwd())

POOL = PooledDB(
    creator=pymysql,    # module to connect sql
    maxconnections=10,  # DB POOL maximum connection
    mincached=2,    # minmum cached connections when initializing
    maxcached=3,    # maximum cached connections, 0 and none represent no limit
    blocking=True,  # if no available connection, if true, block requests
    setsession=[],
    ping=0,
    # settings.MYSQL_CONN_PARAMS
    host='127.0.0.1',port=3306,user='root',passwd='root123',charset="utf8",db='day20'
)

app=Flask(__name__)

def get_user_dict():
    user_dict={}
    with open("FullstackTest/db.txt",mode="r",encoding='utf-8') as f:
        for line in f:
            line=line.strip()
            token,name=line.split(",")
            user_dict[token]=name
    return user_dict

def fetch_one(sql,params):
    # conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root123',charset="utf8",db='day20')
    conn=POOL.connection()
    cursor=conn.cursor()
    cursor.execute(sql,params)
    result=cursor.fetchone()
    conn.close()
    return result


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
        return jsonify({"status":False,'error':'wrong args'})
    encrypt_string=ordered_string+'asdlkfjaskdfaskdflaik'
    return jsonify({"status":True, 'data':encrypt_string, "caller":"v2.bili"})

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)

@app.route("/bili_sql", methods=["POST"])
def bili():
    """
    :params:
    data={"ordered_string":"...."}
    :return: 
    """
    token=request.args.get("token")
    if not token:
        return jsonify({"status":False,'error':'missing token'})
    result=fetch_one("select * from user where token=%s",[token,])
    if not result:
        return jsonify({"status":False,'error':'not user'})
        
    ordered_string=request.json.get("ordered_string")
    if not ordered_string:
        return jsonify({"status":True,'error':'wrong args'})
    encrypt_string=ordered_string+'asdlkfjaskdfaskdflaik'
    return jsonify({"status":True, 'data':encrypt_string, "caller":"v2.bili"})

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)
