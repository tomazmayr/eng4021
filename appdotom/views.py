from django.shortcuts import render

from .models import Jogadores, Estadio, Times

def home(request):
  #função que renderiza a home do site
  return render(request, "home.html")

def list_futebol(request):
  #função que lista as classes importadas do models.py e as atribui um nome e contexto. Retorna o HTML de atributos para que a task seja alterada
  jogadores = Jogadores.objects.all()
  estadio = Estadio.objects.all()
  times = Times.objects.all()
  context = { "Jogadores": jogadores, "Estadios": estadio, "Times": times }
  return render(request, "atributos.html", context=context)

def create_futebol(request):
  #função para criar as tasks de uma das três classes listadas anteriormente e retorna o html com a lista das tarefas criadas
    if request.method == "POST":
        if "done" not in request.POST:
            done = False
        else:
            done = True
        Task.objects.create(title=request.POST["title"],
                            description=request.POST["description"],
                            due_date=request.POST["due-date"],
                            done=done)
        return redirect("tasks-list")

    return render(request, "task_form.html")


def update_futebol(request, task_id):
  #Função que atualiza as tasks com nova descrição ou parâmetro dependendo da URL passada e depois retorna a lista das tasks criadas já alterada
    task = Task.objects.get(id=task_id)
    task.due_date = task.due_date.strftime('%Y-%m-%d')

    if request.method == "POST":
        task.title = request.POST["title"]
        task.description = request.POST["description"]
        task.due_date = request.POST["due-date"]
        if "done" not in request.POST:
            task.done = False
        else:
            task.done = True
        task.save()
        return redirect("tasks-list")

    return render(request, "task_form.html", context={"task": task})


def delete_futebol(request, task_id):
  #Função que dependendo da URL passada deleta uma ou mais tasks, depois retorna a html com a lista das tasks
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
      if "confirm" in request.POST:
        task.delete()

      return redirect("tasks-list")

    return render(request, "delete_form.html", context={"task": task})

