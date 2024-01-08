from rest_framework import serializers
from api.models import Employees,Tasks



class TaskSerializer(serializers.ModelSerializer):
    employee=serializers.StringRelatedField()
    class Meta:
        model=Tasks
        fields="__all__"
        read_only_fields=["id","employee","assigned_date"]

class Employeeserializer(serializers.ModelSerializer):
    tasks=TaskSerializer(read_only=True,many=True) #to list tasks along with emp list
    class Meta:
        model=Employees
        fields="__all__"
        read_only_fields=["id"]

