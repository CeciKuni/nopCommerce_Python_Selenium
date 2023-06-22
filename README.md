# Demo Automation - Python con Selenium y Pytest

Este es mi primer proyecto de automation con Selenium-Webdriver y Python. Seguí las instrucciones del curso: [SDET- QA Automation Techie](https://www.youtube.com/watch?v=57pjD89IFXA ). Me sirvió mucho la guía ya que estuve buscando cómo armar de forma más organizada toda la estructura del proyecto con Page Object Model. Hubo muchas cosas que actualicé y mejoré, ya que el curso es de hace 2 años. También coloqué aparte los "Locators" de los elementos (me gusta tenerlo en un solo lugar).
Me quedó pendiente terminar de configurar el proyecto en Jenkins y ver la manera de compartir los reportes de Allure. Por el momento en esta demo utilizo Pytest-html que genera un reporte simple en html.


## Datos

1. Página de prueba utilizada: [NonCommerce](https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F)
2. Sistema Operativo: Windows 10.
3. Navegadores configurados: Chrome por defecto, Firefox y Edge.
4. IDE: Pycharm (generalmente utilizo Visual Studio Code, pero para Python me pareció mucho más sencillo utilizar Pycharm).
5. El proyecto cuenta con capturas de pantalla en formato .png se puede configurar para que tome capturas donde deseemos. El formato del nombre es el nombre del test + fecha/hora +.png, que se guardan en la carpeta "Screenshots".
6. El reporte html se guarda en la carpeta "Reports". Se va pisando con el nombre "report.html". Se puede o no generar, depende si lo especificamos en el comando.
7. El proyecto también cuenta con un archivo de logs llamado "automation.log" en la carpeta "Logs". Se puede configurar el modo ya sea Debug, Warning, Basic_Format, Critical, etc. Por defecto está en modo INFO. Los mensajes que se ven son los customizados en los tests.

## Instalaciones realizadas

- [Python](https://www.python.org/downloads/). Colocar la ruta de la carpeta Python y python/Scripts en las variables de entorno.
- Pip.
```
$ python get-pip.py
```
- Selenium. Ejecutar el comando en la consola de Windows cmd.
```
$ pip install selenium
```
- [Pycharm](https://www.jetbrains.com/es-es/pycharm/download/#section=windows)
- Desde Pycharm se instalaron las siguientes librerías y frameworks: 
-- Pytest: Python unitTest framework.
-- Pytest-html: Pytest reporte en html.
-- Pytest-xdist: para ejecutar tests en paralelo (varios threads).
-- Openpyxl: soporte para de MS Excel.

## Estructura del proyecto

- [Locators](Locators) - Locators de los elementos web agrupado en clases por módulos.
- [Configurations](Configurations) - Archivo "config.ini" con la url de la página, username, password e email. Se pueden colocar todas las variables a utilizar en esta hoja.
- [Logs](Logs) - Los logs que se van generando. No se pisan por lo tanto hay que ir limpiando cada tanto.
- [PageObjects](PageObjects) - Por cada módulo se crea una página con clases y métodos. Para ser utilizados con los testcases.
- [Reports](Reports) - Carpeta que contiene el reporte en html. La subcarpeta assets tiene la hoja de estilos .css, por si alguien lo quiere modificar.
- [Screenshots](Screenshots) - Se guardan las imágenes de las pruebas (en los tests donde se configuró).
- [TestCases](TestCases) - Contiene las páginas con los diferentes test, separados por funcionalidades. También se encuentra el archivo "conftest.py" donde se configuran los diferentes navegadores a utilizar, por defecto si no se especifica, se utiliza Chrome.
- [TestData](TestData) - Tiene el archivo LoginData.xlsx, se pueden colocar todas las variables a utilizar en las diferentes hojas. En este archivo está la prueba de login con diferentes usuarios y passwords, más el resultado esperado. Se utiliza con el testcase "test_login_ddt.py".
- [Utilities](Utilities) - Métodos para guardar y genera los logs, métodos para leer el archivo de excel y el método para leer el archivo de "config.ini" que se encuentra en "Configurations".

## Comandos
Este comando corre los test con la etiqueta "Regression", y genera un reporte en html.
```
$ pytest --html=Reports\report.html --capture=tee-sys -m "Regression"
```
O bien si se quiere correr un testcase en particular, por ejemplo el de login:
```
$ pytest --html=Reports\report.html --capture=tee-sys TestCases/test_login.py
```
Para especificar otro navegador ya sea Firefox o Edge:
```
$ pytest --html=Reports\report.html --capture=tee-sys TestCases/test_login.py --brower "firefox"
```
Para correr 3 veces en parelelo el mismo test:
```
$ pytest -n=3 --html=Reports\report.html --capture=tee-sys TestCases/test_login.py
```

