import sqlite3
from database_sqlite3 import Employee

# databaze v pameti :memory:
# connection = sqlite3.connect('employee.db')
connection = sqlite3.connect(':memory:')



c = connection.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")


def insert_emp(emp):
    with connection:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
              {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with connection:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with connection:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})



emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)


# nesmi se pouzivat
#c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_1.last , emp_1.pay))

# tohle je bezpecny
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last , emp_1.pay))
#
# connection.commit()
#
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
#
# connection.commit()
#
# c.execute("SELECT * FROM employees WHERE last=?", ('Schafer', ))
# print(c.fetchall())
#
#
#
# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe' })
#
#
# # print(c.fetchone())
# print(c.fetchall())
#
# connection.commit()

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)
connection.close()