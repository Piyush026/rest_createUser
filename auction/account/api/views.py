import json

from account.api.serializers import RegistrationSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view(['POST', ])
def registration_view(request):
    action = request.POST.get('hiddenButton')
    print("hiddenbutton", action)
    if action == 'vendor':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully register a new user"
            data['email'] = account.email
        else:
            data = serializer.errors
        print(data)
        # return Response(data)
        return render(request, 'vendor.html', {"data": json.dumps(data)})
    else:
        serializer = RegistrationSerializer(data=request.data)
        print(serializer)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully register a new user"
            data['email'] = account.email

        else:
            data = serializer.errors
        print(data)
    # return Response(data)
    return render(request, 'bidder.html')
