# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
	queryset = Product.objects.all()
	context = {
		'qs': queryset
	}
	return render(request, "products/product_list.html", context)


@login_required
def product_details(request,pk=None,*args,**kwargs):

	try:
		product = Product.objects.get(pk=pk)
	except Exception as e:
		raise Http404("No product available.")
	context = { 'qs': product }
	return render(request, "products/product_details.html", context)
	