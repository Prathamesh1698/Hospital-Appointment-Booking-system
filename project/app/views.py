from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import Medical
from app.forms import EmpForm, ProductModelForm, UserRegister
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
import datetime


def apt(request):
    if request.user.id:
        user_id = request.user.id

        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            no = request.POST['num']
            date = request.POST['date']
            det = request.POST['department']
            doc = request.POST['doctor']

            content = {}

            if name == "":
                content['nmsg'] = 'Please enter your name  here'
            elif email == "":
                content['emsg'] = 'Please enter email.'
            elif no == "":
                content['nomsg'] = 'Please enter your mobile number'
            elif date == "":
                content['dmsg'] = 'Please enter date'
            elif det not in ('1', '2', '3', '4'):
                content['detmsg'] = 'Please select department name'
            elif doc not in ('Dhirubhai', 'Mukesh', 'Adani', 'Shah'):
                content['docmsg'] = 'Please select doctor.'

            else:
                p = Medical.objects.create(Patient_name=name, Email=email, Mobile=no,
                                           Date=date, Department_name=det, Doctor_name=doc, uid=user_id)
                p.save()
                return redirect('/index')
            return render(request, 'apt.html', content)

        else:
            return render(request, 'apt.html')
    else:
        return redirect("/login")


def index(request):
    if request.user.id:
        user_id = request.user.id
        # p = Medical.objects.all()
        p = Medical.objects.filter(uid=user_id)
        content = {}
        content['data'] = p
        return render(request, 'index.html', content)
    else:
        return redirect('/login')


def edit(request, rid):
    if request.method == "POST":
        uname = request.POST['name']
        uemail = request.POST['email']
        uno = request.POST['num']
        udate = request.POST['date']
        udet = request.POST['department']
        udoc = request.POST['doctor']

        p = Medical.objects.filter(id=rid)
        p.update(Patient_name=uname, Email=uemail, Mobile=uno,
                 Date=udate, Department_name=udet, Doctor_name=udoc)

        return redirect('/index')
    else:

        p = Medical.objects.filter(id=rid)
        content = {}
        content['data'] = p
        return render(request, 'edit.html', content)


def delete(request, rid):
    p = Medical.objects.get(id=rid)
    p.delete()
    return redirect('/index')


def docfilter(request, value):

    p = Medical.objects.filter(Doctor_name=value)
    content = {}
    content['data'] = p
    return render(request, 'index.html', content)


def footer(request):
    return render(request, 'footer.html')


def header(request):
    return render(request, 'header.html')


def base(request):
    return render(request, 'base.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def dept(request):
    return render(request, 'dept.html')


def djangoform(request):

    if request.method == 'POST':
        n = request.POST['name']
        eid = request.POST['empid']
        sal = request.POST['sal']

    else:

        fm = EmpForm()
        content = {}
        content['formdata'] = fm
        return render(request, "djangoform.html", content)


def djangomodelform(request):

    if request.method == 'POST':
        pass

    else:
        fm = ProductModelForm()
        content = {}
        content['mformdata'] = fm
        return render(request, "addproduct.html", content)


def user_register(request):

    if request.method == 'POST':
        regfmdata = UserRegister(request.POST)
        message = {}
        if regfmdata.is_valid():
            regfmdata.save()
            message['msg'] = "User registered successfully."
            message['x'] = 1
            return render(request, "register_success.html", message)

        else:
            message['msg'] = "failed to register user."
            message['x'] = 0
            return render(request, "register_success.html", message)
            # return HttpResponse("Failed to register.")

    else:

        regfm = UserRegister()
        content = {}
        content['regfmdata'] = regfm
        return render(request, 'register.html', content)


def user_login(request):
    fmlog = AuthenticationForm()
    content = {}
    content['logfmdata'] = fmlog
    if request.method == 'POST':
        logfmdata = AuthenticationForm(request=request, data=request.POST)

        if logfmdata.is_valid():
            uname = logfmdata.cleaned_data['username']
            upass = logfmdata.cleaned_data['password']
            r = authenticate(username=uname, password=upass)

            if r is not None:
                login(request, r)
                return redirect('/index')
        else:

            content['msg'] = "Invalid username or password..!!!"

            return render(request, 'login.html', content)

    else:

        return render(request, 'login.html', content)


def user_logout(request):

    logout(request)
    return redirect('/login')


def setcookie(request):

    res = render(request, 'setcookie.html')
    res.set_cookie('Name', 'Prathamesh')
    res.set_cookie('rno', 16)
    res.set_cookie('per', 85.9)
    return res


def getcookie(request):

    n = request.COOKIES['Name']
    r = request.COOKIES['rno']
    per = request.COOKIES['per']

    content = {'n': n, 'roll': r, 'per': per}
    return render(request, 'getcookie.html', content)


def setsession(request):
    request.session['uname'] = "firstuser"
    return render(request, 'setsession.html')


def getsession(request):

    d = request.session['uname']
    content = {}
    content['n'] = d
    return render(request, 'getsession.html', content)
