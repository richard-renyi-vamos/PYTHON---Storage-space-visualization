import os
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def get_folder_sizes(directory):
    folder_sizes = {}
    
    for foldername in os.listdir(directory):
        folder_path = os.path.join(directory, foldername)
        if os.path.isdir(folder_path):
            total_size = sum(os.path.getsize(os.path.join(dp, f)) for dp, dn, filenames in os.walk(folder_path) for f in filenames)
            folder_sizes[foldername] = total_size / (1024 * 1024)  # Convert to MB
    
    return folder_sizes

def visualize_storage():
    directory = filedialog.askdirectory()
    if not directory:
        return
    
    folder_sizes = get_folder_sizes(directory)
    
    if not folder_sizes:
        print("No subfolders found.")
        return
    
    labels = list(folder_sizes.keys())
    sizes = list(folder_sizes.values())
    
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.title(f"Storage Space Usage in {os.path.basename(directory)}")
    plt.show()

# GUI Setup
root = tk.Tk()
root.title("Storage Space Visualizer")
root.geometry("300x150")

btn = tk.Button(root, text="Select Folder", command=visualize_storage)
btn.pack(expand=True)

root.mainloop()
