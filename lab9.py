import numpy as np

# Function 1: Read values from a file into an array
# This function reads numerical values from a text file and stores them in a NumPy array.
def read_values_from_file(filename):
    with open(filename, 'r') as file:
        values = [float(line.strip()) for line in file if line.strip()]
    return np.array(values)
values_file = "./values.txt" # Relative path to the values file
print(read_values_from_file(values_file))

# Function 2: Read Oscillatory Wave Data and Compute Statistics
# This function reads a file containing wave data with length and amplitude values into a NumPy array.
# It also computes the mean and maximum amplitude.
def read_oscillatory_wave_data(filename):
    data = np.loadtxt(filename, delimiter=',') #Assuming CSV format with two columns: length, amplitude
    lengths = data[:, 0]
    amplitudes = data[:, 1]
    mean_amplitude = np.mean(amplitudes)
    max_amplitude = np.max(amplitudes)
    return data, mean_amplitude, max_amplitude 
wave_file = "./wave_data.csv" # Relative path to the wave data file
data, mean_amp, max_amp = read_oscillatory_wave_data(wave_file)
print(f"Mean Amplitude: {mean_amp}, Max Amplitude: {max_amp}") 

# Function 3: Read Standing Wave Data and Compute Wave Speed
# This function reads a file containing standing wave data with length and tension values into a NumPy array.
# It also computes the wave speed using v = sqrt(T/μ), where μ = mass per unit length (assumed to be 1 for simplicity).
def read_standing_wave_data(filename):
    data = np.loadtxt(filename, delimiter=',', dtype = float) #Assuming CSV format
    tensions = data[:, 1]
    mu = 1 # Assuming mass per unit length 
    wave_speeds = np.sqrt(tensions / mu)  # Assuming mass per unit lenght μ = 1 
    return data, wave_speeds 
standing_file = "./standing_wave.csv" # Relative path to the standing wave data file
data, wave_speeds = read_standing_wave_data(standing_file)
print(f"Wave Speeds: {wave_speeds}") 