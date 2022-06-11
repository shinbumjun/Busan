from django.db import models

# Create your models here.

from django.db import models
from users.models import User


class Board(models.Model):
    # 글의 제목, 내용, 작성일, 마지막 수정일
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="boards")
    title = models.CharField("제목", max_length=50, null=False)
    content = models.TextField("내용", null=False)
    dt_created = models.DateTimeField("작성일", auto_now_add=True, null=False)
    dt_modified = models.DateTimeField("수정일", auto_now=True, null=False)
    readcnt = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.readcnt = self.readcnt + 1
        self.save()

