from django.http import JsonResponse, HttpResponse
from .models import Users
from django.views import View
import json
import bcrypt
import jwt



class SignUp(View):
	def post(self, request):
		account_data = json.loads(request.body)
		try:
			hashed_password = bcrypt.hashpw(account_data["password"].encode("utf-8"), bcrypt.gensalt())
			if not Users.objects.filter(email = account_data["email"]):
				Users.objects.create(
						email = account_data["email"],
						password = hashed_password
				)
				return JsonResponse({"message" : "Account Good"}, status = 200)
			else:
				return JsonResponse({"message" : "Already SignUp!"}, status = 400)
		except KeyError:
			return JsonResponse({"message" : "Key Error"}, status = 409)


class SignIn(View):
	def post(self, request):
		account_data = json.loads(request.body)
		try:
			encoded_password = account_data["password"].encode("utf-8")
			if Users.objects.filter(email = account_data["email"]).exists():
				user_jwt = jwt.encode({"email" : account_data["email"]}, "secret", algorithm="HS256")
				signin = Users.objects.get(email = account_data["email"])
				if bcrypt.checkpw(encoded_password, signin.password):
					return JsonResponse({"token" : user_jwt.decode("utf-8")}, status = 200)
				else:
					return JsonResponse({"message" : "Wrong password"}, status = 400)
			else:
				return JsonReponse({"message" : "Wrong Name"}, status = 400)
		except KeyError:
			return JsonResponse({"message" : "Invalid_Key"}, status = 400)
		except:
			return JsonResponse({"message" : "Invalid_token"}, status = 404)



