from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Wines
from itertools import chain

def wines_view(request):
	if request.method == 'POST':
		wines = Wines.objects.all().order_by('price')
	else:		
		wines = Wines.objects.all()
	
	countries = Wines.objects.order_by().values_list('country',flat=True).distinct()
	varieties = Wines.objects.order_by().values_list('variety',flat=True).distinct()
	provincies  = Wines.objects.order_by().values_list('province',flat=True).distinct()
	region_1 = Wines.objects.order_by().values_list('region_1',flat=True).distinct()
	region_2 = Wines.objects.order_by().values_list('region_2',flat=True).distinct()
	regions = list(chain(region_1, region_2))

	return render(request,'wines/wines_list.html',{'wines':wines,'countries':countries,'varieties':varieties,'provincies':provincies,'regions':regions})

def filter_wines(request):
	if request.method =='POST':
		print(request.POST)
		if request.POST.__contains__('variety'):
			variety = request.POST.get('variety')
			wines = Wines.objects.all().filter(variety = variety)
			head = 'Wines of Type : ' + variety
			return render(request,'wines/filtered_wines.html',{'wines':wines,'head':head})

		elif request.POST.__contains__('country'):
			country = request.POST.get('country')
			wines = Wines.objects.all().filter(country = country)
			head = 'Wines in Country : ' + country
			return render(request,'wines/filtered_wines.html',{'wines':wines,'head':head})

		elif request.POST.__contains__('province'):
			province = request.POST.get('province')
			wines = Wines.objects.all().filter(province = province)
			head = 'Wines in Province : ' + province
			return render(request,'wines/filtered_wines.html',{'wines':wines,'head':head})

		elif request.POST.__contains__('region'):
			region = request.POST.get('region')
			wines_1 = Wines.objects.all().filter(region_1 = region)
			wines_2 = Wines.objects.all().filter(region_2 = region)
			wines = list(chain(wines_1, wines_2))
			head = 'Wines in Region : ' + region
			return render(request,'wines/filtered_wines.html',{'wines':wines,'head':head})		

		else :
			return wines_view(request)
	else:
		return HttpResponse('Get req to filter')

