from django.db.models import Q
from ninja import FilterSchema, Query

from tasks.enums import TaskStatus


class TaskFilter(FilterSchema):
    title: str | None = None
    status: TaskStatus | None = Query(
        default=None,
        description='Доступные статусы: created, active, completed',
    )

    def filter_title(self, value: bool) -> Q:
        return Q(title__icontains=value) if value else Q()