# ArisIMDB


- 1.1. Instalasi Django
    - clone git
    - buat venv: python manage.py -m venv venv
    - Langkah ketika bermasalah dengan privillage ketika aktivasi venv:
        - `Set-ExecutionPolicy Unrestricted -Scope Process`
        - `& d:/TUTORIAL/PYTHON/ArisIMDB/venv/Scripts/Activate.ps1`
    - `pip install django pillow pytz sqlparse
    - Membuat admin
        - `django-admin startproject core .` rename folder root menjadi 'django agar ndak bingung
        - python manage.py createsuperuser
    - Membuat app `'movieApp'`
        - `python manage.py startapp movieApp`
        - Registrasi di INSTALLED_APPS
    - Migrate  `python manage.py migrate`
    - jalankan 127.0.0.1:8000/admin, login sebagai superuser

- Buat Model Movie() dan menampilkannya di admin panel
    - code:
    - python manage.py makemigrations movieApp
    - python manage.py migrate
    - cek database sql, akan muncul tabel Movie
    - Registrasi Model ke admin.py agar bisa diakses dari admin panel:
        ```
            from .models import Movie
            
            admin.site.register(Movie)  
        ```
    
    - cek admin panel akan muncul table Movie
    - coba posting

- setup static dan media files
    - static --> css, media --> img
    - core/settings.py
    - 
        ```
            STATIC_URL = '/static/'

            MEDIA_URL = '/media/'
            MEDIA_ROOT = BASE_DIR / 'media'

            STATICFILES_DIRS = [
                BASE_DIR / "static"
            ]

        ```
    - config url untuk media/static
        - core/url.py
        - tambahkan setelah installed_app[]:
        ```
            from django.conf import settings
            from django.conf.urls.static import static

            urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - tes posting, maka field image akan tersimpan otomatis di folder media/movies

- Views
    - movieApp/views.py
        ```
            from django.shortcuts import render
            from django.views.generic import ListView, DetailView
            from .models import Movie


            class MovieList(ListView):
                model = Movie

            class MovieDetail(DetailView):
                model = Movie

        ```
    
- Templates
    - movieApp/templates/movieapp, add:
        - movie_list.html
        - movie_detail.html

- URL
    - core/url.py
    ```
        from django.contrib import admin
        from django.conf import settings
        from django.conf.urls.static import static
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('movieApp.urls', namespace='movieApp')),
        ]

        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
    - movieApp/url.py
    ```
        from django.urls import path
        from .views import MovieList, MovieDetail

        app_name = 'movieApp'

        urlpatterns = [
            path('movie-list', MovieList.as_view(), name='movie_list'),
            path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),

        ]
    ```
    - tes:
        - 127.0.0.1:8000/movie-list --> menampilkan view MovieList() --> menampilkan templates/movie_list.html
        - 127.0.0.1:8000/1/ --> menampilkan view DetailList() --> menampilkan templates/detail_list.html