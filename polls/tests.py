import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice


# Create your tests here.
def create_question(question_text: str, days: int):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelsTest(TestCase):
    def test_was_published_recently_with_future(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_quest = Question(pub_date=time)
        self.assertIs(future_quest.was_published_recently(), False)

    def test_was_published_recently_with_past(self):
        time = timezone.now() + datetime.timedelta(days=-30)
        print(time)
        past_quest = Question(pub_date=time)
        self.assertIs(past_quest.was_published_recently(), False)


class QuestionIndexViewTest(TestCase):
    def test_no_quest(self):
        response = self.client.get(reverse('polls:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'no questions')


class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        future_question = create_question('future_question', 10)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question('past_question', -5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response, past_question.question_text)


# pytania ktore sa z przeszlosci

class QuestionVoteViewTest(TestCase):
    def test_can_not_vote_for_future_question(self):
        future_question = create_question('future_question', 10)
        choice = Choice.objects.create(choice_text="aaa", question = future_question)
        url =reverse('polls:vote', args=(future_question.id))
        form = {'choice': choice.id}

        response=self.client.post(url, date=form)
        self.assertEqual(response.status_code, 404)
