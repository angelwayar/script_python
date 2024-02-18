# Upload Excel to mongoDB

## Crear venv

para crear un entorno virtual `python -m venv venv`

## Acceder al entorno

### WINDOWS

para activar el entorno virtual (En este caso si la carpeta se encuentra en el root)

```text
cd venv
cd Scripts
activate
```

para salir del entorno virtual `deactivate`

### LINUX/MAC

para activar el entorno virtual

```text
 source "direccion del entorno (donde se encuentra el activate)"
```

### Instalando dependencias

Para instalar requirements

```text
pip install -r requirements.txt
```

### Agregar configuraciones

Reemplazar `<<Cadena de CNX>>` agregar la cadena de conexión.

Reemplazar `<<Colección>>` agregar el nombre de la colección.

Reemplazar `<<Excel>>` agregar el nombre del archivo Excel, con su extensión `.xlsx`.
