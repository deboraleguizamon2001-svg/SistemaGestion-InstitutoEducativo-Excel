"""
Script para cargar JSON y convertir a Excel con Tablas Estructuradas y Fórmulas
Archivo de entrada: datos_instituto_2026.json
Archivo de salida: Sistema_Instituto_Datos_Robusto_2026.xlsx
"""

import json
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter
from datetime import datetime

# ============================================================
# CONFIGURACIÓN
# ============================================================
INPUT_FILE = "datos_instituto_2026.json"
OUTPUT_FILE = "Sistema_Instituto_Datos_Robusto_2026.xlsx"

# ============================================================
# VALIDAR QUE EL ARCHIVO JSON EXISTE
# ============================================================
if not os.path.exists(INPUT_FILE):
    print(f"❌ ERROR: El archivo '{INPUT_FILE}' no existe en el directorio actual.")
    print(f"📁 Por favor, coloca el archivo JSON en: {os.path.abspath(INPUT_FILE)}")
    exit(1)

print(f"✓ Archivo encontrado: {INPUT_FILE}")

# ============================================================
# CARGAR DATOS DEL JSON
# ============================================================
try:
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    print(f"✓ JSON cargado exitosamente")
except json.JSONDecodeError as e:
    print(f"❌ ERROR: El archivo JSON tiene errores de sintaxis: {e}")
    exit(1)
except Exception as e:
    print(f"❌ ERROR al cargar el JSON: {e}")
    exit(1)

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================
def estilo_encabezado(ws):
    """Aplica estilos a la fila de encabezados"""
    fill = PatternFill("solid", fgColor="1F4E78")
    font = Font(color="FFFFFF", bold=True, size=11)
    border = Border(
        left=Side(style="thin", color="D9D9D9"),
        right=Side(style="thin", color="D9D9D9"),
        top=Side(style="thin", color="D9D9D9"),
        bottom=Side(style="thin", color="D9D9D9")
    )
    for cell in ws[1]:
        if cell.value:
            cell.fill = fill
            cell.font = font
            cell.border = border
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

def autoajustar_columnas(ws, start_row=1, end_row=None, start_col=1, end_col=None):
    """Ajusta automáticamente el ancho de las columnas"""
    if end_row is None:
        end_row = ws.max_row
    if end_col is None:
        end_col = ws.max_column
    
    for col in range(start_col, end_col + 1):
        max_len = 0
        for row in range(start_row, end_row + 1):
            cell = ws.cell(row=row, column=col)
            v = cell.value
            text = "" if v is None else str(v)
            max_len = max(max_len, len(text))
        
        width = min(max(max_len + 2, 12), 35)
        ws.column_dimensions[get_column_letter(col)].width = width

def crear_tabla_estructurada(ws, nombre_tabla):
    """Crea una tabla estructurada en la hoja"""
    if ws.max_row > 1:
        ref = f"A1:{get_column_letter(ws.max_column)}{ws.max_row}"
        tabla = Table(displayName=nombre_tabla, ref=ref)
        estilo = TableStyleInfo(
            name="TableStyleMedium2",
            showFirstColumn=False,
            showLastColumn=False,
            showRowStripes=True,
            showColumnStripes=False
        )
        tabla.tableStyleInfo = estilo
        ws.add_table(tabla)

# ============================================================
# CREAR WORKBOOK
# ============================================================
wb = Workbook()
wb.remove(wb.active)  # Eliminar hoja por defecto

# Mapeo de nombres de tablas JSON a nombres de hojas Excel
tabla_mapping = {
    "alumnos": ("ALUMNOS", "Tabla_Alumnos"),
    "docentes": ("DOCENTES", "Tabla_Docentes"),
    "cursos": ("CURSOS", "Tabla_Cursos"),
    "inscripciones": ("INSCRIPCIONES", "Tabla_Inscripciones"),
    "plan_de_cuotas": ("PLAN DE CUOTAS", "Tabla_Cuotas"),
    "pagos": ("PAGOS", "Tabla_Pagos"),
    "gastos_operacionales": ("GASTOS OPERACIONALES", "Tabla_Gastos"),
    "ingresos": ("INGRESOS", "Tabla_Ingresos"),
    "sueldos_docentes": ("SUELDOS DOCENTES", "Tabla_Sueldos")
}

# ============================================================
# PROCESAR CADA TABLA
# ============================================================
for clave_json, (nombre_hoja, nombre_tabla) in tabla_mapping.items():
    if clave_json not in datos:
        print(f"⚠ ADVERTENCIA: La tabla '{clave_json}' no existe en el JSON")
        continue
    
    registros = datos[clave_json]
    
    if not registros:
        print(f"⚠ ADVERTENCIA: La tabla '{clave_json}' está vacía")
        continue
    
    # Crear hoja
    ws = wb.create_sheet(nombre_hoja)
    print(f"✓ Creando hoja: {nombre_hoja} ({len(registros)} registros)")
    
    # Obtener encabezados del primer registro
    headers = list(registros[0].keys())
    ws.append(headers)
    
    # Aplicar estilos a encabezados
    estilo_encabezado(ws)
    
    # Agregar datos
    for registro in registros:
        fila = [registro.get(h, "") for h in headers]
        ws.append(fila)
    
    # Ajustar columnas
    autoajustar_columnas(ws)
    
    # Crear tabla estructurada
    crear_tabla_estructurada(ws, nombre_tabla)
    
    # Congelar primera fila
    ws.freeze_panes = "A2"

# ============================================================
# CREAR HOJA DASHBOARD (OPCIONAL)
# ============================================================
print(f"✓ Creando hoja: DASHBOARD")
ws_dashboard = wb.create_sheet("DASHBOARD", 0)  # Insertar al inicio

ws_dashboard["A1"] = "INDICADORES DEL SISTEMA"
ws_dashboard["A1"].font = Font(bold=True, size=14, color="FFFFFF")
ws_dashboard["A1"].fill = PatternFill("solid", fgColor="1F4E78")
ws_dashboard["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws_dashboard.merge_cells("A1:B1")

# Indicadores básicos
row = 3
indicadores = [
    ("Total Alumnos", f"=COUNTA(Tabla_Alumnos[ID Alumno])"),
    ("Alumnos Activos", f'=CONTAR.SI(Tabla_Alumnos[Estado];"Activo")'),
    ("Docentes", f"=COUNTA(Tabla_Docentes[ID Docente])"),
    ("Cursos", f"=COUNTA(Tabla_Cursos[ID Curso])"),
    ("Total Inscripciones", f"=COUNTA(Tabla_Inscripciones[ID Inscripción])"),
    ("Total Cuotas", f"=COUNTA(Tabla_Cuotas[ID Cuota])"),
    ("Cuotas Pagadas", f'=CONTAR.SI(Tabla_Cuotas[Estado];"Pagada")'),
    ("Cuotas Pendientes", f'=CONTAR.SI(Tabla_Cuotas[Estado];"Pendiente")'),
    ("Cuotas Vencidas", f'=CONTAR.SI(Tabla_Cuotas[Estado];"Vencida")'),
    ("Total Facturado", f"=SUMA(Tabla_Cuotas[Importe Base])"),
    ("Total Cobrado", f"=SUMA(Tabla_Pagos[Importe abonado])"),
    ("Total Gastos", f"=SUMA(Tabla_Gastos[Importe])"),
    ("Total Sueldos", f"=SUMA(Tabla_Sueldos[Salario neto])"),
]

for label, formula in indicadores:
    ws_dashboard[f"A{row}"] = label
    ws_dashboard[f"B{row}"] = formula
    ws_dashboard[f"A{row}"].font = Font(bold=True)
    ws_dashboard[f"B{row}"].number_format = "#,##0.00"
    row += 1

ws_dashboard.column_dimensions["A"].width = 28
ws_dashboard.column_dimensions["B"].width = 20

# ============================================================
# GUARDAR ARCHIVO EXCEL
# ============================================================
try:
    wb.save(OUTPUT_FILE)
    print(f"\n✅ ÉXITO: Archivo Excel creado: {OUTPUT_FILE}")
    print(f"📊 Hojas creadas: {', '.join([ws.title for ws in wb.sheetnames])}")
except Exception as e:
    print(f"❌ ERROR al guardar el archivo: {e}")
    exit(1)

# ============================================================
# RESUMEN DE DATOS
# ============================================================
print("\n" + "="*60)
print("RESUMEN DE DATOS CARGADOS")
print("="*60)

if "alumnos" in datos:
    print(f"👥 Alumnos: {len(datos['alumnos'])}")
if "docentes" in datos:
    print(f"👨‍🏫 Docentes: {len(datos['docentes'])}")
if "cursos" in datos:
    print(f"📚 Cursos: {len(datos['cursos'])}")
if "inscripciones" in datos:
    print(f"📝 Inscripciones: {len(datos['inscripciones'])}")
if "plan_de_cuotas" in datos:
    print(f"💰 Cuotas: {len(datos['plan_de_cuotas'])}")
if "pagos" in datos:
    print(f"✅ Pagos: {len(datos['pagos'])}")
if "gastos_operacionales" in datos:
    print(f"💸 Gastos: {len(datos['gastos_operacionales'])}")
if "ingresos" in datos:
    print(f"📈 Ingresos: {len(datos['ingresos'])}")
if "sueldos_docentes" in datos:
    print(f"💼 Sueldos: {len(datos['sueldos_docentes'])}")

print("="*60)
print("\n✨ El archivo está listo para abrir en Microsoft Excel")
print("📍 Ruta: " + os.path.abspath(OUTPUT_FILE))
