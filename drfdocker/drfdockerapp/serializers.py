from rest_framework import serializers

from .models import Task

# class TaskSerializer(serializers.Serializer):
    # title = serializers.CharField(max_length=200)
    # completed = serializers.BooleanField(default=False, blank=True, null=True)
    
    # def create(self, validated_data):
    #     return Task.objects.create(validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.completed = validated_data.get('completed', instance.completed)
    #     instance.save()
    #     return instance

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed']