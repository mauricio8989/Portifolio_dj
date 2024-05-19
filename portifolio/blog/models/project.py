from django.db import models

STATUS = (
    (0, 'coding'),
    (1, 'finished')
)

class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', max_length=200)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title