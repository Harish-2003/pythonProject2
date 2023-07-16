from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import items,cart,cart2
# Create your views here.
def home(r):
    obj=items.objects.all()
    return render(r,'main.html',{'values':obj})
def itemdesc(r,uid):
    object=items.objects.get(id=uid)
    return render(r,'desc.html',{'object':object})
def addcart(r,uid):
    username=r.user.username
    uid=uid
    item1=items.objects.get(id=uid)
    item=item1.name
    obj=cart(username=username,uid=uid,item=item)
    obj.save()
    return redirect('/home')
def viewcart(r):
    obj=cart.objects.all()
    for i in obj:
        if(i.username==r.user.username):
            k=cart2(item=i.item)
    ob2=cart2.objects.all()
    return render(r,'cart.html',{'k':ob2})
