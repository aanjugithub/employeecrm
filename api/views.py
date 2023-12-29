from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import Employeeserializer
from api.models import Employees
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class EmployeeModelViewSetView(viewsets.ModelViewSet):
    serializer_class=Employeeserializer
    model=Employees
    queryset=Employees.objects.all()
    
    
    #localhost:8000/api/v2/employees/?department=hr =then it should give the emp details from hr dept
    def list(self,request,*args,**Kwargs):
        qs=Employees.objects.all()
        if "department" in request.query_params:
            value=request.query_params.get("department")
            qs=qs.filter(department=value)
        serializer=Employeeserializer(qs,many=True)
        return Response(data=serializer.data)
    


    #to get all the departments,custom method
    @action(methods=["get"],detail=False)   #detail true means passing ids fallse -no id is passing
    def departments(self,request,*args,**kwargs):
        qs=Employees.objects.all().values_list("department",flat=True).distinct()
        return Response(data=qs)
    
