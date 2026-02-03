import os
import json
import pytesseract
from pdf2image import convert_from_path

ruta_poppler_bin = r"C:\path\to\poppler\bin"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def procesar_ocr_unificado(ruta_entrada, ruta_salida, inicio_id=113):
    if not os.path.exists(ruta_salida):
        os.makedirs(ruta_salida)

    archivo_jsonl_maestro = "metadata_final.jsonl"
    archivos = [f for f in os.listdir(ruta_entrada) if f.endswith('.pdf')]

    print(f"Iniciando OCR de {len(archivos)} archivos...")

    with open(archivo_jsonl_maestro, 'a', encoding='utf-8') as f_jsonl:
        for i, nombre_pdf in enumerate(archivos, inicio_id):
            id_str = f"{i:03d}"
            ruta_pdf = os.path.join(ruta_entrada, nombre_pdf)
            texto_completo = ""

            print(f"Procesando OCR [{id_str}]: {nombre_pdf}...")

            try:
                paginas_imagenes = convert_from_path(
                    ruta_pdf,
                    dpi=300,
                    poppler_path=ruta_poppler_bin
                )

                for num_pag, imagen in enumerate(paginas_imagenes, 1):
                    texto_pag = pytesseract.image_to_string(imagen, lang='spa')
                    texto_completo += f"\n--- PÁGINA {num_pag} ---\n" + texto_pag

                num_paginas = len(paginas_imagenes)
            except Exception as e:
                print(f"Error crítico en {nombre_pdf}: {e}")
                continue

            nombre_base = nombre_pdf.replace(" ", "_").lower().replace(".pdf", "")
            nombre_txt = f"{id_str}_{nombre_base}.txt"
            ruta_fisica_txt = os.path.join(ruta_salida, nombre_txt)
            ruta_relativa_txt = f"./{ruta_salida}/{nombre_txt}"

            with open(ruta_fisica_txt, 'w', encoding='utf-8') as f_txt:
                f_txt.write(texto_completo)

            palabras = texto_completo.split()
            lineas = texto_completo.splitlines()
            peso = round(os.path.getsize(ruta_pdf) / (1024 * 1024), 2)

            metadata = {
                "id": id_str,
                "nombre_og": nombre_pdf,
                "nombre_out": nombre_txt,
                "local_path": ruta_relativa_txt,
                "paginas": num_paginas,
                "palabras_totales": len(palabras),
                "lineas_totales": len(lineas),
                "peso_mb": peso,
                "metodo_extraccion": "ocr_tesseract_300dpi"
            }

            f_jsonl.write(json.dumps(metadata, ensure_ascii=False) + "\n")
            f_jsonl.flush()
            os.fsync(f_jsonl.fileno())

            print(f"Finalizado [{id_str}]: {nombre_txt}")

if __name__ == "__main__":
    procesar_ocr_unificado("ocr_books", "ocr_txts", inicio_id=113)