from django.contrib import admin
from django.urls import path
from task2.views import function_view, ClassView
from task3.views import main, games, basket


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', function_view, name='function_view'),
    path('class/', ClassView.as_view(), name='ClassView'),
    path('main', main),
    path('games', games),
    path('basket', basket)
]
