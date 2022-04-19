# experiencein/perfis/views.py
from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):

    perfil = Perfil()

    if perfil_id == 1:
        perfil = Perfil('Fábio Henrique', 'fabio.oliveira@ifb.edu.br', '222222', 'IFB')
    if perfil_id == 2:
        perfil = Perfil('Davi Resende', 'davi.reis@estudante.ifb.edu.br', '4002-8922', 'IFB')

    return render(request, 'perfil.html', {'perfil' : perfil})