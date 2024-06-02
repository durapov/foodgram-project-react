from djoser import views as djoser_views
from .models import User
from .serializers import UserSerializer


class UserViewSet(djoser_views.UserViewSet):
    queryset = User.objects.all()
    srializer_class = UserSerializer
