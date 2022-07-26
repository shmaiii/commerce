from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing/", views.create_listing, name="create_listing"),
    path("<str:title>/<int:id>/", views.listing, name="listing"),
    path("<int:id>/watchlistAdd", views.watchlistAdd, name="watchlistAdd"),
    path("remove_from_watchlist/<int:id>", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("category", views.category, name="category")
]
