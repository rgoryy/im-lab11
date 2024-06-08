import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare


def generate_normal_distribution(mean, variance, size):
    return np.random.normal(mean, np.sqrt(variance), size)


def plot_histogram(data, title):
    plt.hist(data, bins=10, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()


def calculate_chi_square(data):
    observed, _ = np.histogram(data, bins=10)
    expected = np.full_like(observed, len(data) / 10)
    chi2, p = chisquare(observed, expected)
    return chi2, p


def generate_and_plot_distribution(mean, variance, size, index):
    data = generate_normal_distribution(mean, variance, size)
    plot_histogram(data, f'Normal Distribution Histogram - Sample {index}')
    chi2, p = calculate_chi_square(data)
    label_result.config(text=f"Chi-square value: {chi2}, p-value: {p}")


root = tk.Tk()
root.title("Normal Distribution Generator")
root.geometry("400x300")

label_mean = ttk.Label(root, text="Mean:")
label_mean.pack()
entry_mean = ttk.Entry(root)
entry_mean.pack()

label_variance = ttk.Label(root, text="Variance:")
label_variance.pack()
entry_variance = ttk.Entry(root)
entry_variance.pack()

label_size = ttk.Label(root, text="Sample Size:")
label_size.pack()
entry_size = ttk.Entry(root)
entry_size.pack()

button_submit = ttk.Button(root, text="Generate and Plot", command=lambda: on_submit())
button_submit.pack()

label_result = ttk.Label(root, text="")
label_result.pack()


def on_submit():
    mean = float(entry_mean.get())
    variance = float(entry_variance.get())
    sizes = [10, 100, 1000]
    for i, size in enumerate(sizes):
        generate_and_plot_distribution(mean, variance, size, i + 1)


root.mainloop()