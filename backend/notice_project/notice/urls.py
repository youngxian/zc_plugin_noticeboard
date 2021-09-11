from django.urls import path
from .views import CreateNoticeView, CommentReactionAPIView, AllNoticesView, CommentDeleteAPIView, NoticeDeleteAPIView, \
    EditNoticeAPIView, RetrieveNoticeCommentsView, CommentCreateAPIView,NoticeDetailAPIView,install,store_notice

# add url routes here

urlpatterns = [

    path('notices/', CreateNoticeView.as_view()),

    path('all-notices', AllNoticesView.as_view()),

    path('comment/reaction/update', CommentReactionAPIView.as_view()),

    path('notice/update', EditNoticeAPIView.as_view()),

    path('comment/delete', CommentDeleteAPIView.as_view()),

    path('notice/delete', NoticeDeleteAPIView.as_view()),

    path('comment/get', RetrieveNoticeCommentsView.as_view()),

    path('comment/create', CommentCreateAPIView.as_view()),

    path('notice/<int:notice_id>/details', NoticeDetailAPIView.as_view()),
    path('install',install, name='install'),
    path('save',store_notice, name='store_notice'),

]