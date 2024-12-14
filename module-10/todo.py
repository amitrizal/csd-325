import tkinter as tk
import tkinter.messagebox as msg

class TodoApp(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()
        
        # Initialize tasks
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # Configure the window
        self.title("Rizal-ToDo")
        self.geometry("300x400")
        
        # Create menu
        menu = tk.Menu(self, bg="blue", fg="white")
        file_menu = tk.Menu(menu, tearoff=0, bg="blue", fg="white")
        file_menu.add_command(label="Exit", command=self.quit)
        menu.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu)
        
        # Canvas and frames
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Pack widgets
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")
        
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()
        
        # Default task with instructions
        todo1 = tk.Label(self.tasks_frame, text="--- Add Items Here --- **Right-Click to Delete**", bg="lightgrey", fg="black", pady=10)
        todo1.bind("<Button-3>", self.remove_task)
        self.tasks.append(todo1)
        
        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)
        
        # Key bindings
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.tasks_canvas.bind("<Configure>", self.task_width)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        
        # Color schemes for alternating tasks
        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

        # Label to display the total number of tasks
        self.task_count_label = tk.Label(self, text=f"Total number of Students: {len(self.tasks) - 1}", bg="blue", fg="white")
        self.task_count_label.pack(side=tk.BOTTOM, fill=tk.X)
    
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()
        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)
            new_task.bind("<Button-3>", self.remove_task)  # Right-click to delete
            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)
            self.task_create.delete(1.0, tk.END)
            self.update_task_count()

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", f"Delete '{task.cget('text')}'?"):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()
            self.update_task_count()

    def update_task_count(self):
        """Update the total number of tasks displayed in the label."""
        self.task_count_label.config(text=f"Total number of Students: {len(self.tasks) - 1}")

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)
        my_scheme_choice = self.colour_schemes[task_style_choice]
        task.configure(bg=my_scheme_choice["bg"], fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")


if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
