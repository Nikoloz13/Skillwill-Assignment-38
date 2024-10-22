from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Note
from . serializers import NoteSerializer

class NoteCollectionView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get(self, request):
        notes = request.user.notes.all()
        serializer = self.serializer_class(instance=notes, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
class NoteSinglentonView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        serializer = self.serializer_class(instance=note)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=note, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        note.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


