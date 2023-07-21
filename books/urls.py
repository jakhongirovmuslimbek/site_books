from django.urls import path
from .views import categoryView, mybooksView, audiosView

urlpatterns = [
    path("categories/<str:cate_id>/", categoryView, name='categories'),
    path("mybooks/<str:user_id>/", mybooksView, name='mybooks'),
    path("audios/<str:book_id>/", audiosView, name='audios'),

]