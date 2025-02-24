# Script de Extracción de Información de Facturas PDF

Este script tiene como objetivo procesar archivos PDF de facturas, extraer información relevante y almacenarla en una base de datos SQLite.

## Dependencias

- Python 3.x
- PyPDF2
- SQLite3

## Instalación

1. Clona o descarga el repositorio en tu máquina local.
2. (OPCIONAL)   
    **Windows**
    ```
    cd inserte-ubicación-del-script
    python -m venv entornoScript
    source entornoScript/Scripts/activate
    ```
    
    **Unix o MacOs**
   
    ```sh directorio del script
    python -m venv entornoScript      
    source entornoScript/bin/activate
    ```
4. Instala las dependencias necesarias:
    ```
    pip install -r inserte-ubicación-del-script/requirements.txt
    ```

## Ejecución

```
python ubicación-del-script/script.py
```

## Lectura de datos
```
python ubicación-del-script/read.py
```
