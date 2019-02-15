from django.test import TestCase
from django.shortcuts import reverse
from .models import Test, Question, RunTest
from .forms import AnswerForm
from django.forms.models import formset_factory


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
        answer_factory = formset_factory(AnswerForm, min_num=2)
        runing_test_1 = {'form-TOTAL_FORMS': '3',
                         'form-INITIAL_FORMS': '0',
                         'form-MIN_NUM_FORMS': '2',
                         'form-MAX_NUM_FORMS': '1000',
                         'form-0-Answer': 'King Arthur',
                         'form-1-Answer': 'Blue',
                         'start': 'Done'}
        answer_form_set = answer_factory(runing_test_1)
        self.assertTrue(answer_form_set.is_valid())

        self.assertEquals(RunTest.objects.all().count(), 0)
        r = reverse('app_tests:run_test', kwargs={'test_id': self.test.id})
        request = self.client.post(r, data=runing_test_1)
        self.assertEquals(RunTest.objects.all().count(), 1)

        runing_test_2 = {'form-TOTAL_FORMS': '3',
                         'form-INITIAL_FORMS': '0',
                         'form-MIN_NUM_FORMS': '2',
                         'form-MAX_NUM_FORMS': '1000',
                         'form-0-Answer': '',
                         'form-1-Answer': '',
                         'start': 'Done'}
        answer_form_set = answer_factory(runing_test_2)
        self.assertFalse(answer_form_set.is_valid())
