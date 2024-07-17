from django.urls import path
from .views import step_one_view, step_two_view, step_three_view, success_view

urlpatterns = [
    path('', step_one_view, name='step_one'),
    path('step_two/', step_two_view, name='step_two'),
    path('step_three/', step_three_view, name='step_three'),
    path('success/', success_view, name='success'),
]
