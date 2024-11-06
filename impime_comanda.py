# pip install *
import win32print
import requests
import sys

# Verificar si se pasó el argumento
if len(sys.argv) != 2:
    print("Por favor, proporciona el uuid_pedido.")
    sys.exit(1)

# Obtener el argumento
uuid_pedido = sys.argv[1]

# url = 'http://127.0.0.1:8400/imprimir_comanda_solo_text?uuid=55e1-2102-a865'
# url = 'http://127.0.0.1:8400/imprimir_comanda_solo_text?uuid=' + uuid_pedido
url = 'https://admin.tiendabarrios.com/imprimir_comanda_solo_text?uuid=' + uuid_pedido

def get_url_text(url):
    response = requests.get(url)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        content = response.text
        return content
        # print(content)  # Muestra el contenido de la página
    else:
        print(f"Error al obtener la página: {response.status_code}")


# Nombre de la impresora
printer_name = "POS-80C"

# Texto a imprimir, alineado manualmente con espacios y ajustando las tildes
receipt_text = get_url_text(url)

# Configura el dispositivo de impresión
hPrinter = win32print.OpenPrinter(printer_name)
try:
    # Inicia un documento
    hJob = win32print.StartDocPrinter(hPrinter, 1, ("Pedido", None, "RAW"))
    win32print.StartPagePrinter(hPrinter)
    
    # Comando para la máxima intensidad de impresión (escala de 0 a 15)
    # max_darkness_command = bytes([27, 33, 15])  # Asegúrate de que 15 sea el valor máximo en tu impresora
    max_darkness_command = bytes([27, 33, 12])  # Asegúrate de que 15 sea el valor máximo en tu impresora

    # Enviar comando para máxima oscuridad antes de imprimir el texto
    win32print.WritePrinter(hPrinter, max_darkness_command)

    # 0x00: Fuente normal (por defecto).
    # 0x01 - 0x0F: Tamaños de fuente más pequeños.
    # 0x10 - 0x1F: Tamaños de fuente más grandes, pero menos distorsionados que valores más altos.

    # Comando para establecer la fuente más grande (ancho y alto aumentados)
    # large_font_command = bytes([27, 33, 0x11])  # Fuente grande
    large_font_command = bytes([27, 33, 0x06])  # Fuente grande
    # large_font_command = bytes([27, 33, 0x10])  # Fuente grande
    # large_font_command = bytes([27, 33, 0x00])  # Fuente normal
    # large_font_command = bytes([27, 33, 0x01])  # Fuente normal
    win32print.WritePrinter(hPrinter, large_font_command)

    # Comando para alinear texto a la izquierda: ESC a 0
    align_left_command = bytes([27, 97, 0])
    win32print.WritePrinter(hPrinter, align_left_command)
    
    # Envía el texto a la impresora con codificación 'latin-1'
    win32print.WritePrinter(hPrinter, receipt_text.encode("latin-1"))
    
    # Avance de varias líneas para dejar espacio antes del corte
    line_feed_command = bytes([10] * 5)  # Avanza 5 líneas
    
    # Comando de corte de papel
    cut_command = bytes([27, 105])  # ESC i para corte completo
    
    # Enviar avance de línea y luego el comando de corte
    win32print.WritePrinter(hPrinter, line_feed_command)
    win32print.WritePrinter(hPrinter, cut_command)
    
    # Finaliza la página y el documento
    win32print.EndPagePrinter(hPrinter)
    win32print.EndDocPrinter(hPrinter)
finally:
    # Cierra la conexión con la impresora
    win32print.ClosePrinter(hPrinter)
