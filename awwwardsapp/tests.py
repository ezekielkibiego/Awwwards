from django.contrib.auth.models import User
from django.test import TestCase
from .models import Project, Profile


class ProjectTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="test_user", first_name="ezekiel", last_name="kibiego"
        )

        self.project = Project(
            title="Test Photos",
            description="Test Category",
            image="image.png",
            user=user,
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

   