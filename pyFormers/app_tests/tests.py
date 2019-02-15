from django.test import TestCase
from .models import Test


class CreateTestCase(TestCase):
    test_name = 'My_testing_test'
    question1 = 'what is your name?'
    question2 = 'what is your favorite color?'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test = Test.objects.create(name=cls.test_name)


class RunTestCase(TestCase):
    pass

