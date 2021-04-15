# HelpNet

## How to run this application
```bash
python -m venv venv # Create a virual environment
source venv/bin/activate # set the virtual environment
pip install -r requirements.txt # Install all the requirements

# Check if there any change in models, If so, prepare a script to apply those changes in the db
python manage.py makemigrations

# apply changes in the db
python manage.py migrate

# create your root/admin user
python manage.py createsuperuser

# Run the server and access via browser to http://127.0.0.1:8000
python manage.py runserver
```

# About the Project (Spanish Version)
_English version coming soon_

This is the Social Network for people who love Helps!

## Red Social de la Gente que ayuda

### Storytelling de donde surgió la idea
Hablando con mi pareja acerca de cómo mostrarle a nuestros hijos la vida real, distinta de los influencers superficiales, para darles una mejor perspectiva de vida, que puedan diseñar su futuro con propósito y no moldeen sus expectativas en base a cosas superficiales y tarden demasiado en darse cuenta que estaban viviendo en una burbuja y no son quienes ellos creían que eran. Por eso pensamos en sumarnos a actividades comunitarias, de ayuda al prójimo, ayudar a limpiar la playa, ayudar en las ollas populares, entregar algunas viandas de comida a personas en situación de calle, entre muchas otras actividades posibles. Pensando en esto vimos que hay limitantes como los horarios disponibles, las actividades que nos interesan, cuales están cercanos a donde vivimos, entre otros.

### Problema
Las personas que quieren sumarse a actividades de ayuda, ecológicas, entre otras se les dificulta sumarse por los horarios disponibles o las actividades a realizar que no son de su interés, además de la poca claridad sobre qué se hará en la actividad, o quienes más están, o cuáles han sido sus opiniones al respecto, entre otras limitantes. Algunas de las actividades no les muestra claramente cómo involucrar a sus hijos.

### Hipotesis
Si se crea algún tipo de plataforma donde ver las actividades según horarios, objetivos, comentarios, etc, donde la persona se vea reflejada en sus pares, donde pueda aclarar dudas, donde se le muestre más información sobre el problema a resolver y como la iniciativa que está consultando ayuda a mitigar el problema… de esta forma mucha más gente se sumará a las iniciativas y los organizadores de las iniciativas tendrán más público cautivo que están interesados.

### Solucion planteada
Crear una app android/iOS que permita a los interesados conocer las distintas iniciativas sociales en su zona, filtrando por areas de atencion (personas en situación de calle, ecologia, personas en depresión, inmigrantes, cooperativas de vivienda, auto-reparación, nivelación escolar, rescate de áreas comunes, etc), leer los comentarios de otros participantes, dejar sus comentarios, ver o dar ranking a una actividad particular o a la iniciativa en particular, ver o publicar fotos de la actividad.
Para los organizadores de una actividad, pueden realizar encuestas y consultar sus resultados. Pueden habilitar/deshabilitar comentarios, ranking, entre otros. Además de todas las tareas administrativas como iniciar el chat con un asistente/suscriptor, ver lista de asistentes, publicar historias (stories) de la actividad, compartir con otras redes sociales.

### Casos de Uso
* Un usuario busca actividades en su zona, y filtra por fecha, categoría/area de atencion, apto para menores, palabras clave, etc
* Un usuario consulta una actividad y se fija en las necesidades insatisfechas donde se puede sumar
* Un usuario se registra en una actividad, para apoyar en algo en especifico o en general donde lo quiera asignar el organizador
* Un usuario dona dinero, ropa, objetos
* Un usuario presta alguna herramienta
* Un organizador crea proyectos/iniciativas
* Un organizador crea actividades asociadas a proyectos/iniciativas
* Un usuario, en su home, tiene un timeline o feed donde ve info/posts de las actividades/proyectos/organizadores/categorías/zonas/otros usuarios que sigue
* Un usuario deja comentarios a los posts en el feed
* El dueño de un post controla si se pueden dejar comentarios en el post
* Un usuario deja una valoración/comentario en el proyecto/actividad/usuario
* Un Usuario publica fotos de una actividad
* Un Organizador controla que fotos se muestran y cuales no
* Un organizador realiza encuestas a los participantes registrados o en su feed
* Un usuario/organizador publica stories y vincularlas con alguna actividad o proyecto
* Un usuario/organizador comparte en otras redes sociales un post, una actividad, un proyecto
* Los usuarios se dejan mensajes en privado (DM)