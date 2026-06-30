# Notas de aprendizaje

## Fase 1: Dataset simulado

### Conceptos nuevos
- Dataset
- CSV
- Datos crudos
- Datos limpios
- Inconsistencias
- Homologacion de nombres
- Calidad de datos

### Errores intencionales incluidos
- Textos con mayusculas/minusculas mezcladas.
- Espacios extras.
- Fechas invalidas.
- Monedas escritas de varias formas.
- Productos duplicados.
- Proveedores duplicados.
- Valores nulos.
- Cantidades negativas.
- IDs inexistentes

## Fase 2: ETL con pandas

### Conceptos nuevos
- ETL: Extract, Transform, Load.
- Dataframe.
- Limpieza de datos
- Normalizacion de texto.
- Conversion de tipos.
- Manejo de valores nulos.
- Exportacion de CSV procesados

### Funciones usadas
- pd.read_csv()
- pd.to_datetume()
- pd.to_numeric()
- df.copy()
- df.drop_duplicates()
- df.to_csv()