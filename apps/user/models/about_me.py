from django.db import models

from apps.base.models import BaseModel


class AboutMe(BaseModel):
    """About user model. Has relation with `User` model by field `user`.

    Attributes:
        text (CharField): text about user.
        user (OneToOneField): relation with `User` model.
    """

    text = models.CharField(max_length=450, verbose_name="О пользователе")
    user = models.OneToOneField(
        to="User",
        related_name="user",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
