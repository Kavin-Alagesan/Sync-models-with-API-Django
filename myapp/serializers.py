from rest_framework import serializers
from myapp.models import Details

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Details
        fields='__all__'

        