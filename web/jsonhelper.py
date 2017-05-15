import json  
from bson.objectid import ObjectId  

class JSONEncoder(json.JSONEncoder):  
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)