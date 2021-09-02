import json

class JSONFormatter():

    def convert_object_to_json(object):
        return json.dumps(object.__dict__)