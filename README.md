

# <span style="color:#2E86C1">Dominican Books Dialect Corpus</span>

Este repositorio contiene los **pipelines de procesamiento** para la creación de un corpus lingüístico basado en 136 libros dominicanos de libre acceso. El objetivo es facilitar el análisis de datos (NLP) sobre el dialecto y la literatura regional.

### <span style="color:#D35400">Requisitos del Sistema</span>

Para ejecutar los scripts de extracción y OCR, es necesario instalar las siguientes dependencias de sistema:

1. **Poppler:** Motor de renderizado necesario para la conversión de PDF a imagen.
2. **Tesseract OCR (v5.0+):** Motor de reconocimiento de caracteres. Se recomienda instalar el paquete de lenguaje español (`spa`).
3. **Python 3.10+:** Con las siguientes librerías:
* `pdfplumber` (Extracción de texto digital)
* `pytesseract` (Wrapper de OCR)
* `pdf2image` (Interfaz para Poppler)



### <span style="color:#D35400">Estructura del Proyecto</span>

El pipeline organiza la salida de datos de la siguiente manera:

* **clean_txts/**: Resultados de la extracción directa de PDFs digitales (ID 001-112).
* **ocr_txts/**: Resultados del procesamiento de libros escaneados (ID 113-136).
* **metadata_final.jsonl**: Archivo maestro en formato JSONL que indexa el corpus completo, incluyendo conteo de palabras, páginas y método de extracción utilizado.

### <span style="color:#D35400">Proceso de Extracción</span>

El framework de procesamiento se divide en dos flujos optimizados:

#### <span style="color:#27AE60">1. Extracción Directa</span>

Diseñada para documentos con capa de texto nativa. Utiliza parámetros de tolerancia espacial para reconstruir oraciones y párrafos, evitando el ruido por saltos de línea incorrectos.

#### <span style="color:#27AE60">2. Pipeline de OCR (Visión Artificial)</span>

Para documentos históricos o escaneos sin capa de texto, se utiliza un proceso de:

* Conversión a imagen a **300 DPI**.
* Reconocimiento óptico mediante el motor Tesseract configurado para el idioma español.
* Preservación de caracteres especiales (ñ, á, é, í, ó, ú).

*Desarrollado para el análisis del dialecto dominicano y procesamiento de lenguaje natural.*

