from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import Employeeserializer,TaskSerializer
from api.models import Employees,Tasks
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions,authentication

# Create your views here.

class EmployeeModelViewSetView(viewsets.ModelViewSet):

    permission_classes=[permissions.IsAdminUser] #admin have the privilage of adding and editing emp detail
    authentication_classes=[authentication.BasicAuthentication]

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
    


    #to get all the departments,custom method-disply all deptmnts
    @action(methods=["get"],detail=False)   #detail true means passing ids false -no id is passing
    def departments(self,request,*args,**kwargs):
        qs=Employees.objects.all().values_list("department",flat=True).distinct()
        return Response(data=qs)

    #asign a task to an emp
    #localhost 8000/api/v2/employees/{id}/add-task

    @action(methods=["post"],detail=True)
    def add_task(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        emp_object=Employees.objects.get(id=id)
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employee=emp_object)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



    #list all tasks of a specific employee  
    #url- localhost 8000/api/v2/employees/{id}/tasks/
    #method-get   
        
    @action(methods=["get"],detail=True)    
    def tasks(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Tasks.objects.filter(employee__id=id)
        serializer=TaskSerializer(qs,many=True)
        return Response(data=serializer.data)
    

#localhost8000/api/v2/task/{taskid}/update
# method=put
