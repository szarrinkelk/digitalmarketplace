from django.shortcuts import render


def detail_view(request):
	print request
	template = "detail_view.html"
	context = {}
	return render(request, template, context)


def list_view(request):
	print request
	template = "list_view.html"
	context = {}
	return render(request, template, context)