from django.urls import reverse
from users.models import User
from articles.models import Category

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField()
    comment_count = models.IntegerField()
    categori = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    # 왜 사용하는지 확인할 것!
    # def get_absolute_url(self):
    #     return reverse('article_detail_view', kwargs={"article_id":self.id})
     
    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Categories'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) # unique=True, 동일한 name을 갖는 카테고리를 만들 수 없다.
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True) # allow_unicode=True, 한글 지원

    def __str__(self):
        return self.name