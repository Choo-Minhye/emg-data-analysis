import pandas as pd
from signal_processing import bp_filter, notch_filter, plot_signal
from feature_extraction import features_estimation

# Load data from Excel file
signal_path = 'data/emg.xlsx'
# signal_path = 'data/220624_EMG_3.xlsx'
emg_signal = pd.read_excel(signal_path).values
channel_name = 'Raw EMG Data'

# Sampling Frequency of 1000 (2000 Samples per second)
sampling_frequency = 1e3
frame = 500
step = 250

# Plot raw sEMG signal
plot_signal(emg_signal, sampling_frequency, channel_name)

emg_signal = emg_signal.reshape((emg_signal.size,))
# Band Stop Filter (BSF)
filtered_signal = notch_filter(emg_signal, sampling_frequency,
                               True)
# Band Pass Filter (BPF)
filtered_signal = bp_filter(filtered_signal, 10, 20,
                            sampling_frequency, True)
