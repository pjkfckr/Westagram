from django.db import models


class Users(models.Model):
	email = models.CharField(max_length = 100)
	password = models.BinaryField(max_length = 500)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = "account"
