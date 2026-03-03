import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Cargar el archivo CSV
df_ecoplas = pd.read_csv(r"c:\Users\Oiden\OneDrive - Universidad Nacional Abierta y a Distancia\Documents\Dataset\ecoplas.csv")

# Mostrar información básica del DataFrame
print("Primeras filas del DataFrame:")
print(df_ecoplas.head())
print("\nInformación del DataFrame:")
print(df_ecoplas.info())

# Limpiar la columna Subtotal (eliminar símbolos $, comas y espacios)
df_ecoplas['Subtotal_limpio'] = df_ecoplas['Subtotal'].astype(str).str.replace('$', '').str.replace(',', '').str.replace(' ', '')
df_ecoplas['Subtotal_limpio'] = pd.to_numeric(df_ecoplas['Subtotal_limpio'], errors='coerce')

# Convertir la columna Fecha a datetime
df_ecoplas['Fecha'] = pd.to_datetime(df_ecoplas['Fecha'], format='%d-%b-%y', errors='coerce')

# Extraer mes y año
df_ecoplas['Mes'] = df_ecoplas['Fecha'].dt.month
df_ecoplas['Año'] = df_ecoplas['Fecha'].dt.year
df_ecoplas['Mes_Año'] = df_ecoplas['Fecha'].dt.to_period('M')

# Agrupar ventas por mes
ventas_por_mes = df_ecoplas.groupby('Mes_Año')['Subtotal_limpio'].sum().reset_index()
ventas_por_mes.columns = ['Mes_Año', 'Total_Ventas']

print("\nVentas por mes:")
print(ventas_por_mes)

# Crear figura con múltiples gráficas
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Análisis de Ventas por Mes - Ecoplas', fontsize=16, fontweight='bold')

# Gráfica 1: Línea de ventas por mes
ax1 = axes[0, 0]
ax1.plot(ventas_por_mes['Mes_Año'].astype(str), ventas_por_mes['Total_Ventas'], 
         marker='o', linewidth=2, markersize=8, color='#2E86AB')
ax1.set_title('Evolución de Ventas Mensuales', fontsize=12, fontweight='bold')
ax1.set_xlabel('Mes', fontsize=10)
ax1.set_ylabel('Total Ventas ($)', fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='x', rotation=45)
for i, v in enumerate(ventas_por_mes['Total_Ventas']):
    ax1.text(i, v, f'${v:,.0f}', ha='center', va='bottom', fontsize=8)

# Gráfica 2: Barras de ventas por mes
ax2 = axes[0, 1]
colors = plt.cm.viridis(np.linspace(0, 1, len(ventas_por_mes)))
bars = ax2.bar(ventas_por_mes['Mes_Año'].astype(str), ventas_por_mes['Total_Ventas'], 
               color=colors, edgecolor='black', linewidth=1.2)
ax2.set_title('Ventas Mensuales (Barras)', fontsize=12, fontweight='bold')
ax2.set_xlabel('Mes', fontsize=10)
ax2.set_ylabel('Total Ventas ($)', fontsize=10)
ax2.tick_params(axis='x', rotation=45)
ax2.grid(axis='y', alpha=0.3)
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'${height:,.0f}', ha='center', va='bottom', fontsize=8)

# Gráfica 3: Cantidad de transacciones por mes
transacciones_por_mes = df_ecoplas.groupby('Mes_Año').size().reset_index(name='Cantidad_Transacciones')
ax3 = axes[1, 0]
ax3.bar(transacciones_por_mes['Mes_Año'].astype(str), transacciones_por_mes['Cantidad_Transacciones'], 
        color='#A23B72', edgecolor='black', linewidth=1.2)
ax3.set_title('Cantidad de Transacciones por Mes', fontsize=12, fontweight='bold')
ax3.set_xlabel('Mes', fontsize=10)
ax3.set_ylabel('Número de Transacciones', fontsize=10)
ax3.tick_params(axis='x', rotation=45)
ax3.grid(axis='y', alpha=0.3)
for i, v in enumerate(transacciones_por_mes['Cantidad_Transacciones']):
    ax3.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

# Gráfica 4: Comparación de ventas y transacciones
ax4 = axes[1, 1]
ax4_twin = ax4.twinx()
line1 = ax4.plot(ventas_por_mes['Mes_Año'].astype(str), ventas_por_mes['Total_Ventas'], 
                 marker='o', linewidth=2, markersize=8, color='#2E86AB', label='Ventas ($)')
line2 = ax4_twin.plot(transacciones_por_mes['Mes_Año'].astype(str), transacciones_por_mes['Cantidad_Transacciones'], 
                      marker='s', linewidth=2, markersize=8, color='#A23B72', label='Transacciones')
ax4.set_title('Ventas vs Transacciones', fontsize=12, fontweight='bold')
ax4.set_xlabel('Mes', fontsize=10)
ax4.set_ylabel('Total Ventas ($)', fontsize=10, color='#2E86AB')
ax4_twin.set_ylabel('Número de Transacciones', fontsize=10, color='#A23B72')
ax4.tick_params(axis='x', rotation=45)
ax4.tick_params(axis='y', labelcolor='#2E86AB')
ax4_twin.tick_params(axis='y', labelcolor='#A23B72')
ax4.grid(True, alpha=0.3)

# Combinar leyendas
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax4.legend(lines, labels, loc='upper left')

plt.tight_layout()
plt.savefig(r"c:\Users\Oiden\OneDrive - Universidad Nacional Abierta y a Distancia\Documents\curso python\ventas_por_mes_ecoplas.png", 
            dpi=300, bbox_inches='tight')
print("\n✓ Gráfica guardada como 'ventas_por_mes_ecoplas.png'")

plt.show()

# Resumen estadístico
print("\n" + "="*60)
print("RESUMEN ESTADÍSTICO DE VENTAS POR MES")
print("="*60)
print(f"Total de ventas: ${ventas_por_mes['Total_Ventas'].sum():,.2f}")
print(f"Promedio mensual: ${ventas_por_mes['Total_Ventas'].mean():,.2f}")
print(f"Mes con mayores ventas: {ventas_por_mes.loc[ventas_por_mes['Total_Ventas'].idxmax(), 'Mes_Año']} - ${ventas_por_mes['Total_Ventas'].max():,.2f}")
print(f"Mes con menores ventas: {ventas_por_mes.loc[ventas_por_mes['Total_Ventas'].idxmin(), 'Mes_Año']} - ${ventas_por_mes['Total_Ventas'].min():,.2f}")
print("="*60)

# ============================================================================
# ANÁLISIS DE LOS 10 PRODUCTOS MÁS VENDIDOS POR MES
# ============================================================================

print("\n" + "="*60)
print("ANÁLISIS DE LOS 10 PRODUCTOS MÁS VENDIDOS")
print("="*60)

# Obtener la lista de meses únicos
meses_unicos = df_ecoplas['Mes_Año'].dropna().unique()
meses_unicos = sorted([m for m in meses_unicos])

# Crear una figura grande con subgráficas para cada mes
num_meses = len(meses_unicos)
filas = (num_meses + 1) // 2  # Redondear hacia arriba
columnas = 2

fig2, axes2 = plt.subplots(filas, columnas, figsize=(20, 6*filas))
fig2.suptitle('Top 10 Productos Más Vendidos por Mes - Ecoplas', fontsize=18, fontweight='bold', y=0.995)

# Aplanar axes2 para iterar fácilmente
if num_meses > 1:
    axes2 = axes2.flatten()
else:
    axes2 = [axes2]

for idx, mes in enumerate(meses_unicos):
    # Filtrar datos del mes
    df_mes = df_ecoplas[df_ecoplas['Mes_Año'] == mes]
    
    # Agrupar por producto y sumar ventas
    productos_mes = df_mes.groupby('Descripción del Producto')['Subtotal_limpio'].sum().reset_index()
    productos_mes.columns = ['Producto', 'Total_Ventas']
    productos_mes = productos_mes.sort_values('Total_Ventas', ascending=False).head(10)
    
    print(f"\n{mes}:")
    print(productos_mes.to_string(index=False))
    
    # Crear gráfica de barras horizontales
    ax = axes2[idx]
    colors_gradient = plt.cm.plasma(np.linspace(0.2, 0.9, len(productos_mes)))
    bars = ax.barh(range(len(productos_mes)), productos_mes['Total_Ventas'], 
                   color=colors_gradient, edgecolor='black', linewidth=1)
    
    # Truncar nombres largos de productos
    productos_truncados = [p[:40] + '...' if len(p) > 40 else p for p in productos_mes['Producto']]
    ax.set_yticks(range(len(productos_mes)))
    ax.set_yticklabels(productos_truncados, fontsize=9)
    ax.set_xlabel('Ventas ($)', fontsize=10)
    ax.set_title(f'{mes}', fontsize=12, fontweight='bold', pad=10)
    ax.invert_yaxis()  # El producto con más ventas arriba
    ax.grid(axis='x', alpha=0.3)
    
    # Agregar valores en las barras
    for i, (bar, value) in enumerate(zip(bars, productos_mes['Total_Ventas'])):
        ax.text(value, bar.get_y() + bar.get_height()/2, 
                f' ${value:,.0f}', 
                va='center', ha='left', fontsize=8, fontweight='bold')

# Ocultar subgráficas vacías si hay número impar de meses
if num_meses % 2 != 0:
    axes2[-1].axis('off')

plt.tight_layout()
plt.savefig(r"c:\Users\Oiden\OneDrive - Universidad Nacional Abierta y a Distancia\Documents\curso python\top10_productos_por_mes.png", 
            dpi=300, bbox_inches='tight')
print("\n✓ Gráfica guardada como 'top10_productos_por_mes.png'")

plt.show()

# ============================================================================
# GRÁFICA ADICIONAL: Top 10 productos generales (todos los meses)
# ============================================================================

print("\n" + "="*60)
print("TOP 10 PRODUCTOS MÁS VENDIDOS (GENERAL)")
print("="*60)

productos_general = df_ecoplas.groupby('Descripción del Producto').agg({
    'Subtotal_limpio': 'sum',
    'Cantidad Vendida': 'sum'
}).reset_index()
productos_general.columns = ['Producto', 'Total_Ventas', 'Cantidad_Total']
productos_general = productos_general.sort_values('Total_Ventas', ascending=False).head(10)

print(productos_general.to_string(index=False))

# Crear figura para top 10 general
fig3, (ax_ventas, ax_cantidad) = plt.subplots(1, 2, figsize=(18, 8))
fig3.suptitle('Top 10 Productos Más Vendidos (General)', fontsize=16, fontweight='bold')

# Gráfica por ventas en pesos
colors_ventas = plt.cm.Spectral(np.linspace(0.1, 0.9, 10))
productos_truncados = [p[:35] + '...' if len(p) > 35 else p for p in productos_general['Producto']]

bars1 = ax_ventas.barh(range(10), productos_general['Total_Ventas'], 
                       color=colors_ventas, edgecolor='black', linewidth=1.2)
ax_ventas.set_yticks(range(10))
ax_ventas.set_yticklabels(productos_truncados, fontsize=10)
ax_ventas.set_xlabel('Ventas Totales ($)', fontsize=11, fontweight='bold')
ax_ventas.set_title('Por Valor en Ventas', fontsize=12, fontweight='bold')
ax_ventas.invert_yaxis()
ax_ventas.grid(axis='x', alpha=0.3)

for i, (bar, value) in enumerate(zip(bars1, productos_general['Total_Ventas'])):
    ax_ventas.text(value, bar.get_y() + bar.get_height()/2, 
                   f' ${value:,.0f}', 
                   va='center', ha='left', fontsize=9, fontweight='bold')

# Gráfica por cantidad vendida
bars2 = ax_cantidad.barh(range(10), productos_general['Cantidad_Total'], 
                         color=colors_ventas, edgecolor='black', linewidth=1.2)
ax_cantidad.set_yticks(range(10))
ax_cantidad.set_yticklabels(productos_truncados, fontsize=10)
ax_cantidad.set_xlabel('Cantidad Total Vendida (unidades)', fontsize=11, fontweight='bold')
ax_cantidad.set_title('Por Cantidad Vendida', fontsize=12, fontweight='bold')
ax_cantidad.invert_yaxis()
ax_cantidad.grid(axis='x', alpha=0.3)

for i, (bar, value) in enumerate(zip(bars2, productos_general['Cantidad_Total'])):
    ax_cantidad.text(value, bar.get_y() + bar.get_height()/2, 
                     f' {int(value):,}', 
                     va='center', ha='left', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig(r"c:\Users\Oiden\OneDrive - Universidad Nacional Abierta y a Distancia\Documents\curso python\top10_productos_general.png", 
            dpi=300, bbox_inches='tight')
print("\n✓ Gráfica guardada como 'top10_productos_general.png'")

plt.show()

print("\n" + "="*60)
print("ANÁLISIS COMPLETADO")
print("="*60)
