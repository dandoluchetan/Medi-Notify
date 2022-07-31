from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from datetime import date,time
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    email=models.EmailField(_('email address'), unique=True)
    first_name=models.CharField(_('First name'),max_length=50)
    last_name=models.CharField(_('Last name'),max_length=50)

# Create your models here.
class MedicineDetails(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=False)
    medicine_name=models.CharField(max_length=128)
    doctor_name=models.CharField(max_length=128)
    start_date=models.DateField(auto_now_add=False,auto_now=False,blank=False)
    end_date=models.DateField(auto_now_add=False,auto_now=False,blank=False)
    
    TABLET=10
    VOLUME=11
    dosage_unit_choice=(
        (TABLET,'tb'),
        (VOLUME,'ml')
    )

    time_1=models.TimeField(auto_now_add=False,auto_now=False,blank=False)
    dosage_1=models.PositiveIntegerField(blank=False,null=False)
    dosage_1_unit=models.IntegerField(choices=dosage_unit_choice,default=TABLET,blank=False,null=False)
    
    time_2=models.TimeField(auto_now_add=False,auto_now=False,blank=True)
    dosage_2=models.PositiveIntegerField()
    dosage_2_unit=models.IntegerField(choices=dosage_unit_choice,default=TABLET)

    time_3=models.TimeField(auto_now_add=False,auto_now=False,blank=True)
    dosage_3=models.PositiveIntegerField()
    dosage_3_unit=models.IntegerField(choices=dosage_unit_choice,default=TABLET)
    
    DAILY=101
    ALTERNATE=102
    WEEKLY=103
    MONTHLY=104
    
    repeat_choice=(
        (DAILY,'daily'),
        (ALTERNATE,'alternate days'),
        (WEEKLY,'weekly'),
        (MONTHLY,'monthly')
    )
    repeat=models.IntegerField(choices=repeat_choice,default=DAILY)

    def __str__(self):
        return medicine_name

class Contacts(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=False)
    contact_name=models.CharField(max_length=128,blank=False)
    contact_phone_number=PhoneNumberField()
    contact_email=models.EmailField(help_text='Optional',blank=True)

    FRIEND=1001
    FATHER=1002
    MOTHER=1003
    SISTER=1004
    BROTHER=1005
    SON=1006
    DAUGHTER=1007
    HUSBAND=1008
    WIFE=1009
    INLAW=1010
    GRANDPARENT=1011
    GRANDCHILD=1012
    AUNT=1013
    UNCLE=1014
    COUSIN=1015

    relation_choice=(
        (FRIEND,'friend'),
        (FATHER,'father'),
        (MOTHER,'mother'),
        (SISTER,'sister'),
        (BROTHER,'brother'),
        (SON,'son'),
        (DAUGHTER,'daughter'),
        (HUSBAND,'husband'),
        (WIFE,'wife'),
        (INLAW,'inlaw'),
        (GRANDPARENT,'grandparent'),
        (GRANDCHILD,'grandchild'),
        (AUNT,'aunt'),
        (UNCLE,'uncle'),
        (COUSIN,'cousin')
    )

    relation_type=models.IntegerField(choices=relation_choice,default=FRIEND)
    def __str__(self):
        return contact_name
    
    

