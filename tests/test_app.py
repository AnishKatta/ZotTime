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

    def test_calculate_results(self):
        place_id_1 = app.locate_classroom("BS3 1200")
        place_id_2 = app.locate_classroom("RH 104")
        results = app.calculate_results(place_id_1, place_id_2)
        self.assertEqual(results[0], "3 mins")
        self.assertEqual(results[1], "0.2 km")


