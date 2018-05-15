# coding:utf-8


class Pagination(object):
    def __init__(self, total_count, current_page, per_page_item_num=10, max_page_num=5):
        # 数据总个数
        self.totalCount = total_count
        # 当前页
        try:
            self.currentPage = int(current_page)
        except:
            self.currentPage = 1
        # 每页显示行数
        self.perPageItemNum = per_page_item_num
        # 最多显示页码
        self.maxPageNum = max_page_num

    def start(self):
        if self.currentPage <= 1:
            return 0
        elif self.currentPage > self.num_pages:
            return (self.num_pages - 1) * self.perPageItemNum
        return (self.currentPage - 1) * self.perPageItemNum

    def end(self):
        if self.currentPage <= 1:
            return self.perPageItemNum
        elif self.currentPage > self.num_pages:
            return self.num_pages * self.perPageItemNum
        return self.currentPage * self.perPageItemNum

    @property
    def num_pages(self):
        """总页数"""
        a, b = divmod(self.totalCount, self.perPageItemNum)
        if b == 0:
            return a
        return a + 1

    def pages_num_range(self):
        """# 当前页
        # current_page
        # 最多现实的页码数量
        # per_page_num
        # 总页数
        # self.num_pages"""
        if self.num_pages < self.perPageItemNum:
            return range(1, self.num_pages + 1)
        part = int(self.perPageItemNum / 2)
        if self.currentPage <= part:
            return range(1, self.perPageItemNum + 1)
        if (self.currentPage + part) > self.num_pages:
            return range(self.num_pages - self.perPageItemNum + 1, self.num_pages + 1)
        return range(self.currentPage - part, self.currentPage + part + 1)

    def page_str(self):
        page_list = []
        first_page = "<li><a href='/index2.html?p=1'>首页</a></li>"
        page_list.append(first_page)
        if self.currentPage <= 1:
            self.currentPage = 1
            prev_page = "<li><a href='#'>上一页</a></li>"
        else:
            prev_page = "<li><a href='/index2.html?p=%s'>上一页</a></li>" % (self.currentPage - 1)
        page_list.append(prev_page)
        for i in self.pages_num_range():
            if i == self.currentPage:
                temp = "<li class='active'><a href='/index2.html?p=%s'>%s</a></li>" % (i, i)
            else:
                temp = "<li><a href='/index2.html?p=%s'>%s</a></li>" % (i, i)
            page_list.append(temp)
        if self.currentPage == self.num_pages:
            next_page = "<li><a href='#'>下一页</a></li>"
        else:
            next_page = "<li><a href='/index2.html?p=%s'>下一页</a></li>" % (self.currentPage + 1)
        page_list.append(next_page)
        last_page = "<li><a href='/index2.html?p=%s'>尾页</a></li>" % self.num_pages
        page_list.append(last_page)
        return ''.join(page_list)