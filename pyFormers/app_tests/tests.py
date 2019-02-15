from django.test import TestCase, Client
from django.shortcuts import reverse
from .models import Test, Question
from .views import add_q


class CreateTestCase(TestCase):
    test_name = 'My_testing_test'

    @classmethod
    def setUp(cls):
        super().setUpClass()
        cls.test = Test.objects.create(name=cls.test_name)

    def test_add_question(self):
        q1 = Question(text='what is your name?')
        q1.save()
        adding_question = {'test_id': self.test.id, 'q_id': q1.id}
        r = reverse('app_tests:add_q', kwargs=adding_question)
        request = self.client.post(r, data=adding_question)
        self.assertEqual(Test.objects.values_list('questions', flat=True).count(), 1)

        q2 = Question(text='what is your favorite color?')
        q2.save()
        adding_question = {'test_id': self.test.id, 'q_id': q2.id}
        r = reverse('app_tests:add_q', kwargs=adding_question)
        request = self.client.post(r, data=adding_question)
        self.assertEqual(Test.objects.values_list('questions', flat=True).count(), 2)

    def test_run_test(self):
        pass
