import redis

REDIS_CONN_PARAMS={
        "host":'127.0.0.1',
        "password":'qwe123',
        "port":6379,
        "encoding":'utf-8'
    }
conn=redis.Redis(**REDIS_CONN_PARAMS)
conn.lpush("test_spider_task_list","123")
conn.lpush("test_spider_task_list","456")
data=conn.rpop("test_spider_task_list")
print(data)