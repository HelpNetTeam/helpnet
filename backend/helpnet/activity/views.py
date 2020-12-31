from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Activity
from .serializers import ActivitySerializer


@csrf_exempt
def activity_list(request):

    if request.method == 'GET':
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActivitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def activity_detail(request, id):
    try:
        activity = Activity.objects.get(pk=id)

    except Activity.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ActivitySerializer(activity)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ActivitySerializer(activity, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        activity.delete()
        return HttpResponse(status=204)

    else:
        return HttpResponse(status=405)
