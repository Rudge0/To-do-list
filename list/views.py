from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Tag


def change_task_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, id=pk)
    task.change_status()
    print("Here")
    return redirect("list:task-list")


def add_task_tag(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk)
    return redirect("list:task-list")


def delete_task_tag(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk)
    return redirect("list:task-list")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10

class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")
