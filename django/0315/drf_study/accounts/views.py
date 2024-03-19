from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request):
    print("request.data")
    print(request.data)
    content = {
        'message': 'Hello, World!',
        'user' : str(request.user)
    }
    return Response(content)