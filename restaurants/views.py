# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from restaurants.models import Restaurant, Comment
from django.utils import timezone
import datetime
from django.template import RequestContext
from restaurants.forms import CommentForm

def menu(request):
    # path = request.path
    # food1 = {'name': '番茄炒蛋', 'price': 60, 'comment': '好吃', 'is_spicy': False}
    # food2 = {'name': '蒜泥白肉', 'price': 100, 'comment': '人氣推薦', 'is_spicy': True}
    #
    # foods = [food1, food2]
    #
    # return render_to_response('menu.html', locals())
    # = Restaurant.objects.get(id=1)
    #restaurants = Restaurant.objects.all()


    if 'id' in request.GET and request.GET['id'] != '':
        restaurant = Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('menu.html', locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")

def meta(request):
    values = request.META.items()
    values = sorted(values)
    # values.sort()
    # k, v = ('USERDOMAIN', request.META['USERDOMAIN'])
    # html = []
    # html.append('<tr><td>{aaa}</td><td>{bbb}</td></tr>'.format(v, v))



    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

def restaurants_list(request):
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html', locals())

def comment(request, id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurant_list/")

    errors = []
    if request.POST:

        f = CommentForm(request.POST)
        if f.is_valid():
            visitor = f.cleaned_data['visitor']
            content = f.cleaned_data['content']
            email = f.cleaned_data['email']
            date_time = datetime.datetime.now()
            Comment.objects.create(
                visitor=visitor,
                email=email,
                content=content,
                date_time=date_time,
                restaurant=r
            )
            f = CommentForm(initial={'content':'no comment'})

    else:
        f = CommentForm()

        # visitor = request.POST['visitor']
        # content = request.POST['content']
        # email = request.POST['email']
        # date_time = timezone.localtime(timezone.now())
        #
        # if any(not request.POST[k] for k in request.POST):
        #     errors.append('* 有空白欄位，請不要留空')
        # if '@' not in email:
        #     errors.append('* email 格式不正確')
        # if not errors:
        #     Comment.objects.create(
        #         visitor=visitor,
        #         email=email,
        #         content=content,
        #         date_time=date_time,
        #         restaurant=r
        #     )
        #     visitor, email, content = ('', '', '')
    #
    # f = CommentForm()


    return render_to_response('comments.html', RequestContext(request, locals()))