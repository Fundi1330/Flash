# from django.test import TestCase

# from flash_app.forms import AuthenticationForm

# import datetime

# from django.utils import timezone

# class TestForms(TestCase):
#     def test_validation_normal(self):
#         date = datetime.date.today() - datetime.timedelta(days=1)
#         form = AuthenticationForm(date={'date': date})
#         self.assertTrue(form.is_valid())

#     def test_validation_past(self):
#         date = datetime.date.today()
#         form = AuthenticationForm(date={'date': date})
#         self.assertTrue(form.is_valid())

#     def test_validation_future(self):
#         date = datetime.date.today() - datetime.timedelta(days=60)
#         form = AuthenticationForm(date={'date': date})
#         self.assertTrue(form.is_valid())