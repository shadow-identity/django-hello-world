def get_settings_dict():
    """ returns dictionary with all settings """
    from django.conf import settings
    settings_dict = {}
    for key in dir(settings):
        settings_dict[key] = getattr(settings, key)
    return settings_dict


def django_settings(request):
    """ push settings_dict to context """
    settings_dict = get_settings_dict()
    return settings_dict