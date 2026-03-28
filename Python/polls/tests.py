from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question
import datetime


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        create_question("Past question", days=-1)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "Past question")

    def test_future_question(self):
        create_question("Future question", days=1)
        response = self.client.get(reverse("polls:index"))
        self.assertNotContains(response, "Future question")

    def test_past_and_future_questions(self):
        create_question("Past question", days=-1)
        create_question("Future question", days=1)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "Past question")
        self.assertNotContains(response, "Future question")

    def test_two_past_questions(self):
        create_question("Past question 1", days=-1)
        create_question("Past question 2", days=-2)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            ["Past question 1", "Past question 2"],
            transform=str,
        )


class QuestionDetailViewTests(TestCase):

    def test_future_question(self):
        future_question = create_question("Future question", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question("Past question", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, "Past question")