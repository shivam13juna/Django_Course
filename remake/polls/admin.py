from django.contrib import admin

from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    ''' The order of entites in fields list, determines the order in which they're viewed on admin page
    '''
    # fields = ['question_text', 'pub_date']]

    fieldsets = (
        ('Wanna change question?', {
            "fields": ['question_text']
            ,
        }),
        ('Date information', {
            'fields': ['pub_date']
        })
    )

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    inlines = [ChoiceInline]
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
