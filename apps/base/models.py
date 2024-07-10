from django.db import models


# class BaseManager(models.Manager):
#     """Base manager for all models."""
#
#     def __delete__(self, instance):
#         # Переписать метод delete(). Помечать как удаленный(deleted_at)
#         pass
#
#     def __all__(self):
#         pass


class BaseModel(models.Model):
    """Base model for all models.

    Attributes:
        objects (models.Manager): for getting access to orm.
    """

    objects = models.Manager()

    # добавить общие поля.
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # deleted_at = models.DateTimeField(auto_now=True, default=None)
    # f = models.ForeignKey(to='df', on_delete=models.PROTECT)

    class Meta:
        abstract = True
