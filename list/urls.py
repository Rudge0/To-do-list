from django.urls import path
from .views import (

    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,

    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,

    change_task_status,
    add_task_tag,
    delete_task_tag
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

    path("tasks/<int:pk>/change-status/", change_task_status, name="change-task-status"),
    path("tasks/<int:pk>/add-tag/", add_task_tag, name="add-task-status"),
    path("tasks/<int:pk>/delete-tag/", delete_task_tag, name="delete-task-status"),

]


app_name = "list"
