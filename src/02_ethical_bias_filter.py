import pandas as pd
import numpy as np

def audit_disparate_impact(df: pd.DataFrame, sensitive_col: str, target_col: str, protected_group: str, unprotected_group: str) -> float:
    """
    Auditoría de Sesgo y Discriminación Algorítmica (Historia 1.2 - EU AI Act)
    
    Criterios de Aceptación (BDD):
    - Calcula la Tasa de Impacto Dispar (Disparate Impact Ratio).
    - Si el Ratio < 0.80 (Regla del 80%), la variable sensible introduce sesgo indirecto y debe eliminarse.
    """
    # Tasa de aprobación para el grupo protegido
    rate_protected = df[df[sensitive_col] == protected_group][target_col].mean()
    
    # Tasa de aprobación para el grupo no protegido
    rate_unprotected = df[df[sensitive_col] == unprotected_group][target_col].mean()
    
    if rate_unprotected == 0:
        return 1.0
        
    disparate_impact_ratio = rate_protected / rate_unprotected
    
    print(f"[AUDITORÍA ÉTICA] Disparate Impact Ratio para '{sensitive_col}': {disparate_impact_ratio:.2f}")
    
    if disparate_impact_ratio < 0.80:
        print(f"[ALERTA] Sesgo detectado en la variable '{sensitive_col}'. Se recomienda eliminar del pipeline.")
    else:
        print(f"[OK] La variable '{sensitive_col}' cumple con el umbral de equidad del EU AI Act.")
        
    return disparate_impact_ratio

if __name__ == "__main__":
    print("Módulo de Auditoría Ética y Regulación de IA cargado correctamente.")
