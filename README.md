# Proyecto Django: Sitio Ficticio de Seguridad

¡Bienvenido al repositorio del **Proyecto de Seguridad en Django**! 🚀 Este proyecto es una aplicación ficticia creada para demostrar fallos de seguridad comunes y explorar su explotación y solución. Además, cuenta con un flujo de trabajo automatizado usando **GitHub Actions** para el despliegue en un servidor mediante **Docker Compose** por **SSH**.

## 📜 Descripción del Proyecto

Este proyecto está diseñado como una plataforma educativa y de prueba, que incluye intencionalmente algunas de las vulnerabilidades más comunes en aplicaciones web. Los principales fallos de seguridad que se incluyen en la aplicación son:

1. **Inyección SQL**: Puntos donde el código es vulnerable a manipulaciones de consulta SQL que pueden afectar a la base de datos.
2. **Inyección de Comandos del Sistema**: Lugares donde se permite la ejecución de comandos del sistema, exponiendo el servidor a manipulaciones no autorizadas.
3. **Fuga de Información Sensible**: Variables y rutas expuestas en el código que contienen información sensible, proporcionando a los usuarios no autorizados acceso a datos confidenciales.

## ⚠️ Importante

> **Advertencia**: Esta aplicación está diseñada con fines educativos y de prueba. No debe usarse en producción o en entornos públicos sin una auditoría de seguridad completa. 

## 📂 Estructura del Proyecto

- **/main**: Carpeta principal de la aplicación Django.
- **/prueba3**: Carpeta principal de la configuracion  Django.
- **/docker-compose.yml**: Archivo de configuración de Docker Compose para construir y ejecutar los contenedores de la aplicación.
- **requirements.txt**: Lista de dependencias de Python necesarias para ejecutar la aplicación.

## 🚩 Vulnerabilidades Incluidas

Aquí están las vulnerabilidades simuladas en esta aplicación:



1. **Inyección de Comandos del Sistema**:
   - Puntos en los que es posible que los usuarios envíen comandos del sistema que serán ejecutados directamente.
   - Ejemplo: Entrada en formularios o en la URL que pasa directamente al sistema sin verificación.

2. **Fuga de Información Sensible**:
   - Código que expone información como contraseñas, claves de API o rutas críticas en texto plano.
   - Ejemplo: Comentarios en el código que exponen detalles de configuración y otros datos sensibles.
   - En codigo puedes utilizar la herramienta web CyberChef para descubrir los secretos de la pagina 
  


## 🚀 Despliegue Automatizado con GitHub Actions y Docker Compose

Este proyecto utiliza **GitHub Actions** para la automatización de despliegue. Cada vez que se realiza un `push` a la rama principal, el flujo de trabajo de GitHub Actions se encarga de:

1. **Construcción y pruebas**: Compila la aplicación y corre pruebas unitarias (si están disponibles).
2. **Despliegue en el Servidor por SSH**: Se conecta por SSH al servidor configurado, transfiere los archivos y ejecuta **Docker Compose** para construir y correr la aplicación en contenedores.

### Configuración de GitHub Actions

Para configurar GitHub Actions para este proyecto:

1. Crea los siguientes **Secretos** en el repositorio de GitHub:
   - `SERVER`: Dirección IP o dominio del servidor de despliegue.
   - `USER_SERVE`: Nombre de usuario con permisos en el servidor.
   - `PASSWORD_SERVER`: Llave privada para autenticación SSH.
   
2. Asegúrate de tener configurado el archivo `.yml` para el flujo de trabajo en `.github/workflows/deploy.yml`. Este archivo debe contener las instrucciones para conectarse al servidor y ejecutar Docker Compose.
