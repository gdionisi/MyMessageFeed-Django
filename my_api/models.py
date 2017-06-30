from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return u'%s' % (self.text[:10])