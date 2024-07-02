import customtkinter as ct

class TaskManager(ct.CTkFrame):
    def __init__(self, root, master, **kwargs):
        super().__init__(master, **kwargs)
        # self.pack(fill="both", expand=True)
        # creating scrollable frame of all task
        self.all_task = ct.CTkScrollableFrame(self, label_text="Tasks ToDo", label_font=("Century Gothic", 20), height=300)
        self.all_task.pack(fill="both", expand=True)
        # creating frames for task values and manipulation
        def create_task():
            task_frame = ct.CTkFrame(self.all_task, corner_radius=10, width=300)
            task_frame.pack(fill="x", padx=10)
            task_frame.grid_columnconfigure(0, weight=1)
            # showing task value
            task_value = ct.CTkCheckBox(task_frame, text=task_entry.get())
            task_value.grid(row=0, column=0, padx=10, pady=10, sticky="w")
            
            task_entry.delete(0,"end")  # clear the entry to add new task

            # creating delete button for task
            # also delete from database
            delete_button = ct.CTkButton(task_frame, text="Delete",width=0, command=lambda: task_frame.pack_forget())
            delete_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")
            # creating edit button for task

            def edit_task():
                task_entry.insert(0, task_value.cget("text"))

            edit_button = ct.CTkButton(task_frame, text="Edit",width=0, command=edit_task)
            edit_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")


        # creating frame for entry and add button
        self.entry_frame = ct.CTkFrame(self, height=50, fg_color="transparent")
        self.entry_frame.pack(fill="both", pady=10)

        # creating task entry field and add button
        task_entry = ct.CTkEntry(self.entry_frame, width=450, height=30, placeholder_text="Enter Task", placeholder_text_color="gray")
        task_entry.grid(row=0, column=0, columnspan=2, padx=20)

        add_btn = ct.CTkButton(self.entry_frame, text="Add new task", width=0, command=create_task)
        add_btn.grid(row=0, column=2)