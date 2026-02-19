from typing import Annotated
from django.db import models


class NewUserInfo(models.Model):
    name: Annotated[
        models.CharField,
        """
        Нет проверки на уникальность.
        Предполагается, что пользователи могут быть с одинаковыми именами.
        Стандартное поле `id` является ключом сессии пользователя.
        """,
    ] = models.CharField(max_length=50)

    def __str__(self):
        return self.name
