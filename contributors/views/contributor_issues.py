from django.views import generic

from contributors.models import Contribution
from contributors.views.mixins import TableSortSearchAndPaginationMixin


class ListView(TableSortSearchAndPaginationMixin, generic.ListView):
    """A list of issues of a contributor."""

    template_name = 'contributor_issues.html'
    sortable_fields = (
        'info__title',
        'repository__full_name',
        'created_at',
        'html_url',
    )
    searchable_fields = (
        'info__title',
        'repository__full_name',
        'created_at',
        'html_url',
    )
    ordering = sortable_fields[0]

    def get_queryset(self):
        """Get issues from contributions.

        Returns:
            Queryset.
        """
        self.queryset = Contribution.objects.select_related('info').filter(
            contributor__login=self.kwargs['slug'], type='iss',
        )
        return super().get_queryset()
