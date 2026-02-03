import fitz
import os
import shutil


def organizar_archivos_ocr(ruta_origen):
    carpeta_ocr = "./ocr_books"

    if not os.path.exists(carpeta_ocr):
        os.makedirs(carpeta_ocr)

    archivos = [f for f in os.listdir(ruta_origen) if f.endswith('.pdf')]
    movidos = 0

    for archivo in archivos:
        ruta_completa = os.path.join(ruta_origen, archivo)
        doc = fitz.open(ruta_completa)

        texto_acumulado = ""
        for i, pagina in enumerate(doc):
            if i >= 10: break
            texto_acumulado += pagina.get_text()
            if len(texto_acumulado.strip()) > 50: break
        doc.close()

        if len(texto_acumulado.strip()) < 20:
            ruta_destino = os.path.join(carpeta_ocr, archivo)
            shutil.move(ruta_completa, ruta_destino)
            movidos += 1
            print(f"Movido: {archivo}")

    return movidos


# --- Ejecución ---
ruta_books = "./clean_books"
total_movidos = organizar_archivos_ocr(ruta_books)

print(f"\nProceso terminado.")
print(f"Se movieron {total_movidos} archivos a la carpeta 'ocr_books'.")
print(f"En 'clean_books' ahora solo quedan los PDFs con texto directo.")