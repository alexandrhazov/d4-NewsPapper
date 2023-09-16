from django import template

# регистрируем библиотеку, в которой регистрируем фильтры
register = template.Library()

black_list = ['козёл', 'сосиска', 'редиска', 'плохое_слово1']


# первый аргумент это значение, к которому применяется второй аргумент фильтра
# регистрируем свой фильтр, который фильтрует нецензурные слова
# 1. Раскладываем полученный список на отдельные слова и итерируемся по ним
# 2. Если итое слово с маленькой буквой совпадает со словом в списке "черных слов",
# то заменяем это слово arg = "***" (|censor:'***') из шаблона
# 3. в конце возвращаем обратно весь очищенный список
@register.filter(name='censor')
def censor(value, arg):
    for i in value.split():
        if i.lower() in black_list:
            value = value.replace(i, arg)
    return value