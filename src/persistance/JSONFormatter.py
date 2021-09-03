from types import SimpleNamespace
import json

class JSONFormatter():

    def convert_object_to_json(object):
        return json.dumps(object.__dict__)

    def convert_array_object_to_json(data):
        result = "["

        for object in data:
            result += json.dumps(object.__dict__)

            if object != data[data.__len__() - 1]:
                result += ","

        result += "]"
        
        return result
    
    def convert_json_to_object(json_string):
        return json.loads(json_string, object_hook=lambda d: SimpleNamespace(**d))