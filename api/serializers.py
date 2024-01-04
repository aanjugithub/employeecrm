from rest_framework import serializers
from api.models import Employees,Tasks

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields="__all__"
        read_only_fields=["id"]

class TaskSerializer(serializers.ModelSerializer):
    employee=serializers.StringRelatedField()
    class Meta:
        model=Tasks
        fields="__all__"
        read_only_fields=["id","employee","assigned_date"]

