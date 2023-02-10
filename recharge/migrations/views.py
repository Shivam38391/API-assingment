from .serializers import PlaneSerializer , RechargSerializer
from rest_framework import generics
from .models import Planes , Recharg
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class PlanListView(generics.ListAPIView):
    
    queryset = Planes.objects.all()
    serializer_class = PlaneSerializer
    
    

class RechargeView(APIView):
    
    def get(self, request):
        r = Recharg.objects.all()
        serializer = RechargSerializer(r, many=True)
        return Response(serializer.data)
        
        

    def post(self, request):
        serializer = RechargSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)
            