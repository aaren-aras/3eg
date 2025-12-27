import mne

raw = mne.io.read_raw_edf(
    "data/raw/subject01/session01.edf",
    preload=True
)

# Band-pass filter (classic EEG)
raw.filter(l_freq=1.0, h_freq=40.0)

# Notch filter (powerline)
raw.notch_filter(freqs=[60])  # or 50 depending on region

# Re-reference
raw.set_eeg_reference("average")

# Save cleaned data
raw.save(
    "data/processed/subject01_session01_clean.fif",
    overwrite=True
)
