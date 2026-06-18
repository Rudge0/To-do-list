from datetime import date

from django.test import TestCase
from django.urls import reverse

from list.models import Tag, Task


class TaskListViewTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Work")
        self.task = Task.objects.create(
            name="Write docs",
            description="Prepare the README",
            deadline=date(2026, 6, 30),
        )
        self.task.tags.add(self.tag)

    def test_task_list_view_renders_tasks_and_tags_context(self):
        response = self.client.get(reverse("list:task-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list/task_list.html")
        self.assertContains(response, self.task.name)
        self.assertIn("tags", response.context)
        self.assertQuerySetEqual(
            response.context["tags"].order_by("pk"),
            Tag.objects.order_by("pk"),
        )


class TaskStatusUpdateViewTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(name="Toggle status")

    def test_post_toggles_task_status_and_redirects(self):
        response = self.client.post(
            reverse("list:change-task-status", args=[self.task.pk])
        )

        self.assertRedirects(response, reverse("list:task-list"))
        self.task.refresh_from_db()
        self.assertTrue(self.task.done)

    def test_get_is_not_allowed(self):
        response = self.client.get(
            reverse("list:change-task-status", args=[self.task.pk])
        )

        self.assertEqual(response.status_code, 405)
