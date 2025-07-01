from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from users.serializers import SocialLoginSerializer
from users.utils import social_login_process

class socialAuthRequestView(GenericAPIView):
    def get(self, request):    
        loginUrl = get_request_kakao_login()
        return Response({'status': 'success', 'result': loginUrl }, status=status.HTTP_200_OK)
    

class socialLoginView(GenericAPIView):
    serializer_class = SocialLoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        code = serializer.validated_data['code']
        print(code)
        try:
            response = social_login_process(code)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(response, status=status.HTTP_200_OK)