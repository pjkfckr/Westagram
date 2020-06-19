from django.db import models
from account.models import Users


class Comments(models.Model):
	email = models.ForeignKey(Users, on_delete = models.CASCADE, blank=True)
	comment = models.TextField(max_length = 600)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = "comments"
