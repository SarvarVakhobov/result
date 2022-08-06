from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def home(request):

    ctx = {}
    num = request.GET.get("q")
    print(num)
    if str(num).__len__()==9:
        result = Result.objects.filter(number__icontains=num)
    else:
        result = None
    
    ctx['result']=result
    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json

    if is_ajax_request:
        html = render_to_string(template_name='result-index.html', context={'result':result})

        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "index.html", context=ctx)