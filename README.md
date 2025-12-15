Ontology-Based Intelligent Tutoring System for Area Calculation
Overview
This project presents an Ontology-Based Intelligent Tutoring System (ITS) designed to support learners in understanding and calculating the area of basic geometric shapes. The system integrates knowledge representation using an ontology with a graphical user interface (GUI) to provide interactive feedback, visual explanations, and step-by-step guidance.
The ITS focuses on fundamental geometry concepts, including the area of Triangle, Rectangle, Square, and Circle, and is intended for beginner-level learners.

Key Features
•	Ontology-driven shape and parameter selection
•	Interactive graphical user interface developed using Python Tkinter
•	Dynamic input fields generated from ontology restrictions
•	Automatic area calculation and correctness evaluation
•	Visual representation of selected shapes with labelled dimensions (cm)
•	Immediate feedback and formula-based suggestions for incorrect answers
•	Offline execution without internet dependency

System Architecture
The system is composed of the following components:
1.	Domain Model (Ontology)
o	Developed using Protégé and OWL
o	Represents shapes, parameters, formulas, and units
o	Supports semantic reasoning and structured knowledge representation
2.	Application Layer (Python)
o	Implements the tutoring logic and user interface
o	Interacts with the ontology using the owlready2 library
3.	User Interface
o	Enables shape selection, parameter input, and answer submission
o	Displays feedback and visual representations to support learning

Technologies Used
•	Python 3
•	Tkinter (GUI development)
•	Owlready2 (Ontology integration)
•	Protégé (Ontology modelling)
•	OWL (Web Ontology Language)

Installation and Setup
Prerequisites
Ensure Python 3 is installed along with the required library:
pip install owlready2
Files Required
•	ShapeMathOntology.owl – Ontology file
•	main.py (or equivalent) – Python application file
Both files must be placed in the same directory.

How to Run
1.	Open a terminal in the project directory
2.	Execute the program:
python main.py
3.	Select a shape from the dropdown
4.	Enter required dimensions in centimetres
5.	Submit your calculated area
6.	View feedback and visual explanation

Educational Value
This ITS demonstrates how ontology-based knowledge representation can enhance traditional learning tools by enabling:
•	Structured domain modelling
•	Intelligent feedback generation
•	Visual and interactive learning support
The system bridges the gap between static learning resources and interactive tutoring by combining AI concepts with practical application development.

Limitations
•	The system covers only basic area calculations
•	No student modelling or adaptive learning is implemented
•	Reasoning is limited to predefined domain rules
________________________________________
Future Improvements
•	Integration of student performance tracking
•	Expansion to additional mathematical topics
•	Advanced misconception modelling using ontology reasoning
•	Web-based deployment for broader accessibility

Author
Developed as part of an academic project on Artificial Intelligence and Intelligent Tutoring Systems.

