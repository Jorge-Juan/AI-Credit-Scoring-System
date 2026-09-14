# Marco de Gobernanza Operativa y Gestión de Proyectos (COO Viewpoint)

## 1. Planificación de Capacidad y Metodología Agil
* **Framework:** Scrum adaptado a entornos regulados de IA de Alto Riesgo.
* **Cadencia:** Sprints de 2 semanas con entregables alineados a hitos regulatorios.
* **Capacidad del Equipo:** 40 Story Points (SP) por Sprint.
* **Velocidad Promedio:** Sprint 1 (35 SP completados) | Sprint 2 (40 SP completados). Eficiencia de planificación: 93.75%.

## 2. Matriz de Asignación de Responsabilidades (RACI)
| Fase / Entregable | COO / Ops Lead | Data Science Lead | Risk & Legal Officer | QA / Testing |
| :--- | :---: | :---: | :---: | :---: |
| Definición de Backlog y BDD | **Accountable** | Responsible | Consulted | Informed |
| Auditoría Econométrica (VIF/Pearson) | Informed | **Responsible** | Consulted | Accountable |
| Filtro de Sesgo (EU AI Act) | **Accountable** | Responsible | Accountable | Informed |
| Protocolo HITL (Control Humano) | **Accountable** | Consulted | Responsible | Informed |

## 3. KPIs de Operaciones y SLAs
* **Cycle Time Promedio:** 3.2 días por Historia de Usuario.
* **SLA de Revisión Humana (HITL):** Resolución de expedientes dudosos en $< 2$ horas por el Comité de Riesgo.
* **Índice de Cobertura Regulatoria:** 100% de criterios de aceptación verificados bajo estándar BDD.

## 4. Registro de Riesgos Operativos y Mitigación (Risk Register)

| ID | Riesgo Identificado | Impacto Operativo | Probabilidad | Plan de Mitigación y Control |
| :--- | :--- | :---: | :---: | :--- |
| **R-01** | Sesgo algorítmico penalizado por la ley (*EU AI Act*) | **Crítico** | Media | Automatización del filtro de Impacto Dispar ($DIR < 0.80$) en pipeline de ingesta. |
| **R-02** | Cuello de botella en comités de riesgo por volumen de revisión | **Alto** | Alta | Delimitación estricta de la banda de duda ($[0.45, 0.55]$) y SLA de resolución $< 2$h. |
| **R-03** | Degradación del rendimiento del modelo (*Concept Drift*) | **Medio** | Alta | Monitorización continua y auditoría trimestral obligatoria (definida en EPIC 4). |
| **R-04** | Falta de explicabilidad ante inspecciones regulatorias | **Crítico** | Baja | Priorización de modelos lineales (Regresión Logística) salvo mejora $\ge 15\%$ en ROC-AUC. |
