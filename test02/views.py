from django.shortcuts import render
from test02 import models
from test02.page_class import Pagination
# Create your views here.


def index2(request):
    num_list = list(models.num2Count.objects.values("id", "number"))
    current_page = request.GET.get('p')
    if current_page:
        obj = Pagination(len(num_list), current_page)
    else:
        obj = Pagination(len(num_list), 1)
    data_list = num_list[obj.start():obj.end()]
    return render(request, "index2.html", locals())