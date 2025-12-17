from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteTests(TestCase):

    def test_note_creation(self):
        note = Note.objects.create(
            title="Test Note",
            content="Test Content"
        )
        self.assertEqual(note.title, "Test Note")

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        response = self.client.post(reverse("note_create"), {
            "title": "New Note",
            "content": "Some content"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 1)
