import pandas as pd
import matplotlib.pyplot as plt

file_path = '/mnt/data/tds/pg57579/RAPL_Measurements/measurements.csv'
data = pd.read_csv(file_path)

fibonacci = [20, 30, 40]

# Function,Language,Program,PowerLimit,Package,Core,GPU,DRAM,Time,Temperature,Memory

# plot que compara o tempo de execução da fibonacci linear

fig, ax = plt.subplots()
times = []
for program in fibonacci:
    filtered_data = data[data['Program'].str.contains(f'fibonacciLinear_{program}') | data['Program'].str.contains(f'fibonacciRecursiva_{program}')]
    print(f"Filtered data for Program {program}:\n", filtered_data)  # Debugging line
    if not filtered_data.empty:
        mean_time = filtered_data['Time'].mean()
        times.append(mean_time)
        #print(f"Program {program}: Mean Time = {mean_time}")  # Debugging line
    else:
        times.append(0)  # Adiciona 0 se não houver dados para o programa

#print("Fibonacci values:", fibonacci)  # Debugging line
#print("Execution times:", times)  # Debugging line

ax.plot(fibonacci, times, marker='o')
ax.set_xlabel('Fibonacci')
ax.set_ylabel('Tempo (s)')
ax.legend(['Tempo de Execução'])
plt.show()
fig.savefig('/mnt/data/tds/pg57579/RAPL_Measurements/plot0.png')