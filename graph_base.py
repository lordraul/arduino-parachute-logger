import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data1.csv")

df["ax"] = df["ax_raw"] / 16384.0 * 9.81
df["ay"] = df["ay_raw"] / 16384.0 * 9.81
df["az"] = df["az_raw"] / 16384.0 * 9.81

df["a"] = (df["ax"]**2 + df["ay"]**2 + df["az"]**2)**0.5

df["time_s"] = df["time(ms)"] / 1000.0

df["v"] = 0

for i, row in df.iterrows():
    if i > 0:
        df["v"][i] = df["v"][i-1] + df["a"][i] * (df["time_s"][i] - df["time_s"][i-1])

plt.figure(figsize=(12, 6))
plt.plot(df["time_s"], df["ax"], label="ax (m/s²)", color='red')
plt.plot(df["time_s"], df["ay"], label="ay (m/s²)", color='green')
plt.plot(df["time_s"], df["az"], label="az (m/s²)", color='blue')
plt.plot(df["time_s"], df["a"], label="a (m/s²)", color='yellow')
plt.plot(df["time_s"], df["v"], label="v (m/s)", color='purple')
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Acceleration vs Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()