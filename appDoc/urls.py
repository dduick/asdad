from django.contrib import admin
from django.urls import path
from documentos.views import *


#urls del proyecto doc4you
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_vista, name='home'), 
    path('login/', login_vista, name='login'),
    path('logout/', logout_vista, name='logout'),
    path('crear_usuario/', create_user, name='crear_usuario'),
    path('crear_doc/', create_doc, name='crear_doc'),
    path('doc_lista/', doc_lista, name='doc_lista'),
    path('doc_detalle/<int:id>', doc_detalle, name='doc_detalle'),
    path('doc_delete/<int:id>/delete', doc_delete, name='doc_delete'),
    path('home2/', home_vista2, name='home2'),
    path('content/', content, name="content"),
    path('doc_lista2/', doc_lista2, name = "doc_lista2"),
    # Otros patrones de URL de tu aplicación


]
