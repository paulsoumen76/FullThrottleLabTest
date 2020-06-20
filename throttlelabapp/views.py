from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from throttlelabapp.mixin import MixinSerializer
import io
from throttlelabapp.models import User
import json
from throttlelabapp.utils import get_object_by_user_id,is_json
from django.core.serializers import serialize
from throttlelabapp.serializers import UserSerializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class UserDetails(View,MixinSerializer):
    def get(self,request,*args,**kwargs):
        data=request.body
        py_data=json.loads(data)
        user_id = py_data.get('user_id',None)
        user=get_object_by_user_id(user_id)
        if user != None:
            return self.serialize_method([user,])
        json_data=json.dumps({'message':'Please provide valid user_id'})
        return HttpResponse(json_data,content_type='application/json',status=400)

    def put(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data=json.dumps({'message':'Please provide valid json_data'})
            return HttpResponse(json_data,content_type='application/json',status=400)
        py_data=json.loads(data)
        user_id=py_data.get('user_id',None)
        user=get_object_by_user_id(user_id)
        if user is None:
            json_data=json.dumps({'message':'Please provide valid user_id'})
            return HttpResponse(json_data,content_type='application/json',status=400)
        serializer=UserSerializers(user,data=py_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            json_data=json.dumps({'message':'user updated successfully'})
            return HttpResponse(json_data,content_type='application/json')
        if serializer.errors:
            json_data=json.dumps(serializer.errors)
            return HttpResponse(json_data,content_type='application/json',status=400)
    def delete(self,request,*args,**kwargs):
        data = request.body
        py_data=json.loads(data)
        user_id = py_data.get('user_id',None)
        user=get_object_by_user_id(user_id)
        if user is None:
            json_data=json.dumps({'message':'Please provide valid user_id'})
            return HttpResponse(json_data,content_type='application/json',status=400)
        user.delete()
        json_data=json.dumps({'message':'user deleted successfully'})
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data=json.dumps({'message':'Please provide valid json_data'})
            return HttpResponse(json_data,content_type='application/json',status=400)
        py_data=json.loads(data)
        serializer=UserSerializers(data=py_data)
        if serializer.is_valid():
            serializer.save()
            json_data=json.dumps({'msg':'User created Successfully'})
            return HttpResponse(json_data,content_type='application/json')
        if serializer.errors:
            json_data=json.dumps(serializer.errors)
            return HttpResponse(json_data,content_type='application/json',status=400)

class UserList(View,MixinSerializer):
    def get(self,request,*args,**kwargs):
        user=User.objects.all()
        serializer = UserSerializers(user,many=True)
        json_data=json.dumps(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

def home_view(request):
    users=User.objects.all()
    return render(request,'throttlelabapp/home.html',{'users':users})     
