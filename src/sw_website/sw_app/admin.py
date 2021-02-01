from django.contrib import admin
from sw_app.models import Story, Card, Confirmation, Independent, DetailedAppropriately
from sw_app.models import Resource, AcceptanceCriteria
# Register your models here.

# admin.site.register(Author)
# admin.site.register(Story)

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     inlines = [BooksInstanceInline]


class ResourceInline(admin.StackedInline):
    model = Resource
    extra = 0

class DetailedAppropriatelyInline(admin.StackedInline):
    model = DetailedAppropriately

class AcceptanceCriteriaInline(admin.StackedInline):
    model = AcceptanceCriteria
    extra = 1

class IndependentInline(admin.StackedInline):
    model = Independent


class ConfirmationInline(admin.StackedInline):
    model = Confirmation

class CardInline(admin.StackedInline):
    model = Card

@admin.register(Story)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        CardInline,
        ConfirmationInline,
        IndependentInline,
        AcceptanceCriteriaInline,
        DetailedAppropriatelyInline,
        ResourceInline
    ]
