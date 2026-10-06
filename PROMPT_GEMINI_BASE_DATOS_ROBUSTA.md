# PROMPT PARA GEMINI - Generación de Base de Datos Robusta para Instituto Educativo

## Objetivo
Generar un conjunto de datos realistas y coherentes de aproximadamente 150 alumnos para un instituto educativo de cursos de Microsoft Excel, incluyendo inscripciones, pagos de cuotas, gastos operacionales, sueldos de docentes e ingresos.

---

## PROMPT COMPLETO PARA GEMINI

```
Eres un experto en generación de datos sintéticos realistas para sistemas de gestión educativa.
Tu tarea es generar una base de datos completa y coherente en formato JSON para un instituto 
educativo especializado en cursos de Microsoft Excel.

REQUISITOS GENERALES:
- Genera datos para EXACTAMENTE 150 alumnos
- Todos los datos deben ser realistas y coherentes entre sí
- Las fechas deben ser consistentes (usa enero 2024 a octubre 2025 como rango)
- Los identificadores deben ser únicos y con formato profesional
- Incluye diversos estados: activos, inactivos, con morosidad, al día, etc.
- Argentina es el país base (usar DNIs argentinos válidos, ciudades, teléfonos locales)

ESTRUCTURA REQUERIDA (JSON):

{
  "alumnos": [
    {
      "id_alumno": "A001",
      "nombre_apellido": "Ana María García López",
      "dni": "30111222",
      "fecha_nacimiento": "2002-05-10",
      "telefono": "1166554433",
      "email": "ana.garcia@gmail.com",
      "direccion": "Av. Siempre Viva 123",
      "localidad": "Córdoba",
      "provincia": "Córdoba",
      "fecha_alta": "2024-01-15",
      "estado": "Activo",
      "observaciones": "Cliente regular"
    },
    ...
  ],
  
  "docentes": [
    {
      "id_docente": "D001",
      "nombre_apellido": "Carlos Andrés Mendoza",
      "dni": "23111222",
      "especialidad": "Excel Básico",
      "telefono": "1144556677",
      "email": "carlos.mendoza@instituto.edu.ar",
      "fecha_contratacion": "2022-03-01",
      "salario_base": 85000
    },
    ...
  ],
  
  "cursos": [
    {
      "id_curso": "C001",
      "nombre_curso": "Excel Básico",
      "categoria": "Ofimática",
      "duracion_semanas": 8,
      "fecha_inicio": "2025-03-01",
      "fecha_finalizacion": "2025-04-26",
      "modalidad": "Presencial",
      "id_docente": "D001",
      "cupo_maximo": 20,
      "arancel_total": 4500,
      "descripcion": "Curso introductorio de Excel"
    },
    ...
  ],
  
  "inscripciones": [
    {
      "id_inscripcion": "I001",
      "id_alumno": "A001",
      "id_curso": "C001",
      "fecha_inscripcion": "2024-01-18",
      "estado": "Confirmada",
      "cantidad_cuotas": 3
    },
    ...
  ],
  
  "plan_de_cuotas": [
    {
      "id_cuota": "CU001",
      "id_alumno": "A001",
      "id_curso": "C001",
      "numero_cuota": 1,
      "fecha_vencimiento": "2025-01-15",
      "importe_base": 1500,
      "fecha_pago": "2025-01-12",
      "estado": "Pagada"
    },
    ...
  ],
  
  "pagos": [
    {
      "id_pago": "P001",
      "id_alumno": "A001",
      "id_curso": "C001",
      "id_cuota": "CU001",
      "fecha_pago": "2025-01-12",
      "importe_abonado": 1500,
      "medio_pago": "Transferencia",
      "numero_comprobante": "REC-001"
    },
    ...
  ],
  
  "gastos_operacionales": [
    {
      "id_gasto": "G001",
      "fecha": "2024-01-05",
      "categoria": "Alquiler",
      "descripcion": "Alquiler de oficinas - enero 2024",
      "importe": 15000,
      "proveedor": "Propietario del inmueble",
      "estado_pago": "Pagado"
    },
    ...
  ],
  
  "ingresos": [
    {
      "id_ingreso": "ING001",
      "fecha": "2025-01-15",
      "tipo": "Cuota de alumno",
      "descripcion": "Pago de cuota CU001",
      "importe": 1500,
      "origen": "Alumno A001",
      "medio": "Transferencia"
    },
    ...
  ],
  
  "sueldos_docentes": [
    {
      "id_sueldo": "S001",
      "id_docente": "D001",
      "mes": "2024-01",
      "salario_base": 85000,
      "bonificacion": 5000,
      "descuentos": 8500,
      "salario_neto": 81500,
      "fecha_pago": "2024-01-31"
    },
    ...
  ]
}

INSTRUCCIONES DETALLADAS:

### 1. ALUMNOS (150 registros)
- Genera nombres variados con apellidos argentinos comunes
- DNI: Usa números válidos en rango 20000000 a 45000000
- Teléfono: Formato 11XXXXXXXX, 221XXXXXXX, 261XXXXXXX (códigos de área reales)
- Email: Usar combinaciones de nombre_apellido@gmail.com, @hotmail.com, @yahoo.com, @outlook.com
- Localidades: Distribuir entre Buenos Aires, AMBA, Córdoba, Rosario, Mendoza, La Plata, Salta, Tucumán
- Fecha de alta: Entre 2023-06-01 y 2025-09-30
- Estado: 70% Activo, 20% Inactivo, 10% Suspendido
- Observaciones: Variar (Cliente regular, Derivación de colega, Publicidad online, etc.)

### 2. DOCENTES (4-6 docentes)
- Nombres realistas con especialidades en Excel/BI
- Especialidades: Excel Básico, Excel Intermedio, Power Query, Dashboardes, BI, Automatización
- Salarios base: Entre 75,000 y 120,000 pesos argentinos
- Fechas de contratación: Variadas desde 2022

### 3. CURSOS (6-10 cursos)
- Categorías: Ofimática, Business Intelligence, Automatización, Reporting
- Modalidades: Presencial, Virtual, Híbrido (distribuir)
- Aranceles: Entre 3500 y 10000 pesos (según duración y modalidad)
- Fechas: Distribuir en 2025 (inicio y fin realistas)
- Cupos: Entre 10 y 25 alumnos

### 4. INSCRIPCIONES (150+ registros, ya que algunos alumnos se inscriben en 2 cursos)
- Cada alumno debe tener al menos 1 inscripción
- Algunos alumnos (15-20%) pueden estar inscriptos en 2 cursos
- Estados: 85% Confirmada, 10% Pendiente, 5% Cancelada
- Cantidad de cuotas: 2, 3 o 4 dependiendo del arancel

### 5. PLAN DE CUOTAS (250-300 registros)
IMPORTANTE: La coherencia es crítica aquí.
- Cada inscripción genera N cuotas (según cantidad_cuotas)
- Fechas de vencimiento: Mensuales, comenzando 15 días después de inscripción
- Importes base: Total arancel / cantidad de cuotas
- Fechas de pago: 
  * 60% de cuotas pagadas ANTES del vencimiento
  * 20% de cuotas pagadas DESPUÉS del vencimiento (atraso 5-25 días)
  * 20% de cuotas SIN PAGO (dejar null/vacío)
- Estados: Calcular dinámicamente (Pagada si tiene fecha_pago, Vencida si HOY > vencimiento sin pago, Pendiente)

### 6. PAGOS (200-250 registros)
- UN PAGO por cuota pagada
- Los importes deben ser EXACTAMENTE iguales al importe_base de la cuota
- Medios de pago: Transferencia (45%), Efectivo (25%), Tarjeta (20%), Débito (10%)
- Número de comprobante: Secuencial (REC-001, REC-002, etc.)
- RELACIÓN CRÍTICA: Para cada fila en PAGOS, debe existir una cuota correspondiente con fecha_pago

### 7. GASTOS OPERACIONALES (60-80 registros)
Distribuir por categorías y períodos:
- Alquiler: 15,000-18,000/mes (12 meses = 180,000-216,000 total)
- Servicios (luz, agua, internet): 3,000-5,000/mes
- Suministros y materiales: 2,000-3,000/mes
- Seguros: 8,000-12,000/trimestre
- Publicidad y marketing: 5,000-8,000/mes
- Mantenimiento y reparaciones: 1,000-2,000/mes (ocasional)
- Impuestos y contribuciones: 20,000/bimestre
- Total de gastos anuales: Aproximadamente 350,000-450,000 pesos

Estados de pago: 90% Pagado, 10% Pendiente

### 8. INGRESOS (200-250 registros)
- El 80-85% debe provenir de cuotas de alumnos
- El 5-10% de otros ingresos (consultoría, material, certificados)
- Cada pago registrado en PAGOS genera un ingreso en esta tabla
- Deben coincidir los montos y fechas
- Medios: Transferencia (50%), Efectivo (30%), Tarjeta (15%), Débito (5%)

### 9. SUELDOS DOCENTES (48-72 registros)
- Un registro POR DOCENTE POR MES (12 meses × cantidad de docentes)
- Meses: 2024-01 a 2025-09
- Bonificación: 0-10% del salario base (variable según desempeño)
- Descuentos: 10% del salario base (aportes, impuestos)
- Salario neto: Salario base + bonificación - descuentos
- Fecha de pago: Último día hábil del mes
- Total de sueldos (9 meses × 5 docentes aprox): 3,825,000-4,500,000 pesos

CRITERIOS DE COHERENCIA:

1. RELACIONES ENTRE TABLAS:
   - Cada ID Alumno en inscripciones debe existir en alumnos
   - Cada ID Curso en inscripciones debe existir en cursos
   - Cada ID Cuota en pagos debe existir en plan_de_cuotas
   - Cada ID Docente en cursos debe existir en docentes
   - Cada pago en PAGOS debe reflejar una cuota en PLAN DE CUOTAS

2. LÓGICA FINANCIERA:
   - Total de INGRESOS debe ser aproximadamente 55-70% del total de ARANCELES FACTURADOS
     (porque 20-30% de cuotas no se pagan)
   - Total de GASTOS + SUELDOS + INGRESOS debe cuadrar de forma realista
   - Margen operacional: INGRESOS - GASTOS - SUELDOS debe ser 10-20% (ganancia)

3. FECHAS:
   - Todas las fechas deben ser lógicas y progresivas
   - Fecha de pago nunca anterior a fecha de inscripción
   - Fecha de cuota coherente con fecha de inscripción

4. DIVERSIDAD:
   - Variar patrones de pago (a tiempo, atrasados, sin pagar)
   - Variar estados de alumnos (activos, inactivos, suspendidos)
   - Variar tipos de cursos, modalidades y precios
   - Distribuir geográficamente en varias provincias
   - Usar diferentes géneros en nombres
   - Incluir casos excepcionales (impagos recientes, morosos, cancelaciones)

FORMATO DE SALIDA:

Por favor, genera el JSON completo, válido y bien formateado.
Incluye exactamente:
- 150 alumnos
- 5 docentes
- 8 cursos
- 160-180 inscripciones
- 280-320 cuotas
- 200-240 pagos
- 70 gastos operacionales
- 200-240 ingresos
- 45 sueldos docentes (5 docentes × 9 meses)

Verifica que:
✓ No haya duplicados en IDs
✓ Las relaciones foráneas sean coherentes
✓ Los montos cuadren
✓ Las fechas sean lógicas
✓ La diversidad de datos sea alta
✓ El JSON sea válido y parseable

¡Comienza la generación!
```

---

## INSTRUCCIONES DE USO

### Paso 1: Copiar el Prompt
Copia el prompt completo (la sección entre los backticks ```) a Gemini o a tu interfaz de ChatGPT/Claude.

### Paso 2: Especificar el Formato
Si Gemini genera el JSON en bloques de código, pide que:
- Lo divida en archivos separados si es muy largo
- Lo formatee de forma válida sin truncar
- Lo proporcione en bloques descargables

### Paso 3: Integración con Python
Una vez que tengas el JSON, guárdalo como `datos_instituto_robusto.json` y crea un script Python que:

```python
import json
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

# Cargar datos del JSON
with open('datos_instituto_robusto.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Crear Excel desde los datos JSON
wb = Workbook()

# Cada tabla en su propia hoja
for tabla_nombre, registros in datos.items():
    if registros:
        ws = wb.create_sheet(tabla_nombre.upper())
        
        # Encabezados
        headers = list(registros[0].keys())
        ws.append(headers)
        
        # Datos
        for registro in registros:
            ws.append([registro.get(h, "") for h in headers])
        
        # Tabla estructurada
        tabla = Table(displayName=f"Tabla_{tabla_nombre}", ref=f"A1:{chr(64+len(headers))}{len(registros)+1}")
        tabla.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2")
        ws.add_table(tabla)

wb.save("Sistema_Instituto_Datos_Robusto.xlsx")
print("Archivo Excel generado con éxito!")
```

---

## VARIACIONES DEL PROMPT (Según tu necesidad)

### Opción A: Si quieres más Morosidad
Reemplaza en la sección Plan de Cuotas:
```
"Fechas de pago: 
  * 40% de cuotas pagadas ANTES del vencimiento
  * 30% de cuotas pagadas DESPUÉS del vencimiento (atraso 10-60 días)
  * 30% de cuotas SIN PAGO"
```

### Opción B: Si quieres menos Gastos
Reemplaza en Gastos Operacionales:
```
Total de gastos anuales: Aproximadamente 250,000-300,000 pesos
```

### Opción C: Si quieres más Ingresos Secundarios
Reemplaza en Ingresos:
```
- El 70% debe provenir de cuotas de alumnos
- El 15% de otros ingresos (consultoría, material, certificados, talleres extra)
- El 15% de donaciones/subsidios
```

---

## VALIDACIÓN DE DATOS

Una vez generado el JSON, valida que:

1. **Unicidad de IDs**
   ```sql
   - Cada A001, A002... debe aparecer solo una vez en alumnos
   - Cada CU001, CU002... debe aparecer solo una vez en plan_de_cuotas
   - Cada P001, P002... debe aparecer solo una vez en pagos
   ```

2. **Coherencia de Montos**
   ```
   - Suma de cuotas = Arancel total del curso
   - Suma de pagos = Suma de ingresos de tipo "Cuota de alumno"
   - Total ingresos - Total gastos - Total sueldos = Ganancia neta
   ```

3. **Consistencia de Fechas**
   ```
   - fecha_pago >= fecha_inscripcion
   - fecha_vencimiento >= fecha_inscripcion + 15 días
   - fecha_pago <= fecha_vencimiento + 60 días (máximo atraso realista)
   ```

---

## PRÓXIMOS PASOS

1. **Copia el prompt a Gemini** y espera la generación
2. **Guarda el JSON** con el nombre `datos_instituto_robusto.json`
3. **Ejecuta el script Python** proporcionado arriba
4. **Abre el Excel** y verifica que todo esté correcto
5. **Aplica fórmulas** desde el script anterior de `generar_sistema_excel_avanzado.py`

---

## PREGUNTAS ADICIONALES PARA GEMINI (Opcionales)

Si necesitas ajustes, puedes hacer preguntas como:

- "¿Cuál es el total de ingresos vs gastos? ¿Cuál es la ganancia neta?"
- "¿Cuántos alumnos tienen deuda? ¿Cuál es la tasa de morosidad?"
- "¿Cuál es el promedio de pago de cuotas?"
- "¿Qué docente tiene más alumnos?"
- "¿Cuál es el mes con más ingresos?"

---

Espero que este prompt te sea de gran utilidad. ¡Adelante!
