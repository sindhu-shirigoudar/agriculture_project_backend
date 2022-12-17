from django.contrib.auth.models import User
import datetime


def create_user(username, email):
    x = datetime.datetime.now()
    current_year = x.year
    current_year = str(current_year)
    password = username + 'P' + current_year + '_$'
    user = User.objects.create_user(username, email, password)

    # def update_user():

