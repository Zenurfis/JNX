import psycopg2


def connect_create():
    """some data for table 'departments'"""
    departments_list = [('IT',), ('Accounting',), ('Legal',), ('Management',)]

    """sql insertion"""
    sql_insert_departments = "INSERT INTO departments(department_name) VALUES(%s)"

    """some data for table 'expenses'"""
    expenses_list = [(1, 'January', 2017, 300000,),
                     (1, 'February', 2016, 200000,),
                     (1, 'March', 2018, 1500100,),
                     (1, 'October', 2019, 100000,),
                     (2, 'January', 2018, 200000,),
                     (2, 'April', 2018, 1500000,),
                     (2, 'September', 2018, 30000,),
                     (2, 'December', 2019, 1200430,),
                     (3, 'May', 2018, 180000,),
                     (3, 'June', 2018, 125888,),
                     (3, 'January', 2020, 750000,),
                     (4, 'February', 2016, 300000,)]

    """sql insertion"""
    sql_insert_expenses = "INSERT INTO expenses(department_id, month, year, expense) VALUES(%s, %s, %s, %s)"

    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE departments (
            department_id  SERIAL PRIMARY KEY,
            department_name TEXT NOT NULL
        )
        """,
        """ 
        CREATE TABLE expenses (
            id SERIAL PRIMARY KEY,
            department_id  INT NOT NULL,
            month TEXT NOT NULL,
            year INT NOT NULL,
            expense INT
        )
        """)
    conn = None
    try:
        """create a connection"""
        conn = psycopg2.connect(host="localhost", database="jnx_db", user="postgres", password="Postgres123321")
        
        """ create a cursor"""
        cur = conn.cursor()
        
        """create table one by one"""
        for command in commands:
            cur.execute(command)
            
        """execute insertion"""
        cur.executemany(sql_insert_departments, departments_list)
        cur.executemany(sql_insert_expenses, expenses_list)
        
       """commit changes"""
        conn.commit()
    
        """close communication with the PostgreSQL database server"""
        cur.close()

    """handle exceptions"""
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    connect_create()