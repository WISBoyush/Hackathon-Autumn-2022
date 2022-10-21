from django.contrib.auth.models import Group, Permission


def create_groups(*args, **kwargs):  # noqa
    # student, is_created = Group.objects.get_or_create(name='student')
    # if not is_created:
    #     return
    # tutor, is_created = Group.objects.get_or_create(name='tutor')
    # if not is_created:
    #     return
    # staff, is_created
    Group.objects.get_or_create(name='student')
    Group.objects.get_or_create(name='tutor')
    Group.objects.get_or_create(name='staff')
