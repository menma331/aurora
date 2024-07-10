from django.db import models

from apps.base.models import BaseModel


class Tag(BaseModel):
    tag_name = models.CharField(
        max_length=12, unique=True, db_index=True, verbose_name="Название тега"
    )
    user = models.ManyToManyField(
        to="User",
        related_name="tag",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
