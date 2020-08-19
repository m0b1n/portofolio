from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from datetime import datetime

from portofolio.models import MyUser
from django.contrib.auth.models import Permission
import logging


logger = logging.getLogger('django')


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    full_name = forms.CharField(label='Full Name')
    date_of_birth = forms.DateTimeInput()

    def __init__(self, *args, **kwargs): 
        super(UserCreationForm, self).__init__(*args, **kwargs) 
        self.fields['full_name'] = forms.CharField(label=("Full Name"), max_length=75)

    class Meta:
        model = MyUser
        fields = ('full_name', 'phone_number', 'date_of_birth','groups', 'password1', 'password2')
        labels = {
        "date_of_birth": "Birth Date"
    }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.first_name = self.cleaned_data.get("full_name").split(' ')[0]
        user.last_name = self.cleaned_data.get("full_name").split(' ')[1]
        if commit:
            user.save()
        
        
        # grp = self.cleaned_data.get("groups")
        # logger.info(user.id)
        # for g in grp:
        #     logger.info('name:{}'.format(g))
        #     g1 = Group.objects.get(name = g)
        #     pers = g1.permissions.all()
        #     # logger.info(g1.permissions.all())
        #     # for per in g1.permissions.all():
        #         # logger.info(per.id)
        #         # user.user_permissions.add(per)
        #     user.user_permissions.add(*pers)
            
        
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('phone_number', 'user_name', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin','date_of_birth')
    fieldsets = (
        (None, {'fields': ('user_name', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','email','phone_number', 'date_of_birth')}),
        ('Permissions', {'fields': ('user_permissions', 'groups')}),
        ('Status', {'fields': ('is_active','is_admin','is_superuser')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'phone_number', 'date_of_birth','groups', 'password1', 'password2'),
        }),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)
admin.site.register(Permission)
