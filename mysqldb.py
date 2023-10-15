import mysql.connector
mydb = mysql.connector.connect(host = "localhost",user = "root",password = "root", database = "book_shop")

mycursor = mydb.cursor()
#mycursor.execute("SELECT * from books WHERE pages >=437 LIMIT 5")
mycursor.execute("SELECT title,stock_quantity, CONCAT(author_fname,'  ',author_lname) AS AUTHOR from books ORDER BY released_year")

for i in mycursor:
    print(i)