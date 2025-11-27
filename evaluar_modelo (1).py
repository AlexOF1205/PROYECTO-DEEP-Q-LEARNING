import matplotlib.pyplot as plt
import pandas as pd

file_path = "logs/dqn/ALE-Alien-v5_1/0.monitor.csv"


df = pd.read_csv(file_path, skiprows=2, header=None)


df.columns = ["length", "reward", "time"]


df = df[pd.to_numeric(df["reward"], errors="coerce").notna()]
df = df.reset_index(drop=True)


print("Número de episodios:", len(df))
print(df.head())


plt.figure(figsize=(10,5))
plt.plot(df["reward"])
plt.title("Recompensa por episodio DQN")
plt.xlabel("Episodio")
plt.ylabel("Recompensa")
plt.grid()
plt.show()


plt.figure(figsize=(10,5))
plt.plot(df["length"])
plt.title("Duración del episodio (steps)")
plt.xlabel("Episodio")
plt.ylabel("Steps")
plt.grid()
plt.show()


window = 50
df["reward_smooth"] = df["reward"].rolling(window, min_periods=1).mean()

plt.figure(figsize=(10,5))
plt.plot(df["reward"], alpha=0.3, label="Reward")
plt.plot(df["reward_smooth"], linewidth=3, label=f"Media móvil ({window})")
plt.title("Curva de aprendizaje DQN (recompensa suavizada)")
plt.xlabel("Episodio")
plt.ylabel("Recompensa")
plt.legend()
plt.grid()
plt.show()


