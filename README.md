# Juego Pokémon

Programa que a partir de un csv con información sobre diferentes pokémon permite 

1. Ver la lista completa de pokémons
2. Ver la "tarjeta" de cada pokémon donde se incluye su información general
3. Agregar pokémons nuevos
4. Modificar pokémons existentes
5. Eliminar pokémons
6. Simular batallas basadas en las características de los pokémon (cuyas reglas se listan más adelante)

# Estructura del proyecto

├── data/

│   └── pokemon.csv              # CSV con la información de los pokémon

├── battle_system.py             # Lógica de las batallas

├── main.py                      # Archivo principal para la ejecución del programa

├── pokemon.py                   # Archivo para gestionar la información de cada pokémon

├── requirements.txt             # Dependencias requeridas

└── README.md                    # Información del proyecto

# Reglas de las batallas

Lógica de cada batalla

1. Duración: Las batallas son por turnos, uno tras otro.
2. Objetivo: Reducir el HP del pokémon rival a 0.
3. Victoria: El último pokémon en pie (HP>0) gana.

Lógica de los turnos

1. Primero ataca el pokémon con mayor velocidad
2. Cada pokémon ataca una vez por turno

Tipos de pokémon comunes

Fuego, Agua, Planta, Eléctrico, Lucha, Psíquico, Fantasma, Dragón

Efectividad (casos donde el ataque se duplica o reduce dependiendo de los tipos)

    Super efectivo (x2 daño):

        * Fuego > Planta
        * Agua > Fuego
        * Planta > Agua
        * Eléctrico > Agua


    Poco efectivo (x0.5 daño):

        * Fuego > Agua
        * Agua > Planta
        * Planta > Fuego

    Normal (1x daño):

        * Todos los demás casos

Características que se tuvieron en cuenta:

    1. Ataque: Daño base de los ataques
    2. Defensa: Reduce el daño recibido
    3. Velocidad: Determina quién ataca primero
    4. HP: Puntos de vida

# Como ejecutar el programa

1. Clone el proyecto
2. Vaya a la carpeta del proyecto en VS Code
3. Corra en la terminal bash el comando:  "pip install -e ." sin las comillas. Esto instala el proyecto como un paquete de python e instala las dependencias.
4. Ejecute el archivo main.py

En consolo se mostrará el menú del juego:

==================================================
          SISTEMA DE BATALLAS POKÉMON
==================================================
1. Ver lista de Pokémon
2. Ver detalles de un Pokémon
3. Agregar Pokémon
4. Modificar Pokémon
5. Eliminar Pokémon
6. Batalla
7. Salir

