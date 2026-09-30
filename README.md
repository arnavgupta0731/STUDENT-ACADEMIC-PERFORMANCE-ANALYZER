# Student Academic Performance Analyzer

## Project Description

Student Academic Performance Analyzer is a command-line Python application that allows to organize and analyze students' academic performance. User can add students' information and their marks in different subjects and receive total, average, grade, pass/fail, and class rank as an output. The program also provides information about the student's best and worst subjects to help the user understand the student's performance.

The project is suitable for a beginning programmer, as it covers functions, lists and dictionaries, classes, input validation, sorting, calculations, exceptions, modules, and basic automated testing. Program works with held records in memory for simplicity and is an appropriate for a simple Python application.

### Short Description

A Python command-line application that organizes students' marks and analyzes their academic performance by calculating grades, performance reports, subject statistics, class ranking, and strong/weak subjects.

## Main Features

- Student and marks management
- Subject-wise grade calculation
- Individual performance analysis
- Class and subject statistics
- Student ranking
- Strong/weak subject identification
- Input validation and error handling
- Simple console visualization
- Basic automated tests

## Technologies

- Python 3.10+
- Python standard library
- Git/GitHub
The application does not require any third-party Python packages.

## Project Structure

- `src/main.py` – Main menu and user interaction
- `src/models.py` – Student data model
- `src/student_manager.py` – Student record management
- `src/grade_calculator.py` – Grade and pass/fail calculation
- `src/performance_analyzer.py` – Individual/class performance analysis
- `src/subject_statistics.py` – Subject statistics
- `src/ranking.py` – Class ranking functionality
- `src/reporting.py` – Report generation and console visualization
- `src/validation.py` – Input validation and error handling
- `tests/test_project.py` – Validation tests

## How to Run

In the project directory, run the following command:

```text
python src/main.py
```

In the main menu, select the 8th option if you want to import some sample records to test the program.

## Testing

To run the tests, execute the following command:

```text
python tests/test_project.py
```
You should see the following output:

```text
All tests passed.
```
## Band of Grades

The application uses the following grades:

- 'A+': 90 - 100
- 'A': 80 - 89
- 'B': 70 - 79
- 'C': 60 - 69
- 'D': 50 - 59
- 'F': 0 - 49

The grade bands are part of the program's design specification.

## Restrictions and Limitations

Since this project is designed to demonstrate a simple Python application, the data is stored in memory and wiped out after the program is closed. This architecture is selected on purpose to focus on the CSE1021 programming concepts.

## Future Improvements
The following improvements could be made:
- Store data in external storage (files or database)

- Add new features, such as attendance tracking
- Add GUI (Graphical User Interface)
- Add report export function
- Add authentication and authorization