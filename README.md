# Hotel Reservations

Sistema de gestión de reservas para hoteles, desarrollado en Python con interfaz gráfica usando Tkinter y base de datos PostgreSQL.

---

## Requisitos del sistema

- **Python 3.x**
- **PostgreSQL instalado localmente**
- **Librerías Python:**
  - `psycopg2`
  - `tkinter` (incluida en la mayoría de instalaciones Python)
- **Archivo de base de datos**: Debes crear la base de datos y las tablas manualmente (ver más abajo).
- **Archivo CSV**: `People_list.csv` debe estar presente en la raíz del proyecto para gestión de usuarios.

---

## Instalación

### 1. Instalación de dependencias

```bash
pip install psycopg2
```

### 2. Base de datos PostgreSQL

El sistema utiliza una base de datos **local** llamada `proyecto_finalbd`. Debes crearla en tu instancia de PostgreSQL:

```sql
CREATE DATABASE proyecto_finalbd;
```

Luego, crea las siguientes tablas mínimas:

```sql
CREATE TABLE huesped (
    id_huesped VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100),
    nacionalidad VARCHAR(50)
);

CREATE TABLE telefonos_huesped (
    id_huesped VARCHAR(50) REFERENCES huesped(id_huesped),
    telefonos VARCHAR(20)
);
```

**Credenciales por defecto** (puedes cambiarlas en el código fuente si lo deseas):
- Usuario: `postgres`
- Contraseña: `basesdedatos`
- Host: `localhost`
- Puerto: `5432`

### 3. Archivo CSV

Debes tener en la raíz del proyecto el archivo `People_list.csv` con el siguiente formato por defecto para registrar usuarios:

```
nombre_usuario,id,nacionalidad,telefono
```

---

## Ejecución

El archivo principal es **`main.pyw`**:

```bash
python main.pyw
```

Esto abrirá la interfaz gráfica principal del sistema de reservas.

---

## Funcionalidades principales

- Registro y administración de usuarios (clientes).
- Registro y modificación de datos de habitaciones y reservas.
- Gestión de pagos (efectivo y tarjeta).
- Visualización y búsqueda de registros en la interfaz gráfica.
- Persistencia de datos tanto en base de datos como en archivos CSV.

---

## Consideraciones importantes

- **La base de datos no está incluida en el repositorio**: debes crearla y poblarla manualmente.
- **El sistema está diseñado para ejecutarse localmente**, no en la nube.
- **No hay migraciones automáticas** ni scripts de inicialización en este repositorio.
- **Si hay errores de conexión, revisa tus credenciales y la existencia de la base de datos y las tablas.**
- **El entorno debe permitir la ejecución de aplicaciones gráficas Tkinter.**

---

## Contribuir

1. Haz un fork del repositorio.
2. Crea una rama con tus cambios.
3. Haz un pull request explicando tu aportación.

---

## Autor

- Wendy Cardenas (@WENDY132310)

---
