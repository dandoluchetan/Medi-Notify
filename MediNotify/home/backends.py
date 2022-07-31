from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model#returns the user model that is active in this project, i.e returns home.CustomUser
from django.db.models import Q

UserModel=get_user_model()

class EmailBackend(ModelBackend):
    #will make sure user's can use either username or email to login.
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            user=UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
