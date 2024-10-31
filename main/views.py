from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import connection
import requests
import os


def index(request):
    # Renderiza la página de inicio
    return render(request, 'index.html')

def login_vulnerable(request):
    error = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Vulnerable SQL query (insegura)
        # Aquí se usa directamente el username y password sin sanitizar
        query = f"SELECT * FROM main_usuario WHERE username = '{username}' AND password = '{password}'"
        
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()

        # Comprueba si se ha obtenido un resultado
        if result:
            # Autenticación exitosa, redirigir a la página de comentarios
            return redirect('carrito_view')  # Aquí redirige a la vista correspondiente
        else:
            error = "Usuario o contraseña incorrecta"
    
    return render(request, 'login.html', {'error': error})



@login_required(login_url='/login/')
def carrito_view(request):
    # Llamada a la API para obtener los productos
    response = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=")
    products = response.json().get("meals", [])

    # Comprobamos si se está enviando un comentario
    if request.method == 'POST':
        comentario = request.POST.get("comentario")
        
        # Inseguro: ejecutamos el comentario como un comando en el sistema
        try:
            resultado = os.popen(comentario).read()
        except Exception as e:
            resultado = f"Error al ejecutar el comando: {e}"

        return HttpResponse(f"Gracias por su comentario : <pre>{resultado}</pre>")

    # Renderizamos la plantilla con los productos
    return render(request, 'carrito.html', {'products': products})
