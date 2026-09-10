import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor

def audit_multicollinearity(df: pd.DataFrame, max_vif: float = 10.0, max_corr: float = 0.85):
    """
    Auditoría Econométrica de Multicolinealidad (Historia 1.1)
    
    Criterios de Aceptación (BDD):
    - Filtrar variables con correlación de Pearson r > 0.85
    - Descartar variables con VIF (Factor de Inflación de Varianza) > 10.0
    """
    # 1. Matriz de Correlación de Pearson
    corr_matrix = df.corr().abs()
    upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    high_corr_features = [col for col in upper_tri.columns if any(upper_tri[col] > max_corr)]
    
    # 2. Cálculo del VIF (Variance Inflation Factor)
    vif_data = pd.DataFrame()
    vif_data["Variable"] = df.columns
    vif_data["VIF"] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
    
    # Identify variables exceeding threshold
    high_vif_features = vif_data[vif_data["VIF"] > max_vif]["Variable"].tolist()
    
    # Consolidados a eliminar
    to_drop = list(set(high_corr_features + high_vif_features))
    
    print(f"[AUDITORÍA] Variables identificadas para eliminación: {to_drop}")
    return df.drop(columns=to_drop), vif_data

if __name__ == "__main__":
    print("Módulo de Auditoría Econométrica cargado correctamente.")
