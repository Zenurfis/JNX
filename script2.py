import psycopg2
import csv

def fetch_data():
    """variable for a year to report"""
    report_year = 2018
    
    conn = None
    try:
        """connect to a db"""
        conn = psycopg2.connect(host="localhost", database="jnx_db", user="postgres", password="489295Postgres")
        
        """create a cursor"""
        cur = conn.cursor()
        
        """execute an sql query"""
        cur.execute('''SELECT expenses.year, departments.department_name, SUM(expenses.expense) as Total 
                        FROM expenses LEFT JOIN departments on expenses.department_id = departments.department_id
                        WHERE expenses.year = (%s)
                        GROUP BY departments.department_name, expenses.year 
                        ORDER BY expenses.year''', (report_year,))
        
        """fetch data"""
        rows = cur.fetchall()
        
        """name of the .csv file including the year"""
        file_name = str(report_year) + 'report.csv'
        
        """create file to write and write"""
        f = open(file_name, 'w')
        with f:
            writer = csv.writer(f)
            writer.writerows(rows)
        """commit changes and close the cursor"""
        conn.commit()
        cur.close()

    """handle an exception"""
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    fetch_data()