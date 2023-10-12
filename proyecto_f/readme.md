# MedicalDB

MedicalDB es una aplicación web diseñada para médicos con el propósito de gestionar y administrar la información de los pacientes en un entorno hospitalario.

## Objetivo Funcional

El objetivo funcional de MedicalDB es proporcionar a los médicos una herramienta eficaz para administrar y mantener registros de los pacientes. La aplicación permite a los médicos realizar las siguientes acciones:

- Agregar nuevos pacientes al sistema.
- Editar la información de los pacientes existentes.
- Eliminar pacientes del sistema.
- Aministracion del personal.
- Visualizar Hospitales.
- Facilitar la ubiacion del hospital.
- Buscar pacientes por DNI o número de matrícula de médico.
- Asignar y gestionar avatares para los usuarios.

## Modelos

La aplicación MedicalDB incluye los siguientes modelos:

1. **Pacientes**: Este modelo almacena información sobre los pacientes, incluyendo campos como nombre, apellido y DNI. El DNI se utiliza como clave principal para identificar a los pacientes de forma única.

2. **Avatar**: Este modelo se encarga de almacenar los avatares asignados por los usuarios.

3. **Medicos** Este modelo almacena el personal del hospital con su informacion personal, matricula, hospital donde trabajan y rama en la que se desempeñan. La matricula se utiliza como clave principal para identificar a los pacientes de forma única.

4. **Pacientes Internados**: Este modelo almacena información sobre los pacientes que se encuentran internados en el hospital, incluyendo campos como nombre, apellido y DNI. El DNI se utiliza como clave principal para identificar a los pacientes de forma única.

5. **Hospitales** Este modelo almacena los hospitales que trabajan bajo MedicalDB, almacena un id, el nombre del hospital, la direccion y la localidad. El id se utiliza como clave principal para identificar a los hospitales de forma única.

## Vistas

MedicalDB cuenta con varias vistas, algunas de las cuales requieren que los usuarios estén autenticados para acceder. Estas son algunas de las vistas clave:

- **Registro y Login**: Vistas de autenticación de usuarios para el registro y el inicio de sesión.

- **Lista de Pacientes**: Permite a los médicos ver la lista de pacientes almacenados en el sistema. Incluye dos buscadores: uno para buscar pacientes por DNI y otro para buscar pacientes asignados a un médico por número de matrícula.
  
- **Lista de Pacientes Internados**: Permite a los médicos ver la lista de pacientes en internacion almacenados en el sistema. Incluye tres buscadores: uno para buscar pacientes por DNI, otro para buscar pacientes asignados a un médico por número de matrícula y otro para buscar pacientes por la sala en la que se encuentren.

- **Lista de Hospitales**: Permite a los médicos ver los hospitales registrados en la BD. Incluye dos buscadores: uno para buscar un hospital por id y otro para buscar hospitales por una localidad.

- **Lista Medicos**: Permite ver a los medicos registrados, esta vista les asigna un numero de matricula y permite vincularlos a un hospital y a una rama.

- **Editar Paciente**: Permite a los médicos editar la información de un paciente existente.

- **Eliminar Paciente**: Permite a los médicos eliminar un paciente del sistema.

- **Agregar Paciente**: Permite a los médicos agregar nuevos pacientes al sistema.
  
- **Editar Paciente Internado**: Permite a los médicos editar la información de un paciente en internacion.

- **Eliminar Paciente Internado**: Permite a los médicos eliminar un paciente que estuviera en internacion del sistema.

- **Agregar Paciente Internado**: Permite a los médicos agregar nuevos pacientes que hayan sido internados al sistema.

- **Página de Inicio**: Ofrece información general sobre la aplicación y sus funcionalidades.

- **Acerca de Mí**: Una vista personal que brinda información sobre el autor del proyecto.

## Video de la App

Adjunto video mostrando como funciona la App

`https://youtu.be/h92S4lL0xnw`

## Ingreso a la pagina

Para acceder a MedicalDB, sigue estos pasos:

1. Ejecuta el servidor de desarrollo de Django con `python manage.py runserver`.

2. Abre tu navegador web y ve a `http://127.0.0.1:8000/`

## Usuario Administrador (Superusuario)

Para acceder al panel de administración de MedicalDB como superusuario, sigue estos pasos:

1. Ejecuta el servidor de desarrollo de Django con `python manage.py runserver`.

2. Abre tu navegador web y ve a `http://localhost:8000/admin/`.

3. Inicia sesión con las siguientes credenciales:
   - **Usuario**: fpietraroia@gmail.com
   - **Contraseña**: feli1012

El superusuario tiene acceso completo al panel de administración de Django y puede gestionar todos los aspectos de la aplicación.

¡Disfruta utilizando MedicalDB para gestionar tus pacientes de manera eficiente!
