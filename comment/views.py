from .models import Comments
from account.models import Users
from django.views import View
from django.http import JsonResponse
import jwt
import json

def login_decorator(func):
	def wrapper(self, request):
		try:
			user_token = request.headers.get("Authorization")
			decoded_token = jwt.decode(user_token, "secret", algorithms="HS256")
			if Users.objects.filter(email = decoded_token["email"]).exists():
				user = Users.objects.get(email = decoded_token["email"])
				request.user = user
				return func(self, request)
			else:
				return JsonReponse({"message" : "dosen't match data"}, status = 400)
		except KeyError:
			return JsonResponse({"message" : "Invalid Key"}, status = 400)
	return wrapper
					
	





class CommentsView(View):

	@login_decorator
	def post(self, request):

		user = request.user
		user_comment = json.loads(request.body)
		try:
			Comments(
					email = Users.objects.get(email = user.email),
					comment = user_comment['comment'],
			).save()
			return JsonResponse({"message" : "good"}, status = 200)
		except KeyError:
			return JsonResponse({"message" : "KeyError"}, status = 400)

	def get(self, request):
		user_comment = Comments.objects.values()
		return JsonResponse({"Comments" : list(user_comment)}, status =200)

	
