from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.sessions.models import Session

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
         return HttpResponse('Welcome!~'+request.GET['user_name'])

        # values = request.GET.items()
        # html = []
        # for k, v in values:
        #     html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
        # return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

    else:
        return render_to_response('welcome.html', locals())

def set_c(request):
    response = HttpResponse('Set your lucky_number as 8')
    response.set_cookie('lucky_number', 8)
    return response

def get_c(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('Your lucky number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('no cookies.')

def session_test(request):
    sid = request.COOKIES['sessionid']
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:' + sid + '<br>Expire_date:' + str(s.expire_date) + '<br>Data:' + str(s.get_decoded())

    return HttpResponse(s_info)