from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleTheme, Themes


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        self.is_main_counter = 0
        for form in self.forms:
            print(form)
            form_data = form.cleaned_data
            if form_data and form_data['is_main']:
                self.is_main_counter += 1
            if self.is_main_counter > 1:
                raise ValidationError('Основным может быть только один раздел.')
            if self.is_main_counter == 0:
                raise ValidationError('Укажите основной раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = ArticleTheme
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Themes)
class ThemesAdmin(admin.ModelAdmin):
    pass
