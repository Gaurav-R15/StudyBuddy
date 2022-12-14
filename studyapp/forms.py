from django import forms
from .models import Meeting, Profile
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class MeetingCreateForm(forms.ModelForm):
    class Meta:
        model = Meeting
        # no idea if this is right
        # start_time = forms.DateTimeField()
        # end_time = forms.DateTimeField()
        fields = [
            'location',
            'course',
            'start_time',
            'end_time',
            'post_text',
            'buddies' 
        ]
        widgets = {
            'start_time': DateTimePickerInput(options = {
                "showClose": True,
                "showClear": True,
            }),
            'end_time': DateTimePickerInput(options = {
                "showClose": True,
                "showClear": True,
            }), 
        }
# class EnrollForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = [
#             'profile_courses',
#         ]