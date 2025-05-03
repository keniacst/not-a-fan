# not-a-fan

## Descripción
Esta herramienta analiza tus seguidores de Instagram procesando archivos HTML o JSON de tus listas de seguidores y seguidos. Te ayuda a identificar usuarios que no te siguen de vuelta y genera archivos CSV fáciles de usar con los resultados.

## Características
- Extrae nombres de usuario de Instagram de archivos HTML o JSON
- Compara listas de seguidores y seguidos
- Identifica usuarios que no te siguen de vuelta
- Genera archivos CSV organizados con los resultados
- Soporte para analizar múltiples cuentas especificando diferentes carpetas de entrada
- Detección automática del tipo de archivo (HTML o JSON)

## Requisitos
- Python 3.6 o superior
- Paquetes de Python requeridos:
  - re (biblioteca estándar)
  - csv (biblioteca estándar)
  - os (biblioteca estándar)
  - sys (biblioteca estándar)
  - time (biblioteca estándar)
  - argparse (biblioteca estándar)
  - json (biblioteca estándar)

## Instalación
1. Clona este repositorio o descarga los archivos
2. No se requieren paquetes externos ya que la herramienta solo usa bibliotecas estándar de Python

## Cómo usar

### Paso 1: Obtener tus datos de Instagram
Para obtener tus datos de Instagram, sigue estos pasos:

1. Inicia sesión en Instagram y ve a la configuración de tu cuenta
2. Navega a "Centro de cuentas" y luego selecciona "Tu información y permisos"
3. Haz clic en "Descargar tu información"
4. En el formulario que aparece:
   - Selecciona "Descargar o transferir información"
   - Elige tu cuenta de Instagram
   - Marca "Parte de tu información"
   - Selecciona únicamente "Seguidores y seguidos"
   - Elige "Descargar en dispositivo"
5. En la siguiente pantalla:
   - Para el intervalo de fechas, selecciona "Desde el principio"
   - En formato selecciona "JSON"
   - Haz clic en "Crear archivos"
6. Instagram procesará tu solicitud y te enviará una notificación cuando tus datos estén listos para descargar
7. Descarga y extrae los archivos
8. Busca los archivos "followers_1.html" y "following.html" (formato HTML) o "followers_1.json" y "following.json" (formato JSON)
9. Crea una carpeta llamada "data" en la raíz de este proyecto y coloca tus archivos dentro


### Paso 2: Ejecutar el análisis
Abre una terminal y ejecuta:

```bash
python main.py [carpeta_de_entrada]
```

Por ejemplo:
```bash
python main.py data
```

También puedes especificar una carpeta de salida personalizada:
```bash
python main.py data --output mis_resultados
```

### Paso 3: Ver los resultados
La herramienta generará los siguientes archivos en la carpeta de salida (por defecto: `processed_[carpeta_de_entrada]`):
- `followers.csv`: Lista de todos tus seguidores
- `following.csv`: Lista de todas las cuentas que sigues
- `not_following_back.csv`: Lista de cuentas que no te siguen de vuelta

## Uso avanzado

### Análisis de múltiples cuentas
Puedes analizar diferentes cuentas de Instagram organizando sus archivos HTML o JSON en carpetas separadas:

```bash
python main.py datos_cuenta1
python main.py datos_cuenta2
```

Esto creará carpetas de salida separadas llamadas `processed_datos_cuenta1` y `processed_datos_cuenta2`.

### Detección automática de tipo de archivo
La herramienta detecta automáticamente si tus archivos son HTML o JSON. Solo necesitas asegurarte de que los archivos tengan los nombres correctos:
- Para archivos HTML: `followers_1.html` y `following.html`
- Para archivos JSON: `followers_1.json` y `following.json`

## Opciones de línea de comandos
```
uso: main.py [-h] [--output OUTPUT] [carpeta_de_entrada]

Analizar seguidores de Instagram.

argumentos posicionales:
  carpeta_de_entrada    Carpeta que contiene archivos HTML o JSON (por defecto: data)

argumentos opcionales:
  -h, --help            mostrar este mensaje de ayuda y salir
  --output OUTPUT, -o OUTPUT
                        Carpeta para guardar resultados (por defecto: processed_[carpeta_de_entrada])
```

## Salida
El script mostrará un resumen del análisis en la terminal:
- Número total de seguidores
- Número total de cuentas que sigues
- Número de cuentas que no te siguen de vuelta
- Lista de archivos generados
- Tiempo de ejecución

## Licencia
Este proyecto está disponible para uso personal.

## Aviso legal
Esta herramienta está destinada solo para análisis personal. Por favor, respeta los términos de servicio y políticas de privacidad de Instagram al usar esta herramienta.