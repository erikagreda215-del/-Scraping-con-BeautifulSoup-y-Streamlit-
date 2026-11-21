# Práctica de Web Scraping con BeautifulSoup y Streamlit

Extracción del catálogo completo de [Books to Scrape](https://books.toscrape.com) (1000 libros en 50 categorías) y dashboard interactivo para analizarlo.

## Estructura

```
proyecto_scraping_libros/
├── scraper/
│   └── scraper.py      # Parte 1: scraping con BeautifulSoup y guardado en CSV
├── app/
│   └── app.py          # Parte 2: dashboard con Streamlit
├── data/
│   ├── libros.csv      # información de cada libro (lo genera el scraper)
│   └── precios.csv     # precio de cada libro, se une por "id"
├── requirements.txt    # librerías necesarias
├── .gitignore
└── README.md
```

## Cómo ejecutarlo

```bash
# 1. Crear y activar un entorno virtual (Windows / PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1

# 2. Instalar las librerías
pip install -r requirements.txt

# 3. Parte 1: hacer el scraping (tarda unos 2-3 minutos por las pausas)
python scraper/scraper.py

# 4. Parte 2: abrir el dashboard en el navegador
streamlit run app/app.py
```

## Datos extraídos

| Columna | Tipo | Ejemplo |
|---|---|---|
| id | número | 1 |
| titulo | texto | It's Only the Himalayas |
| categoria | texto | Travel |
| rating | número (1-5) | 2 |
| disponible | booleano | True |
| url_libro / url_portada | texto (URL) | https://books.toscrape.com/... |
| fecha_extraccion | fecha | 2026-11-21 |
| precio (precios.csv) | número decimal | 45.17 |
| moneda (precios.csv) | texto | GBP |

## Ética y buenas prácticas

- **robots.txt**: el scraper lo revisa antes de empezar con `RobotFileParser` y se para si no da permiso.
- **User-Agent propio**: todas las peticiones se identifican como un proyecto educativo.
- **Pausa de 1 segundo** entre peticiones (`time.sleep`) para no saturar el servidor.
- **Web autorizada**: Books to Scrape es una web creada para practicar scraping. No se recogen datos personales.

## Dificultades y cómo se resolvieron

- **El símbolo £ salía como `Â£`**: la web no indica su codificación y `requests` la adivinaba mal. Se fuerza `respuesta.encoding = "utf-8"`.
- **Títulos cortados** (`A Light in the ...`): el texto del enlace está recortado, así que se lee el atributo `title`, que tiene el título completo.
- **La puntuación no es un número**: está en una clase CSS (`star-rating Three`). Se traduce con un diccionario `{"One": 1, ...}`.
- **Las URLs son relativas** (`../../../libro/index.html`): se convierten en absolutas con `urljoin`.
- **La categoría no aparece en el listado general**: por eso se recorre la web categoría por categoría, siguiendo el botón *next* de cada una.

## Conclusiones del análisis

En la pestaña de Streamlit se responde a preguntas como *¿influye el precio en la valoración?*. En este catálogo la correlación entre precio y puntuación es prácticamente nula: los precios y las estrellas de la web son aleatorios, como avisa la propia página.
