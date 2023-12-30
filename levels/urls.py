from django.urls import path
from . import views

urlpatterns = [
    path('level0', views.level0, name='level0'),
    path('level1', views.level1, name='level1'),
    path('level2', views.level2, name='level2'),
    path('level3', views.level3, name='level3'),
    path('level4', views.level4, name='level4'),

    path('mauchly', views.level5, name='level5'),
    path('h0lb3rt0n', views.level6, name='level6'),
    path('kroehuwrq', views.level7, name='level7'),
    path('2018', views.level8, name='level8'),
    path('october_2022', views.level9, name='level9'),
    path('0x7bc', views.level10, name='level10'),
    path('teams', views.level11, name='level11'),
    path('linus_torvalds', views.level12, name='level12'),
    path('42', views.level13, name='level13'),
    path('111111111', views.level14, name='level14'),
    path('volons', views.level15, name='level15'),
    path('kigali', views.level16, name='level16'),
    path('progress', views.level17, name='level17'),
    path('24551', views.level18, name='level18'),
    path('chef', views.level19, name='level19'),
    path('n', views.level20, name='level20'),
    path('discipline', views.level21, name='level21'),
    path('98', views.level22, name='level22'),
    path('listobject', views.level23, name='level23'),
    path('1658175046', views.level24, name='level24'),

    path('mountain', views.level25_part1, name='level25_part1'),
    path('3005', views.level25_part2_and_level_26, name='level25_part2_and_level_26'),

    path('alx_otter_baguette_water_terminal', views.level27, name='level27'),

    # The following are to mock the error pages
    path('<str:url>', views.custom_404_view_1, name='error_404_1'),
    path('<str:url>/', views.custom_404_view_1, name='error_404_1'),
]
