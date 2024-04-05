import tkinter as tk
from tkinter import messagebox

class SportsFacilityApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sports Facility Management System")

        # Initialize slots availability (0: available, 1: booked)
        self.slots = [0, 0, 0, 0, 0]

        # Create labels, buttons, and checkboxes
        self.label = tk.Label(master, text="Select a facility:")
        self.label.pack()

        self.facility_var = tk.StringVar(master)
        self.facility_var.set("Gym")  # Default facility
        self.facility_menu = tk.OptionMenu(master, self.facility_var, "Gym", "Squash Court", "Badminton Court")
        self.facility_menu.pack()

        self.check_button = tk.Button(master, text="Check Availability", command=self.check_availability)
        self.check_button.pack()

        self.book_button = tk.Button(master, text="Book Slot", command=self.book_slot)
        self.book_button.pack()

        self.slots_frame = tk.Frame(master)
        self.slots_frame.pack()
        self.slots_var = []
        for i in range(5):
            var = tk.IntVar()
            chk = tk.Checkbutton(self.slots_frame, text=f"Slot {i+1}: 2-{i+3}pm", variable=var)
            chk.pack(anchor=tk.W)
            self.slots_var.append(var)

    def check_availability(self):
        facility = self.facility_var.get()
        # Simulating availability (0: available, 1: booked)
        available_slots = [1, 0, 1, 1, 0]  # Example availability data
        for i, slot_status in enumerate(available_slots):
            self.slots_var[i].set(slot_status)

    def book_slot(self):
        facility = self.facility_var.get()
        selected_slots = [var.get() for var in self.slots_var]
        selected_indices = [i for i, val in enumerate(selected_slots) if val == 1]
        if selected_indices:
            for idx in selected_indices:
                self.slots[idx] = 1
            messagebox.showinfo("Booking", f"Slots {selected_indices} booked for {facility}.")
        else:
            messagebox.showwarning("Booking", "Please select at least one slot.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SportsFacilityApp(root)
    root.mainloop()
