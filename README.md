# Bookings_Test_Falabella

API RESt capaz de gestionar reservas de hoteles

Para la ejecución del servidor web backend construido en flask:

1. Creacion de un ambiente virutal

    ```bash
    ~/Bookings$ python3 -m venv env
    ```

2. Activar el ambiete virtual

    Linux:

    ```bash
    ~/Bookings$ source env/bin/activate
    ```

    Windows:

    ```powershell
    ~/Bookings$ env\Scripts\activate.bat
    ```

3. Intalar todos los paquetes de python

    ```bash
    (env) ~/Bookings$ pip install -r requirements.txt
    ```

4. configurar el archivo de arranque del servidor web

    Linux:

    ```bash
    (env) ~/Bookings$ export FLASK_APP=Bookings.py
    ```

    Windows:

    ```powershell
    (env) ~/Bookings$ set FLASK_APP=Bookings.py
    ```

    4.1 (opcional) iniciar en modo debug o de desarrollo

    Linux:

    ```bash
    (env) ~/Bookings$ export FLASK_ENV=development
    ```

    Windows:

    ```powershell
    (env) ~/Bookings$ set FLASK_ENV=development
    ```

5. correr la aplicacion

    ```bash
    (env) ~/Bookings$ flask run
    ```

    Si se desea correr con una direccion ip diferente a la de local host:

    ```bash
    (env) ~/Bookings$ flask run -h <0.0.0.0>
    ```