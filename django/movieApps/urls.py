from django.urls import path
from .views import MovieList, MovieDetail, MovieCategory , MovieLanguage , MovieSearch , MovieYear


app_name = 'movieApps'

urlpatterns = [
    # path('', TemplateView.as_view(), template_name="movieApp/home.html"),
    # path('', Home.as_view(), name='home'),
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
    path('category/<str:category>', MovieCategory.as_view() , name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view() , name='movie_language'),
    path('search/', MovieSearch.as_view() , name='movie_search'),
    path('<slug:slug>', MovieDetail.as_view() , name='movie_detail'),
    path('year/<int:year>', MovieYear.as_view() , name='movie_year'),

]