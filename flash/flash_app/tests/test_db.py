# from django.test import TestCase
# from flash_app.models import FlashUser

# class DBTestCase(TestCase):
#     @classmethod
#     def setUpTestData(self):
#         FlashUser.objects.create(username='Bot.bot', full_name='Bot botik', email='bot@gmail.com')

#     def test_full_name(self):
#         user = FlashUser.objects.get(id=1)
#         full_name = user._meta.get_field('full_name').verbose_name
#         self.assertEqual(full_name, 'full name')

#     def test_join_date(self):
#         user = FlashUser.objects.get(id=1)
#         join_date = user._meta.get_field('date_joined').verbose_name
#         self.assertEqual('date joined', join_date)

#     def test_str(self):
#         user = FlashUser.objects.get(id=1)
#         excpeted = f'<FlashUser {user.username}>'
#         self.assertEqual(str(user), excpeted)