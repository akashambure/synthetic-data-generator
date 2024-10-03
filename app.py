from tkinter import *
from tkinter import messagebox, filedialog
from faker_module import DataGenerator
import pandas as pd

class Application:

    def __init__(self):
        # home page
        self.root = Tk()
        self.root.title("Synthetic Data Generator")
        self.root.geometry("600x600")
        self.root.config(bg="#B4A6A3")

        heading = Label(self.root, text="Synthetic Data Generator", bg="#B4A6A3", 
                        fg="black", font=("Helvetica", 24))
        heading.pack(pady=20)

        welcome_text = Label(self.root, text="Welcome to Synthetic Data Generator", 
                             bg="#B4A6A3", fg="black", font=("Helvetica", 16))
        welcome_text.pack(pady=20)

        # Create a frame to hold the buttons
        self.button_frame = Frame(self.root, bg="#B4A6A3")
        self.button_frame.pack(pady=20)

        # Create buttons and place them in three columns with increased gap

        # Name
        self.name_button = self.button_structure("Name")
        self.button_grid(self.name_button, 0, 0)

        # Age
        self.age_button = self.button_structure("Age")
        self.button_grid(self.age_button, 0, 1)

        # Language
        self.language_button = self.button_structure("Language")
        self.button_grid(self.language_button, 0, 2)

        # Mobile Number
        self.mobile_number_button = self.button_structure("Mobile Number")
        self.button_grid(self.mobile_number_button, 1, 0)

        # Email
        self.email_button = self.button_structure("Email")
        self.button_grid(self.email_button, 1, 1)

        # Address
        self.address_button = self.button_structure("Address")
        self.button_grid(self.address_button, 1, 2)

        # Postal Code
        self.postal_code_button = self.button_structure("Postal Code")
        self.button_grid(self.postal_code_button, 2, 0)

        # Aadhar Number
        self.aadhar_number_button = self.button_structure("Aadhar Number")
        self.button_grid(self.aadhar_number_button, 2, 1)

        # Job Title
        self.job_title_button = self.button_structure("Job Title")
        self.button_grid(self.job_title_button, 2, 2)

        # Salary
        self.salary_button = self.button_structure("Salary")
        self.button_grid(self.salary_button, 3, 0)

        # Bank Account Number
        self.bank_account_number_button = self.button_structure("Bank Account Number")
        self.button_grid(self.bank_account_number_button, 3, 1)

        # Bank Name 
        self.bank_name_button = self.button_structure("Bank Name")
        self.button_grid(self.bank_name_button, 3, 2)

        # Next button
        self.next_button = Button(self.button_frame, text="Next", bg="#AE7AF1", font=("Helvetica", 12), 
                                    width=20, height=2, command=lambda: self.generation_page())
        self.next_button.grid(row=4, column=2, padx=20, pady=30)  # Increased padx

        self.root.mainloop()

    def button_structure(self, text_name):
        return Button(self.button_frame, text=text_name, bg="#B4A6A3", font=("Helvetica", 12), 
                      width=20, height=2, command=lambda: self.change_color(text_name))
    
    def button_grid(self, button, row, column):
        button.grid(row=row, column=column, padx=20, pady=10)  # Increased padx

    # List to store the names of the clicked buttons
    clicked_button_names = []

    # function to change color of button if clicked
    def change_color(self, button_text):
        for widget in self.button_frame.winfo_children():
            if widget.cget("text") == button_text:
                widget.config(bg="green")
                self.clicked_button_name = button_text  # Save the button's name
                #print(f"Clicked button name: {self.clicked_button_name}")
                self.clicked_button_names.append(self.clicked_button_name)

    def generation_page(self):
        self.root.destroy()
        self.root = Tk()
        self.root.title("Synthetic Data Generator")
        self.root.geometry("600x600")
        self.root.config(bg="#B4A6A3")

        # text asking user how many records to generate

        self.n_records_text = Label(self.root, text="How many records do you want to generate?", bg="#B4A6A3", fg="black", font=("Helvetica", 16))
        self.n_records_text.pack(pady=20)

        self.n_records_entry = Entry(self.root, width=20)
        self.n_records_entry.pack(pady=20)

        # submit button
        self.submit_button = Button(self.root, text="Submit", bg="#AE7AF1", font=("Helvetica", 12), 
                                    width=20, height=2, command=lambda: self.generate_data())
        self.submit_button.pack(pady=20)

        # Back to home button

        self.back_button = Button(self.root, text="Back", bg="#AE7AF1", font=("Helvetica", 12), width=20, height=2, command=lambda: self.home_page())
        self.back_button.pack(pady=20)

        self.root.mainloop()

    def generate_data(self):
        # Create an instance of the DataGenerator class
        data_generator = DataGenerator(int(self.n_records_entry.get()))

        # Selecting the columns to be generated based on the clicked buttons

        if len(self.clicked_button_names) == 0:
            messagebox.showerror("Error", "Please select at least one column to generate data.")
        else:
            data = {}
            if 'Name' in self.clicked_button_names:
                data['Name'] = data_generator.names()
            if 'Age' in self.clicked_button_names:
                data['Age'] = data_generator.age()
            if 'Language' in self.clicked_button_names:
                data['Language'] = data_generator.lang()
            if 'Mobile Number' in self.clicked_button_names:
                data['Mobile Number'] = data_generator.mobile_numbers()
            if 'Email' in self.clicked_button_names:
                data['Email'] = data_generator.email()
            if 'Address' in self.clicked_button_names:
                data['Address'] = data_generator.address()
            if 'Postal Code' in self.clicked_button_names:
                data['Postal Code'] = data_generator.postcode()
            if 'Aadhar Number' in self.clicked_button_names:
                data['Aadhar Number'] = data_generator.aadhaar()
            if 'Job Title' in self.clicked_button_names:
                data['Job Title'] = data_generator.job()
            if 'Salary' in self.clicked_button_names:
                data['Salary'] = data_generator.esal()
            if 'Bank Account Number' in self.clicked_button_names:
                data['Bank Account Number'] = data_generator.bankac()
            if 'Bank Name' in self.clicked_button_names:
                data['Bank Name'] = data_generator.bank()

            df = pd.DataFrame(data)

            # Save the generated data to a file
            self.save_file(df)

    def save_file(self, df):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", 
                                                 filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            df.to_csv(file_path, index=False)
            messagebox.showinfo("Success", f"File saved at: {file_path}")

    def home_page(self):
        self.root.destroy()
        self.__init__()

app = Application()
