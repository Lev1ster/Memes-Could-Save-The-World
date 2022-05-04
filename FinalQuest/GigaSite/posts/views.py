from django.shortcuts import render

# Create your views here.
def index(request, question_id):
	return HttpResponse("Hello! This is posts");
