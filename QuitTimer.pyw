import tkinter as tk
from datetime import datetime

class ElapsedTimeApp:
    def __init__(self, root):
        # Start date and time
        self.start_datetime = datetime(2024, 1, 9, 9, 30) # Edit this to your quit date. (Year, Month, Day, Hour, Minutes)
        self.cost_per_day = 75                            # Cost per day, edit this to your spending per day
        
        self.root = root
        self.root.title("Fuck Kratom!")
        self.root.geometry("275x100")
        
        # Keeping the window always on top
        self.root.attributes('-topmost', True)

        # Setting up the labels to display elapsed time
        bold_font = ('Helvetica', 16, 'bold')
        self.hours_label = tk.Label(self.root, font=bold_font)
        self.hours_label.pack(expand=True)
        
        self.days_label = tk.Label(self.root, font=bold_font)
        self.days_label.pack(expand=True)

        self.cost_label = tk.Label(self.root, font=bold_font)
        self.cost_label.pack(expand=True)

        # Update the labels every second
        self.update_labels()

    def update_labels(self):
        # Calculate the elapsed time
        current_time = datetime.now()
        elapsed_time = current_time - self.start_datetime
        elapsed_hours = elapsed_time.total_seconds() / 3600  # hours with fractional part
        elapsed_days = elapsed_time.total_seconds() / (3600 * 24)  # days with fractional part

        # Calculate the total cost
        total_cost = elapsed_days * self.cost_per_day

        # Update the labels text
        self.hours_label.config(text=f"T+{elapsed_hours:.2f} hours")
        self.days_label.config(text=f"T+{elapsed_days:.2f} days")
        self.cost_label.config(text=f"Total Savings: ${total_cost:.2f}")

        # Schedule the labels to be updated after 1 second
        self.root.after(1000, self.update_labels)

# Create the main window
root = tk.Tk()
app = ElapsedTimeApp(root)

# Run the application
root.mainloop()
