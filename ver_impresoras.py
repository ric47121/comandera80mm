import win32print

# Obtiene todas las impresoras instaladas
printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)

# Imprime la lista de impresoras
for printer in printers:
    print(f"Nombre de la impresora: {printer[2]}")
