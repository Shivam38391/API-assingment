from django.urls import path
from  . import views

urlpatterns = [
    path('plan/' , views.PlanListView.as_view(), name='plan'),
    path('recharge/' , views.RechargeView.as_view(), name='recharge'),
    
    
]