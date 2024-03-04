from django.shortcuts import get_object_or_404
from django.http import *
import json
from home1.models import Students
from django.views.decorators.csrf import csrf_exempt

# retrieving  flutter variables
@csrf_exempt
def login_check(request):

    # Check if the request method is POST
    if request.method == 'POST':
        
        # Load JSON data from request body
        data = json.loads(request.body)
        
        # Extract username and password from flutter JSON data
        f_uname = data.get('username', None)
        f_pwd = data.get('password', None)

        # Check if the user exists in database ?
        
        try:
            student = Students.objects.get(username=f_uname, password=f_pwd)
            details = {
                'user': student.username,
                'pass': student.password
            }
            return JsonResponse({'data':details},status=200)
        
        except Students.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
