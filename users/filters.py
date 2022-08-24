import django_filters
from django_filters import FilterSet

from users.models import Profile


class UserFilters(FilterSet):

    last_name = django_filters.CharFilter(
        field_name="user__last_name", lookup_expr="icontains"
    )
    first_name = django_filters.CharFilter(
        field_name="user__first_name", lookup_expr="icontains"
    )
    username = django_filters.CharFilter(
        field_name="user__username", lookup_expr="icontains"
    )
    email = django_filters.CharFilter(field_name="user__email", lookup_expr="icontains")
    is_active = django_filters.BooleanFilter(field_name="user__is_active")
    gender = django_filters.CharFilter(
        field_name="user__gender", lookup_expr="icontains"
    )


    class Meta:
        model = Profile

        fields = [
            "last_name",
            "first_name",
            "username",
            "email",
            "is_active",
            "gender",
        ]