import pytest
import account
from account.forms import SignUpForm,LoginForm
from account.views import login_view
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User


# test login user 
@pytest.mark.django_db
def test_auth_view(client):
    user = User.objects.create(username = 'mih', password ='1234')
    client.login(username = 'mih', password ='1234')
    url = reverse('account:login')
    response = client.get(url)

    assert response.status_code == 200 


@pytest.mark.parametrize('data_registration', [
    {'username': 'ded', 'email': 'artemsim2011@mail.ru', 'password1': 'abcd12339', 'password2': 'abcd12339'},

])




# @pytest.fixture
# def valid_data():
#     return {
#         'username': 'al',
#         'email': 'artemsim20121@mail.ru',
#         "password1": 'artemsimOP1234d5',
#         "password2": 'artemsimOP1234d5',
#     }

# test form registaration
@pytest.mark.django_db
def test_register_form(data_registration):
    form = SignUpForm(data=data_registration)
    assert form.is_valid()

    user = form.save()
    assert user.email == 'artemsim2011@mail.ru' 

# @pytest.mark.parametrize('data_login',[
#     {'username': 'artem', 'password': '!S:cLm2)y=Tm,b@'},
# ])

# @pytest.mark.django_db
# def test_login_form(data_login):
#     form = LoginForm(data=data_login)
#     assert form.is_valid()

