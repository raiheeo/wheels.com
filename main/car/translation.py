from .models import Car
from modeltranslation.translator import TranslationOptions,register

@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'color', 'type_change')
