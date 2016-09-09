from __future__ import unicode_literals

from django.db import models

class info_form(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length = 100, null = True, blank = False)
    Reg = models.CharField(max_length = 100, null = True, blank = False)
    cc_myself = models.BooleanField(default=True)
    #det = models.ChoiceField(choices = ['Pondi','Chennai', 'Mahab'])

    def __unicode__(self): return self.full_name
