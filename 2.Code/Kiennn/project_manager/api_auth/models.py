from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class CustomUser(AbstractUser):
    # Thêm các trường tùy chỉnh của bạn vào đây
    api_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
    
    def check_password(self, password):
        return self.password == password

    # Định rõ related_name cho các trường groups và user_permissions
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='custom_users',  # Đặt tên related_name tùy ý
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_users_permissions',  # Đặt tên related_name tùy ý
        related_query_name='custom_user_permission'
    )