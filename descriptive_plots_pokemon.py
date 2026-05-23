"""Script externo para generar gráficos descriptivos del dataset Pokemon.

Dependencias:
- pandas
- matplotlib
- seaborn
- openpyxl

Ejecutar desde la terminal del proyecto:
    python descriptive_plots_pokemon.py
"""

import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def load_data(path: Path) -> pd.DataFrame:
    return pd.read_excel(path)


def plot_type_distribution(df: pd.DataFrame, output_dir: Path) -> None:
    plt.figure(figsize=(12, 6))
    order = df['Type 1'].value_counts().index
    sns.countplot(data=df, x='Type 1', order=order, palette='tab20')
    plt.title('Distribución de Pokémon por Tipo 1')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Cantidad de Pokémon')
    plt.xlabel('Tipo 1')
    plt.tight_layout()
    plt.savefig(output_dir / 'type1_distribution.png')
    plt.close()


def plot_stat_histograms(df: pd.DataFrame, output_dir: Path) -> None:
    numeric_columns = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    plt.figure(figsize=(14, 10))
    for i, col in enumerate(numeric_columns, start=1):
        plt.subplot(3, 3, i)
        sns.histplot(df[col], kde=True, color='steelblue', edgecolor='black')
        plt.title(col)
    plt.tight_layout()
    plt.savefig(output_dir / 'numeric_stat_histograms.png')
    plt.close()


def plot_generation_summary(df: pd.DataFrame, output_dir: Path) -> None:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='Generation', y='Total', palette='pastel')
    plt.title('Total de estadísticas por Generación')
    plt.xlabel('Generación')
    plt.ylabel('Total de estadísticas')
    plt.tight_layout()
    plt.savefig(output_dir / 'total_by_generation.png')
    plt.close()


def plot_legendary_comparison(df: pd.DataFrame, output_dir: Path) -> None:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='Legendary', y='Total', palette=['#4c72b0', '#dd8452'])
    plt.title('Comparación del Total de estadísticas: Legendary vs No Legendary')
    plt.xlabel('Legendario')
    plt.ylabel('Total de estadísticas')
    plt.tight_layout()
    plt.savefig(output_dir / 'legendary_vs_total.png')
    plt.close()


def plot_correlation_heatmap(df: pd.DataFrame, output_dir: Path) -> None:
    numeric_columns = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    corr = df[numeric_columns].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Mapa de correlaciones entre estadísticas numéricas')
    plt.tight_layout()
    plt.savefig(output_dir / 'correlation_heatmap.png')
    plt.close()


def main() -> None:
    project_root = Path(__file__).resolve().parent
    dataset_path = project_root / 'dataset' / 'Pokemon.xlsx'
    output_dir = project_root / 'plots'
    output_dir.mkdir(exist_ok=True)

    if not dataset_path.exists():
        raise FileNotFoundError(f'No se encontró el archivo de datos: {dataset_path}')

    df = load_data(dataset_path)
    print('Datos cargados correctamente. Número de filas:', len(df))
    print('Columnas:', df.columns.tolist())

    plot_type_distribution(df, output_dir)
    plot_stat_histograms(df, output_dir)
    plot_generation_summary(df, output_dir)
    plot_legendary_comparison(df, output_dir)
    plot_correlation_heatmap(df, output_dir)

    print('Gráficos guardados en:', output_dir)


if __name__ == '__main__':
    main()
