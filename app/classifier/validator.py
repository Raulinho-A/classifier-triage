import pandas as pd
from app.classifier.model_loader import expected_columns, expected_types

def validate(input_dict: dict) -> pd.DataFrame:
    """
    Convierte el input dict en un DataFrame validado, ordenado y listo para predecir.
    """
    df = pd.DataFrame([input_dict])

    missing_cols = set(expected_columns) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Faltan columnas obligatorias: {missing_cols}")
    
    extra_cols = set(df.columns) - set(expected_columns)
    if extra_cols:
        raise ValueError(f"Columnas no reconocidas en el modelo: {extra_cols}")
    
    df = df[expected_columns]

    for col, expected_type in expected_types.items():
        try:
            df[col] = df[col].astype(expected_type)
        except ValueError as e:
            raise ValueError(f"Error al convertir '{col}' a tipo {expected_type}: {str(e)}")
        
    return df