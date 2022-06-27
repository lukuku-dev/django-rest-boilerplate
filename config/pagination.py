from rest_framework import pagination


class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 20
    max_limit = 100
