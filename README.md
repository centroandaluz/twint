# TWINT - Twitter Intelligence Tool
![2](https://i.imgur.com/iaH3s7z.png)
![3](https://i.imgur.com/hVeCrqL.png)

[![PyPI](https://img.shields.io/pypi/v/twint.svg)](https://pypi.org/project/twint/) [![Build Status](https://travis-ci.org/twintproject/twint.svg?branch=master)](https://travis-ci.org/twintproject/twint) [![Python 3.5|3.6](https://img.shields.io/badge/Python-3.5%2F3.6-blue.svg)](https://www.python.org/download/releases/3.0/) [![GitHub license](https://img.shields.io/github/license/haccer/tweep.svg)](https://github.com/haccer/tweep/blob/master/LICENSE)

> Sin autenticación. Sin API. Sin limites.

Twint es una herramienta avanzada de búsqueda de Twitter escrita en Python que permite buscar Tweets de los perfiles de Twitter **sin** usar la API de Twitter.

Twint utiliza los operadores de búsqueda de Twitter para permitirle extraer Tweets de usuarios específicos, eliminar Tweets relacionados con ciertos temas, hashtags y tendencias, u ordenar información * confidencial * de Tweets como el correo electrónico y los números de teléfono. Es muy útil, y da mucho lugar para la creatividad.

Twint también realiza consultas especiales a Twitter, lo que le permite también buscar los seguidores de un usuario de Twitter, los Tweets que le han gustado a un usuario y a quién sigue **sin** ninguna autenticación, API, Selenium o emulación de navegador.

## Beneficios
Algunos de los beneficios de usar Twint vs Twitter API:
- Puede obtener casi __todos los Tweets (los límites de la API de Twitter son solo para los últimos 3200 Tweets);
- Configuración inicial rápida;
- Se puede utilizar de forma anónima y sin registrarse en Twitter;
- **Sin limitaciones de tarifas**.

## Límites impuestos por Twitter
Twitter limita los desplazamientos mientras navega por la el perfil del usuario. Esto significa que con `.Profile` o con` .Favorites` podrás obtener ~ 3200 tweets.

## Requisitos
- Python 3.6;
- aiohttp;
- aiodns;
- beautifulsoup4;
- cchardet;
- elasticsearch;
- pysocks;
- pandas (>=0.23.0);
- aiohttp_socks;
- schedule;
- geopy;
- fake-useragent.

## Instalación

**Git:**
```bash
git clone https://github.com/twintproject/twint.git
pip3 install -r requirements.txt
```

**Pip:**
```bash
pip3 install twint
```

ó

```bash
pip3 install --user --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint
```

**Pipenv**:
```bash
pipenv install -e git+https://github.com/twintproject/twint.git#egg=twint
```
CLI Ejemplos básicos y combos
Algunos ejemplos simples para ayudarlo a comprender los conceptos básicos:

- `twint -u username` - Elimine todos los Tweets de la línea de tiempo de * user *.
- `twint -u username -s pineapple` - Elimine todos los Tweets de la línea de tiempo del * usuario * que contenga _pineapple_.
- `twint -s pineapple` - Recoge cada Tweet que contenga * pineapple * de los Tweets de todos.
- `twint -u username --year 2014` - Recopila tweets que fueron tuiteados ** antes de ** 2014.
- `twint -u username --desde 2015-12-20` - Recopila tweets que se tuitearon desde 2015-12-20.
- `twint -u username -o file.txt` - Raspe los Tweets y guárdelos en file.txt.
- `twint -u username -o file.csv --csv` - Raspe los Tweets y guárdelos como un archivo csv.
- `twint -u username --email --phone` - Muestra Tweets que pueden tener números de teléfono o direcciones de correo electrónico.
- `twint -s" Donald Trump "--verified` - Muestra tweets de usuarios verificados que tuitearon sobre Donald Trump.
- `twint -g =" 48.880048,2.385939,1km "-o file.csv --csv` - Raspe Tweets desde un radio de 1 km alrededor de un lugar en París y expórtelos a un archivo csv.
- `twint -u username -es localhost: 9200` - Salida de Tweets a Elasticsearch
- `twint -u username -o file.json --json` - Raspe los Tweets y guárdelos como un archivo json.
- `twint -u username --database tweets.db` - Guarda Tweets en una base de datos SQLite.
- `twint -u username --followers` - Raspe a los seguidores de un usuario de Twitter.
- `twint -u username --siguiendo` - Raspe a quien sigue un usuario de Twitter.
- `twint -u username --favorites` - Recopila todos los Tweets que un usuario ha favorecido (reúne ~ 3200 tweet).
- `twint -u username --siguiendo --user-full` - Recopila información completa del usuario que una persona sigue
- `twint -u username --profile-full` - Use un método lento pero efectivo para recopilar Tweets del perfil de un usuario (Recolecta ~ 3200 Tweets, Incluidos Retweets).
- `twint -u username --retweets` - Use un método rápido para reunir los últimos 900 Tweets (que incluyen retweets) del perfil de un usuario.
- `twint -u username --resume resume_file.txt` - Reanuda una búsqueda comenzando desde la última ID de desplazamiento guardada.

Más detalles sobre los comandos y opciones se encuentran en el [wiki] (https://github.com/twintproject/twint/wiki/Commands)

## Ejemplo de módulo

Twint ahora se puede usar como módulo y es compatible con el formato personalizado. ** Más detalles se encuentran en la [wiki] (https://github.com/twintproject/twint/wiki/Module) **

```python
import twint

# Configure
c = twint.Config()
c.Username = "noneprivacy"
c.Search = "#osint"
c.Format = "Tweet id: {id} | Tweet: {tweet}"

# Run
twint.run.Search(c)
```
> Salida

`955511208597184512 2018-01-22 18:43:19 GMT <now> pineapples are the best fruit`

```python
import twint

c = twint.Config()

c.Username = "noneprivacy"
c.Custom["tweet"] = ["id"]
c.Custom["user"] = ["bio"]
c.Limit = 10
c.Store_csv = True
c.Output = "none"

twint.run.Search(c)
```

## Opciones de almacenamiento
- Escribir en el archivo;
- CSV;
- JSON
- SQLite;
- Elasticsearch.

## Configuración de Elasticsearch

Los detalles sobre la configuración de Elasticsearch con Twint se encuentran en [wiki] (https://github.com/twintproject/twint/wiki/Elasticsearch).

## Visualización gráfica
! [gráfico] (https://i.imgur.com/EEJqB8n.png)

Los detalles de [Gráfico] (https://github.com/twintproject/twint/wiki/Graph) también se encuentran en el [wiki] (https://github.com/twintproject/twint/wiki/Graph).

Estamos desarrollando una aplicación de escritorio Twint.

! [4] (https://i.imgur.com/DzcfIgL.png)

## PREGUNTAS MÁS FRECUENTES
> Intenté quitarle tweets a un usuario, sé que existen pero no los entiendo

Twitter puede prohibir las cuentas, lo que significa que sus tweets no estarán disponibles a través de la búsqueda. Para resolver esto, pase `--profile-full` si está usando Twint a través de CLI o, si está usando Twint como módulo, agregue` config.Profile_full = True`. Tenga en cuenta que este proceso será bastante lento.
## Más ejemplos

#### Seguidores Siguiendo

> Para obtener solo nombres de usuario seguidor / siguientes nombres de usuario

`twint -u username --followers`

`twint -u username --following`

> Para obtener información del usuario de seguidores / usuarios siguientes

`twint -u username --followers --user-full`

`twint -u username --following --user-full`

#### Lista de usuarios

> Para obtener solo la información del usuario

`twint -u username --user-full`

> Para obtener información de los usuarios de una lista de usuarios

`twint --userlist inputlist --user-full`

## Publicaciones de blog destacadas:
- https://pielco11.ovh/posts/twint-osint/
- https://null-byte.wonderhowto.com/how-to/mine-twitter-for-targeted-information-with-twint-0193853/
- https://towardsdatascience.com/analyzing-tweets-with-nlp-in-minutes-with-spark-optimus-and-twint-a0c96084995f
