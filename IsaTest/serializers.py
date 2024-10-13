from .models  import Saccos
from rest_framework import serializers

class SaccosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saccos
        fields = '__all__'