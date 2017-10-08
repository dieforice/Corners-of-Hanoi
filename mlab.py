import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds113925.mlab.com:13925/corners

host = "ds113925.mlab.com"
port = 13925
db_name = "corners"
user_name = "banhbao"
password = "banhbao"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
