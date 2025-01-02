from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.fields import ReCaptchaV2Checkbox
import imghdr
from django.core.exceptions import ValidationError

def validate_image(value):
    """
    Validates if the file has an allowed image extension (.jpg, .jpeg, .png, .gif)
    """
    try:
        # Check if file was uploaded
        if not value:
            raise ValidationError("No file was submitted.")
        
        # Valid extensions
        valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
        
        # Get the file extension
        ext = value.name.split('.')[-1].lower()
        
        # Check if extension is allowed
        if ext in valid_extensions:
            return value
                
        raise ValidationError(
            f"Invalid file extension. Got: .{ext}. "
            f"Allowed extensions: {', '.join(valid_extensions)}"
        )
    except Exception as e:
        raise ValidationError(f"Validation error: {str(e)}")


class userRegistration(UserCreationForm):
    full_name = forms.CharField(
        help_text='Enter your full name',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'})
    )
    email = forms.EmailField(
        help_text='ENTER YOUR EMAIL',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    image = forms.ImageField(validators=[validate_image], required=False)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = get_user_model()
        fields = ['full_name', 'username', 'email', 'password1', 'password2', 'image']
        exclude = ['profile_picture']

    def __init__(self, *args, **kwargs):
        super(userRegistration, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'You can enter your mobile number'
        })
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})
        self.fields['image'].widget.attrs.update({
            'class': 'form-control file-upload',
            'id': 'fileUpload',
            'onchange': 'validateFileSize(this)',
            'name' : 'image',
        })

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        name_parts = full_name.split()

        # Handle cases where there are multiple or no parts
        if len(name_parts) == 1:
            self.cleaned_data['first_name'] = name_parts[0]
            self.cleaned_data['last_name'] = ""
        elif len(name_parts) > 1:
            self.cleaned_data['first_name'] = name_parts[0]
            self.cleaned_data['last_name'] = " ".join(name_parts[1:])
        else:
            raise forms.ValidationError("Please enter at least a first name.")

        return full_name

    def save(self, commit=True):
        user = super(userRegistration, self).save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username or Email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})

    username = forms.CharField(
        widget=forms.TextInput(),
        label="Username or Email*"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Password*"
    )
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox()
    )

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address'
    }))
    image = forms.ImageField(validators=[validate_image], required=False)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'image']
        exclude = ['profile_picture']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'First Name'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())