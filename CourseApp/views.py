from django.shortcuts import render
from .models import Course

#
# from django.core import serializers
# from django.http import JsonResponse, HttpResponse
# from django.template import loader

# Create your views here.

def CourseView(request):
    # print(request._meta)
    c = Course.objects.filter(course_duration=3) # -> list
    out = []
    for i in c:
        out.append(i.__dict__)
    # out = [
    #         {
    #             'course_id': 1, 'course_name': 'BE', 'course_duration': 4
    #         },
    #         {   'course_id': 2, 'course_name': 'BA', 'course_duration': 3
    #         },
    #         {   'course_id': 3, 'course_name': 'ME', 'course_duration': 2
    #         },
    #         {
    #             'course_id': 4, 'course_name': 'MCA', 'course_duration': 3
    #         },
    #         {   'course_id': 5, 'course_name': 'BCA', 'course_duration': 3
    #         }
    #     ]
    return render(request, 'course.html', {'course': out})









# def CourseView(request):
#     # c = [Course.objects.get(course_duration=2)] # -> object
#     # c = Course.objects.filter(course_duration=5) # -> list
#     c = Course.objects.all() # -> list
#     # print(c)
#     out = []
#     for i in c:
#         out.append(i.__dict__)
#
#     tem = loader.get_template('course.html')
#
#     return HttpResponse(tem.render({'course': out}))

    # return render(request, 'course.html', {'course': out})
    # res = serializers.serialize('json', c)
    # res = serializers.serialize('python', c)
    # return Response({'course': out}, tem
                        # content_type=application/html)
    # return JsonResponse(res, safe=False)