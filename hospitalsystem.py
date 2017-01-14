import sqlite3

connection = sqlite3.connect('hospital.db')

cursor=connection.cursor()

print('Hospital System')
option='Y'
while(option=='Y' or option=='y'):
    choice = input('What do you want to do today? \n(A)dd new patient?\n(D)elete patient?\n(S)et patient\'s doctor? \n(L)ist of patients and doctors? \n(E)xit')


    if(choice=='A' or choice=='a'):
      patient_name = input('Enter patient\'s name to add:')
      cursor.execute('''insert into patients(name,doctors_id) values(?,?)''',(patient_name,''))
      connection.commit()

    elif(choice=='D' or choice=='d'):
      patient_id = int(input('Enter patient\'s id to delete:'))
      cursor.execute('''delete from patients where id=(?)''',(patient_id,))
      connection.commit()

    elif(choice=='S' or choice=='s'):
      patient_id = int(input('Enter patient\'s id to edit:'))
      cursor.execute('''select id from patients where id=(?)''',(patient_id,))
      patient = cursor.fetchall()
      if(len(patient)==0):
          print('Invalid Patient ID')
      else:
          doctor_id = int(input('Enter doctor\'s id:'))
          cursor.execute('''select id from doctors where id=(?)''',(doctor_id,))
          doctor = cursor.fetchall()
          if(len(doctor)==0):
              print('Invalid Doctor ID')
          else:
              res = cursor.execute('''update patients set doctors_id=? where id=?''',(doctor_id,patient_id))
              connection.commit()

    elif(choice=='L' or choice=='l'):
      print('------------------------------')
      print('| ID | Patient | ID | Doctor |')
      print('------------------------------')
      cursor.execute('''select p.id,p.name,d.id,d.name from patients p left join doctors d on p.doctors_id=d.id''')
      details = cursor.fetchall()
      for row in details:
        print('| ',row[0],'|',row[1],'| ',row[2],'|',row[3],'|')
      print('------------------------------')

    elif(choice=='E' or choice=='e'):
        break
    else:
        print('Invalid option')
    print('\n')

