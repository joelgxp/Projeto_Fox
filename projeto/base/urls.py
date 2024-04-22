from django.contrib import admin
from django.urls import path
from index.views import index_view, auth_login_view, auth_register_view, usuarios_view, veiculo_view, ordemservico_view, dashboard_view


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', index_view.index, name='index'),
    
    path('usuarios/', usuarios_view.UsuariosView.as_view(), name='usuarios'),
    
    path('auth_login/', auth_login_view.auth_login, name='auth_login'),
    path('auth_register/', auth_register_view.auth_register, name='auth_register'),
    path('auth_logout/', auth_login_view.auth_logout, name='auth_logout'),
    
    path('dashboard/', dashboard_view.get_veiculos, name='dashboard'),
    path('profile/', index_view.profile, name='profile'),
    
    path('veiculos/', veiculo_view.get_veiculos, name='veiculos'),
    path('veiculo/cadastro', veiculo_view.create_veiculo, name='cadastro_veiculo'),
    path('veiculo/editar/<int:id>', veiculo_view.update_veiculo, name='veiculo_editar'),
    
    path('ordemservico/', ordemservico_view.get_ordem_servico, name='ordem_servico'),
    path('ordemservico/criar', ordemservico_view.create_ordem_servico, name='criar_ordem_servico'),
    path('ordemservico/adicionarServico', ordemservico_view.insert_servico_os, name='adicionar_servico_ordem_servico'),
    path('ordemservico/editar/<int:id>', ordemservico_view.edit_ordem_servico, name='editar_ordem_servico'),
    
]
