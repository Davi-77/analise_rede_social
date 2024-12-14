import pandas as pd   #pip install pandas matplotlib seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess data
df = pd.read_csv("dados_instagram.csv")
df["data"] = pd.to_datetime(df["data"])
df["hora"] = df["data"].dt.hour

# Calculate average engagement per hour
engajamento_por_hora = df.groupby("hora")["likes"].mean()

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(x=engajamento_por_hora.index, y=engajamento_por_hora.values, palette="viridis")
plt.title("Engajamento Médio por Hora", fontsize=16)
plt.xlabel("Hora do Dia", fontsize=12)
plt.ylabel("Curtidas Médias", fontsize=12)
plt.xticks(range(0, 24))
plt.show()

# df_exploded = df.explode("hashtags")

# hashtags_populares = df.exploded["hashtags"].value_counts()
# print(hashtags_populares.head(10))