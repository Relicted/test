from rest_framework import serializers

from apps.todo import models


class FilterDeleteTaskSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(archived=False)
        return super(FilterDeleteTaskSerializer, self).to_representation(data)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id', 'column', 'name', 'description', 'archived')
        list_serializer_class = FilterDeleteTaskSerializer


class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = models.Column
        fields = ('id', 'name', 'tasks')


class DeleteTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id',)


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id', 'name', 'column', 'description')


class MoveTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('column',)


class EditTaskSerializer(serializers.ModelSerializer):
    column = serializers.PrimaryKeyRelatedField(read_only=True)
    archived = serializers.CharField(read_only=True)
    class Meta:
        model = models.Task
        fields = ('id', 'name', 'description', 'column', 'archived')
