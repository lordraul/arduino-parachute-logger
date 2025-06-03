import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("drop.csv")

df["ax"] = df["ax_raw"] / 16384.0 * 9.81
df["ay"] = df["ay_raw"] / 16384.0 * 9.81
df["az"] = df["az_raw"] / 16384.0 * 9.81

df["time_s"] = df["time(ms)"] / 1000.0

df["vx"] = 0.0
df["vy"] = 0.0
df["vz"] = 0.0

for i, row in df.iterrows():
    if i > 0:
        df["vx"][i] = df["vx"][i-1] + df["ax"][i] * (df["time_s"][i] - df["time_s"][i-1])
        df["vy"][i] = df["vy"][i-1] + df["ay"][i] * (df["time_s"][i] - df["time_s"][i-1])
        df["vz"][i] = df["vz"][i-1] + df["az"][i] * (df["time_s"][i] - df["time_s"][i-1])

df["v"] = (df["vx"]**2.0 + df["vy"]**2.0 + df["vz"]**2.0)**0.5

plt.figure(figsize=(12, 6))
plt.plot(df["time_s"], df["ax"], label="ax (m/s²)", color='red')
plt.plot(df["time_s"], df["ay"], label="ay (m/s²)", color='green')
plt.plot(df["time_s"], df["az"], label="az (m/s²)", color='blue')
plt.plot(df["time_s"], df["vx"], label="vx (m/s)", color='cyan')
plt.plot(df["time_s"], df["vy"], label="vy (m/s)", color='magenta')
plt.plot(df["time_s"], df["vz"], label="vz (m/s)", color='yellow')
plt.plot(df["time_s"], df["v"], label="v (m/s)", color='darkslateblue')
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Acceleration vs Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()