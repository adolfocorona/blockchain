from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail

def user_login(request):
    return render(request, 'login.html')

def home_view(request):
    # Aquí puedes realizar cualquier lógica necesaria para tu página de inicio
    # Por ejemplo, podrías consultar la base de datos para obtener datos que se mostrarán en la página.
    # Luego, renderizas la plantilla y la devuelves como respuesta.
    return render(request, 'home.html')

def transferencias_view(request):
    # Aquí puedes colocar la lógica para mostrar la página de transferencias
    # Por ejemplo, podrías obtener datos de transferencias desde la base de datos
    # y pasarlos a la plantilla para renderizarlos en la página

    # Aquí se muestra una renderización básica de la plantilla 'transferencias.html'
    return render(request, 'transferencias.html')

def aboutus_view(request):
    # Aquí puedes colocar la lógica para mostrar la página de transferencias
    # Por ejemplo, podrías obtener datos de transferencias desde la base de datos
    # y pasarlos a la plantilla para renderizarlos en la página

    # Aquí se muestra una renderización básica de la plantilla 'transferencias.html'
    return render(request, 'aboutus.html')

def services_view(request):
    # Aquí puedes colocar la lógica para mostrar la página de transferencias
    # Por ejemplo, podrías obtener datos de transferencias desde la base de datos
    # y pasarlos a la plantilla para renderizarlos en la página

    # Aquí se muestra una renderización básica de la plantilla 'transferencias.html'
    return render(request, 'services.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_type = request.POST['userType']
        name = request.POST['name']

        if user_type == 'cliente':
            client_id = 1234
            message = f'Hola {name}, tu ID de cliente es: {client_id}. Es muy importante que guardes este ID para poder iniciar sesión.'
        elif user_type == 'empleado':
            employee_id = 1234
            message = f'Hola {name}, tu ID de empleado es: {employee_id}. Es muy importante que guardes este ID para poder iniciar sesión.'

        # Enviar un correo electrónico de confirmación al usuario
        send_mail(
            'Registro exitoso',
            message,
            'adolfocoronaaa@gmail.com',  # Cambia esto por tu dirección de correo
            [email],
            fail_silently=False,
        )
        return redirect('home')  # Redirigir al usuario a la página de inicio después del registro
    else:
        form = UserCreationForm()
    return render(request, 'login.html', {'form': form})