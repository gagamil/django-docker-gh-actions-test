from django.test import TestCase


class FooTestCase(TestCase):
    def test_foo(self):
        self.assertEqual(1-1, 0)