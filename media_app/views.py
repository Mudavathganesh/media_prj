from django.http import HttpResponse
from.form import Resume_form
from django.shortcuts import render
# Create your views here.
def resume(request):
    if request.method=='POST':
        form=Resume_form(request.POST,request.FILES)
        if form.is_valid():
            return HttpResponse("data added ")
        else:
            return HttpResponse("data not added")
    else:
        form=Resume_form
        return render(request,'application.html',{'abc':form})
