import pandas as pd
import matplotlib.pyplot as plt
import os

# Create the directory if it doesn't exist
output_dir = './graficos'
os.makedirs(output_dir, exist_ok=True)

file_path = './measurements.csv'
data = pd.read_csv(file_path)

fibonacci = [10, 20, 30, 40, 50, 60, 70, 80]

# Tempo de Execução para Fibonacci Linear
fig_linear, ax_linear = plt.subplots()
times_linear = []
for program in fibonacci:
    filtered_data_linear = data[data['Function'].str.contains(f'FibonacciLinear_{program}')]
    if not filtered_data_linear.empty:
        mean_time_linear = filtered_data_linear['Time'].mean() * 1000  
        print(f"Tempos de execução para FibonacciLinear({program}): {mean_time_linear} ms")
        times_linear.append(mean_time_linear)
    else:
        times_linear.append(0) 

ax_linear.plot(fibonacci, times_linear, marker='o')
ax_linear.set_xlabel('Fibonacci')
ax_linear.set_ylabel('Tempo (ms)') 
ax_linear.legend(['Tempo de Execução'])
fig_linear.savefig(os.path.join(output_dir, 'O0_tempo_exec_linear.png'))

# Tempo de Execução para Fibonacci Recursiva
fig_recursiva, ax_recursiva = plt.subplots()
times_recursiva = []
for program in fibonacci:
    filtered_data_recursiva = data[data['Function'].str.contains(f'FibonacciRecursiva_{program}')]
    if not filtered_data_recursiva.empty:
        mean_time_recursiva = filtered_data_recursiva['Time'].mean() * 1000  
        print(f"Tempos de execução para FibonacciRecursiva({program}): {mean_time_recursiva} ms")
        times_recursiva.append(mean_time_recursiva)
    else:
        times_recursiva.append(0) 

ax_recursiva.plot(fibonacci, times_recursiva, marker='o')
ax_recursiva.set_xlabel('Fibonacci')
ax_recursiva.set_ylabel('Tempo (ms)') 
ax_recursiva.legend(['Tempo de Execução'])
fig_recursiva.savefig(os.path.join(output_dir, 'O0_tempo_exec_recursiva.png'))

# Consumo de Energia para Fibonacci Linear
fig_linear, ax_linear = plt.subplots()
energy_linear = []
for program in fibonacci:
    filtered_data_linear = data[data['Function'].str.contains(f'FibonacciLinear_{program}')]
    if not filtered_data_linear.empty:
        mean_energy_linear = filtered_data_linear['Package'].mean()  
        print(f"Consumo de Energia para FibonacciLinear({program}): {mean_energy_linear}")
        energy_linear.append(mean_energy_linear)
    else:
        energy_linear.append(0)

ax_linear.plot(fibonacci, energy_linear, marker='o')
ax_linear.set_xlabel('Fibonacci')
ax_linear.set_ylabel('Package')
ax_linear.legend(['Consumo de Energia'])
fig_linear.savefig(os.path.join(output_dir, 'O0_consumo_energia_linear.png'))

# Consumo de Energia para Fibonacci Recursiva
fig_recursiva, ax_recursiva = plt.subplots()
energy_recursiva = []
for program in fibonacci:
    filtered_data_recursiva = data[data['Function'].str.contains(f'FibonacciRecursiva_{program}')]
    if not filtered_data_recursiva.empty:
        mean_energy_recursiva = filtered_data_recursiva['Package'].mean()  
        print(f"Consumo de Energia para FibonacciRecursiva({program}): {mean_energy_recursiva}")
        energy_recursiva.append(mean_energy_recursiva)
    else:
        energy_recursiva.append(0)

ax_recursiva.plot(fibonacci, energy_recursiva, marker='o')
ax_recursiva.set_xlabel('Fibonacci')
ax_recursiva.set_ylabel('Package')
ax_recursiva.legend(['Consumo de Energia'])
fig_recursiva.savefig(os.path.join(output_dir, 'O0_consumo_energia_recursiva.png'))

# Temperatura para Fibonacci Linear
fig_linear, ax_linear = plt.subplots()
temperature_linear = []
for program in fibonacci:
    filtered_data_linear = data[data['Function'].str.contains(f'FibonacciLinear_{program}')]
    if not filtered_data_linear.empty:
        mean_temperature_linear = filtered_data_linear['Temperature'].mean()  
        print(f"Temperatura para FibonacciLinear({program}): {mean_temperature_linear}")
        temperature_linear.append(mean_temperature_linear)
    else:
        temperature_linear.append(0)

ax_linear.plot(fibonacci, temperature_linear, marker='o')
ax_linear.set_xlabel('Fibonacci')
ax_linear.set_ylabel('Temperature')
ax_linear.legend(['Temperatura'])
fig_linear.savefig(os.path.join(output_dir, 'O0_temperatura_linear.png'))

# Temperatura para Fibonacci Recursiva
fig_recursiva, ax_recursiva = plt.subplots()
temperature_recursiva = []
for program in fibonacci:
    filtered_data_recursiva = data[data['Function'].str.contains(f'FibonacciRecursiva_{program}')]
    if not filtered_data_recursiva.empty:
        mean_temperature_recursiva = filtered_data_recursiva['Temperature'].mean()  
        print(f"Temperatura para FibonacciRecursiva({program}): {mean_temperature_recursiva}")
        temperature_recursiva.append(mean_temperature_recursiva)
    else:
        temperature_recursiva.append(0)

ax_recursiva.plot(fibonacci, temperature_recursiva, marker='o')
ax_recursiva.set_xlabel('Fibonacci')
ax_recursiva.set_ylabel('Temperature')
ax_recursiva.legend(['Temperatura'])
fig_recursiva.savefig(os.path.join(output_dir, 'O0_temperatura_recursiva.png'))

# Core para Fibonacci Linear
fig_linear, ax_linear = plt.subplots()
core_linear = []
for program in fibonacci:
    filtered_data_linear = data[data['Function'].str.contains(f'FibonacciLinear_{program}')]
    if not filtered_data_linear.empty:
        mean_core_linear = filtered_data_linear['Core'].mean()  
        print(f"Core para FibonacciLinear({program}): {mean_core_linear}")
        core_linear.append(mean_core_linear)
    else:
        core_linear.append(0)

ax_linear.plot(fibonacci, core_linear, marker='o')
ax_linear.set_xlabel('Fibonacci')
ax_linear.set_ylabel('Core')
ax_linear.legend(['Core'])
fig_linear.savefig(os.path.join(output_dir, 'O0_core_linear.png'))

# Core para Fibonacci Recursiva
fig_recursiva, ax_recursiva = plt.subplots()
core_recursiva = []
for program in fibonacci:
    filtered_data_recursiva = data[data['Function'].str.contains(f'FibonacciRecursiva_{program}')]
    if not filtered_data_recursiva.empty:
        mean_core_recursiva = filtered_data_recursiva['Core'].mean()  
        print(f"Core para FibonacciRecursiva({program}): {mean_core_recursiva}")
        core_recursiva.append(mean_core_recursiva)
    else:
        core_recursiva.append(0)

ax_recursiva.plot(fibonacci, core_recursiva, marker='o')
ax_recursiva.set_xlabel('Fibonacci')
ax_recursiva.set_ylabel('Core')
ax_recursiva.legend(['Core'])
fig_recursiva.savefig(os.path.join(output_dir, 'O0_core_recursiva.png'))

# Memória para Fibonacci Linear
fig_linear, ax_linear = plt.subplots()
memory_linear = []
for program in fibonacci:
    filtered_data_linear = data[data['Function'].str.contains(f'FibonacciLinear_{program}')]
    if not filtered_data_linear.empty:
        mean_memory_linear = filtered_data_linear['Memory'].mean()  
        print(f"Memória para FibonacciLinear({program}): {mean_memory_linear}")
        memory_linear.append(mean_memory_linear)
    else:
        memory_linear.append(0)

ax_linear.plot(fibonacci, memory_linear, marker='o')
ax_linear.set_xlabel('Fibonacci')
ax_linear.set_ylabel('Memory')
ax_linear.legend(['Memory'])
fig_linear.savefig(os.path.join(output_dir, 'O0_memory_linear.png'))

# Memória para Fibonacci Recursiva
fig_recursiva, ax_recursiva = plt.subplots()
memory_recursiva = []
for program in fibonacci:
    filtered_data_recursiva = data[data['Function'].str.contains(f'FibonacciRecursiva_{program}')]
    if not filtered_data_recursiva.empty:
        mean_memory_recursiva = filtered_data_recursiva['Memory'].mean()  
        print(f"Memória para FibonacciRecursiva({program}): {mean_memory_recursiva}")
        memory_recursiva.append(mean_memory_recursiva)
    else:
        memory_recursiva.append(0)

ax_recursiva.plot(fibonacci, memory_recursiva, marker='o')
ax_recursiva.set_xlabel('Fibonacci')
ax_recursiva.set_ylabel('Memory')
ax_recursiva.legend(['Memory'])
fig_recursiva.savefig(os.path.join(output_dir, 'O0_memory_recursiva.png'))

# DRAM para Fibonacci Linear
fig_linear, ax_linear = plt.subplots()
dram_linear = []
for program in fibonacci:
    filtered_data_linear = data[data['Function'].str.contains(f'FibonacciLinear_{program}')]
    if not filtered_data_linear.empty:
        mean_dram_linear = filtered_data_linear['DRAM'].mean()  
        print(f"DRAM para FibonacciLinear({program}): {mean_dram_linear}")
        dram_linear.append(mean_dram_linear)
    else:
        dram_linear.append(0)

ax_linear.plot(fibonacci, dram_linear, marker='o')
ax_linear.set_xlabel('Fibonacci')
ax_linear.set_ylabel('DRAM')
ax_linear.legend(['DRAM'])
fig_linear.savefig(os.path.join(output_dir, 'O0_dram_linear.png'))

# DRAM para Fibonacci Recursiva
fig_recursiva, ax_recursiva = plt.subplots()
dram_recursiva = []
for program in fibonacci:
    filtered_data_recursiva = data[data['Function'].str.contains(f'FibonacciRecursiva_{program}')]
    if not filtered_data_recursiva.empty:
        mean_dram_recursiva = filtered_data_recursiva['DRAM'].mean()  
        print(f"DRAM para FibonacciRecursiva({program}): {mean_dram_recursiva}")
        dram_recursiva.append(mean_dram_recursiva)
    else:
        dram_recursiva.append(0)

ax_recursiva.plot(fibonacci, dram_recursiva, marker='o')
ax_recursiva.set_xlabel('Fibonacci')
ax_recursiva.set_ylabel('DRAM')
ax_recursiva.legend(['DRAM'])
fig_recursiva.savefig(os.path.join(output_dir, 'O0_dram_recursiva.png'))