from django.db import models

class Script(models.Model):
    prompt = models.TextField()
    generated_script = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Script {self.id} - {self.created_at}"
