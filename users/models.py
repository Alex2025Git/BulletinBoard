from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Необходимо указать Email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """описание модели пользователя"""

    CHOICES_USER_ROLE = [
        ("admin", "Администратор"),
        ("user", "Пользователь"),
    ]

    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="Адрес электронной почты",
        help_text="Укажите адрес электронной почты"
    )
    token_for_password = models.CharField(
        max_length=110,
        verbose_name="Токен",
        blank=True,
        unique=True,
        null=True
    )
    object = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    phone = models.CharField(
        max_length=35,
        unique=True,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    first_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Имя",
        blank=True,
        null=True,
        help_text="Укажите Имя",
    )

    last_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Фамилия",
        blank=True,
        null=True,
        help_text="Укажите Фамилию",
    )
    image = models.ImageField(
        upload_to="image",
        verbose_name="Фото",
        blank=True,
        null=True,
        help_text="Загрузите фото",
    )

    role = models.CharField(
        max_length=100,
        choices=CHOICES_USER_ROLE,
        default="user",
        help_text="Укажите роль"
        ,
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
        help_text="Укажите страну",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
