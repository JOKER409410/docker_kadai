import random

from django.shortcuts import get_object_or_404, redirect, render

from .forms import SeatAssignForm
from .models import Seat


def seat_list(request):
    """座席一覧（行ごとにグルーピングして表示）"""
    seats = Seat.objects.all()
    rows = {}
    for seat in seats:
        rows.setdefault(seat.row, []).append(seat)
    grouped_rows = [rows[r] for r in sorted(rows)]

    context = {
        "grouped_rows": grouped_rows,
        "total_seats": seats.count(),
        "occupied_count": seats.filter(status="occupied").count(),
    }
    return render(request, "seats/seat_list.html", context)


def seat_assign(request, seat_id):
    """座席に氏名を登録して使用中にする（在庫管理でいう新規登録・編集）"""
    seat = get_object_or_404(Seat, id=seat_id)

    if request.method == "POST":
        form = SeatAssignForm(request.POST, instance=seat)
        if form.is_valid():
            seat = form.save(commit=False)
            seat.status = "occupied"
            seat.save()
            return redirect("seats:seat_list")
    else:
        form = SeatAssignForm(instance=seat)

    return render(request, "seats/seat_form.html", {"form": form, "seat": seat})


def seat_clear(request, seat_id):
    """座席を空席に戻す（在庫管理でいう削除・在庫クリア）"""
    seat = get_object_or_404(Seat, id=seat_id)
    if request.method == "POST":
        seat.occupant_name = None
        seat.status = "empty"
        seat.save()
    return redirect("seats:seat_list")


def seat_shuffle(request):
    """使用中の座席の氏名をランダムに並び替える（加点ポイント：条件付き自動並び替え）"""
    if request.method == "POST":
        seats = list(Seat.objects.filter(status="occupied"))
        names = [seat.occupant_name for seat in seats]
        random.shuffle(names)
        for seat, name in zip(seats, names):
            seat.occupant_name = name
            seat.save()
    return redirect("seats:seat_list")