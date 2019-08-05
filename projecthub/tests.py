from django.test import TestCase
from .models import Project,Review,Profile

# Create tests here.
class ProjectTestClass(TestCase):

    def setUp(self):
        self.new_project= Project(title = 'Test project',project = 'This is a random test Project')
        self.new_project.save()

    def tearDown(self):
        Project.objects.all().delete()

class ReviewTestClass(TestCase):

    def setUp(self):
        self.new_review= Review(title = 'Test review',review = 'This is a random test Review')
        self.new_review.save()

    def tearDown(self):
        Review.objects.all().delete()

class ProfileTestClass(TestCase):

    def setUp(self):
        self.new_profile= Profile(title = 'Test profile',profile = 'This is a random test Profile')
        self.new_profile.save()


    def tearDown(self):
        Profile.objects.all().delete()