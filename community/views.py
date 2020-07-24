from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from community.forms import *
from .models import Post

# Create your views here.
def write(request): # urls.py에서 사용자의 요청이 request 인자에 담김
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = Form()

	return render(request, 'write.html', {'form':form}) # write.html에 form 데이터가 전달됨 {'변수명':변수}

def list(request):
	articleList = Article.objects.all() # Article이라는 DB 테이블에 있는 모든(all) 컬럼을 가져와라
	return render(request, 'list.html', {'articleList':articleList})

def view(request, num="1"): # num의 defualt값이 1
	article = Article.objects.get(id=num)
	return render(request, 'view.html', {'article':article})

def curtime(request):
	return render(request, 'curtime.html')

def timeselect():
	return render(request, 'timeselect.html')

def create_post(request):
	posts = Post.objects.all()
	response_data = {}

	if request.POST.get('action') == 'post':
		title = request.POST.get('title')
		description = request.POST.get('description')

		response_data['title'] = title
		response_data['description'] = description

		Post.objects.create(
			title = title,
			description = description
			)
		return JsonResponse(response_data)

	return render(request, 'create_post.html', {'posts':posts})


class SignUpView(CreateView):
	template_name = 'user-name.html'
	form_class = UserCreationForm

def validate_username(request):
	username = request.GET.get('username', None)
	data = {
		'is_taken': User.objects.filter(username__iexact=username).exists()
	}
	return JsonResponse(data)
