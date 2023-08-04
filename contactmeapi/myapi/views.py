from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from .serializers import ContactDetailsSerializer
# Create your views here.

@api_view(["POST"])
def PostContact(request):
    if request.method == "POST":
        # the api_view decorator abstracts away the need to check if any other method apart from POST is used.
        # use your own tests instead of using serializer
        userInput = json.loads(request.body)
        name = userInput["name"]
        email = userInput["email"]
        subject = userInput["subject"]
        message = userInput["message"]
        
        """        
        tasks for tomorrow:  
        - don't bother with the serializer ( difficult to coordinate error messages )
        - CHECK if environment variables were correctly implemented (https://codinggear.blog/django-environment-variables/)
        - use regex to test if there is a digit in name ( search for a digit and special characters. Allow only [a-z][A-Z])
        - use regex to test for email pattern
        - figure out how to test for sql injection in subject and message. Only accept alphabets and numbers.
        - save to database
        - figure out throttling + error messages for throttling
        - figure out EC2 hosting (if it is the right choice)
        """
        
        serializer = ContactDetailsSerializer(data=json.loads(request.body))
    
        if serializer.is_valid(raise_exception=True):
            return JsonResponse({"status_code":"200","message":"Successfully Hit the api", "echoing": serializer.data})

       
        # if userInput['name']
        
        return JsonResponse({"status_code":"200","message":"Close!, but no cigar", "echoing": userInput})
    