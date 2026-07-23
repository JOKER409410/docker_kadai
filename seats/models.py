from django.db import models


class Seat(models.Model):
    STATUS_CHOICES = [
        ("empty", "空席"),
        ("occupied", "使用中"),
    ]

    row = models.PositiveIntegerField("行")
    col = models.PositiveIntegerField("列")
    occupant_name = models.CharField("氏名", max_length=50, blank=True, null=True)
    status = models.CharField("状態", max_length=10, choices=STATUS_CHOICES, default="empty")
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        ordering = ["row", "col"]
        unique_together = ("row", "col")
        verbose_name = "座席"
        verbose_name_plural = "座席"

    def __str__(self):
        return f"{self.row}-{self.col} {self.occupant_name or ''}"