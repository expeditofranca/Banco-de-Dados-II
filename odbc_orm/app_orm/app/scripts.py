import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_orm.settings')
django.setup()

from app.models import Projeto, Atividade

p = Projeto.objects.create(nome="Projeto 1", lider="João")

Atividade.objects.create(
    titulo="Atividade 1",
    descricao="Teste",
    projeto=p
)

p.lider = "Maria"
p.save()

for proj in Projeto.objects.all():
    print(proj.nome)
    for a in proj.atividades.all():
        print(" -", a.titulo)