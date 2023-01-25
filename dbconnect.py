# DB Management
import sqlite3
conn=sqlite3.connect('data.db',check_same_thread=False)
c=conn.cursor()

class DBConnection:

    def create_usertable(self):
        c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT) ')
    def add_userdata (self,username, password):
        c.execute('INSERT INTO userstable (username, password) VALUES (?, ?)', (username, password))
        conn.commit()

    def login_user(self,username, password):
            c.execute("SELECT * FROM userstable WHERE username=? AND password =?",(username, password))
            #c.execute(f"SELECT * FROM userstable WHERE username='{username}' AND password ='{password}'")
            data=c.fetchall()
            return(data)
    def view_all_users(self):
        c.execute('SELECT * FROM userstable')
        data=c.fetchall()
        return(data)
db=DBConnection()
# db.create_usertable()
# db.add_userdata('zaid1','zaid123')
# db.add_userdata('zaid','zaid123')
# db.login_user('zaid','zaid123')
# db.view_all_users()
