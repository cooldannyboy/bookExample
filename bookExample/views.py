from django.shortcuts import render_to_response
from django.http import HttpResponse

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