from django.db import models
from django.utils.translation import ugettext_lazy as _
from i18nfield.fields import I18nCharField, I18nTextField

from prtx_faq.prtx import PRTX


class FAQCategory(models.Model):
    event = models.ForeignKey(to='pretixbase.Event' if PRTX == 'pretix' else 'event.Event', on_delete=models.CASCADE, related_name='faq_categories')
    name = I18nCharField(verbose_name=_('Name'))
    position = models.PositiveIntegerField(verbose_name=_('Position'))

    class Meta:
        unique_together = (('event', 'name'), )
        ordering = ('position', 'id')


class FAQ(models.Model):
    category = models.ForeignKey(to=FAQCategory, on_delete=models.CASCADE, related_name='questions', verbose_name=_('Category'))
    question = I18nCharField(verbose_name=_('Question'))
    answer = I18nTextField(verbose_name=_('Answer'))
    tags = models.CharField(null=True, blank=True, max_length=180, verbose_name=_('Tags'), help_text=('Tags can help people find related questions. Please enter the tags separated by commas.'))
    position = models.PositiveIntegerField(verbose_name=_('Position'))

    class Meta:
        ordering = ('position', 'id')