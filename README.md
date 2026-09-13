# AI Credit Scoring System | Product Requirement Document (PRD)

> **Resumen Ejecutivo:** Marco de gobernanza, auditoría econométrica y gestión ágil para la implantación de un sistema predictivo de riesgo crediticio mediante Inteligencia Artificial.

---

**Objetivos Estratégicos del Producto**

* **Rigor Cuantitativo:** Mitigación de multicolinealidad ($VIF > 10$) y estabilidad econométrica en entorno financiero.
* **Gobernanza y Ética de IA:** Eliminación de sesgos discriminatorios en variables sociodemográficas bajo los requisitos del EU AI Act.
* **Gestión de Producto:** Trazabilidad de requisitos en Jira usando metodología Scrum y BDD (*Behavior-Driven Development*).

---

**Estructura del Backlog (Jira Workspace)**

| Épica | Enfoque Estratégico | Estándar de la Industria |
| :--- | :--- | :--- |
| **EPIC 1** | Gobernanza y Tratamiento Econométrico de Datos | CRISP-DM / BDD (Gherkin) |
| **EPIC 2** | Evaluación Comparativa (ML vs. Redes Neuronales) | Métrica ROC-AUC / Matriz de Confusión |
| **EPIC 3** | Despliegue Operativo y Protocolo de Control Humano | Protocolo *Human-in-the-loop* (HITL) |

---

**Criterios de Aceptación Técnicos (Gherkin / BDD)**

```gherkin
Escenario: Auditoría de Multicolinealidad (Historia 1.1)
  Dado un dataset de 10.000 solicitudes de crédito
  Cuando se ejecute la matriz de correlación de Pearson entre variables explicativas
  Entonces se deben descartar variables con r > 0.85 y VIF > 10

```
---

**Métricas de Gestión de Proyectos y Gobernanza Operativa**

* **Velocidad y Planificación:** 2 Sprints ejecutados al 100% de cumplimiento dentro del alcance temporal.
* **Gestión del Riesgo:** Matriz RACI integrada y alineada con la normativa europea de IA (*EU AI Act*).
* **Control Operativo:** Definición de SLAs de atención manual ($< 2$ horas) para casos de incertidumbre algorítmica.
* **Documentación Ejecutiva:** Consultar el detalle de gobernanza y capacidad en `docs/OPERATIONAL_GOVERNANCE.md`.
  
---

**Trazabilidad del Proyecto**
* **Jira Workspace:** [Acceso al Tablero y Backlog Activo](https://jorgejuanmartindemiguel.atlassian.net/jira/software/projects/SCRUM/boards/1?filter=&groupBy=none)
* **Metodología:** Scrum / PSPO I Framework
