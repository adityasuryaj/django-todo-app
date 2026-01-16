from django.db import models

class Todo(models.Model):
    title = models.CharField("Judul",max_length=200)
    description = models.TextField("Deskripsi", blank=True)
    is_completed = models.BooleanField("Selesai?", default=False)
    created_at = models.DateTimeField("Dibuat pada", auto_now_add=True)

    class Meta:
        ordering = ['is_completed','-created_at']

    def __str__(self):
        return self.title
