import unittest
import app


class TestApp(unittest.TestCase):

    def test_locate_classroom(self):
        course_classroom = "BS3 1200"
        place_id = app.locate_classroom(course_classroom)
        self.assertEqual(place_id, "ChIJgbL5DBHe3IARegC37HJWgDU")

    def test_find_classroom(self):
        course_classroom = app.find_classroom("2024", "Fall", "34061")
        self.assertEqual(course_classroom, "RH 104")

