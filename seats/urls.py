from django.urls import path

from . import views

app_name = "seats"

urlpatterns = [
    path("", views.seat_list, name="seat_list"),
    path("seats/<int:seat_id>/assign/", views.seat_assign, name="seat_assign"),
    path("seats/<int:seat_id>/clear/", views.seat_clear, name="seat_clear"),
    path("shuffle/", views.seat_shuffle, name="seat_shuffle"),
]