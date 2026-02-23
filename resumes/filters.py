import django_filters
from .models import ResumeUpload


class ResumeFilter(django_filters.FilterSet):
    uploaded_after = django_filters.DateFilter(
        field_name="uploaded_at", lookup_expr="gte"
    )
    uploaded_before = django_filters.DateFilter(
        field_name="uploaded_at", lookup_expr="lte"
    )

    class Meta:
        model = ResumeUpload
        fields = ["uploaded_at", "uploaded_before"]
