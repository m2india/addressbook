from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from addressbook.apps.models import add
from addressbook.apps.forms import adddetailform

def adddetails(request):
	
	if request.method =="POST":
		form = adddetailform(request.POST) # adddetailform is a form name
		info = "Initialization"
		if form.is_valid():
			name = form.cleaned_data['name']
			dateofbirth = form.cleaned_data['dateofbirth']
			address = form.cleaned_data['address']
			phone_number = form.cleaned_data['phone_number']
			email = form.cleaned_data['email']
			state = form.cleaned_data['state']
			country = form.cleaned_data['country']
			p = add() # model name add
			p.name = name
			p.dateofbirth  = dateofbirth
			p.address = address
			p.phone_number = phone_number
			p.email =  email
			p.state = state
			p.country = country
			p.save()
			#info = " see congregation "
			
		else:
			info = " informations "
		form = adddetailform() 
		ctx = {'form':form, 'information':info}
		return HttpResponse(' your submitted successfull, thank you !') # after send thanks msg
		return render_to_response('addform.html', ctx, context_instance=RequestContext(request))
		
			
			
	else:
		form = adddetailform()
		ctx = {'form':form}
		
		return render_to_response('addform.html',ctx, context_instance=RequestContext(request))
		#return HttpResponse('Thanks for your comment!')
		
		
		
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        ads = add.objects.filter(name__icontains=q)
        ctx = {'ads': ads, 'query': q}
        return render_to_response('search_form.html',ctx, context_instance=RequestContext(request))
    else:
        ctx = {'error': True}
        return render_to_response('search_form.html',ctx, context_instance=RequestContext(request))
		
		
		
		
		
		
		
				
