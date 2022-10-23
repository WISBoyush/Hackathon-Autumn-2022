from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from chat.models import Chat
from chat.serializers import ChatSerializer


class ChatViewSet(ModelViewSet):
    model = Chat
    serializer_class = ChatSerializer

    def partial_update(self, request, *args, **kwargs):
        if 'answer' not in request.data:
            return Response(status=400, data='The answer is required')
        answer = request.data.get('answer')
        instance = self.model.objects.get(id=self.kwargs.get('pk'))
        instance.answer = answer
        instance.status = "ANSWERED"
        instance.save()
        serializer = self.serializer_class(instance)
        return Response(status=200, data=serializer.data)

