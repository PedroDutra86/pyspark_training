import streamlit as st
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os
import sys

# --- Inicialização ---
def initialize_spark():
    """Inicializa a sessão Spark."""
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

    spark = (
        SparkSession.builder
        .master('local')
        .appName('PySpark_01')
        .getOrCreate()
    )
    return spark

def load_data(spark, file_path):
    """Carrega os dados do arquivo CSV usando Spark."""
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    return df

def display_dataframe(df, title, num_rows=5):
    """Exibe um DataFrame do Spark no Streamlit."""
    st.subheader(title)
    try:
        st.dataframe(df.limit(num_rows).toPandas())
    except Exception as e:
        st.error(f"Erro ao converter para Pandas DataFrame: {e}")


def display_column_types(df):
    """Exibe os tipos de dados de cada coluna."""
    st.subheader("Tipos de Colunas")
    schema = df.schema
    for field in schema:
        st.write(f"- **{field.name}**: {field.dataType}")

def display_null_counts(df):
    """Exibe a contagem de valores nulos por coluna."""
    st.subheader("Contagem de Nulos por Coluna")
    for column in df.columns:
        null_count = df.filter(col(column).isNull()).count()
        st.write(f"- **{column}**: {null_count}")

def rename_columns(df):
    """Renomeia as colunas do DataFrame."""
    port_df = (
        df.withColumnRenamed('show_id', 'id')
        .withColumnRenamed('type', 'tipo')
        .withColumnRenamed('title', 'titulo')
        .withColumnRenamed('director', 'diretor')
        .withColumnRenamed('cast' ,'atores_principais')
        .withColumnRenamed('country', 'pais')
        .withColumnRenamed('date_added', 'data_dicionado')
        .withColumnRenamed('release_year', 'ano_lancamento')
        .withColumnRenamed('rating', 'classificacao')
        .withColumnRenamed('duration', 'duracao')
        .withColumnRenamed('listed_in', 'categoria')
        .withColumnRenamed('description', 'descricao')
    )
    return port_df

def select_columns(df, columns):
    """Seleciona colunas específicas do DataFrame."""
    selected_df = df.select(columns)
    return selected_df

def filter_dataframe(df, filter_condition):
    """Filtra o DataFrame com base na condição fornecida."""
    try:
        filtered_df = df.filter(filter_condition)
        return filtered_df
    except Exception as e:
        st.error(f"Erro ao aplicar o filtro: {e}")
        return None  # Importante retornar None em caso de erro


# --- Interface Streamlit ---
def main():
    st.title("Análise de Dados Netflix com PySpark e Streamlit")

    # Inicializa Spark
    spark = initialize_spark()

    # Carrega os dados
    file_path = './netflix_titles.csv'  # Garanta que o arquivo esteja no mesmo diretório
    try:
        df = load_data(spark, file_path)
        st.success("Dados carregados com sucesso!")
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return  # Encerra se não conseguir carregar os dados

    # Exibe o DataFrame original
    display_dataframe(df, "DataFrame Original (Amostra)")

    # Exibe os tipos de colunas
    display_column_types(df)

    # Exibe a contagem de nulos
    display_null_counts(df)

    # Renomeia as colunas
    port_df = rename_columns(df)
    display_dataframe(port_df, "DataFrame com Colunas Renomeadas (Amostra)")

    # --- Seleção de Colunas ---
    st.subheader("Seleção de Colunas")
    available_columns = df.columns
    selected_columns = st.multiselect("Selecione as colunas para exibir:", available_columns, default=['title', 'description'])

    if selected_columns:
        selected_df = select_columns(df, selected_columns)
        display_dataframe(selected_df, "DataFrame com Colunas Selecionadas (Amostra)")
    else:
        st.warning("Por favor, selecione pelo menos uma coluna.")

    # --- Filtragem de Dados ---
    st.subheader("Filtragem de Dados")
    filter_expression = st.text_input("Digite a expressão de filtro (ex: country == 'Brazil' and type == 'Movie'):")

    if filter_expression:
        filtered_df = filter_dataframe(df, filter_expression)
        if filtered_df is not None:  # Verifica se houve erro no filtro
            display_dataframe(filtered_df, "DataFrame Filtrado (Amostra)")

    # Finaliza a sessão Spark
    spark.stop()

if __name__ == "__main__":
    main()
