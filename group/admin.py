from django.contrib import admin

from group.models import Teacher, Student, Group

# Register your models here.
admin.site.register(Teacher)
# admin.site.register(Student)
# admin.site.register(Group)


@admin.register(Student)
class Students(admin.ModelAdmin):
    list_display = ('student_full_name', 'contacts', 'groups_list')

    def student_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    def groups_list(self, obj):
        # print(obj, '!!!!!!!!!!!!!!!!')
        return [x.title for x in obj.groups.all()]


@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'count', 'students_list')

    def count(self, obj):
        return obj.students.count()

    def students_list(self, obj):
        return [x for x in obj.students.all()]


