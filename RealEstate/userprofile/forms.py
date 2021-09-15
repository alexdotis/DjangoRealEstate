from listing.models import ExtraFeature,Listing,ListingImages
from django import forms
from authentication.models import Agent, User
from django.forms.models import inlineformset_factory
from .models import AssignmentProperty


class UserUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs) -> None:
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']



class AgentProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(AgentProfileUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Agent
        fields = '__all__'
        exclude = ('user',)


class AgentPropertyCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(AgentPropertyCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Listing
        fields = "__all__"
        exclude = ('updated_at', 'active','agent')


class ExtraFeaturesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(ExtraFeaturesForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ExtraFeature
        fields = ('feature', 'choice',)


class ListingImagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(ListingImagesForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ListingImages
        fields = ('image',)


FeatureForm = inlineformset_factory(
    Listing, ExtraFeature, form=ExtraFeaturesForm, extra=2, can_delete=False)
ImagesForm = inlineformset_factory(
    Listing, ListingImages, form=ListingImagesForm, extra=3, can_delete=False)
# OtherInitialForm  = inlineformset_factory(Property,PropertyImages,form=PropertyImagesForm,can_delete=False,extra=2)


class UserAddListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(UserAddListingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = AssignmentProperty
        fields = '__all__'
        exclude = ('user', 'is_assigned')


class UserListingUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(UserListingUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = AssignmentProperty
        fields = '__all__'
        exclude = ('agency',)
