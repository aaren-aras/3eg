import mne

raw = mne.io.read_raw_fif(
    "data/processed/subject01_session01_clean.fif",
    preload=True
)

# Power spectral density
raw.plot_psd(fmax=50)

# Topomap (if montage is valid)
raw.plot_sensors(show_names=True)
