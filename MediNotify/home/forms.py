from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Contacts,MedicineDetails
from phonenumber_field.formfields import PhoneNumberField 
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .widget import DatePicker,TimePicker

class SignUpForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=get_user_model()
        fields=('first_name','last_name','username','email','password1','password2')
    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
    # def save(self,commit=True):
    #     instance=super(SignUpForm,self).save(commit=False)
    #     instance=self.cleaned_data['email']
    #     if commit:
    #         instance.save()
    #     return instance
class LoginForm(AuthenticationForm):
    username=forms.CharField(label='Email/Username')
    def __init__(self,request,*args,**kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control input-lg'
        self.fields['username'].widget.attrs['placeholder']='Enter Email / Username'
        self.fields['password'].widget.attrs['class']='form-control input-lg'
        self.fields['password'].widget.attrs['placeholder']='Enter Password'


class MedicineDetailsForm(forms.ModelForm):    
    start_date=forms.DateField(widget=DatePicker(attrs={'class':'form-control'}))
    end_date=forms.DateField(widget=DatePicker(attrs={'class':'form-control'}))
    time_1=forms.TimeField(widget=TimePicker(attrs={'class':'form-control'}))
    time_2=forms.TimeField(widget=TimePicker(attrs={'class':'form-control'}),required=False)
    time_3=forms.TimeField(widget=TimePicker(attrs={'class':'form-control'}),required=False)

    medicine_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Medicine Name'}))
    doctor_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Doctor Name'}))
    
    dosage_1=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Dose at time 1'}))
    dosage_2=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Dose at time 2'}),required=False)
    dosage_3=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Dose at time 3'}),required=False)

    dosage_1_unit=forms.ChoiceField(choices=MedicineDetails.dosage_unit_choice,initial='',widget=forms.Select(attrs={'class':'form-control','placeholder':'tb/ml?'}),required=True)
    dosage_2_unit=forms.ChoiceField(choices=MedicineDetails.dosage_unit_choice,widget=forms.Select(attrs={'class':'form-control','placeholder':'tb/ml?'}),required=False)
    dosage_3_unit=forms.ChoiceField(choices=MedicineDetails.dosage_unit_choice,widget=forms.Select(attrs={'class':'form-control','placeholder':'tb/ml?'}),required=False)

    repeat=forms.ChoiceField(choices=MedicineDetails.repeat_choice,widget=forms.Select(),required=True)
    class Meta:
        model=MedicineDetails
        fields=['medicine_name','doctor_name','start_date','end_date','time_1','dosage_1','dosage_1_unit','time_2','dosage_2','dosage_2_unit','time_3','dosage_3','dosage_3_unit','repeat']
    
class ContactsForm(forms.ModelForm):
    contact_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the person name you wish to notify'}))
    relation_type=forms.ChoiceField(choices=Contacts.relation_choice,widget=forms.Select(attrs={'class':'form-control','placeholder':'Your relation with the person?'}),required=True)
    contact_phone_number=PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='IN',attrs={'class':'form-control','placeholder':'Enter the contact number of the person (whatsapp)'}),required=True)
    contact_email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter the email of the person (optional)'}),required=False)
    class Meta:
        model=Contacts
        fields=['contact_name','relation_type','contact_phone_number','contact_email']