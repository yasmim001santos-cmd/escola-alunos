from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import redirect, render

from .forms import AlunoForm
from .models import Aluno


def lista(request):
    alunos = Aluno.objects.all()
    return render(request, "alunos/lista.html", {"alunos": alunos})


def criar(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Aluno cadastrado.")
        return redirect("lista")
    return render(request, "alunos/form.html", {"form": form, "titulo": "Novo aluno"})

def editar(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        messages.success(request, "Aluno atualizado.")
        return redirect("lista")

    return render(request, "alunos/form.html", {
        "form": form,
        "titulo": "Editar aluno"
    })
def excluir(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)

    if request.method == "POST":
        aluno.delete()
        messages.success(request, "Aluno excluído.")
        return redirect("lista")

    return render(request, "alunos/confirmar_exclusao.html", {
        "aluno": aluno
    })