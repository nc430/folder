from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from test01 import models


# Create your views here.

# USER_LIST = []
# for i in range(1, 999):
#     temp = {'name': "root" + str(i), 'age': i}
#     USER_LIST.append(temp)
class CustomPaginator(Paginator):
    """扩展内置分页类，实现自定制分页"""

    def __init__(self, current_page, per_pager_num, *args, **kwargs):
        self.current_page = int(current_page)
        self.per_page_num = int(per_pager_num)
        super(CustomPaginator, self).__init__(*args, **kwargs)

    def pages_num_range(self):
        """# 当前页
        # current_page
        # 最多现实的页码数量
        # per_page_num
        # 总页数
        # self.num_pages"""
        if self.num_pages < self.per_page_num:
            return range(1, self.num_pages + 1)
        part = int(self.per_page_num / 2)
        if self.current_page <= part:
            return range(1, self.per_page_num + 1)
        if (self.current_page + part) > self.num_pages:
            return range(self.num_pages - self.per_page_num + 1, self.num_pages + 1)
        return range(self.current_page - part, self.current_page + part + 1)


def index(request):
    base_page = 10
    num_list = list(models.Num_count.objects.values("id", "number"))
    current_page = request.GET.get("p")
    if current_page:
        current_page = int(current_page)
    else:
        current_page = 1
    start_page = (current_page - 1) * base_page
    end_page = base_page * current_page
    finally_list = num_list[start_page:end_page]
    if current_page <= 1:
        prev_page = 1
        next_page = current_page + 1
    else:
        prev_page = current_page - 1
        next_page = current_page + 1
    return render(request, 'index.html', locals())


def index1(request):
    current_page = request.GET.get("p")
    num_list = list(models.Num_count.objects.values("id", "number"))
    try:
        if current_page:
            paginator = CustomPaginator(current_page, 10, num_list[:199], 10)
            try:
                posts = paginator.page(current_page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            return render(request, "index1.html", locals())
        else:
            num_list = list(models.Num_count.objects.values("id", "number"))
            paginator = CustomPaginator(1, 10, num_list[:199], 10)
            try:
                posts = paginator.page(1)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            return render(request, "index1.html", locals())
    except:
        paginator = CustomPaginator(1, 10, num_list[:199], 10)
        posts = paginator.page(1)
        return render(request, "index1.html", locals())