# clinic-patient-management-system

This is a python-based CLI application that demonstrates how small health clinics manage patient records,appointments, and medical history using Object Oriented Programming(OOP).  It consists of the following objects:
- **Receptionist** registers staff and patients and manages appointments
- **Admin** updates the credentials of staff members and patients
- **Nurse** views patient information, updates patient records, records vitals such as blood pressure and weight while checking the appointments
- **Doctor** views patient records, order lab tests, view lab results,prescriptions, and update patient status

![CLI Interface](demo_pics/cli_if.png)
*Main Interface*

![Admin's Interface](demo_pics/admin_if.png)
*Admin's Interface*

![Receptionist's Interface](demo_pics/receptionist_if.png)
*Receptionist's Interface*

![Nurse's Interface](demo_pics/nurse_if.png)
*Nurse's Interface*

![Doctor's Interface](demo_pics/doctor_if.png)
*Doctor's Interface*

## Prerequisites
Ensure you have installed Python in your machine:

```bash
python --version
```

**Optional**:Create and activate the Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
```

Fork [this repository](https://github.com/joshua-odero/clinic-patient-management-system.git) , then clone it to your preferred folder with the following command:

```bash
git clone <your SSH/Http path>
```

## Installing dependencies
Switch to the app directory using the **cd** command, Use the **pip** to install the project dependencies from pypi such as:
- **pytest** to run automated tests for the program
- **Rich** for styling terminal output (colors, formatting) 
- **iniconfig** and **pluggy** which are plugins used internally by pytest.

```bash
cd clinic-patient-management-system
```

```bash
pip install <package_name>
```
or

Install all the packages required by the Doctor module:

```bash
pip install -r Doctor/requirements.txt
```

## Running the project
In the project's root directory, execute the following command to run a .py script within the directory. Use **python** or **python3** commands depending on your OS:

```bash
python3 <example_file.py>
```
OR

```bash
python <example_file.py>
```
## Task assignment instructions
This OOP project has collaborators who handle different modules:
- **CLI entry point** by Joshua Odero
- **Receptionist Module** by Ronaldo Nyakwama
- **Admin Module** by Joshua Odero
- **Nurse Module** by Angela Musamali
- **Doctor Module** by Samantha Bora
