from django.shortcuts import HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from .task_test import test
from .models import Task, Student, Teacher, Gruop
from .test1 import route
import re


def get_man(user):
    if user.is_staff:
        return user.teacher
    else:
        return user.student


@login_required(login_url='/learn/')
def main(request):
    if request.user.is_staff:
        man = request.user.teacher
        templ = loader.get_template("main_teacher.html")
    else:
        man = request.user.student
        templ = loader.get_template("main.html")
    context = {"man": man}
    return HttpResponse(templ.render(context, request))


@login_required(login_url='/learn/')
def level(request, lvl_id=1):
    man = get_man(request.user)
    if int(lvl_id) > man.coins + 1:
        return redirect("level", man.coins + 1)
    el = Task.objects.get(pk=lvl_id)
    templ = loader.get_template("level.html")
    if int(lvl_id) > man.coins:
        will_be = man.coins+1
    else:
        will_be = man.coins
    next_lvl = str(int(lvl_id)+1)
    context = {"lvl": lvl_id, "txt": el.text.split(";"), "man": man, "wb": will_be, "next_lvl": next_lvl}
    return HttpResponse(templ.render(context, request))


@login_required(login_url='/learn/')
def get_answer(request, lvl_id=1):
    script = request.body.decode('ascii')[1:-1]
    script = re.sub("\\\\", script, "\\").replace("\\", "")
    res, err = test(script)
    res_test = route[int(lvl_id)]()
    if res_test:
        if request.user.is_staff:
            man = Teacher.objects.get(id=request.user.teacher.id)
        else:
            man = request.user.student
        if man.coins + 1 == int(lvl_id):
            man.coins += 1
        man.save()
    if res_test:
        return HttpResponse(res, status=200)
    return HttpResponse(err, status=201)


@login_required(login_url='/learn/')
def get_result(request, lvl_id=1):
    script = request.body.decode('ascii')[1:-1]
    script = re.sub("\\\\", script, "\\").replace("\\", "")
    res, err = test(script)
    if err == "":
        return HttpResponse(res, status=200)
    return HttpResponse(err, status=201)


@login_required(login_url='/learn/')
def new_group(request):
    gname = request.POST["gname"]
    gr = Gruop.objects.create(name=gname, idTeacher=request.user.teacher)
    return redirect("tables")


@login_required(login_url='/learn/')
def del_group(request):
    # gname = request.POST["valToDel"]
    print(request.POST)
    # gr = Gruop.objects.create(name=gname, idTeacher=request.user.teacher)
    return redirect("tables")


@login_required(login_url='/learn/')
def table(request):
    if request.user.is_staff:
        data = request.user.teacher.groups()
        templ = loader.get_template("groups_teacher1.html")
    else:
        data = request.user.student.groupmates()
        templ = loader.get_template("result_student.html")
    context = {"data": data}
    return HttpResponse(templ.render(context, request))


@login_required(login_url='/learn/')
def table_s(request, group_id):
    if request.user.is_staff:
        data = Gruop.objects.get(idGroup=group_id).students()
        templ = loader.get_template("result_teacher.html")
    else:
        data = request.user.student.group()
        templ = loader.get_template("result_student.html")
    context = {"data": data}
    return HttpResponse(templ.render(context, request))


@login_required(login_url='/learn/')
def settings(req):
    templ = loader.get_template("settings.html")
    context = {}
    return HttpResponse(templ.render(context, req))


def index(req):
    templ = loader.get_template("start_page.html")
    context = {}
    if req.method == "GET":
        return HttpResponse(templ.render(context, req))
    else:
        if req.POST["type"] == "login":
            user = authenticate(req, username=req.POST["uname"], password=req.POST["pass"])
            if user is not None:
                login(req, user)
                return redirect("main")
            else:
                return HttpResponse(templ.render(context, req))
        if req.POST["type"] == "signup":
            if req.POST["pass1"] == req.POST["pass2"]:
                user = User.objects.create_user(username=req.POST["uname"], password=req.POST["pass1"])
                user.is_staff = True
                user.save()
                teacher = Teacher.objects.create(user=user, coins=0)
                teacher.save()
                return redirect("main")
            else:
                return HttpResponse(templ.render(context, req))


def log_out(request):
    logout(request)
    return redirect("index")
