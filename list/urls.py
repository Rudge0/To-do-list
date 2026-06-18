from django.urls import path
from list.views import (
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TaskStatusUpdateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),

    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),

    path(
        "tasks/<int:pk>/change-status/",
        TaskStatusUpdateView.as_view(),
        name="change-task-status",
    ),
]


app_name = "list"
