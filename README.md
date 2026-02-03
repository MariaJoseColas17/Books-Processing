# Books-Processing

Este repositorio contiene los **pipelines de procesamiento** para la creación de un corpus lingüístico basado en 136 libros dominicanos de libre acceso. El objetivo es facilitar el análisis de datos (NLP) sobre el dialecto y la literatura regional.

## Requisitos del Sistema
Para ejecutar los scripts de extracción y OCR, es necesario instalar las siguientes dependencias de sistema:

1. **Poppler:** Motor de renderizado necesario para la conversión de PDF a imagen.
2. **Tesseract OCR (v5.0+):** Motor de reconocimiento de caracteres. Se recomienda instalar el paquete de lenguaje español (`spa`).
3. **Python 3.10+:** Con las siguientes librerías:
   - `pdfplumber` (Extracción de texto digital)
   - `pytesseract` (Wrapper de OCR)
   - `pdf2image` (Interfaz para Poppler)

## Estructura del Proyecto
El pipeline organiza la salida de datos de la siguiente manera:

* `clean_txts/`: Resultados de la extracción directa de PDFs digitales (ID 001-112).
* `ocr_txts/`: Resultados del procesamiento de libros escaneados (ID 113-136).
* `metadata_final.jsonl`: Archivo maestro en formato JSONL que indexa el corpus completo, incluyendo conteo de palabras, páginas, método de extracción utilizado, entre otros.

## Proceso de Extracción
El framework de procesamiento se divide en dos flujos optimizados:

### 1. Extracción Directa
Diseñada para documentos con capa de texto nativa. Utiliza parámetros de tolerancia espacial para reconstruir oraciones y párrafos, evitando el ruido por saltos de línea incorrectos.

### 2. Pipeline de OCR (Vision Artificial)
Para documentos históricos o escaneos sin capa de texto, se utiliza un proceso de:
- Conversión a imagen a **300 DPI**.
- Reconocimiento óptico mediante el motor Tesseract configurado para el idioma español.
- Preservación de caracteres especiales (ñ, á, é, í, ó, ú).

---
*Desarrollado para el análisis del dialecto dominicano y procesamiento de lenguaje natural.*
