from django.core.cache import cache

from .models import Category


menu = [
    {'title': 'о сайте', 'url': 'myapp:about'},
    {'title': 'добавть товар', 'url': 'myapp:add_item'},
    {'title': 'обратная связь', 'url': 'myapp:contact'},

]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        # кэшируем запрос
        cat = cache.get('cats')
        if not cat:
            cat = Category.objects.all()
            cache.set('cat', cat, 60)

        # если пользователь не зареган, удаляем из меню добавление итема
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['cat'] = cat
        context['menu'] = user_menu
        return context
