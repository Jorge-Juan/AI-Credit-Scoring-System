import pandas as pd
import numpy as np

def apply_human_in_the_loop_protocol(df: pd.DataFrame, score_col: str, lower_threshold: float = 0.45, upper_threshold: float = 0.55):
    """
    Protocolo de Control Humano / Human-in-the-Loop (Historia 3.1 - EPIC 3)
    
    Criterios de Aceptación (BDD):
    - Solicitudes con Scoring entre 0.45 y 0.55 derivan a revisión manual por el equipo de Riesgos.
    - Solicitudes < 0.45 se deniegan automáticamente.
    - Solicitudes > 0.55 se aprueban automáticamente.
    """
    conditions = [
        (df[score_col] < lower_threshold),
        (df[score_col] >= lower_threshold) & (df[score_col] <= upper_threshold),
        (df[score_col] > upper_threshold)
    ]
    choices = ['RECHAZADO_AUTOMATICO', 'REVISION_HUMANA_REQUERIDA', 'APROBADO_AUTOMATICO']
    
    df['Resolucion'] = np.select(conditions, choices, default='REVISION_HUMANA_REQUERIDA')
    
    human_review_count = (df['Resolucion'] == 'REVISION_HUMANA_REQUERIDA').sum()
    print(f"[HITL PROTOCOL] Operaciones derivadas a comité humano de riesgo: {human_review_count} / {len(df)}")
    
    return df

if __name__ == "__main__":
    print("Módulo de Protocolo Human-in-the-Loop (HITL) cargado correctamente.")
