import tkinter as tk
from tkinter import ttk, messagebox
from owlready2 import *
import math

# -----------------------------
# Load Ontology
# -----------------------------
onto = get_ontology("ShapeMathOntology.owl").load()
Shape = onto.Shape

# -----------------------------
# Get all shapes (including nested subclasses)
# -----------------------------
def get_all_shapes(cls):
    result = []
    for sub in cls.subclasses():
        result.append(sub)
        result.extend(get_all_shapes(sub))
    return result

shape_classes = get_all_shapes(Shape)

# -----------------------------
# Read parameters from ontology
# -----------------------------
def get_parameters(shape_class):
    params = set()
    for axiom in shape_class.is_a:
        if isinstance(axiom, Restriction):
            if axiom.property.name == "hasParameter":
                if hasattr(axiom.value, "name"):
                    params.add(axiom.value.name.replace("Parameter", ""))
    return list(params)

# -----------------------------
# Area calculation
# -----------------------------
def calculate_area(shape, values):
    if shape == "Triangle":
        return 0.5 * values["Base"] * values["Height"]
    if shape == "Square":
        return values["Side"] ** 2
    if shape == "Rectangle":
        return values["Length"] * values["Width"]
    if shape == "Circle":
        return math.pi * values["Radius"] ** 2

# -----------------------------
# Draw shape with dimension labels
# -----------------------------
def draw_shape(shape, values):
    canvas.delete("all")

    if shape == "Triangle":
        canvas.create_polygon(120, 200, 220, 60, 320, 200,
                              outline="black", fill="#cce5ff", width=2)
        canvas.create_text(220, 210, text=f"Base = {values['Base']} cm")
        canvas.create_text(330, 130, text=f"Height = {values['Height']} cm")

    elif shape == "Rectangle":
        canvas.create_rectangle(100, 80, 340, 220,
                                outline="black", fill="#d4edda", width=2)
        canvas.create_text(220, 240, text=f"Length = {values['Length']} cm")
        canvas.create_text(360, 150, text=f"Width = {values['Width']} cm", anchor="w")

    elif shape == "Square":
        canvas.create_rectangle(140, 80, 300, 240,
                                outline="black", fill="#fff3cd", width=2)
        canvas.create_text(220, 260, text=f"Side = {values['Side']} cm")

    elif shape == "Circle":
        canvas.create_oval(120, 80, 320, 280,
                           outline="black", fill="#f8d7da", width=2)
        canvas.create_text(330, 180, text=f"Radius = {values['Radius']} cm", anchor="w")

# -----------------------------
# Tkinter UI
# -----------------------------
root = tk.Tk()
root.title("Ontology-Based Intelligent Tutoring System – Area Tutor")
root.geometry("500x780")

frame_shape = tk.LabelFrame(root, text="Step 1: Choose Shape")
frame_params = tk.LabelFrame(root, text="Step 2: Enter Parameters")
frame_answer = tk.LabelFrame(root, text="Step 3: Your Answer")
frame_feedback = tk.LabelFrame(root, text="Tutor Feedback")
frame_canvas = tk.LabelFrame(root, text="Visual Representation (with dimensions)")

for f in (frame_shape, frame_params, frame_answer, frame_feedback, frame_canvas):
    f.pack(fill="x", padx=5, pady=5)

canvas = tk.Canvas(frame_canvas, width=460, height=320, bg="white")
canvas.pack()

entries = {}

# -----------------------------
# Utility
# -----------------------------
def clear_frame(frame):
    for w in frame.winfo_children():
        w.destroy()

# -----------------------------
# Shape selection
# -----------------------------
def on_shape_selected(event=None):
    clear_frame(frame_params)
    clear_frame(frame_answer)
    clear_frame(frame_feedback)
    canvas.delete("all")
    entries.clear()

    shape_name = shape_var.get()
    shape_class = onto[shape_name]
    parameters = get_parameters(shape_class)

    if not parameters:
        tk.Label(frame_params, text="❌ No parameters defined in ontology").pack()
        return

    for p in parameters:
        tk.Label(frame_params, text=f"{p} (cm)").pack(anchor="w")
        e = tk.Entry(frame_params)
        e.pack()
        entries[p] = e

    tk.Label(frame_answer, text="Enter YOUR area answer:").pack()
    global student_entry
    student_entry = tk.Entry(frame_answer)
    student_entry.pack()

    tk.Button(frame_answer, text="Submit", command=evaluate).pack(pady=5)

# -----------------------------
# Evaluation
# -----------------------------
def evaluate():
    clear_frame(frame_feedback)

    try:
        values = {k: float(v.get()) for k, v in entries.items()}
        student = float(student_entry.get())
    except:
        messagebox.showerror("Error", "Please enter numeric values only.")
        return

    shape = shape_var.get()
    correct = calculate_area(shape, values)

    draw_shape(shape, values)

    tk.Label(frame_feedback, text=f"Shape Selected: {shape}",
             font=("Arial", 11, "bold")).pack(anchor="w")

    tk.Label(frame_feedback, text="Parameters used:",
             font=("Arial", 10, "bold")).pack(anchor="w")

    for k, v in values.items():
        tk.Label(frame_feedback, text=f"• {k} = {v} cm").pack(anchor="w")

    if math.isclose(student, correct, rel_tol=1e-9):
        tk.Label(frame_feedback, text="✅ Correct Answer! Well done.",
                 fg="green", font=("Arial", 13, "bold")).pack(pady=6)
    else:
        tk.Label(frame_feedback, text="❌ Incorrect Answer.",
                 fg="red", font=("Arial", 13, "bold")).pack(pady=6)

        if shape == "Triangle":
            hint = "Area = (Base × Height) / 2"
        elif shape == "Rectangle":
            hint = "Area = Length × Width"
        elif shape == "Square":
            hint = "Area = Side × Side"
        elif shape == "Circle":
            hint = "Area = π × Radius²"

        tk.Label(frame_feedback, text="Suggestion:",
                 font=("Arial", 11, "bold")).pack(anchor="w")
        tk.Label(frame_feedback, text=hint,
                 font=("Arial", 10, "italic")).pack(anchor="w")

    tk.Label(frame_feedback,
             text=f"Correct Area = {round(correct, 3)} cm²",
             font=("Arial", 11)).pack(pady=4)

# -----------------------------
# Dropdown
# -----------------------------
shape_var = tk.StringVar()
shape_box = ttk.Combobox(
    frame_shape,
    textvariable=shape_var,
    state="readonly",
    values=[cls.name for cls in shape_classes]
)
shape_box.pack()
shape_box.bind("<<ComboboxSelected>>", on_shape_selected)

root.mainloop()
