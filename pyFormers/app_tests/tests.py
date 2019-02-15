from django.test import TestCase
from django.shortcuts import reverse
from .models import Test, Question
from .views import
from django.db.models import Count


class CreateTestCase(TestCase):
    test_name = 'My_testing_test'

    @classmethod
    def setUp(cls):
        super().setUpClass()
        cls.test = Test.objects.create(name=cls.test_name)

    def test_add_question(self):
        q1 = Question.objects.create(text='what is your name?')
        add_quest_url = reverse('add_q')
        # request = self.client.post(add_quest_url)
        self.assertEqual(Test.objects.values_list('questions'), 1)


# class RunTestCase(TestCase):
#     pass

