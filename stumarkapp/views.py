from django.shortcuts import render,redirect, get_object_or_404
from .models import cs_dep
from .models import csdep_sem2
from.models import csdep_sem3
from.models import csdep_sem4
from.models import csdep_sem5
from .models import csdep_sem6

from .forms import cs_sem1
from .forms import cs_sem2
from .forms import cs_sem3
from .forms import cs_sem4
from .forms import cs_sem5
from .forms import cs_sem6

# Create your views here.
def home(request):
    return render(request,'home.html')
def base(request):
    return render(request,'base.html')
def dep_read(request):
    return render(request,'dep_read.html')
def viewmark(request):
    return render(request,'viewmark.html')
def readstu(request):
    students = cs_dep.objects.all()
    sem2=csdep_sem2.objects.all()
    context = {
        'students': students,
        'semester2':sem2,
    }
    return render(request, 'readstu.html', context)

def nsem1(request):
    a=cs_dep()
    if request.method=='POST':
        if request.POST.get('stuname')and request.POST.get('regno')and request.POST.get('stuclass')and request.POST.get('sub1')and request.POST.get('sub2')and request.POST.get('sub3')and request.POST.get('sub4')and request.POST.get('sub5'):
            a.stuname=request.POST.get('stuname')
            a.regno=request.POST.get('regno')
            a.stuclass = request.POST.get('stuclass')
            a.sub1 = request.POST.get('sub1')
            a.sub2 = request.POST.get('sub2')
            a.sub3 = request.POST.get('sub3')
            a.sub4 = request.POST.get('sub4')
            a.sub5 = request.POST.get('sub5')
            a.save()
        return render(request,'viewmark.html')
    return render(request,'nsem1.html')

def usem1(request):
    sem1=cs_dep.objects.all()
    return render(request, 'usem1.html', locals())

def esem1(request,id):
    ac={}
    obj=get_object_or_404(cs_dep, pk=id)
    form = cs_sem1(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/usem1")
    ac["cc"]=form
    return render(request,"esem1.html",ac)

def dsem1(request):
    sem1=cs_dep.objects.all()
    return render(request,'dsem1.html',locals() )
def delsem1(request,id):
    ds={}
    obj=get_object_or_404(cs_dep, pk=id)
    if request.method=="POST":
        obj.delete()
        return redirect("/dsem1")
    return render(request,"delsem1.html",ds)

def nsem2(request):
    a=csdep_sem2()
    if request.method=='POST':
        if request.POST.get('stuname')and request.POST.get('regno')and request.POST.get('stuclass')and request.POST.get('sub6')and request.POST.get('sub7')and request.POST.get('sub8')and request.POST.get('sub9')and request.POST.get('sub10'):
            a.stuname=request.POST.get('stuname')
            a.regno=request.POST.get('regno')
            a.stuclass = request.POST.get('stuclass')
            a.sub6 = request.POST.get('sub6')
            a.sub7 = request.POST.get('sub7')
            a.sub8 = request.POST.get('sub8')
            a.sub9 = request.POST.get('sub9')
            a.sub10 = request.POST.get('sub10')
            a.save()
        return render(request,'viewmark.html')
    return render(request,'nsem2.html')

def usem2(request):
    sem2=csdep_sem2.objects.all()
    return render(request, 'usem2.html', locals())

def esem2(request,id):
    ac={}
    obj=get_object_or_404(csdep_sem2, pk=id)
    form = cs_sem2(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/usem2")
    ac["cc"]=form
    return render(request,"esem2.html",ac)

def dsem2(request):
    sem2=csdep_sem2.objects.all()
    return render(request, "dsem2.html", locals())
def delsem2(request,id):
    ds = {}
    obj = get_object_or_404(csdep_sem2, pk=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/dsem2")
    return render(request, "delsem2.html", ds)

def csread_y2(request):
    cssem3=csdep_sem3.objects.all()
    cssem4=csdep_sem4.objects.all()
    context = {
        'sem3': cssem3,
        'sem4':cssem4,
    }
    return render(request,'csread_y2.html', context)

def nsem3(request):
    a=csdep_sem3()
    if request.method=='POST':
        if request.POST.get('stuname') and request.POST.get('regno') and request.POST.get('stuclass') and request.POST.get('sub11') and request.POST.get('sub12') and request.POST.get('sub13') and request.POST.get('sub14') and request.POST.get('sub15') :
            a.stuname=request.POST.get('stuname')
            a.regno = request.POST.get('regno')
            a.stuclass = request.POST.get('stuclass')
            a.sub11 = request.POST.get('sub11')
            a.sub12 = request.POST.get('sub12')
            a.sub13 = request.POST.get('sub13')
            a.sub14 = request.POST.get('sub14')
            a.sub15 = request.POST.get('sub15')
            a.save()
        return render(request,'viewmark.html')
    return render(request,'nsem3.html')

def usem3(request):
    sem3=csdep_sem3.objects.all()
    return render(request,'usem3.html', locals())
def esem3(request,id):
    ac = {}
    obj = get_object_or_404(csdep_sem3, pk=id)
    form = cs_sem3(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/usem3")
    ac["cc"] = form
    return render(request, "esem3.html", ac)
def dsem3(request):
    sem3=csdep_sem3.objects.all()
    return render(request, "dsem3.html", locals())
def delsem3(request,id):
    ds = {}
    obj = get_object_or_404(csdep_sem3, pk=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/dsem3")
    return render(request, "delsem3.html", ds)

def nsem4(request):
    ab = csdep_sem4()
    if request.method == 'POST':
        if request.POST.get('stuname') and request.POST.get('regno') and request.POST.get('stuclass') and request.POST.get('sub16') and request.POST.get('sub17') and request.POST.get('sub18') and request.POST.get('sub19') and request.POST.get('sub20'):
            ab.stuname = request.POST.get('stuname')
            ab.regno = request.POST.get('regno')
            ab.stuclass = request.POST.get('stuclass')
            ab.sub16 = request.POST.get('sub16')
            ab.sub17 = request.POST.get('sub17')
            ab.sub18 = request.POST.get('sub18')
            ab.sub19 = request.POST.get('sub19')
            ab.sub20 = request.POST.get('sub20')
            ab.save()
        return render(request,'viewmark.html')
    return render(request, 'nsem4.html')
def usem4(request):
    sem4=csdep_sem4.objects.all()
    return render(request,'usem4.html', locals())
def esem4(request,id):
    ax = {}
    obj = get_object_or_404(csdep_sem4, pk=id)
    form = cs_sem4(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/usem4")
    ax["cc"] = form
    return render(request, "esem4.html", ax)
def dsem4(request):
    sem4=csdep_sem4.objects.all()
    return render(request, "dsem4.html", locals())
def delsem4(request,id):
    ds = {}
    obj = get_object_or_404(csdep_sem4, pk=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/dsem4")
    return render(request, "delsem4.html", ds)


def csread_y3(request):
    cssem5=csdep_sem5.objects.all()
    cssem6=csdep_sem6.objects.all()
    context = {
        'sem5': cssem5,
        'sem6':cssem6,
    }
    return render(request,'cs_y3/csread_y3.html', context)
def nsem5(request):
    ac=csdep_sem5()
    if request.method=='POST':
        if request.POST.get('stuname') and request.POST.get('regno') and request.POST.get('stuclass') and request.POST.get('sub21') and request.POST.get('sub22') and request.POST.get('sub23') and request.POST.get('sub24') and request.POST.get('sub25'):
            ac.stuname=request.POST.get('stuname')
            ac.regno = request.POST.get('regno')
            ac.stuclass = request.POST.get('stuclass')
            ac.sub21 = request.POST.get('sub21')
            ac.sub22 = request.POST.get('sub22')
            ac.sub23 = request.POST.get('sub23')
            ac.sub24 = request.POST.get('sub24')
            ac.sub25 = request.POST.get('sub25')
            ac.save()
        return render(request, 'viewmark.html')
    return render(request, "cs_y3/nsem5.html")
def usem5(request):
    sem5 = csdep_sem5.objects.all()
    return render(request, 'cs_y3/usem5.html', locals())
def esem5(request,id):
    aq = {}
    obj = get_object_or_404(csdep_sem5, pk=id)
    form = cs_sem5(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/usem5")
    aq["cc"] = form
    return render(request, "cs_y3/esem5.html", aq)
def dsem5(request):
    sem5=csdep_sem5.objects.all()
    return render(request, "cs_y3/dsem5.html", locals())
def delsem5(request,id):
    ds = {}
    obj = get_object_or_404(csdep_sem5, pk=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/dsem5")
    return render(request, "cs_y3/delsem5.html", ds)
def nsem6(request):
    ac=csdep_sem6()
    if request.method=='POST':
        if request.POST.get('stuname') and request.POST.get('regno') and request.POST.get('stuclass') and request.POST.get('sub26') and request.POST.get('sub27') and request.POST.get('sub28') and request.POST.get('sub29') and request.POST.get('sub30'):
            ac.stuname=request.POST.get('stuname')
            ac.regno = request.POST.get('regno')
            ac.stuclass = request.POST.get('stuclass')
            ac.sub26 = request.POST.get('sub26')
            ac.sub27 = request.POST.get('sub27')
            ac.sub28 = request.POST.get('sub28')
            ac.sub29 = request.POST.get('sub29')
            ac.sub30 = request.POST.get('sub30')
            ac.save()
        return render(request, 'viewmark.html')
    return render(request, "cs_y3/nsem6.html")
def usem6(request):
    sem6 = csdep_sem6.objects.all()
    return render(request, 'cs_y3/usem6.html', locals())
def esem6(request,id):
    aq = {}
    obj = get_object_or_404(csdep_sem6, pk=id)
    form = cs_sem6(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/usem6")
    aq["cc"] = form
    return render(request, "cs_y3/esem6.html", aq)
def dsem6(request):
    sem6=csdep_sem6.objects.all()
    return render(request, "cs_y3/dsem6.html", locals())
def delsem6(request,id):
    ds = {}
    obj = get_object_or_404(csdep_sem6, pk=id)
    if request.method == "POST":
        obj.delete()
        return redirect("/dsem6")
    return render(request, "cs_y3/delsem6.html", ds)