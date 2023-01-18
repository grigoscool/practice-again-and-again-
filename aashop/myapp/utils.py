from .models import Category


menu = [
    {'title': 'о сайте', 'url': 'about'},
    {'title': 'добавть товар', 'url': 'add_item'},
    {'title': 'обратная связь', 'url': 'contact'},
    {'title': 'Войти', 'url': 'login'}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cat = Category.objects.all()
        context['cat'] = cat
        context['menu'] = menu
        return context
