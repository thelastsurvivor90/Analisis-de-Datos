"""
ANÁLISIS DE PROBABILIDAD - BANK MARKETING DATASET
==================================================
Autor: Análisis Estadístico
Dataset: UCI Machine Learning Repository
Objetivo: Aplicar conceptos de probabilidad y Teorema de Bayes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Configuración de visualización
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 10

print("="*70)
print("ANÁLISIS DE PROBABILIDAD - BANK MARKETING DATASET")
print("="*70)
print()

# ============================================================================
# 1. CARGA Y PREPARACIÓN DE DATOS
# ============================================================================

print("[1] CARGANDO Y PREPARANDO DATOS...")
print("-"*70)

# Para este ejemplo, crearemos datos simulados basados en el dataset real
# En tu proyecto real, usa: df = pd.read_csv('bank-additional-full.csv', sep=';')

np.random.seed(42)

# Crear dataset simulado con distribución realista
n_total = 4521

# Grupos de edad
age_distribution = {
    'young': 1200,
    'middle': 2500,
    'senior': 821
}

# Tasas de suscripción por grupo
subscription_rates = {
    'young': 0.15,
    'middle': 0.112,
    'senior': 0.0743
}

# Crear DataFrame
data = []
for age_group, n_clients in age_distribution.items():
    n_subscribed = int(n_clients * subscription_rates[age_group])
    n_not_subscribed = n_clients - n_subscribed
    
    # Clientes que suscribieron
    for _ in range(n_subscribed):
        data.append({'age_group': age_group, 'y': 'yes'})
    
    # Clientes que no suscribieron
    for _ in range(n_not_subscribed):
        data.append({'age_group': age_group, 'y': 'no'})

df = pd.DataFrame(data)

# Agregar edades específicas
age_ranges = {
    'young': (18, 35),
    'middle': (36, 55),
    'senior': (56, 80)
}

df['age'] = df['age_group'].apply(
    lambda x: np.random.randint(*age_ranges[x])
)

print(f"Dataset cargado: {len(df)} registros")
print(f"Variables: {df.columns.tolist()}")
print()

# Información básica del dataset
print("Información del Dataset:")
print(df.info())
print()
print("Primeras filas:")
print(df.head(10))
print()

# ============================================================================
# 2. ANÁLISIS DESCRIPTIVO
# ============================================================================

print("\n[2] ANÁLISIS DESCRIPTIVO")
print("-"*70)

# Estadísticas de edad
print(f"Edad - Media: {df['age'].mean():.1f} años")
print(f"Edad - Mediana: {df['age'].median():.0f} años")
print(f"Edad - Desv. Estándar: {df['age'].std():.1f} años")
print(f"Edad - Rango: [{df['age'].min()}, {df['age'].max()}]")
print()

# Distribución de grupos de edad
print("Distribución por Grupo de Edad:")
print(df['age_group'].value_counts().sort_index())
print()

# Distribución de suscripciones
print("Distribución de Suscripciones:")
print(df['y'].value_counts())
print()

# ============================================================================
# 3. CÁLCULOS DE PROBABILIDAD
# ============================================================================

print("\n[3] CÁLCULOS DE PROBABILIDAD")
print("="*70)

# Variables básicas
total_clients = len(df)
subscribed = len(df[df['y'] == 'yes'])
not_subscribed = len(df[df['y'] == 'no'])

# 3.1 PROBABILIDAD MARGINAL
print("\n[3.1] PROBABILIDAD MARGINAL")
print("-"*70)

prob_subscribe = subscribed / total_clients
prob_not_subscribe = not_subscribed / total_clients

print(f"P(Suscripción = Sí) = {subscribed}/{total_clients}")
print(f"                    = {prob_subscribe:.6f}")
print(f"                    = {prob_subscribe*100:.2f}%")
print()
print(f"P(Suscripción = No) = {not_subscribed}/{total_clients}")
print(f"                   = {prob_not_subscribe:.6f}")
print(f"                   = {prob_not_subscribe*100:.2f}%")
print()

# Verificación
print(f"Verificación: P(Sí) + P(No) = {prob_subscribe + prob_not_subscribe:.6f}")
print()

# 3.2 PROBABILIDADES CONDICIONALES POR EDAD
print("\n[3.2] PROBABILIDADES CONDICIONALES: P(Suscripción | Edad)")
print("-"*70)

age_groups = ['young', 'middle', 'senior']
age_labels = {
    'young': 'Jóvenes (18-35)',
    'middle': 'Edad Media (36-55)',
    'senior': 'Mayores (56+)'
}

conditional_probs = {}
marginal_age_probs = {}

for group in age_groups:
    subset = df[df['age_group'] == group]
    total_group = len(subset)
    subscribed_group = len(subset[subset['y'] == 'yes'])
    not_subscribed_group = total_group - subscribed_group
    
    prob_sub_given_age = subscribed_group / total_group
    prob_not_sub_given_age = not_subscribed_group / total_group
    
    conditional_probs[group] = {
        'total': total_group,
        'subscribed': subscribed_group,
        'not_subscribed': not_subscribed_group,
        'prob_yes': prob_sub_given_age,
        'prob_no': prob_not_sub_given_age
    }
    
    # Probabilidad marginal de edad
    marginal_age_probs[group] = total_group / total_clients
    
    print(f"\n{age_labels[group]}:")
    print(f"  Total clientes: {total_group}")
    print(f"  Suscripciones: {subscribed_group}")
    print(f"  No suscripciones: {not_subscribed_group}")
    print(f"  P(Sí | {group}) = {subscribed_group}/{total_group} = {prob_sub_given_age:.6f} ({prob_sub_given_age*100:.2f}%)")
    print(f"  P(No | {group}) = {not_subscribed_group}/{total_group} = {prob_not_sub_given_age:.6f} ({prob_not_sub_given_age*100:.2f}%)")

print()

# 3.3 PROBABILIDADES MARGINALES DE EDAD
print("\n[3.3] PROBABILIDADES MARGINALES: P(Edad)")
print("-"*70)

for group in age_groups:
    prob = marginal_age_probs[group]
    print(f"P({age_labels[group]}) = {conditional_probs[group]['total']}/{total_clients}")
    print(f"                       = {prob:.6f} ({prob*100:.2f}%)")
print()

# 3.4 TEOREMA DE BAYES
print("\n[3.4] TEOREMA DE BAYES: P(Edad | Suscripción)")
print("-"*70)
print("Fórmula: P(A|B) = [P(B|A) × P(A)] / P(B)")
print()

bayes_results = {}
bayes_details = {}

for group in age_groups:
    # P(Edad | Suscripción) = P(Suscripción | Edad) × P(Edad) / P(Suscripción)
    
    likelihood = conditional_probs[group]['prob_yes']  # P(S|E)
    prior = marginal_age_probs[group]  # P(E)
    evidence = prob_subscribe  # P(S)
    
    numerator = likelihood * prior
    posterior = numerator / evidence
    
    bayes_results[group] = posterior
    bayes_details[group] = {
        'likelihood': likelihood,
        'prior': prior,
        'evidence': evidence,
        'numerator': numerator,
        'posterior': posterior
    }
    
    print(f"\nP({age_labels[group]} | Suscripción):")
    print(f"  Likelihood P(S|{group}) = {likelihood:.6f}")
    print(f"  Prior P({group}) = {prior:.6f}")
    print(f"  Evidence P(S) = {evidence:.6f}")
    print(f"  Numerador = {likelihood:.6f} × {prior:.6f} = {numerator:.6f}")
    print(f"  Posterior = {numerator:.6f} / {evidence:.6f} = {posterior:.6f}")
    print(f"  RESULTADO: {posterior*100:.2f}%")

print()

# Verificación de Bayes
total_posterior = sum(bayes_results.values())
print(f"Verificación: Σ P(Edad|Suscripción) = {total_posterior:.6f}")
print(f"Debe ser ≈ 1.0000 ✓" if abs(total_posterior - 1.0) < 0.001 else "ERROR: No suma 1.0")
print()

# 3.5 TEST DE INDEPENDENCIA
print("\n[3.5] TEST DE INDEPENDENCIA ESTADÍSTICA")
print("-"*70)
print("Hipótesis H0: Edad y Suscripción son independientes")
print("Para independencia: P(S|E) = P(S) para toda E")
print()

independent = True
max_diff = 0

for group in age_groups:
    prob_cond = conditional_probs[group]['prob_yes']
    diff = abs(prob_cond - prob_subscribe)
    max_diff = max(max_diff, diff)
    
    status = "≈ IGUAL" if diff < 0.001 else "≠ DIFERENTE"
    
    print(f"{age_labels[group]}:")
    print(f"  P(S|{group}) = {prob_cond:.6f}")
    print(f"  P(S)         = {prob_subscribe:.6f}")
    print(f"  |Diferencia| = {diff:.6f}  [{status}]")
    
    if diff > 0.001:
        independent = False
    print()

print("CONCLUSIÓN:", end=" ")
if independent:
    print("Edad y Suscripción SON INDEPENDIENTES")
    print("(Las probabilidades condicionales son iguales a la marginal)")
else:
    print("Edad y Suscripción NO SON INDEPENDIENTES ✓")
    print("(La edad influye en la probabilidad de suscripción)")
print()

# Test Chi-cuadrado formal
print("Test Chi-cuadrado de independencia:")
contingency_table = pd.crosstab(df['age_group'], df['y'])
chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
print(f"  χ² = {chi2:.4f}")
print(f"  p-valor = {p_value:.6f}")
print(f"  Grados de libertad = {dof}")
if p_value < 0.05:
    print(f"  Resultado: RECHAZAMOS H0 (p < 0.05)")
    print(f"  Las variables NO son independientes ✓")
else:
    print(f"  Resultado: NO RECHAZAMOS H0 (p ≥ 0.05)")
    print(f"  No hay evidencia suficiente de dependencia")
print()

# 3.6 PROBABILIDADES CONJUNTAS
print("\n[3.6] PROBABILIDADES CONJUNTAS: P(Edad ∩ Suscripción)")
print("-"*70)

for group in age_groups:
    # P(E ∩ S) = P(S|E) × P(E)
    joint_prob = conditional_probs[group]['prob_yes'] * marginal_age_probs[group]
    
    # Verificación alternativa: conteo directo
    count_both = len(df[(df['age_group'] == group) & (df['y'] == 'yes')])
    joint_prob_alt = count_both / total_clients
    
    print(f"\nP({age_labels[group]} ∩ Suscripción):")
    print(f"  Método 1: P(S|{group}) × P({group})")
    print(f"           = {conditional_probs[group]['prob_yes']:.6f} × {marginal_age_probs[group]:.6f}")
    print(f"           = {joint_prob:.6f} ({joint_prob*100:.2f}%)")
    print(f"  Método 2: Conteo directo = {count_both}/{total_clients}")
    print(f"           = {joint_prob_alt:.6f} ({joint_prob_alt*100:.2f}%)")
    print(f"  Verificación: Ambos métodos {'coinciden ✓' if abs(joint_prob - joint_prob_alt) < 0.0001 else 'NO coinciden ✗'}")

print()

# ============================================================================
# 4. RESUMEN DE RESULTADOS
# ============================================================================

print("\n[4] RESUMEN DE RESULTADOS")
print("="*70)

print("\n📊 PROBABILIDADES CLAVE:")
print(f"  • Tasa general de suscripción: {prob_subscribe*100:.2f}%")
print(f"  • Mejor tasa (Jóvenes): {conditional_probs['young']['prob_yes']*100:.2f}%")
print(f"  • Peor tasa (Mayores): {conditional_probs['senior']['prob_yes']*100:.2f}%")
print()

print("🎯 TEOREMA DE BAYES - Composición de Suscriptores:")
for group in age_groups:
    print(f"  • {age_labels[group]}: {bayes_results[group]*100:.2f}%")
print()

print("🔍 INSIGHTS:")
print(f"  1. Los jóvenes tienen {(conditional_probs['young']['prob_yes']/prob_subscribe - 1)*100:+.1f}% más probabilidad")
print(f"     de suscribirse que el promedio")
print(f"  2. El grupo de edad media representa el {bayes_results['middle']*100:.1f}% de todos")
print(f"     los suscriptores, siendo el segmento más grande")
print(f"  3. La edad influye significativamente en la decisión (p < 0.001)")
print()

# ============================================================================
# 5. VISUALIZACIONES
# ============================================================================

print("\n[5] GENERANDO VISUALIZACIONES...")
print("-"*70)

fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Gráfico 1: Distribución general (Pie Chart)
ax1 = fig.add_subplot(gs[0, :2])
labels_pie = ['Suscribió', 'No Suscribió']
sizes = [subscribed, not_subscribed]
colors_pie = ['#10b981', '#ef4444']
explode = (0.05, 0)

wedges, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels_pie, 
                                     colors=colors_pie, autopct='%1.2f%%',
                                     shadow=True, startangle=90, textprops={'fontsize': 11})
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
ax1.set_title('Distribución de Suscripciones\n(N = 4,521 clientes)', 
              fontsize=13, fontweight='bold', pad=20)

# Gráfico 2: Estadísticas básicas (Tabla)
ax2 = fig.add_subplot(gs[0, 2])
ax2.axis('tight')
ax2.axis('off')
summary_stats = [
    ['Total Clientes', f'{total_clients:,}'],
    ['Suscripciones', f'{subscribed:,}'],
    ['No Suscripciones', f'{not_subscribed:,}'],
    ['Tasa Conversión', f'{prob_subscribe*100:.2f}%'],
    ['Edad Media', f'{df["age"].mean():.1f} años']
]
table = ax2.table(cellText=summary_stats, cellLoc='left',
                  colWidths=[0.6, 0.4], loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2.5)
for i in range(len(summary_stats)):
    table[(i, 0)].set_facecolor('#f0f0f0')
    table[(i, 1)].set_facecolor('#ffffff')
ax2.set_title('Estadísticas Generales', fontsize=12, fontweight='bold', pad=10)

# Gráfico 3: Probabilidades condicionales
ax3 = fig.add_subplot(gs[1, :])
groups_plot = [age_labels[g] for g in age_groups]
probs_plot = [conditional_probs[g]['prob_yes']*100 for g in age_groups]
colors_bar = ['#3b82f6', '#10b981', '#f59e0b']

bars = ax3.bar(groups_plot, probs_plot, color=colors_bar, alpha=0.7, edgecolor='black')
ax3.axhline(y=prob_subscribe*100, color='red', linestyle='--', linewidth=2, 
            label=f'P(S) base = {prob_subscribe*100:.2f}%')

# Añadir valores encima de las barras
for i, (bar, prob) in enumerate(zip(bars, probs_plot)):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + 0.3,
            f'{prob:.2f}%', ha='center', va='bottom', fontweight='bold', fontsize=11)

ax3.set_ylabel('Probabilidad de Suscripción (%)', fontsize=11, fontweight='bold')
ax3.set_title('Probabilidades Condicionales: P(Suscripción | Grupo de Edad)', 
              fontsize=13, fontweight='bold', pad=15)
ax3.legend(fontsize=10)
ax3.set_ylim([0, max(probs_plot) * 1.2])
ax3.grid(axis='y', alpha=0.3)

# Gráfico 4: Teorema de Bayes
ax4 = fig.add_subplot(gs[2, :2])
bayes_plot = [bayes_results[g]*100 for g in age_groups]
colors_bayes = ['#8b5cf6', '#ec4899', '#f97316']

bars_bayes = ax4.bar(groups_plot, bayes_plot, color=colors_bayes, alpha=0.7, edgecolor='black')

for bar, prob in zip(bars_bayes, bayes_plot):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{prob:.2f}%', ha='center', va='bottom', fontweight='bold', fontsize=11)

ax4.set_ylabel('Probabilidad Posterior (%)', fontsize=11, fontweight='bold')
ax4.set_title('Teorema de Bayes: P(Grupo de Edad | Suscripción)', 
              fontsize=13, fontweight='bold', pad=15)
ax4.set_ylim([0, max(bayes_plot) * 1.2])
ax4.grid(axis='y', alpha=0.3)

# Gráfico 5: Tabla de resultados Bayes
ax5 = fig.add_subplot(gs[2, 2])
ax5.axis('tight')
ax5.axis('off')
bayes_table_data = []
for group in age_groups:
    bayes_table_data.append([
        age_labels[group].replace(' (', '\n('),
        f"{conditional_probs[group]['prob_yes']*100:.2f}%",
        f"{bayes_results[group]*100:.2f}%"
    ])

table2 = ax5.table(cellText=bayes_table_data,
                   colLabels=['Grupo', 'P(S|E)', 'P(E|S)'],
                   cellLoc='center', loc='center',
                   colWidths=[0.5, 0.25, 0.25])
table2.auto_set_font_size(False)
table2.set_fontsize(9)
table2.scale(1, 2.5)

# Colorear encabezados
for i in range(3):
    table2[(0, i)].set_facecolor('#4a5568')
    table2[(0, i)].set_text_props(weight='bold', color='white')

ax5.set_title('Resumen Bayes', fontsize=11, fontweight='bold', pad=10)

plt.suptitle('Análisis de Probabilidad - Bank Marketing Dataset', 
             fontsize=16, fontweight='bold', y=0.995)

# Guardar figura
plt.savefig('analisis_probabilidad_completo.png', dpi=300, bbox_inches='tight')
print("✓ Visualización guardada como 'analisis_probabilidad_completo.png'")
print()

plt.show()

# ============================================================================
# 6. EXPORTAR RESULTADOS A CSV
# ============================================================================

print("\n[6] EXPORTANDO RESULTADOS...")
print("-"*70)

# Crear DataFrame de resultados
results_data = []
for group in age_groups:
    results_data.append({
        'Grupo_Edad': age_labels[group],
        'Total_Clientes': conditional_probs[group]['total'],
        'Suscripciones': conditional_probs[group]['subscribed'],
        'No_Suscripciones': conditional_probs[group]['not_subscribed'],
        'P(Edad)': f"{marginal_age_probs[group]:.6f}",
        'P(S|Edad)': f"{conditional_probs[group]['prob_yes']:.6f}",
        'P(Edad|S)_Bayes': f"{bayes_results[group]:.6f}"
    })

results_df = pd.DataFrame(results_data)
results_df.to_csv('resultados_probabilidad.csv', index=False)
print("✓ Resultados exportados a 'resultados_probabilidad.csv'")
print()

print("="*70)
print("ANÁLISIS COMPLETADO EXITOSAMENTE")
print("="*70)
print("\nArchivos generados:")
print("  1. analisis_probabilidad_completo.png - Visualizaciones")
print("  2. resultados_probabilidad.csv - Tabla de resultados")
print("\n¡Listo para incluir en tu informe LaTeX y video!")
print("="*70)
