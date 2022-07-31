from django import forms
from ads.models import Pic
from humanize import naturalsize
from django.core.files.uploadedfile import InMemoryUploadedFile
class CreateForm(forms.ModelForm):
    max_upload_limit=2*1024*1024
    max_upload_limit_text=naturalsize(max_upload_limit)

    picture=forms.FileField(required=False,help_text="File to upload <="+max_upload_limit_text)
    upload_field_name='picture'
    class Meta:
        model=Pic
        fields=['title','text','picture']
    #till GET

    #From POST
    #To validate size of picture in case someone bypass the JQuery
    def clean(self):
        cleaned_data=super().clean()
        pic=cleaned_data.get('picture')
        if pic is None: return
        if len(pic)>self.max_upload_limit:
            self.add_error('picture','File must be less than '+self.max_upload_limit_text+' bytes')
    
    def save(self,commit=True):
        instance=super(CreateForm,self).save(commit=False)
        f=instance.picture
        if isinstance(f,InMemoryUploadedFile):#extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearr
            
        if commit:
            instance.save()
        return instance



    
