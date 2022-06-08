import graphene
from .utils import get_paginator


# Now we create a corresponding PaginatedType for that object type:
class ProductPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()