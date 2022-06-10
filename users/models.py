from django.db import models


class User(models.Model):
    use_in_migrations = True
    username = models.CharField(primary_key=True, max_length=10)  # 필드 설정.
    password = models.CharField(max_length=10)
    name = models.TextField()
    email = models.TextField()
    regDate = models.DateField()

    class Meta:
        db_table = 'users'  # 자바의 @Table(name="users")

    def __str__(self):  # 자바의 toString
        return f'{self.pk} {self.username}'

