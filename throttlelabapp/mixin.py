from django.core.serializers import serialize
import json
from django.http import HttpResponse

class MixinSerializer(object):
    def serialize_method(self,user):
        json_data=serialize('json',user)
        py_data = json.loads(json_data)
        user_list=[]
        for data in py_data:
            user_list.append(data['fields'])
        json_data = json.dumps(user_list)
        return HttpResponse(json_data,content_type='application/json')
