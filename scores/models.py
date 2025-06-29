from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from users.models import CustomUser
from django.core.validators import FileExtensionValidator

class InstrumentTag(TaggedItemBase):
    class Meta:
        verbose_name = 'Instrument Tag'
        verbose_name_plural = 'Instrument Tags'

class Score(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('professional', 'Professional'),
    ]

    title = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='scores')
    composer = models.CharField(max_length=255)
    arranger = models.CharField(max_length=255, blank=True, null=True)
    instruments = TaggableManager(
        verbose_name='Instruments',
        help_text='Select the instruments played in this score',
        through=InstrumentTag,
        related_name='score_instruments',
    )
    time_signature = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    description = models.TextField(blank=True, null=True)
    tags = TaggableManager(
        blank=True,
        related_name='score_tags',
    )
    pdf_file = models.FileField(upload_to='scores/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.composer}"
    


    class Meta:
        verbose_name = 'Instrument'
        verbose_name_plural = 'Instrument Tags'