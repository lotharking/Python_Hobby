"""Django models utilities"""

# Django
from django.db import models


class CRideModel(models.Model):
    """Shared Ride base model.
    
    CRideModel acts as an abstract base class from which every
    other model in the project will inherit. this class provides 
    every table with the following attibutes:
        + Created (Datetime): Shore the datetime the object was created
        + Modified (Datetime): Shore the last datetime the object was modified
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta options."""

        abstract = True
        
        get_latest_by = 'created'

        ordering = ['-created', '-modified']