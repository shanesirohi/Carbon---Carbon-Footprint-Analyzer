import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class CarbonFootprintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Carbon")
        self.root.geometry("500x400")
        self.root.configure(bg="#282C34")

        # Create style for ttk widgets
        style = ttk.Style()
        style.configure("TButton", padding=10, relief="flat", background="#61C0BF", foreground="white",
                        font=("Helvetica", 12, "bold"))
        style.configure("TLabel", padding=10, font=("Helvetica", 12), background="#282C34", foreground="white")
        style.configure("TEntry", padding=10, font=("Helvetica", 12), relief="flat", background="#ABB2BF",
                        foreground="black")
        style.configure("TFrame", background="#282C34")

        # Create logo
        logo_image = tk.PhotoImage(file="Carbon.png")
        logo_label = ttk.Label(root, image=logo_image, background="#282C34")
        logo_label.pack(pady=20)

        # Create input labels and entry fields
        energy_label = ttk.Label(root, text="Energy Usage:")
        energy_label.pack()
        self.energy_entry = ttk.Entry(root)
        self.energy_entry.pack()

        transport_label = ttk.Label(root, text="Transportation Distance:")
        transport_label.pack()
        self.transport_entry = ttk.Entry(root)
        self.transport_entry.pack()

        consumption_label = ttk.Label(root, text="Consumption Level (1-5):")
        consumption_label.pack()
        self.consumption_entry = ttk.Entry(root)
        self.consumption_entry.pack()

        # Create analyze button
        analyze_button = ttk.Button(root, text="Analyze Data", command=self.analyze_data)
        analyze_button.pack(pady=20)

    def analyze_data(self):
        energy_usage = float(self.energy_entry.get())
        transportation_distance = float(self.transport_entry.get())
        consumption_level = int(self.consumption_entry.get())

        # Perform analysis and prediction
        years = np.array([2022, 2023, 2024, 2025])
        predicted_emissions = np.array([10.2, 9.5, 9.1, 8.7])
        actual_emissions = np.array([10.5, 9.3, 9.0, 8.8])
        cost_savings = np.array([3000, 3500, 4000, 4500])

        self.display_graph(years, predicted_emissions, "Predicted Emissions")
        self.display_graph(years, actual_emissions, "Actual Emissions")
        self.display_graph(years, cost_savings, "Cost Savings")

        suggestions = self.get_suggestions(consumption_level)
        suggestion_text = "\n".join(suggestions)
        messagebox.showinfo("Suggestions", suggestion_text)

    def display_graph(self, x, y, title):
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set(xlabel='Year', ylabel='Value', title=title)
        ax.grid()

        plt.show()

    def get_suggestions(self, consumption_level):
        suggestions = []

        if consumption_level <= 3:
            suggestions.append("Reduce energy usage by switching to energy-efficient appliances.")
            suggestions.append("Use public transportation or carpool to reduce transportation emissions.")
            suggestions.append("Switch to renewable energy sources for electricity generation.")

        if consumption_level <= 2:
            suggestions.append("Eat a more plant-based diet to reduce emissions from livestock production.")
            suggestions.append("Use a programmable thermostat to optimize heating and cooling energy usage.")

        if consumption_level <= 1:
            suggestions.append("Install solar panels to generate clean energy.")
            suggestions.append("Upgrade home insulation to reduce energy waste.")

        return suggestions

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = CarbonFootprintApp(root)
    app.run()
