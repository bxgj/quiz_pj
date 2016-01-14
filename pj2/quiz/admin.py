from django.contrib import admin
from quiz.models import Question, Choice, Player,Supplier, Consumer

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    list_display=('question_text','question_category','question_score','question_level','question_limit_second','question_creater','question_create_at','question_close_at')
    inlines = [ChoiceInline]
    readonly_fields=('question_level','question_solver',)
    search_fields=['question_text','question_creater__player_name']
#    list_filter=['question_level']
#    fields=('question_level',)

class SupplierAdmin(admin.ModelAdmin):
    list_display=('player_name','player_score','create_count','rank')
    exclude=('role',)

class ConsumerAdmin(admin.ModelAdmin):
    list_display=('player_name','player_score','answer_count','success_count','fail_count','rank')
    exclude=('role',)

admin.site.register(Question,QuestionAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Consumer,ConsumerAdmin)
