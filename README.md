# Tercera-pre-entrega-Mancebo
Tercera pre-entrega Mancebo 
Facturance
Facturance es una aplicación web desarrollada con Django que permite el registro de clientes, productos, búsqueda de productos y lleva un registro e historial de ventas.

Estructura del proyecto
El proyecto principal se denomina "TerceraPreEntregaMancebo" y consta de dos aplicaciones:

TerceraPreEntregaManceboApp: Esta aplicación contiene los modelos de productos, detalles de ventas y ventas. Aquí se gestionan las funcionalidades relacionadas con el registro de productos y el seguimiento de las ventas.

Clientes: Esta aplicación se encarga del registro de clientes. Aquí se pueden agregar los datos de los clientes.

Requisitos previos
Python 3.7 o superior
Django 3.0 o superior
Instalación
Clona el repositorio de Facturance:
bash

git clone https://github.com/tu_usuario/Facturance.git
Accede al directorio del proyecto:
bash

cd Facturance
Crea y activa un entorno virtual (opcional pero se recomienda):
bash

python3 -m venv env
source env/bin/activate
Instala las dependencias requeridas:

pip install -r requirements.txt
Realiza las migraciones de la base de datos:

python manage.py makemigrations
python manage.py migrate
Inicia el servidor de desarrollo de Django:

python manage.py runserver
Accede a la aplicación en tu navegador web:
arduino

http://localhost:8000/
Uso
Registra los clientes:

Accede a la sección "Clientes" en el menú de navegación.
Haz clic en el botón "Agregar cliente" para registrar un nuevo cliente.
Completa los campos requeridos y guarda los cambios.
Registra los productos:

Accede a la sección "Productos" en el menú de navegación.
Haz clic en el botón "Agregar producto" para registrar un nuevo producto.
Ingresa los detalles del producto y guarda los cambios.
Busca productos:

Utiliza la barra de búsqueda en la


