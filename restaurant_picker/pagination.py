'''
Customize pagination
'''
import math
from collections import OrderedDict
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class DisplaySize(LimitOffsetPagination):
    '''
    Customize class for pagination
    '''
    page_size = 2
    page_query_param = 'page'

    def get_paginated_response(self, data):
        total = self.count
        per_page = self.limit
        per_page = 0 if total == 0 else per_page
        current_page = int(self.offset/self.limit)+1
        final_page = int(math.ceil(self.count/self.limit))
        final_page = 1 if final_page == 0 else final_page
        # print("PAGINATION CALLED!")
        order_dickt = OrderedDict([
            ('total', total),
            ('per_page', per_page),
            ('current_page', current_page),
            ('final_page', final_page),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ])
        return Response(order_dickt)
        