from django.urls import path
from app import views

urlpatterns = [
    path("",views.home,name='home'),
    path("add_task/",views.create,name='create'),
    path("delete/<int:id>",views.dele,name='delete'),
    path("history/",views.history,name='history'),
    path("update/<int:id>",views.upd,name='update'),
    path("about/",views.about,name='about'),
    path("restore<int:id>",views.restore,name='restore'),
    path("dele_restore/<int:id>",views.dele_restore,name='dele_restore'),
    path("restore_all/",views.restore_all,name='restore_all'),
    path("dele_all/",views.dele_all,name='dele_all'),
    path("contact/",views.contact,name='contact')
]
