from animals.models import Announcement, Comment
from animals.serializers import AnnouncementDetailSerializer,CommentDetailSerializer, AnnouncementLitSerializer, CommentListSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from animals.permissions import IsOwner

class NoteCreate(generics.CreateAPIView):
    serializer_class = AnnouncementDetailSerializer

class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentDetailSerializer

class ListCommentView(generics.ListAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()

class ListAnnouncementView(generics.ListAPIView):
    serializer_class = AnnouncementLitSerializer
    queryset = Announcement.objects.all()

class AnnouncementDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnnouncementDetailSerializer
    queryset = Announcement.objects.all()
    permission_classes = (IsOwner,) #дает разрешение на редактирование в api только тому пользователю, который и создавал запись