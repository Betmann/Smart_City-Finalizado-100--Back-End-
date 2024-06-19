from django.urls import path, include
from . import views
from app_smart.api.viewsets import (
    CreateUserAPIViewSet,
    SensorViewSet,
    TemperaturaDataViewSet,
    UmidadeDataViewSet,
    LuminosidadeDataViewSet,
    ContadorDataViewSet,
    SensorFilterView
)
from app_smart.api.filters import (
    SensorFilter,
    TemperaturaFilterView,
    UmidadeFilterView,
    LuminosidadeFilterView,
    ContadorFilterView
)

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Configuração do roteador padrão do Django REST Framework
router = DefaultRouter()
router.register(r'sensores', SensorViewSet)
router.register(r'temperatura', TemperaturaDataViewSet)
router.register(r'umidade', UmidadeDataViewSet)
router.register(r'luminosidade', LuminosidadeDataViewSet)
router.register(r'contador', ContadorDataViewSet)

# URLs do aplicativo
urlpatterns = [
    path('', views.abre_index, name='abre_index'),  # URL para a página inicial
    path('api/create_user/', CreateUserAPIViewSet.as_view(), name='create_user'),  # URL para criar usuário
    path('usuarios', views.autenticacao, name='cad_user'),  # URL para a página de autenticação
    path('cad_user/', views.cad_user, name='cad_user'),  # URL para cadastrar usuário
    path('api/', include(router.urls)),  # Inclui as URLs do roteador
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # URL para obter token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # URL para atualizar token JWT
    path('api/sensor_filter/', SensorFilterView.as_view(), name='sensor_filter'),  # URL para filtro de sensores
    path('api/temperatura_filter/', TemperaturaFilterView.as_view(), name='temperatura_filter'),  # URL para filtro de dados de temperatura
    path('api/umidade_filter/', UmidadeFilterView.as_view(), name='umidade_filter'),  # URL para filtro de dados de umidade
    path('api/luminosidade_filter/', LuminosidadeFilterView.as_view(), name='luminosidade_filter'),  # URL para filtro de dados de luminosidade
    path('api/contador_filter/', ContadorFilterView.as_view(), name='contador_filter'),  # URL para filtro de dados de contador
]
