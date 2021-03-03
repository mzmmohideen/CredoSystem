from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Course
from django.contrib.auth.models import User
from .credo import InputForm

#
# from django.core import serializers
# from django.http import JsonResponse, HttpResponse
# from django.template import loader

# Create your views here.

@csrf_exempt
def UserReg(request):
    if request.method == 'GET':
        return render(request, 'registration.html', {
            'form': InputForm()
        })
    elif request.method == 'POST':
        User.objects.create(**request.POST)
        return HttpResponse('success', status=200)
    else:
        return HttpResponse('failed', status=400)



# @csrf_exempt
# def UserRegForm(request):
#     print(request.POST)
#

def CourseView(request):
    duration = request.GET.get('duration', 'not exist')
    if bool(duration) == True and duration.isdigit():
        duration = int(duration)
    else:
        print(duration)
        duration = 3
    c = Course.objects.filter(course_duration=duration) # -> list
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