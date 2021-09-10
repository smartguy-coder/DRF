from django.db import models

# Добавить Post, Comment, Category модели в проект (со связями между ними) - аналог любого блога.


class User(models.Model):
    """
    everyone can create post and comment other posts
    """
    first_name = models.CharField(max_length=30, null=False)
    surname = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=False)
    user_age = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.first_name}, {self.surname}"

    class Meta:
        constraints = [models.CheckConstraint(check=models.Q(user_age__gte=18), name='user_age_gte_18'), ]


class PostCategory(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['category']


class Post(models.Model):
    post_title = models.CharField(max_length=100, null=False)
    post_time_published = models.DateTimeField(auto_now_add=True)
    post_category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, null=False)  # one category can have many posts
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)  # one user can create many posts

    def __str__(self):
        return f'{self.post_title}'

    class Meta:
        ordering = ['post_time_published']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)    # many comments for one post
    comment_text = models.TextField(max_length=200, null=False)
    comment_time_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text

    class Meta:
        order_with_respect_to = ['post']