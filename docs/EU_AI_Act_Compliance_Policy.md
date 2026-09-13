# Manual de Gobernanza, Auditoría Econométrica y Cumplimiento Regulatorio (EU AI Act)

## 1. Alcance y Marco Metodológico
Este documento establece los estándares de supervisión operativa para el modelo de **AI Credit Scoring**, bajo el marco **CRISP-DM** y la regulación europea para sistemas de IA de alto riesgo.

---

## 2. Auditoría Econométrica de Datos (`src/01_multicollinearity_audit.py`)
Para garantizar la estabilidad de los estimadores y evitar errores de sobreajuste:
* **Matriz de Pearson:** Eliminación sistemática de pares de variables explicativas con correlación $|r| > 0.85$.
* **Factor de Inflación de la Varianza (VIF):** Descarte de atributos con $VIF > 10.0$, mitigando la multicolinealidad severa en el pipeline de datos.

---

## 3. Equidad Algorítmica y Control de Sesgo (`src/02_ethical_bias_filter.py`)
Conforme al Reglamento Europeo de IA, se evalúa el **Disparate Impact Ratio ($DIR$)** sobre colectivos protegidos:

$$DIR = \frac{\text{Tasa de Aprobación Group}_{\text{protegido}}}{\text{Tasa de Aprobación Group}_{\text{control}}}$$

* **Criterio de Aceptación:** Si $DIR < 0.80$ (Regla del 80%), la variable sensible introduce discriminación indirecta y queda automáticamente excluida del entrenamiento.

---

## 4. Benchmark Modelos vs. Explicabilidad (`src/03_model_benchmark.py`)
Se aplica un principio de interpretabilidad regulatoria:
* **Modelo Base:** Regresión Logística (totalmente auditable).
* **Modelo Complejo:** Red Neuronal Perceptrón Multicapa (`MLPClassifier`).
* **Regla de Adopción:** La Red Neuronal solo se desplegará si logra una mejora relativa $\ge 15\%$ en la métrica ROC-AUC frente a la Regresión Logística. En caso contrario, prevalece la interpretabilidad del modelo lineal.

---

## 5. Protocolo Operativo Human-in-the-Loop (`src/04_human_in_the_loop.py`)
El sistema segrega la resolución de solicitudes según la probabilidad de riesgo predicha ($S$):
* **Rechazo Automático:** $S < 0.45$
* **Aprobación Automática:** $S > 0.55$
* **Revisión Manual Obligatoria (HITL):** $S \in [0.45, 0.55]$. Se congela la ejecución automática y se deriva a ticket de auditoría en el Comité de Riesgos.
