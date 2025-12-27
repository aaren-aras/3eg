import mne

# Load EDF / BDF / FIF / BrainVision
raw = mne.io.read_raw_edf(
    "data/raw/subject01/session01.edf",
    preload=True
)

print(raw.info)
print(raw.ch_names)

# Plot raw signals
raw.plot(
    duration=10,
    n_channels=8,
    scalings="auto"
)
