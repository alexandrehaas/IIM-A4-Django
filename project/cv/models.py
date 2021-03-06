from django.db import models
from django import forms
from multiselectfield import MultiSelectField
from django.forms import ModelForm
from .validators import validate_file_extension

# Create your models here.
SKILLS = (
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('js', 'JavaScript'),
        ('sass', 'Sass'),
        ('ts', 'Typescript'),
        ('react', 'React'),
        ('angular', 'Angular'),
        ('vue', 'Vue'),
        ('swift', 'Swift'),
        ('kotlin', 'Kotlin'),
        ('reactNative', 'React Native'),
        ('ionic', 'Ionic'),
        ('php', 'PHP'),
        ('symfony', 'Symfony'),
        ('laravel', 'Laravel'),
        ('drupal', 'Drupal'),
        ('wordpress', 'Wordpress')
    )

class Applicant(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=320, unique=True)
    skills = MultiSelectField(max_choices=8, max_length=255, choices=SKILLS, blank=True)
    cv = models.FileField(upload_to='cv/', validators=[validate_file_extension])
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.email}"

class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ['first_name', 'last_name', 'email', 'skills', 'cv']
        widgets = {
            'first_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'email': forms.TextInput(attrs={'class' : 'form-control'}),
            'cv': forms.FileInput(attrs={'class': "form-control-file"})
            }

class SearchSkill(ModelForm):
    class Meta:
        model = Applicant
        fields = ['skills']