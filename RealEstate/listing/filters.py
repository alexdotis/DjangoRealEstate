
from django_filters import FilterSet, filters
from django import forms
from .models import Listing
from typing import List, Tuple


def listing_choices(value: str) -> List[Tuple[str, str]]:
    model = Listing
    choices = model._meta.get_field(value).choices
    if choices is not None:
        return choices
    else:
        values = model.objects.values_list(
            value, flat=True).distinct()
        choices = list(set([(i, i)for i in values]))
        return sorted(choices)


class HomepageFilterForm(FilterSet):
    city = filters.ChoiceFilter(choices=listing_choices(
        'city'), empty_label='Cities', widget=forms.Select(attrs={'class': 'form-control select2'}))

    property_type = filters.ChoiceFilter(choices=listing_choices(
        'property_type'), empty_label='Property Type', widget=forms.Select(attrs={'class': 'form-control select2'}))

    class Meta:
        model = Listing
        fields = ['city', 'property_type']


class ListingFilter(FilterSet):
    status = filters.ChoiceFilter()
    bedrooms = filters.ChoiceFilter()
    bathrooms = filters.ChoiceFilter()

    min_size = filters.ChoiceFilter(field_name='area', label='Min size', lookup_expr='gt',
                                    choices=[(i, i) for i in range(100, 1100, 100)])
    max_size = filters.ChoiceFilter(field_name='area', label='Max size', lookup_expr='lt',
                                    choices=[(i, i)for i in range(1000, 11000, 1000)])

    subcategory = filters.CharFilter(
        field_name='subcategory', lookup_expr='icontains')
    city = filters.ChoiceFilter(field_name='city')

    order_by = filters.OrderingFilter(choices=[
        ('-price', 'High to Low'),
        ('price', 'Low to High'),
        ('-created_at', 'New'),
        ('created_at', 'Old'),
    ], empty_label='Sort By')

    def __init__(self, *args, **kwargs):
        super(ListingFilter, self).__init__(*args, **kwargs)

        self.filters['order_by'].field.widget.attrs.update(
            {'class': 'btn btn-primary btn-sm dropdown-toggle'})

        for field in self.get_fields():
            if self.filters[field].extra.get('choices') is None:
                self.filters[field].extra['choices'] = listing_choices(field)

            if len(field.split('_')) > 1:
                self.filters[field].extra.update(
                    {'empty_label': ' '.join(field.split('_')).title()})
            else:
                self.filters[field].extra.update(
                    {'empty_label': field.title()})
            self.filters[field].extra.update(
                {'widget': forms.Select(attrs={'class': 'form-control select2'})})

    class Meta:
        model = Listing
        fields = ['status','city',
                  'property_type', 'bedrooms',
                  'bathrooms', 'min_size', 'max_size']
