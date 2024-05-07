import json
from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger






# Create your views here.
from math import sin, cos, atan2, sqrt

from SAFE_DRIVE_APP.models import *

def first(request):
    return render(request,"firstindex.html")
@login_required(login_url='/')

def home(request):
    return render(request,"Admin/adminindex.html")

@login_required(login_url='/')
def adminhome(request):
    return render(request,"Admin/adminfstindex.html")

def login(request):
    return render(request,'login_page.html')

def logoutcode(request):
    auth.logout(request)
    return render(request,'login_page.html')

def logincode(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    try:

        ob = login_table.objects.get(Username=username, Password=password)
        # if ob.Username!=username or ob.Password!=password:
        if ob.Username==username and ob.Password==password:
            if ob.type == 'admin':
                obb=auth.authenticate(username="amrutha",password="amrutha")
                if obb is not None:
                    auth.login(request,obb)
                request.session['lid']=ob.id
                return HttpResponse('''<script>alert("welcome to admin home"); window.location="/adminhome"</script>''')
            else:
                return HttpResponse('''<script>alert("invalid username and password"); window.location="/login"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid username and password"); window.location="/login"</script>''')

    except Exception as e:
        print(e)
        return HttpResponse('''<script>alert("invalid username and password"); window.location="/login"</script>''')
# ........................................................................................................................

@login_required(login_url='/')
def addblind(request):
    return render(request, 'Admin/editblindspot.html')

@login_required(login_url='/')
def addblindspot(request):
    name=request.POST['textfield']
    date=datetime.today()
    ab=Blindspot_table()
    ab.Name=name
    ab.Latitude=0
    ab.Longitude=0
    ab.Date=date
    ab.save()
    request.session['mid']=ab.id
    return HttpResponse('''<script>alert("Successfully added"); window.location="/map"</script>''')
@login_required(login_url='/')
def add1(request):
    try:
        latitude=request.POST['lat']
        longitude=request.POST['lon']
        name=request.POST['name']
        date = datetime.today()
        ab=Blindspot_table()
        ab.Latitude=latitude
        ab.Name=name
        ab.Date = date
        ab.Longitude=longitude
        ab.save()
        return HttpResponse('''<script>alert("Successfully added"); window.location="/viewblind"</script>''')
    except:
        return HttpResponse('''<script>alert("Select Latitude and Longitude"); window.location="/map"</script>''')
# ..................................................................................................................................................
@login_required(login_url='/')
def map(request):
    return render(request,'Admin/map.html')

@login_required(login_url='/')
def viewblind(request):
    ob= Blindspot_table.objects.all().order_by('-id')
    # return render(request,'Admin/view blind spot.html',{'val':ob})
    print(ob,"==========")


    my_objects = Blindspot_table.objects.all().order_by('-id')

    # Number of items to display per page
    items_per_page = 5
    paginator = Paginator(my_objects, items_per_page)
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

        # Pass the Page object to the template
    return render(request, 'Admin/view blind spot.html', {'my_objects': my_objects})
    # return render(request, 'your_template.html', {'my_objects': my_objects})

@login_required(login_url='/')
def search_blind(request):
    Name=request.POST['textfield']
    ob=Blindspot_table.objects.filter(Name__istartswith=Name)
    # return render(request,'Admin/view blind spot.html',{'val':ob})

  # Number of items to display per page
    items_per_page = 5
    paginator = Paginator(ob, items_per_page)
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'Admin/view blind spot.html', {'my_objects': my_objects})



def dltblind(request,id):
    ob=Blindspot_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Place deleted"); window.location="/viewblind"</script>''')




@login_required(login_url='/')
def editblind(request,id):
    request.session['ed']=id
    ob=Blindspot_table.objects.get(id=id)
    return render(request, 'Admin/editblindspot.html', {"val":ob})
@login_required(login_url='/')
def editblindspot(request):
    name=request.POST['name']
    lat=request.POST['lat']
    lon=request.POST['lon']

    ob=Blindspot_table.objects.get(id=request.session['ed'])
    ob.Name=name
    ob.Latitude=lat
    ob.Longitude=lon

    ob.save()
    return HttpResponse('''<script>alert("Edited successfully!! "); window.location="/viewblind#about"</script>''')






#.......................................................................................................................



@login_required(login_url='/')
def addlocation(request):
    return render(request,'Admin/Add important location.html')
@login_required(login_url='/')
def addloc(request):
    name=request.POST['textfield']
    Desc=request.POST['']
    img=request.POST['img']
    fs=FileSystemStorage()
    fsave=fs.save(img.name,img)

    date=datetime.today()
    ab=imp_location_table()
    ab.Name=name
    ab.photo=fsave
    ab.Description=Desc
    ab.Latitude=0
    ab.Longitude=0
    ab.Date=date
    ab.save()
    request.session['mid']=ab.id
    return HttpResponse('''<script>alert("Successfully added"); window.location="/map1#about"</script>''')
@login_required(login_url='/')
def addlocat(request):
    latitude=request.POST['lat']
    longitude=request.POST['lon']
    name=request.POST['name']
    Desc=request.POST['name1']
    img=request.FILES['img']

    fs = FileSystemStorage()
    fsave = fs.save(img.name, img)
    date = datetime.today()
    ab=imp_location_table()
    ab.Latitude=latitude
    ab.Name=name
    ab.Description=Desc
    ab.photo=fsave
    ab.Date = date
    ab.Longitude=longitude
    ab.save()
    return HttpResponse('''<script>alert("Successfully added"); window.location="/viewlocation#about"</script>''')

@login_required(login_url='/')
def map1(request):
    return render(request,'Admin/map2.html')



@login_required(login_url='/')
def viewlocation(request):
    ob = imp_location_table.objects.all().order_by('-id')
    # return render(request,'Admin/View imporatnt location.html',{'val':ob})
    print(ob,"=================")

    my_objects=imp_location_table.objects.all().order_by('-id')

    items_per_page = 5
    paginator = Paginator(my_objects, items_per_page)
    page = request.GET.get('page')
    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)
    return render(request,'Admin/View imporatnt location.html',{'my_objects':my_objects})



@login_required(login_url='/')
def search_loc(request):
    t3=request.POST['textfield']
    ob=imp_location_table.objects.filter(Q(Name__istartswith=t3)|Q(Description__istartswith=t3))
    # return render(request,'Admin/View imporatnt location.html',{'val':ob})

    items_per_page = 5
    paginator = Paginator(ob, items_per_page)
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'Admin/View imporatnt location.html', {'my_objects': my_objects})


@login_required(login_url='/')
def dltloc(request,id):
    ob=imp_location_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Place deleted"); window.location="/viewlocation#about"</script>''')



@login_required(login_url='/')
def editlocation(request,id):
    request.session['ed']=id
    ob=imp_location_table.objects.get(id=id)
    return render(request,'Admin/editlocation.html',{"val":ob})


@login_required(login_url='/')
def editlocpost(request):
    name=request.POST['name']
    lat=request.POST['lat']
    lon=request.POST['lon']
    desc=request.POST['name1']
    img = request.FILES['img']

    if 'img' in request.FILES:
        fs = FileSystemStorage()
        fsave = fs.save(img.name, img)




        ob=imp_location_table.objects.get(id=request.session['ed'])
        ob.photo=fsave
        ob.Name=name
        ob.Latitude = lat
        ob.Longitude= lon
        ob.Description=desc

        ob.save()
    else:
        ob = imp_location_table.objects.get(id=request.session['ed'])

        ob.Name = name
        ob.Latitude = lat
        ob.Longitude = lon
        ob.Description = desc

        ob.save()

    return HttpResponse('''<script>alert("Edited successfully!! "); window.location="/viewlocation#about"</script>''')












# ......................................................................................................................




#
# def viewuser (request):
#     ob = user_table.objects.all().order_by('-id')
#     print(ob,"=================")
#     # return render(request, 'Admin/View user.html',{'val': ob})
#
#     my_objects=user_table.objects.all().order_by('-id')
#
#     items_per_page = 5
#     paginator = Paginator(my_objects, items_per_page)
#     page = request.GET.get('page')
#     try:
#         # Get the Page object for the requested page
#         my_objects = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver the first page
#         my_objects = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g., 9999), deliver the last page
#         my_objects = paginator.page(paginator.num_pages)
#     return render(request,'Admin/View user.html',{'my_objects':my_objects})

"...................................................................................."



@login_required(login_url='/')
def viewuser(request):
    my_objects = user_table.objects.all().order_by('-id')

    for obj in my_objects:
        # Calculate age based on date of birth
        obj.age = calculate_age(obj.Dob)

    items_per_page = 5
    paginator = Paginator(my_objects, items_per_page)
    page = request.GET.get('page')

    try:
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        my_objects = paginator.page(1)
    except EmptyPage:
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'Admin/View user.html', {'my_objects': my_objects})


def calculate_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))









@login_required(login_url='/')
def search_user(request):
    t1=request.POST['textfield']
    # place=request.POST['textfield2']
    ob=user_table.objects.filter(Q(Firstname__istartswith=t1)| Q(Place__istartswith=t1))
    # return render(request,'Admin/View user.html',{'val':ob})

    items_per_page = 5
    paginator = Paginator(ob, items_per_page)
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'Admin/View user.html', {'my_objects': my_objects})









# .............................................................................................................................................
def viewambulance (request):
    ob= ambulance_table.objects.all().order_by('-id')
    # return render(request,'Admin/view and verify ambulance.html',{'val':ob})
    print(ob, "=================")
    # return render(request, 'Admin/View user.html',{'val': ob})

    my_objects = ambulance_table.objects.all().order_by('-id')

    for obj in my_objects:
        # Calculate age based on date of birth
        obj.age = calculate_age(obj.Dob)

    items_per_page = 5
    paginator = Paginator(my_objects, items_per_page)
    page = request.GET.get('page')
    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)
    return render(request, 'Admin/view and verify ambulance.html', {'my_objects': my_objects})




def calculates_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))




@login_required(login_url='/')
def search_ambulance(request):
    t2=request.POST['textfield']
    ob=ambulance_table.objects.filter(Q(Firstname__istartswith=t2)|Q(Place__istartswith=t2))
    # return render(request,'Admin/view and verify ambulance.html',{'val':ob})

    items_per_page = 5
    paginator = Paginator(ob, items_per_page)
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'Admin/view and verify ambulance.html', {'my_objects': my_objects})

@login_required(login_url='/')
def verifyambulance (request):
    return render(request,'Admin/View user.html')

@login_required(login_url='/')
def admin_accept_ambulace(request,id):
    ob=login_table.objects.filter(id=id).update(type="ambulance")
    return HttpResponse('''<script>alert("accepted"); window.location="/viewambulance#about"</script>''')


@login_required(login_url='/')
def reject_ambulance(request,id):
    ob=login_table.objects.filter(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Rejected"); window.location="/viewambulance#about"</script>''')

# ............................................................................................................................

def viewtraffic(request):
    ob=location_table.objects.all()
    loc=[]
    for i in ob:
        data={"lat":i.Latitude,"long":i.Longitude,"uname":i.USER_ID.Firstname}
        loc.append(data)

    return render(request,'Admin/trafficinfo.html',{'p':loc})
@login_required(login_url='/')
def viewpothole (request):
    ob = pothole_table.objects.all().order_by('-id')
    # return render(request,'Admin/view and verify ambulance.html',{'val':ob})

    items_per_page = 5
    paginator = Paginator(ob, items_per_page)
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'Admin/View pothole information.html', {'my_objects': my_objects})




@login_required(login_url='/')
def dlt_poth(request,id):
    ob=pothole_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Place deleted"); window.location="/viewpothole"</script>''')





@login_required(login_url='/')
def searchpoth(request):
    date=request.POST['textfield']
    ob = pothole_table.objects.filter(Date=date).order_by('-id')
    items_per_page = 5
    paginator = Paginator(ob, items_per_page)
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'Admin/View pothole information.html', {'my_objects': my_objects})



@login_required(login_url='/')
def viewaccident(request):
    ob=accident_table.objects.all().order_by('-id')
    items_per_page = 5
    paginator = Paginator(ob, items_per_page)
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)
    return render(request,'Admin/View accident information.html',{'my_objects':my_objects})




@login_required(login_url='/')
def search_acci(request):
    try:
        date=request.POST['textfield']
        request.session['d']=date
        ob = accident_table.objects.filter(Date=date).order_by('-id')
        items_per_page = 5
        paginator = Paginator(ob, items_per_page)
        page = request.GET.get('page')

        try:
            # Get the Page object for the requested page
            my_objects = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            my_objects = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver the last page
            my_objects = paginator.page(paginator.num_pages)
        return render(request, 'Admin/View accident information.html',{'my_objects': my_objects})

    except:
        date = request.session['d']

        ob = accident_table.objects.filter(Date=date).order_by('-id')
        items_per_page = 5
        paginator = Paginator(ob, items_per_page)
        page = request.GET.get('page')

        try:
            # Get the Page object for the requested page
            my_objects = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            my_objects = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver the last page
            my_objects = paginator.page(paginator.num_pages)
        return render(request, 'Admin/View accident information.html', {'my_objects': my_objects})


@login_required(login_url='/')
def viewfeed (request):
    ob = Feedback_table.objects.all().order_by('-id')
    items_per_page = 5
    paginator = Paginator(ob, items_per_page)
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'Admin/View feedback.html', {'my_objects': my_objects})




@login_required(login_url='/')
def searchfeed(request):
    date=request.POST['textfield']
    ob = Feedback_table.objects.filter(Date=date).order_by('-id')
    items_per_page = 5
    paginator = Paginator(ob, items_per_page)
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'Admin/View feedback.html', {'my_objects': my_objects})




@login_required(login_url='/')
def viewcomp (request):
    ob = Complaint_table.objects.all().order_by('-id')
    items_per_page = 5
    paginator = Paginator(ob, items_per_page)
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'Admin/view complaint.html', {'my_objects': my_objects})

@login_required(login_url='/')
def search_comp(request):
    date=request.POST['textfield']
    ob = Complaint_table.objects.filter(Date=date).order_by('-id')
    items_per_page = 5
    paginator = Paginator(ob, items_per_page)
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)
    return render(request, 'Admin/view complaint.html',{'my_objects': my_objects})


@login_required(login_url='/')
def sendreply (request,id):
    request.session['cid']=id
    return render(request,'Admin/send reply.html')

@login_required(login_url='/')
def sendcompreply(request):
    reply=request.POST['textarea']
    ob=Complaint_table.objects.get(id=request.session['cid'])
    ob.Reply=reply
    ob.save()
    return HttpResponse('''<script>; window.location="/viewcomp#about"</script>''')










"=============================================android================================================================================================================"
def login_code(request):
    print(request.POST)
    un = request.POST['uname']
    pw = request.POST['pswrd']
    try:
        users = login_table.objects.get(Username= un,Password= pw)
        if users.Username == un and users.Password == pw:
            if users is None:
                data = {"task" : "invalid"}
            else:
                data = {"task" : "valid","id":users.id,'type':users.type}
            l = json.dumps(data)
            print(l)
            return HttpResponse(l)
        else:
            data = {"task": "invalid"}
    except:
        data = {"task": "invalid"}
    l = json.dumps(data)
    return HttpResponse(l)
def checkun(request):
    print(request.POST)
    un = request.POST['uname']

    try:
        users = login_table.objects.filter( Username= un)

        if len(users)==0:
            data = {"task" : "invalid"}
        else:
            data = {"task" : "valid"}
        l = json.dumps(data)
        print(l)
        return HttpResponse(l)

    except Exception as e:
        print(e)
        data = {"task": "invalid"}
    l = json.dumps(data)
    return HttpResponse(l)



def addaccident(request):
    try:
        latitude=request.POST['lati']
        longitude=request.POST['longi']
        lid=request.POST['lid']

        ob=accident_table()
        ob.Latitude=latitude
        ob.Longitude=longitude
        ob.Date=datetime.today()
        ob.Time=datetime.today()
        ob.Status="pending"
        ob.USER_ID=user_table.objects.get(LOGIN=lid)
        ob.save()
        data = {"task": "valid"}
        l = json.dumps(data)
        print(l)
    except:
        ob.save()
        data = {"task": "invalid"}
        l = json.dumps(data)
        print(l)


    return HttpResponse(l)



# def accident_notify(request):
#     print(request.POST,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
#     lati = float(request.POST["lati"])
#     longi = float(request.POST["longi"])
#     lid = request.POST["lid"]
#
#     obb = accident_table.objects.filter(~Q(USER_ID__LOGIN=lid))
#
#     print(obb)
#
#     for i in obb:
#         lat2 = float(i.Latitude)
#         lon2 = float(i.Longitude)
#         # Approximate radius of earth in km
#         R = 6373.0
#
#         # lat1 = radians(lat1)
#         # lon1 = radians(lon1)
#         # lat2 = radians(lat2)
#         # lon2 = radians(lon2)
#
#         dlon = float(lon2) - float(longi)
#         dlat = float(lat2) - float(lati)
#
#         a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
#         print(a)
#         try:
#             c = 2 * atan2(sqrt(a), sqrt(1 - a))
#         except:
#             c = 2 * atan2(sqrt(a), sqrt(a - 1))
#
#         distance = R * c
#         print(distance, "jjjjjjjjjjjjjjjjjjjjj")
#
#         if distance < 1000:
#             obu = location_table.objects.exclude(USER_ID__LOGIN__id=lid)
#             r = []
#             for j in obu:
#                 lat2 = float(j.Latitude)
#                 lon2 = float(j.Longitude)
#                 # Approximate radius of earth in km
#                 R = 6373.0
#
#                 # lat1 = radians(lat1)
#                 # lon1 = radians(lon1)
#                 # lat2 = radians(lat2)
#                 # lon2 = radians(lon2)
#
#                 dlon = float(lon2) - float(longi)
#                 dlat = float(lat2) - float(lati)
#
#                 a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
#                 print(a)
#                 try:
#                     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#                 except:
#                     c = 2 * atan2(sqrt(a), sqrt(a - 1))
#
#                 distance = R * c
#                 print(distance, "jjjjjjjjjjjjjjjjjjjjj")
#                 if distance < 1000:
#                     data = {"task": "accident"}
#                     r = json.dumps(data)
#                     print(r)
#                     return HttpResponse(r)
#             data = {"task": "accident"}
#             r = json.dumps(data)
#             print(r)
#             return HttpResponse(r)
#
#     data = {"task": "valid"}
#     l = json.dumps(data)
#     return HttpResponse(l)


def updatelocation(request):
    print(request.POST,"yyyyyyyyyyyyyyyyyyyyyyy")
    lati=float(request.POST['lati'])
    longi=float(request.POST['longi'])
    lid=request.POST['lid']

    ob=accident_table.objects.filter(USER_ID__LOGIN__id=lid,Date=datetime.today())
    for i in ob:
        try:
            lat2 = float(i.Latitude)
            lon2 = float(i.Longitude)
            # Approximate radius of earth in km
            R = 6373.0

            # lat1 = radians(lat1)
            # lon1 = radians(lon1)
            # lat2 = radians(lat2)
            # lon2 = radians(lon2)

            dlon = float(lon2) - float(longi)
            dlat = float(lat2) - float(lati)

            a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
            print(a)
            try:
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
            except:
                c = 2 * atan2(sqrt(a), sqrt(a - 1))

            distance = R * c
            print(distance, "jjjjjjjjjjjjjjjjjjjjj")
            if distance>40:
                i.delete()
        except:
            pass


    ob=location_table.objects.filter(USER_ID__LOGIN__id=lid)
    if len(ob)>0:
        ob = location_table.objects.get(USER_ID__LOGIN__id=lid)
        ob.Latitude=lati
        ob.Longitude=longi
        ob.USER_ID=user_table.objects.get(LOGIN__id=lid)
        ob.save()
    else:
        ob = location_table()
        ob.Latitude = lati
        ob.Longitude = longi
        ob.USER_ID = user_table.objects.get(LOGIN__id=lid)
        ob.save()

    obb = Blindspot_table.objects.all()

    print(obb)

    for i in obb:
        lat2 = float(i.Latitude)
        lon2 = float(i.Longitude)
        # Approximate radius of earth in km
        R = 6373.0

        # lat1 = radians(lat1)
        # lon1 = radians(lon1)
        # lat2 = radians(lat2)
        # lon2 = radians(lon2)

        dlon = float(lon2) - float(longi)
        dlat = float(lat2) - float(lati)

        a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
        print(a)
        try:
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
        except:
            c = 2 * atan2(sqrt(a), sqrt(a - 1))

        distance = R * c
        print(distance,"jjjjjjjjjjjjjjjjjjjjj")

        if distance < 1000:
            obu=location_table.objects.exclude(USER_ID__LOGIN__id=lid)
            r=[]
            for j in obu:
                lat2 = float(j.Latitude)
                lon2 = float(j.Longitude)
                # Approximate radius of earth in km
                R = 6373.0
                # lat1 = radians(lat1)
                # lon1 = radians(lon1)
                # lat2 = radians(lat2)
                # lon2 = radians(lon2)
                dlon = float(lon2) - float(longi)
                dlat = float(lat2) - float(lati)
                a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
                print(a)
                try:
                    c = 2 * atan2(sqrt(a), sqrt(1 - a))
                except:
                    c = 2 * atan2(sqrt(a), sqrt(a - 1))
                distance = R * c
                print(distance, "jjjjjjjjjjjjjjjjjjjjj")
                if distance < 1000:
                    data = {"task": "alert1"}
                    r = json.dumps(data)
                    print(r)
                    return HttpResponse(r)
            data = {"task": "alert"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
    data = {"task": "valid"}
    l = json.dumps(data)
    return HttpResponse(l)

def patholenottification(request):

    print("***********************************************",request.POST)
    lati=float(request.POST["lati"])
    longi=float(request.POST["longi"])
    lid=request.POST["lid"]

    obb = pothole_table.objects.all()

    print(obb,"Pothhole")
    pothnot=""
    accident=""

    for i in obb:
        lat2 = float(i.Latitude)
        lon2 = float(i.Longitude)
        # Approximate radius of earth in km
        R = 6373.0

        # lat1 = radians(lat1)
        # lon1 = radians(lon1)
        # lat2 = radians(lat2)
        # lon2 = radians(lon2)

        dlon = float(lon2) - float(longi)
        dlat = float(lat2) - float(lati)

        a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
        print(a)
        try:
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
        except:
            c = 2 * atan2(sqrt(a), sqrt(a - 1))

        distance = R * c
        print(distance, "jjjjjjjjjjjjjjjjjjjjj-poth")

        if distance < 1000:
            # obu = location_table.objects.exclude(USER_ID__LOGIN__id=lid)
            # r = []
            # for j in obu:
            #     lat2 = float(j.Latitude)
            #     lon2 = float(j.Longitude)
            #     # Approximate radius of earth in km
            #     R = 6373.0
            #
            #     # lat1 = radians(lat1)
            #     # lon1 = radians(lon1)
            #     # lat2 = radians(lat2)
            #     # lon2 = radians(lon2)
            #
            #     dlon = float(lon2) - float(longi)
            #     dlat = float(lat2) - float(lati)
            #
            #     a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
            #     print(a)
            #     try:
            #         c = 2 * atan2(sqrt(a), sqrt(1 - a))
            #     except:
            #         c = 2 * atan2(sqrt(a), sqrt(a - 1))
            #
            #     distance = R * c
            #     print(distance, "jjjjjjjjjjjjjjjjjjjjj--poth")
            #     # if distance < 1000:
                pothnot="alert33"
                    # data = {"task": "alert"}
                    # r = json.dumps(data)
                    # print(r)
                    # return HttpResponse(r)
    # print(request.POST, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    lati = float(request.POST["lati"])
    longi = float(request.POST["longi"])
    lid = request.POST["lid"]
    obb3 = accident_table.objects.filter(~Q(USER_ID__LOGIN=lid),Status="pending")
    print(obb3)

    for i in obb3:
        lat2 = float(i.Latitude)
        lon2 = float(i.Longitude)
        # Approximate radius of earth in km
        R = 6373.0
        # lat1 = radians(lat1)
        # lon1 = radians(lon1)
        # lat2 = radians(lat2)
        # lon2 = radians(lon2)

        dlon = float(lon2) - float(longi)
        dlat = float(lat2) - float(lati)

        a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
        print(a)
        try:
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
        except:
            c = 2 * atan2(sqrt(a), sqrt(a - 1))

        distance = R * c
        print(distance, "jjjjjjjjjjjjjjjjjjjjj")

        if distance < 1000:
            # obu = location_table.objects.exclude(USER_ID__LOGIN__id=lid)
            # r = []
            # for j in obu:
            #     lat2 = float(j.Latitude)
            #     lon2 = float(j.Longitude)
            #     # Approximate radius of earth in km
            #     R = 6373.0
            #
            #     # lat1 = radians(lat1)
            #     # lon1 = radians(lon1)
            #     # lat2 = radians(lat2)
            #     # lon2 = radians(lon2)
            #
            #     dlon = float(lon2) - float(longi)
            #     dlat = float(lat2) - float(lati)
            #
            #     a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
            #     print(a)
            #     try:
            #         c = 2 * atan2(sqrt(a), sqrt(1 - a))
            #     except:
            #         c = 2 * atan2(sqrt(a), sqrt(a - 1))
            #
            #     distance = R * c
            #     print(distance, "jjjjjjjjjjjjjjjjjjjjj")
            #     if distance < 1000:
            #         accident="alert"
            #         # data = {"task": "accident"}
            #         # r = json.dumps(data)
            #         # print(r)
            #         # return HttpResponse(r)
            accident = "alert2"
            # data = {"task": "accident"}
            # r = json.dumps(data)
            # print(r)
            # return HttpResponse(r)

    data = {"task":pothnot,"task3":accident}
    l = json.dumps(data)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!",data)
    return HttpResponse(l)


def registration(request):
  try:
    fname = request.POST['fname']
    lname = request.POST['lname']
    gender = request.POST['gender']
    dob = request.POST['dob']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    phone = request.POST['phone']
    photo=request.FILES['file']
    ff=FileSystemStorage()
    fsave=ff.save(photo.name,photo)
    email= request.POST['email']
    username= request.POST['username']
    password=request.POST['password']
    ob=login_table()
    ob.Username=username
    ob.Password=password
    ob.type='user'
    ob.save()
    ob1=user_table()
    ob1.Firstname=fname
    ob1.Lastname=lname
    ob1.Gender=gender
    ob1.Place = place
    ob1.Post=post
    ob1.Pin=pin
    ob1.Dob=dob
    ob1.Phone=phone
    ob1.Email=email
    ob1.Photo=fsave
    ob1.LOGIN=ob
    ob1.save()
    data = {"task": "valid"}
    l = json.dumps(data)
    print(l)
    return HttpResponse(l)
  except:
      data = {"task": "Duplicate Entry"}
      l = json.dumps(data)
      print(l)
      return HttpResponse(l)

def registration2(request):
  try:
    fname = request.POST['fname']
    lname = request.POST['lname']
    gender = request.POST['gender']
    dob = request.POST['dob']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    phone = request.POST['phone']
    model=request.POST['model']
    type=request.POST['type']
    v_no=request.POST['vehicle_no']
    owner=request.FILES['file3']
    ff3 = FileSystemStorage()
    ffsave = ff3.save(owner.name,owner)
    photo=request.FILES['file1']
    ff=FileSystemStorage()
    fsave=ff.save(photo.name,photo)
    id= request.FILES['file2']
    ff1 = FileSystemStorage()
    fsavee = ff1.save(id.name, id)
    email= request.POST['email']
    username= request.POST['username']
    password=request.POST['password']
    ob=login_table()
    ob.Username=username
    ob.Password=password
    ob.type='pending'
    ob.save()
    ob1=ambulance_table()
    ob1.Firstname=fname
    ob1.Lastname=lname
    ob1.Gender=gender
    ob1.Place = place
    ob1.Post=post
    ob1.Pin=pin
    ob1.Dob=dob
    ob1.Phone=phone
    ob1.Email=email
    ob1.Type=type
    ob1.make_model=model
    ob1.vehicle_no=v_no
    ob1.ownership=ffsave
    ob1.Photo=fsave
    ob1.Id_proof=fsavee
    ob1.LOGIN=ob
    ob1.save()
    data = {"task": "valid"}
    l = json.dumps(data)
    print(l)
    return HttpResponse(l)
  except Exception as e:
      print(e)
      data = {"task": "Duplicate Entry"}
      l = json.dumps(data)
      print(l)
      return HttpResponse(l)

def logout(request):
    print(request.POST)
    lid=request.POST['lid']
    try:
        ob=location_table.objects.get(USER_ID__LOGIN=lid)
        ob.delete()
    except:
        pass
    data = {"task": "valid"}
    l = json.dumps(data)
    print(l)
    return HttpResponse(l)

def view_profile(request):
    lid=request.POST['lid']
    data=[]
    ob=user_table.objects.filter(LOGIN__id=lid)
    for i in ob:
        row={'fname':i.Firstname,'lname':i.Lastname,'phone':i.Phone,'place':i.Place,'post':i.Post,'pin':i.Pin,'dob':str(i.Dob),'email':i.Email,'photo':str(i.Photo.url),'gender':i.Gender}
        data.append(row)
    print(data,"==================")
    return JsonResponse(data,safe=False)

def update_prof(request):
    try:
        if "file" in request.FILES:
            fname = request.POST['fname']
            lname = request.POST['lname']
            gender = request.POST['gender']
            dob = request.POST['dob']
            place = request.POST['place']
            post = request.POST['post']
            pin = request.POST['pin']
            phone = request.POST['phone']
            photo = request.FILES['file']
            ff = FileSystemStorage()
            fsave = ff.save(photo.name, photo)
            email = request.POST['email']
            lid=request.POST['lid']
            ob1 = user_table.objects.get(LOGIN__id=lid)
            ob1.Firstname = fname
            ob1.Lastname = lname
            ob1.Gender = gender
            ob1.Place = place
            ob1.Post = post
            ob1.Pin = pin
            ob1.Dob = dob
            ob1.Phone = phone
            ob1.Email = email
            ob1.Photo = fsave

            ob1.save()
            data = {"task": "valid"}
            l = json.dumps(data)
            print(l)
            return HttpResponse(l)
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            gender = request.POST['gender']
            dob = request.POST['dob']
            place = request.POST['place']
            post = request.POST['post']
            pin = request.POST['pin']
            phone = request.POST['phone']
            email = request.POST['email']
            lid = request.POST['lid']
            ob1 = user_table.objects.get(LOGIN__id=lid)
            ob1.Firstname = fname
            ob1.Lastname = lname
            ob1.Gender = gender
            ob1.Place = place
            ob1.Post = post
            ob1.Pin = pin
            ob1.Dob = dob
            ob1.Phone = phone
            ob1.Email = email
            ob1.save()
            data = {"task": "valid"}
            l = json.dumps(data)
            print(l)
            return HttpResponse(l)
    except Exception as e:
        print(e)
        data = {"task": "Duplicate Entry"}
        l = json.dumps(data)
        print(l)
        return HttpResponse(l)


def view_profile_ambulance(request):
    lid = request.POST['lid']
    data = []
    ob = ambulance_table.objects.filter(LOGIN__id=lid)
    for i in ob:
        row = {'fnamee': i.Firstname, 'lnamee': i.Lastname, 'phonee': i.Phone, 'placee': i.Place, 'postt': i.Post,'pinn': i.Pin, 'dobb': str(i.Dob), 'emaill': i.Email, 'photoo': str(i.Photo.url), 'genderr': i.Gender}
        data.append(row)
    print(data, "==================")
    return JsonResponse(data, safe=False)








def update_prof_ambulance(request):
    try:
        if "file" in request.FILES:
            fname = request.POST['fnamee']
            lname = request.POST['lnamee']
            gender = request.POST['genderr']
            dob = request.POST['dobb']
            place = request.POST['placee']
            post = request.POST['postt']
            pin = request.POST['pinn']
            phone = request.POST['phonee']
            photo = request.FILES['file']
            ff = FileSystemStorage()
            fsave = ff.save(photo.name, photo)
            email = request.POST['emaill']
            lid = request.POST['lid']

            ob1 = ambulance_table.objects.get(LOGIN__id=lid)
            ob1.Firstname = fname
            ob1.Lastname = lname
            ob1.Gender = gender
            ob1.Place = place
            ob1.Post = post
            ob1.Pin = pin
            ob1.Dob = dob
            ob1.Phone = phone
            ob1.Email = email
            ob1.Photo = fsave

            ob1.save()
            data = {"task": "valid"}
            l = json.dumps(data)
            print(l)
            return HttpResponse(l)
        else:
            fname = request.POST['fnamee']
            lname = request.POST['lnamee']
            gender = request.POST['genderr']
            dob = request.POST['dobb']
            place = request.POST['placee']
            post = request.POST['postt']
            pin = request.POST['pinn']
            phone = request.POST['phonee']
            email = request.POST['emaill']
            lid = request.POST['lid']
            ob1 = ambulance_table.objects.get(LOGIN__id=lid)
            ob1.Firstname = fname
            ob1.Lastname = lname
            ob1.Gender = gender
            ob1.Place = place
            ob1.Post = post
            ob1.Pin = pin
            ob1.Dob = dob
            ob1.Phone = phone
            ob1.Email = email
            ob1.save()
            data = {"task": "valid"}
            l = json.dumps(data)
            print(l)
            return HttpResponse(l)
    except Exception as e:
        print(e,"Errrrr")
        data = {"task": "Duplicate Entry"}
        l = json.dumps(data)
        print(l)
        return HttpResponse(l)


def pothole_noti_insertion(request):

    latitude=request.POST['lati']
    longitude=request.POST['longi']
    date=datetime.now()
    time=datetime.now()
    lid=request.POST['lid']

    ob=pothole_table()
    ob.Latitude=latitude
    ob.Longitude=longitude
    ob.Date=date
    ob.Time=time
    ob.USER_ID=user_table.objects.get(LOGIN=lid)
    ob.save()
    data = {"task": "valid"}
    l = json.dumps(data)
    print(l)
    return JsonResponse(data, safe=False)




def sendcomp(request):

    comp=request.POST['comp']

    lid=request.POST['lid']

    ob=Complaint_table()
    ob.USER_ID=user_table.objects.get(LOGIN__id=lid)
    ob.complaint=comp
    ob.Reply="pending"
    ob.Date=datetime.today()


    ob.save()
    data = {"task": "valid"}
    l = json.dumps(data)
    print(l)
    return JsonResponse(data, safe=False)


def user_view_comp(request):
    lid = request.POST['lid']
    data = []
    ob = Complaint_table.objects.filter(USER_ID__LOGIN__id=lid)
    for i in ob:
        row = {'comp':i.complaint,"reply":i.Reply,"date":i.Date,"id":i.id}
        data.append(row)
    print(data, "==================")
    return JsonResponse(data, safe=False)



def sview_location(request):
    pname=request.POST['pname']
    data=[]
    ob=imp_location_table.objects.filter(Name__istartswith=pname).order_by('-id')
    for i in ob:
        print(i.photo.url)
        row={'name':i.Name,'desc':i.Description,'date':str(i.Date),'latitude':i.Latitude,'longitude':i.Longitude,'photo':str(i.photo.url),'lid':i.id}
        data.append(row)
    print(data,"==================")
    return JsonResponse(data,safe=False)




def view_location(request):
    # lid=request.POST['lid']
    data=[]
    ob=imp_location_table.objects.all().order_by('-id')
    for i in ob:
        print(i.photo.url)
        row={'name':i.Name,'desc':i.Description,'date':str(i.Date),'latitude':i.Latitude,'longitude':i.Longitude,'photo':str(i.photo.url),'lid':i.id}
        data.append(row)
    print(data,"==================")
    return JsonResponse(data,safe=False)




def view_alert(request):
    # lid=request.POST['lid']
    data=[]
    # ob=accident_table.objects.all().order_by('-id')
    # for i in ob:
    #
    #     row={'name':i.USER_ID.Firstname,'date':str(i.Date),'time':str(i.Time),'latitude':i.Latitude,'longitude':i.Longitude,'image':str(i.USER_ID.Photo.url),'aid':i.id}
    #     data.append(row)
    # print(data,"==================")


    lati = float(request.POST["lat"])
    longi = float(request.POST["lon"])

    obb3 = accident_table.objects.filter(Status="pending").order_by('-id')
    # obb3 = accident_table.objects.all().order_by('-id')
    print(obb3)

    for i in obb3:
        lat2 = float(i.Latitude)
        lon2 = float(i.Longitude)
        # Approximate radius of earth in km
        R = 6373.0
        # lat1 = radians(lat1)
        # lon1 = radians(lon1)
        # lat2 = radians(lat2)
        # lon2 = radians(lon2)

        dlon = float(lon2) - float(longi)
        dlat = float(lat2) - float(lati)

        a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
        print(a)
        try:
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
        except:
            c = 2 * atan2(sqrt(a), sqrt(a - 1))

        distance = R * c
        print(distance, "jjjjjjjjjjjjjjjjjjjjj")

        if distance < 1000:

            row = {'name': i.USER_ID.Firstname, 'date': str(i.Date), 'time': str(i.Time), 'latitude': i.Latitude,
                   'longitude': i.Longitude, 'image': str(i.USER_ID.Photo.url), 'aid': i.id,"status":i.Status}
            data.append(row)

    return JsonResponse(data,safe=False)



def update_status(request):
    aid = request.POST['aid']
    lid=request.POST["lid"]
    accident_table.objects.filter(id=aid).update(Status='updated',AMBULANCE=ambulance_table.objects.get(LOGIN=lid))
    data = {"task": "valid"}
    l = json.dumps(data)
    print(l)
    return JsonResponse(data, safe=False)













def send_feed(request):

    feedback=request.POST['feed']

    lid=request.POST['lid']

    ob=Feedback_table()
    ob.USER_ID=user_table.objects.get(LOGIN__id=lid)
    ob.Feedback=feedback

    ob.Date=datetime.today()


    ob.save()
    data = {"task": "valid"}
    l = json.dumps(data)
    print(l)
    return JsonResponse(data, safe=False)


# ................................................................................................

def delete_alert(request):


    aid=request.POST['pid']

    ob=pothole_table.objects.get(id=aid)

    ob.delete()
    data = {"task": "valid"}
    l = json.dumps(data)
    print(l)
    return JsonResponse(data, safe=False)


def view_potholealert(request):
    lid = request.POST['lid']
    data = []
    ob =pothole_table.objects.filter(USER_ID__LOGIN__id=lid)
    for i in ob:
        row = {'date': i.Date, 'time': i.Time, 'latitude': i.Latitude, 'longitude': i.Longitude,'pid':i.id}
        data.append(row)
    print(data, "==================")
    return JsonResponse(data, safe=False)




def delete_alert2(request):


    mid=request.POST['aaid']

    ob=accident_table.objects.get(id=mid)

    ob.delete()
    data = {"task": "valid"}
    l = json.dumps(data)
    print(l)
    return JsonResponse(data, safe=False)


def view_myalert(request):
    lid = request.POST['lid']
    data = []
    ob =accident_table.objects.filter(USER_ID__LOGIN__id=lid)
    for i in ob:
        row = {'date': i.Date, 'time': i.Time, 'latitude': i.Latitude, 'longitude': i.Longitude,'aaid':i.id}
        data.append(row)
    print(data, "==================")
    return JsonResponse(data, safe=False)






# ......................................................................................................................................


def view_updated_accident(request):

        lid=request.POST['lid']
        data = []


        obb3 = accident_table.objects.filter(Status="updated",AMBULANCE__LOGIN=lid).order_by('-id')

        for i in obb3:
             row = {'name': i.USER_ID.Firstname, 'date': str(i.Date), 'time': str(i.Time), 'latitude': i.Latitude,'longitude': i.Longitude, 'image': str(i.USER_ID.Photo.url), 'aid': i.id, "status": i.Status}
             data.append(row)

        return JsonResponse(data, safe=False)









