import pymysql
con=pymysql.connect(host="localhost",user="root",passwd="123456",database="connect")
print(con)
cursor = con.cursor()


#value from the user
reg=int(input("enter your register number"))
name=input("enter the name:")
department=input("enter your email")

#insertion
cursor.execute('''
insert into students(reg_no,name,department)
values(%s,%s,%s)
''',(reg,name,department))
con.commit()
print("values stored successfully")

#display
cursor.execute('select * from students')
rows=cursor.fetchall()
for i in rows:
    print("The values in the table are\n",i)
                 
