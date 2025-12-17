import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess(data_path):
    """
    Preprocessing aman untuk dataset campuran (numerik + kategori):
    - Semua kolom object dikonversi ke category codes
    - Label dipastikan numerik
    - Normalisasi fitur
    """

    # Load dataset
    df = pd.read_csv(data_path)

    # Konversi SEMUA kolom object ke category codes
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype('category').cat.codes

    # Pisahkan fitur dan label (kolom terakhir)
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    # Normalisasi fitur
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test

