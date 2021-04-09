from django.shortcuts import render
from django.http import HttpResponse
# from djoser.serializers import LoginSerializer
# from djoser.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt 

def index(request):
    print('yes')
    return render(request, 'index.html')
    # HttpResponse()


# class ApiLoginView(LoginView):
    # serializer_class = LoginSerializer
    # pass

@csrf_exempt
def LoginCheck(request):
	# print('request.method', request.method)
	# print(request.POST)
	# exit()
	auth_data = {
		"username" : request.POST.get('username'),
		"password" : request.POST.get('password')
	}
	# auth_data = {
	# 	"username" : "mohi",
	# 	"password" : "123"
	# }
	# user_name = User.objects.get(username="mohi", password="123")
	# status = authenticate(username=user_name, password="123")
	
	status = authenticate(**auth_data)
	print('status', status, auth_data)
	return HttpResponse("Not signed in")
	# status = authenticate(**auth_data)
	# if status:
	# 	user = User.objects.get(username=auth_data["username"])
	# print('status', status, auth_data)
	# return HttpResponse({"token": user})


@csrf_exempt
def LoginView(request):
	# print('request.method', request.method)
	# if request.method =="POST":
	# 	print('request.POST', request.POST)
	# 	exit()
	# 	return None
	# 	# .get('value')

	
	return render(request, 'login.html')