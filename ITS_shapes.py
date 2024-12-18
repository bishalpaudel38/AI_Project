from owlready2 import get_ontology
from tkinter import Tk, Label, Button, Listbox, Scrollbar, VERTICAL, RIGHT, Y, Frame, X, LEFT, BOTH, Entry, StringVar
from tkinter import ttk

# Load the ontology
ontology_file = "math_shapes_ontology.owl"  
ontology = get_ontology(ontology_file).load()

# Function to fetch classes
def fetch_classes():
    listbox.delete(0, "end")  # Clear the listbox
    for cls in ontology.classes():
        listbox.insert("end", f"Class: {cls.name}")

# Function to fetch individuals
def fetch_individuals():
    listbox.delete(0, "end")  # Clear the listbox
    for individual in ontology.individuals():
        listbox.insert("end", f"Individual: {individual.name}")

# Function to fetch object properties
def fetch_object_properties():
    listbox.delete(0, "end")  # Clear the listbox
    for prop in ontology.object_properties():
        listbox.insert("end", f"Object Property: {prop.name}")

# Function to fetch data properties
def fetch_data_properties():
    listbox.delete(0, "end")  # Clear the listbox
    for prop in ontology.data_properties():
        listbox.insert("end", f"Data Property: {prop.name}")

# Function to search in the ontology
def search_ontology():
    query = search_var.get().lower()  # Get search query and convert to lowercase
    listbox.delete(0, "end")  # Clear the listbox
    for cls in ontology.classes():
        if query in cls.name.lower():
            listbox.insert("end", f"Class: {cls.name}")
    for individual in ontology.individuals():
        if query in individual.name.lower():
            listbox.insert("end", f"Individual: {individual.name}")
    for prop in ontology.object_properties():
        if query in prop.name.lower():
            listbox.insert("end", f"Object Property: {prop.name}")
    for prop in ontology.data_properties():
        if query in prop.name.lower():
            listbox.insert("end", f"Data Property: {prop.name}")

# Build the enhanced UI
root = Tk()
root.title("Math Shapes Ontology Viewer")
root.geometry("700x600")
root.configure(bg="#f0f8ff")  # Set the background color to AliceBlue

# Header Label
header = Label(
    root,
    text="Math Shapes Ontology Viewer",
    font=("Helvetica", 20, "bold"),
    fg="white",
    bg="#4b0082",  # Indigo
    pady=10
)
header.pack(fill=X)

# Frame for search bar
search_frame = Frame(root, bg="#f0f8ff", pady=10)
search_frame.pack(fill=X)

search_var = StringVar()  # Variable to store the search query
search_label = Label(
    search_frame,
    text="Search:",
    font=("Arial", 12),
    bg="#f0f8ff",
    fg="#4b0082"
)
search_label.pack(side=LEFT, padx=10)

search_entry = Entry(
    search_frame,
    textvariable=search_var,
    font=("Arial", 12),
    width=30,
    relief="solid",
    bd=1
)
search_entry.pack(side=LEFT, padx=10)

search_button = ttk.Button(
    search_frame, text="Search", style="TButton", command=search_ontology
)
search_button.pack(side=LEFT, padx=10)

# Frame for buttons
button_frame = Frame(root, bg="#f0f8ff", pady=10)
button_frame.pack(fill=X)

# Styled Buttons
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)

class_button = ttk.Button(
    button_frame, text="Show Classes", style="TButton", command=fetch_classes
)
class_button.pack(side=LEFT, padx=10)

individual_button = ttk.Button(
    button_frame, text="Show Individuals", style="TButton", command=fetch_individuals
)
individual_button.pack(side=LEFT, padx=10)

object_prop_button = ttk.Button(
    button_frame, text="Show Object Properties", style="TButton", command=fetch_object_properties
)
object_prop_button.pack(side=LEFT, padx=10)

data_prop_button = ttk.Button(
    button_frame, text="Show Data Properties", style="TButton", command=fetch_data_properties
)
data_prop_button.pack(side=LEFT, padx=10)

# Frame for listbox
listbox_frame = Frame(root, bg="#f0f8ff")
listbox_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Scrollbar and Listbox
scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(
    listbox_frame,
    yscrollcommand=scrollbar.set,
    font=("Courier", 12),
    bg="#d8bfd8",  # Thistle
    fg="black",
    height=20,
    selectbackground="#4b0082",  # Indigo
    selectforeground="white"
)
listbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Footer Label
footer = Label(
    root,
    text="Math Shapes Ontology Viewer - Developed in Python",
    font=("Arial", 10),
    bg="#4b0082",  # Indigo
    fg="white",
    pady=5
)
footer.pack(fill=X)

# Run the application
root.mainloop()