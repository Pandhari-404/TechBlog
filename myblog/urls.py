from django.urls import path
from myblog import views
from django.contrib import admin
from django.shortcuts import render


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render, {'template_name': 'home.html'}, name='home'),
    path('article/', render, {'template_name': 'article.html'}, name='article'),
    path('categories/', render, {'template_name': 'categories.html'}, name='categories'),
    path('about/', render, {'template_name': 'about.html'}, name='about'),
    path('readblog/', render, {'template_name': 'readblog.html'}, name='readblog'),
    path('css grid/', render, {'template_name': 'css grid.html'}, name='css grid'),
    path('javascript features/', render, {'template_name': 'JavaScript freatures.html'}, name='javascript features'),
    path('responsive desine/', render, {'template_name': 'responsive desine.html'}, name='responsive desine'),
    path('web development tips/', render, {'template_name': 'web development tips.html'}, name='web development tips'),
    path('productivity hacks/', render, {'template_name': 'Productivity Hacks.html'}, name='productivity hacks'),
    path('tech trends/', render, {'template_name': 'Tech Trends.html'}, name='tech trends'),
    path('bootstrap guide/', render, {'template_name': 'bootstrap guide.html'}, name='bootstrap guide'),
    path('ui-ux-principles/', render, {'template_name': 'UI_UX_Principles.html'}, name='ui_ux_principles'),
    path('messages/', render, {'template_name': 'messages.html'}, name='messages'),
    path('contact/', views.contact, name='contact'),
]
