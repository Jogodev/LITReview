"""
URL configuration for litreview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import authentication.views
import review.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('home/', review.views.home, name='home'),
    path('posts/', review.views.posts, name='posts'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),

    # tickets
    path('tickets/create_ticket/', review.views.ticket_create, name='create_ticket'),
    path('tickets/<int:ticket_id>', review.views.ticket_details, name='ticket_details'),
    path('tickets/<int:ticket_id>/update/', review.views.ticket_update, name='ticket_update'),
    path('tickets/<int:ticket_id>/delete/', review.views.ticket_delete, name='ticket_delete'),

    # reviews
    path('reviews/review_create', review.views.review_create, name='review_create'),
    path('reviews/<int:review_id>', review.views.review_details, name='review_details'),
    path('reviews/<int:review_id>/update', review.views.review_update, name='review_update'),
    path('reviews/<int:review_id>/delete', review.views.review_delete, name='review_delete'),
    path('reviews/answer/<int:ticket_id>', review.views.review_answer, name='review_answer'),

    # follow unfollow
    path('subscriptions/', authentication.views.subscriptions_page, name='subscriptions'),
    path('subscriptions/follow', authentication.views.follow, name='follow'),
    path('subscriptions/unfollow/<int:id>', authentication.views.unfollow, name='unfollow'),
    path('subscriptions/blocked', authentication.views.blocked, name='blocked'),
    path('subscriptions/unblocked/<int:id>', authentication.views.unblocked, name='unblocked'),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
