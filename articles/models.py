from django.db import models


class Article(models.Model):
    use_in_migrations = True
    articleId = models.CharField(primary_key=True, max_length=10)  # 필드 설정.
    title = models.TextField()
    content = models.TextField()
    writtenDate = models.DateField()

    class Meta:
        db_table = 'articles'  # 자바의 @Table(name="users")

    def __str__(self):
        return f'{self.pk} {self.articleId}'

