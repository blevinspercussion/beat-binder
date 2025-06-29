from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from users.models import CustomUser
from django.core.validators import FileExtensionValidator, ValidationError

class InstrumentTag(TaggedItemBase):
    class Meta:
        verbose_name = 'Instrument Tag'
        verbose_name_plural = 'Instrument Tags'

def validate_file_size(value):
    max_size = 10 * 1024 * 1024  # 10MB
    if value.size > max_size:
        raise ValidationError("File too large. Max size is 10MB.")

class Score(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('professional', 'Professional'),
    ]

    title = models.CharField(max_length=255, db_index=True)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='scores')
    composer = models.CharField(max_length=255, db_index=True)
    arranger = models.CharField(max_length=255, blank=True, null=True)
    instruments = models.CharField(max_length=255, help_text="Comma-separated list of instruments")
    time_signature = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    description = models.TextField(blank=True, null=True)
    tags = TaggableManager(blank=True, related_name='score_tags')
    pdf_file = models.FileField(
        upload_to='scores/',
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf']),
            validate_file_size
        ]
    )
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.composer}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('score_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-created_at']
