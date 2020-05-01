import json
import random
import string
import urllib

from django.conf import settings
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_code_generator(instance, model_field):
    new_code_number = random_string_generator()
    Klass = instance.__class__

    qs_exists = Klass.objects.filter(**{model_field: new_code_number}).exists()
    if qs_exists:
        return unique_code_generator(instance)
    return new_code_number


# Unique Slug Generator
def unique_slug_generator(instance, source_model_field="title", output_model_field="slug", new_slug=None):
    Klass = instance.__class__

    instance_name = getattr(instance, source_model_field)
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance_name)

    qs_exists = Klass.objects.filter(**{output_model_field: slug}).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=4))
        return unique_slug_generator(
            instance,
            source_model_field=source_model_field,
            output_model_field=output_model_field,
            new_slug=new_slug
        )

    return slug
