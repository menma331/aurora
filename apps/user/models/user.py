from django.db import models
from django.db.transaction import atomic
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from apps.user.models.about_me import AboutMe


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers

    Attrs:


    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        with atomic():
            email = self.normalize_email(email)

            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        with atomic():
            extra_fields.setdefault("is_active", True)
            extra_fields.setdefault("is_staff", True)
            extra_fields.setdefault("is_admin", True)
            extra_fields.setdefault("is_superuser", True)

            return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    """
    Custom user model.

    Attributes:
        name (str): User's name. Maximum length is 12 characters.
        email (str): User's email address. Must be unique.
        gender (str): User's gender. Possible values: "M" (Male), "F" (Female).
        age (date): User's birthdate. Default value is '1970-11-11'.
        purpose_of_communication (str): User's purpose of communication. Possible values:
            "DT" (Dating), "FR" (Friendly communication), "SR" (Serious relationship), "DK" (Don't know yet).
        about_me (OneToOne): Relationship to the `AboutMe` model, contains information "About Me".
        city (str): User's city of residence. Maximum length is 15 characters.
        is_verified (bool): Indicates if the user is verified. Default is False.
        is_banned (bool): Indicates if the user is banned. Default is False.
        is_active (bool): Indicates if the user is active. Default is True.
        is_admin (bool): Indicates if the user is an administrator. Default is False.
        is_staff (bool): Indicates if the user is a staff member. Default is False.
        is_superuser (bool): Indicates if the user is a super administrator. Default is False.
    """

    class GenderChoices(models.TextChoices):
        """Choices for choosing a gender."""

        MALE = "M", _("Мужской")
        FEMALE = "F", _("Женский")

    class PurposeOfCommunication(models.TextChoices):
        """Choices for choosing a purpose of communication."""

        DATING = "DT", _("Свидания")
        FRIENDSHIP = "FR", _("Дружеское общение")
        SERIUS_RELATIONSHIP = "SR", _("Серьёзные отношения")
        DONT_KNOW = "DK", _("Пока не знаю")

    objects = UserManager()
    name = models.CharField(max_length=12, verbose_name="Имя")
    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    gender = models.CharField(
        max_length=1, choices=GenderChoices.choices, verbose_name="Пол"
    )
    age = models.DateField(default='1970-11-11', verbose_name="Возраст")
    purpose_of_communication = models.CharField(
        max_length=2,
        choices=PurposeOfCommunication.choices,
        blank=True,
        default=PurposeOfCommunication.DONT_KNOW,
        verbose_name="Цель общения",
    )
    about_me = models.OneToOneField(
        to=AboutMe,
        related_name="about_me",
        on_delete=models.CASCADE,
        verbose_name="Обо мне",
    )
    city = models.CharField(max_length=15, verbose_name="Город")
    # tags = models.ForeignKey
    # avatars = models.ForeignKey(to='Avatar', )
    is_verified = models.BooleanField(
        default=False, verbose_name="Пользователь верифицирован"
    )
    is_banned = models.BooleanField(default=False, verbose_name="Пользователь забанен")
    is_active = models.BooleanField(default=True, verbose_name="Пользователь онлайн")
    is_admin = models.BooleanField(
        default=False, verbose_name="Пользователь администратор"
    )
    is_staff = models.BooleanField(default=False, verbose_name="Пользователь сотрудник")
    is_superuser = models.BooleanField(
        default=False, verbose_name="Пользователь супер-админ"
    )

    USERNAME_FIELD = 'email'
