from rest_framework.decorators import api_view
from django.http.response import JsonResponse


@api_view(['POST'])
def book_post(request):
    return JsonResponse({'data':'', 'success':True})

@api_view(['GET'])
def book_collection(request):
    try:
        return JsonResponse({'data':'', 'success':True})
    except:
        return JsonResponse({'message':'Books not avaliable', 'success':False})

@api_view(['GET', 'DELETE', 'PUT'])
def book_single(request):
    return JsonResponse({'data':'', 'success':True}) 
