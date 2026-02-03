import pdfplumber
import os
import json


def procesar_todo_desde_cero(ruta_entrada, ruta_salida):
    if not os.path.exists(ruta_salida):
        os.makedirs(ruta_salida)

    archivos = [f for f in os.listdir(ruta_entrada) if f.endswith('.pdf')]
    archivo_jsonl = "metadata_final.jsonl"

    # Usamos 'w' para asegurar que el archivo empiece limpio cada vez
    with open(archivo_jsonl, 'w', encoding='utf-8') as f_jsonl:
        for i, nombre_pdf in enumerate(archivos, 1):
            id_str = f"{i:03d}"
            ruta_pdf = os.path.join(ruta_entrada, nombre_pdf)
            texto_completo = ""

            try:
                with pdfplumber.open(ruta_pdf) as pdf:
                    for pagina in pdf.pages:
                        texto_pag = pagina.extract_text(x_tolerance=5, y_tolerance=3)
                        if texto_pag:
                            texto_completo += texto_pag + "\n"
                    num_paginas = len(pdf.pages)
            except Exception as e:
                print(f"Error leyendo {nombre_pdf}: {e}")
                continue

            nombre_base = nombre_pdf.replace(" ", "_").lower().replace(".pdf", "")
            nombre_txt = f"{id_str}_{nombre_base}.txt"
            ruta_relativa_txt = f"./{ruta_salida}/{nombre_txt}"
            ruta_fisica_txt = os.path.join(ruta_salida, nombre_txt)

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
                "metodo_extraccion": "digital_directo"

            }

            # --- LA CORRECCIÓN CLAVE AQUÍ ---
            linea_json = json.dumps(metadata, ensure_ascii=False) + "\n"
            f_jsonl.write(linea_json)

            # Estas dos líneas obligan al sistema a guardar los datos AHORA
            f_jsonl.flush()
            os.fsync(f_jsonl.fileno())

            print(f"Escrito en JSONL [{id_str}/{len(archivos)}]: {nombre_txt} | P: {len(palabras)} L: {len(lineas)}")


# --- Ejecución ---
procesar_todo_desde_cero("clean_books", "clean_txts")