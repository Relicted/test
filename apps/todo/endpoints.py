from rest_framework.generics import (
    ListCreateAPIView,
    DestroyAPIView,
    CreateAPIView,
    UpdateAPIView
)
from rest_framework.permissions import IsAuthenticated

from apps.todo.serializers import (
    ColumnSerializer,
    DeleteTaskSerializer,
    CreateTaskSerializer,
    MoveTaskSerializer,
    EditTaskSerializer,
)
from apps.todo.models import Column, Task


class ColumnListAPIView(ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = ColumnSerializer

    def get_queryset(self):
        return Column.objects.filter(
            user=self.request.user
        ).select_related('user').prefetch_related('tasks')


class ArchiveTaskAPIVView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = DeleteTaskSerializer

    def perform_destroy(self, instance):
        instance.archived = True
        instance.save()


class CreateTaskAPIView(CreateAPIView):
    serializer_class = CreateTaskSerializer


class MoveTaskAPIView(UpdateAPIView):
    serializer_class = MoveTaskSerializer

    def get_queryset(self):
        return Task.objects.filter(column__user=self.request.user)


class EditTaskAPIView(MoveTaskAPIView):
    serializer_class = EditTaskSerializer