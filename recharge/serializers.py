from rest_framework import serializers

from recharge.models import Planes , Recharg

class PlaneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Planes
        fields = "__all__"


class RechargSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recharg
        fields = "__all__"