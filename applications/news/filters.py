import django_filters

from .models import News

class NewsFilter(django_filters.FilterSet):
    class Meta:
        models = News
        fields = ('title', 'content')
