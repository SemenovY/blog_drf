from rest_framework.pagination import PageNumberPagination


class NewsFeedPagination(PageNumberPagination):
    page_size = 10
