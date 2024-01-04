#firstly, import tkinter as tk, 
#and then import tkinter as ttk to use the comobox for gender 
#and lastly import mysql.connector to make sure it will connect to database
import tkinter as tk
from tkinter import ttk



def collect_data():
    participant_full_name = participant_full_name_entry.get()
    print("Full Name: ", participant_full_name)
    participant_email = participant_email_entry.get()
    print("Email: ", participant_email)
    participant_phone_no = int (participant_phone_no_entry.get())
    print ("Phone Number: ", participant_phone_no )
    participant_age = int(participant_age_spinbox.get())
    print("Age: ", participant_age)
    participant_gender = participant_gender_combobox.get()
    print("Gender:", participant_gender)
    registration_fee = 25 #registration fee
    print ("Your registration fee is RM", registration_fee)

    
    # Function to calculate fee based on age
    def calculate_fee():
        registration_fee = 25  # Default registration fee
        if participant_age < 18:
            registration_fee = 25 - (0.1 * 25)  # 10% discount for participant age under 18
        elif participant_age >= 50:
            registration_fee = 25 - (0.15 * 25)  # 15% discount for participant age 50 and above
        return registration_fee

    fee_value = calculate_fee()

    # Display the registration fee in the label
    registration_fee_label.config(text=f'Your registration fee is RM {fee_value:.2f}')



# Create GUI
root = tk.Tk()
root.configure(background="light blue")
root.title("5K Run Registration Form")
root.geometry('400x510')
# To center the root on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = (screen_width - 500) // 0.5
y_coordinate = (screen_height - 540) // 0.5

# the big title for the form page
label = tk.Label(root, text='5K RUN REGISTRATION', font=("Baskerville Old Face", '14', "bold"), bg="light blue")
label.grid(row=0, column=0, padx=10, pady=10)

frame = tk.Frame(root, bg="light blue")
frame.grid(row=1, column=0)

# Participant Information Frame
participant_info_frame = tk.LabelFrame(frame, text="Participant Information", font=("Times New Roman", 11), bg="gray", width=300)  
participant_info_frame.grid(row=0, column=0, padx=10, pady=20 , rowspan=3, columnspan=7, sticky="nsew")

participant_full_name = tk.Label(participant_info_frame, text="Full Name", font=("Times New Roman", 11), bg="gray")
participant_full_name.grid(row=1, column=0, padx=(0,5))
participant_full_name_entry = tk.Entry(participant_info_frame, width=27)
participant_full_name_entry.grid(row=1, column=5)

participant_email = tk.Label(participant_info_frame, text="Email", font=("Times New Roman", 11), bg="gray")
participant_email.grid(row=2, column=0, padx=(0,5))
participant_email_entry = tk.Entry(participant_info_frame, width=27)
participant_email_entry.insert(0, "@gmail.com")  # this value will show up at the emial entry box
participant_email_entry.grid(row=2, column=5)

participant_phone_no = tk.Label(participant_info_frame, text="Number Phone ", font=("Times New Roman", 11), bg="gray")
participant_phone_no.grid (row=3, column=0, padx=(0,5))
participant_phone_no_entry =tk.Entry (participant_info_frame, width=27)
participant_phone_no_entry.grid (row=3, column=5)

participant_age = tk.Label(participant_info_frame, text="Age", font=("Times New Roman", 11), bg="gray")
participant_age.grid(row=4, column=0, padx=(0,5) )
participant_age_spinbox = tk.Spinbox(participant_info_frame, width=25, from_=12, to=100) #open for 12 years old until 100 years old
participant_age_spinbox.grid(row=4, column=5)

participant_gender = tk.Label(participant_info_frame, text="Gender", font=("Times New Roman", 11), bg="gray")
participant_gender.grid(row=5, column=0, padx=(0,5))
participant_gender_combobox = ttk.Combobox(participant_info_frame, width=25, values=["Male", "Female"])
participant_gender_combobox.grid(row=5, column=5)

for widget in participant_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=6)


# Registration Fee and Discount Frame
registration_fee_and_discount_frame = tk.LabelFrame(frame, text="Registration Fee and Discount", font=("Times New Roman", 11), bg="gray")
registration_fee_and_discount_frame.grid(row=5, column=0, padx=20, pady=10, rowspan=3, sticky="nsew")

registration_fee = tk.StringVar()
registration_fee_info = (
    "The registration fee is only RM25\n"
    "Participant age under 18 will get 10% discount\n"
    "Participant age 50 and above will get 15% discount\n"
)
label = tk.Label(registration_fee_and_discount_frame, textvariable=registration_fee, justify=tk.LEFT, font=("Times New Roman", 11), bg="white")
label.grid(row=0, column=0, padx=10, pady=5)
registration_fee.set(registration_fee_info)

# Label to display the calculated registration fee
registration_fee_label = tk.Label(registration_fee_and_discount_frame, text="", font=("Times New Roman", 11), bg="gray")
registration_fee_label.grid(row=1, column=0, padx=10, pady=5)

# Register button for user to complete their registration process
register_button = tk.Button( text="Register", font=("Times New Roman", 11), bg="gray", command=collect_data)
register_button.grid(row=6, pady=20)
register_button.config

# Configure grid weights to make the frames expandable
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

root.mainloop()