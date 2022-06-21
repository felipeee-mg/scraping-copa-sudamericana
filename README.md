## Web scraping de los equipos participantes de la Copa Conmebol Sudamericana entre los años 2010 y 2020🏆

Programa de web scraping realizado en Python que obtiene desde la página web [transfermarkt.es](https://www.transfermarkt.es/copa-sudamericana/teilnehmer/pokalwettbewerb/CS/saison_id/2021) datos sobre los clubes de fútbol participantes de la Copa Conmebol Sudamericana entre las ediciones de los años 2010 y 2020. Lo anterior con el objetivo de generar un dataset en formato CSV para su uso en un proyecto de título🎓.


### Datos extraídos💻

Los datos extraídos para cada equipo en cada edición del torneo son los siguientes:
* __Nombre del Equipo__, indica el nombre oficial del equipo de fútbol.
* __Año de su participación__, indica la edición de la competición en la cual el equipo participó.
* __País__, indicia el país al cual pertenece el equipo de fútbol.
* __Valor de mercado__, representa la suma total de la valorización en millones de euros de los jugadores de su plantilla en el año en que el equipo participó de la competición.
* __Promedio del valor de mercado__, representa el promedio en millones de euros del valor de mercado del equipo el año en el que participó de la competición.
* __Promedio de edad__, representa el promedio de edad de todos los jugadores de la plantilla del equipo el año en que participó de la competición.
* __Cantidad de jugadores en la plantilla__, representa la cantidad de jugadores inscritos por el equipo para la temporada.
* __Cantidad de jugadores extranjeros__, representa la cantidad de jugadores extranjeros inscritos por el equipo para la temporada.


### Librerias utilizadas📚

* BeautifulSoup4.
* Requests.
* pandas.
