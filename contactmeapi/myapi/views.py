from django.shortcuts import render
from rest_framework.decorators import api_view, throttle_classes
from django.http import JsonResponse
import json, re
from .serializers import ContactDetailsSerializer
from. models import contactDetails
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

        email_pattern = "((\\w+)@(\\w+).com)"
        if not re.match(email_pattern,email):
            return JsonResponse({"status_code":"400 Bad Request","error":"Email format is incorrect. Please enter a valid email."})
        
        if len(name) == 0:
            return JsonResponse({"status_code":"400 Bad Request","error":"Name field is required"})
        elif len(name) > 250:
            return JsonResponse({"status_code":"400 Bad Request","error":"Name field exceeds maximum 250 character limit"})
        elif re.search("[^\w\s]", name):
          return JsonResponse({"status_code":"400 Bad Request","error":"Name field can only contain alphabets"})
        
        if len(subject) == 0:
            return JsonResponse({"status_code":"400 Bad Request","error":"subject field is required"})
        elif len(subject) > 80:
            return JsonResponse({"status_code":"400 Bad Request","error":"subject field exceeds maximum 80 character limit"})
        elif re.search("[^\w\s,'.:;\"/\()-?!]", subject):
            return JsonResponse({"status_code":"400 Bad Request","error":"subject field can only contain alphabets and punctuation. Remove any special characters."})
        
        if len(message) == 0:
            return JsonResponse({"status_code":"400 Bad Request","error":"message field is required"})
        elif len(message) > 1000:
            return JsonResponse({"status_code":"400 Bad Request","error":"message field exceeds maximum 80 character limit"})
        elif re.search("[^\w\s,'.:;\"/\()-?!]", message):
            return JsonResponse({"status_code":"400 Bad Request","error":"message field can only contain alphabets and punctuation. Remove any special characters."})
        """        
        tasks for tomorrow:  
        - don't bother with the serializer ( difficult to coordinate error messages )
        - CHECK if environment variables were correctly implemented (https://codinggear.blog/django-environment-variables/)
        - use regex to test if there is a digit in name ( search for a digit and special characters. Allow only [a-z][A-Z]) (done)
        - use regex to test for email pattern (done)
        - figure out how to test for sql injection in subject and message. Only accept alphabets and numbers. (no need to do this as I am not retrieving information)
        - save to database (done)
        - figure out EC2 hosting (if it is the right choice)
        """
        
        serializer = ContactDetailsSerializer(data=json.loads(request.body))
    
        if serializer.is_valid(raise_exception=True):
            contactDetails.objects.create(name=name, email=email,subject=subject,message=message)
            return JsonResponse({"status_code":"200","message":"Successfully Hit the api", "echoing": serializer.data})

       

    