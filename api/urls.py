from django.urls import path
from api import views

urlpatterns = [
    path('tasks',views.TodoItemViews.as_view(),name="todo_list"),
    path('tasks/<int:id>', views.TodoItemViews.as_view(),name="todo_task+update+delete"),
    path('tasks/search',views.TaskSearch.as_view(),name='search item')
]