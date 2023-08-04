from rest_framework import serializers
from .models import contactDetails

class ContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactDetails
        exclude = ["id"]
