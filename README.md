# Hospital System

The Hospital System is a mini program for a digital service to help the Hospital to identify which patients are being helped. When starting the program, the user will be prompted to select one of the available features (see below).

There is two tables for the Hospital system, one is for patients and one is for doctors. The patients and doctors tables are like this:

```
Doctors Table
---------------
| ID | Name   |
| ---| ------ |
| 01 | John   |
| 02 | Greg   |
| 03 | Emily  |
| 04 | Lee    |
| 05 | Melody |
| 06 | Bertha |
---------------

Patients Table
--------------------------------
| ID | Name    | Doctor's ID   |
| ---| ------- | ------------- |
| 01 | Carolyn |       05      |
| 02 | Dennis  |       01      |
| 03 | Sean    |       03      |
| 04 | Lillian |       04      |
| 05 | Michael |       03      |
| 06 | Janet   |       02      |
| 07 | Linda   |       06      |
--------------------------------
```

## Running the program

* The program does not have a GUI, it can be run from the command line.

* When running the program, the user will be prompted to select one of the following options to execute a feature.

```
Hospital System
What do you want to do today?
(A)dd new patient?
(D)elete patient?
(S)et patient's doctor?
(L)ist of patients and doctors?

> A
```

## Features

* List of program features:

### Feature 1: Add new patient
* When `Add new patient` is selected, the user will be prompted to enter his name (note: duplicate entry is allowed):

```
Enter patient's name to add: __
```

### Feature 2: Delete patient
* When `Delete patient` is selected, the user will be prompted to enter the patient's id to be deleted:

```
Enter patient's id to delete: __
```

### Feature 3: Set patient's Doctor
* When `Set patient's Doctor` is selected, the user will be prompted to enter the patient's id to be edit the patient's record for adding a doctor or transferring a doctor by entering the doctor's id:

```
Enter patient's id to edit: __
```

* Once entered, the user will be prompted again to enter the doctor's id:

```
Enter doctor's id:__
```

### Feature 4: List of patient's and doctors
* When `List of patient's and doctors` is selected, the program will display a table that lists patient name and doctor name next to it. Ex:

```
--------------------
| Patient | Doctor |
| ------- | ------ |
| Carolyn | Melody |
| Dennis  | John   |
| Sean    | Emily  |
| Lillian | Lee    |
| Michael | Emily  |
| Janet   | Greg   |
| Linda   | Bertha |
--------------------
```
