# importing important modules
import tkinter
import customtkinter as ct


# importing files
import Register, Task


# Login class
class LoginManager(ct.CTkFrame):
    def __init__(self, root, master, **kwargs):
        super().__init__(master, **kwargs)

        # Widgets ->
        
        self.login_label = ct.CTkLabel(self, text="Login to your Account", font=("Century Gothic", 20))
        self.login_label.grid(row=0, column=0, columnspan=3, padx=40, pady=20)

        self.user_entry = ct.CTkEntry(self, width=220, placeholder_text="Username",  corner_radius=8)
        self.user_entry.grid(row=1, column=0, columnspan=3, padx=40, pady=20)
        
        self.pwd_entry = ct.CTkEntry(self, width=220, placeholder_text="Password", corner_radius=8, show='*')
        self.pwd_entry.grid(row=2, column=0, columnspan=3, padx=40, pady=20)


        # Button functions

        def forget_pwd():
            pass

        
        def login_app():
            self.place_forget()
            root.show_frame(Task.TaskManager)


        def login_function():
            username = self.user_entry.get()
            password = self.pwd_entry.get()
            details = (username != "") and (password != "")
            if details:
                # login logic
                # if username == "admin" and password == "password":
                login_app()
                # else:
                #     tkinter.messagebox.showerror("Error", "Password does not match")
                # pass
            else:
                tkinter.messagebox.showerror("Error", "Please fill all the fields")

        

        self.forget_pwd_btn = ct.CTkButton(self, text="Forget Password", text_color="white", fg_color="transparent", width=0)
        self.forget_pwd_btn.grid(row=3, column=2)

        self.login_btn = ct.CTkButton(self, text="Login", corner_radius=6, width=220, command= login_function)
        self.login_btn.grid(row=4, column=0, padx=40, pady=(20, 10), columnspan=3)
        
        self.register_btn = ct.CTkButton(self, text="Register User", corner_radius=6, width=220, command= lambda :  root.show_frame(Register.RegisterManager))
        self.register_btn.grid(row=5, column=0, padx=40, pady=20, columnspan=3)

