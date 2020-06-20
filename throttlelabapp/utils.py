from django.views.generic import View
from throttlelabapp.models import User
import json
def get_object_by_user_id(user_id):
    try:
        user=User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        user=None
    return user
def is_json(data):
    try:
        json_data=json.loads(data)
        valid=True
    except ValueError:
        valid=False
    return valid
