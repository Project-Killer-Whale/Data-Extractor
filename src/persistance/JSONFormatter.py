import json

class JSONFormatter():

    def convert_object_to_json(object):
        return json.dumps(object.__dict__)

    def convert_array_object_to_json(data):
        result = "["

        for object in data:
            result += json.dumps(object.__dict__)

        result += "]"
        
        return result