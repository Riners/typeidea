from django.db import models

# Create your models here.


from blog.models import Post


class Comment(models.Model):
    STATUS_NOMARL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NOMARL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    target = models.ForeignKey(Post, verbose_name="评论目标")
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱")
    status = models.PositiveIntegerField(default=STATUS_NOMARL,
                                         choices=STATUS_ITEMS, verbose_name="状态")
    # is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    # owner = models.ForeignKey(User, verbose_name="作者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta():
        verbose_name = verbose_name_plural = '评论'
