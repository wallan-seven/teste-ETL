import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def extracao(path):
    return pd.read_csv(path)

def conversao(df):
    df = df.dropna()
    df["sacos"] = (df["saldo_kg"] / 60).round(2)
    df["sacos_inteiros"] = df["saldo_kg"] // 60
    df["resto_kg"] = df["saldo_kg"] % 60
    return df

def carregar(df, path):
    df.to_csv(path, index=False)

def main():
    entrada = os.path.join(BASE_DIR, "clientes_saldo.csv")
    saida = os.path.join(BASE_DIR, "cliente_saldo_convertido.csv")

    df = extracao(entrada)
    df_tratado = conversao(df)
    carregar(df_tratado, saida)

if __name__ == "__main__":
    main()
