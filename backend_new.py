

import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS restaurant (id INTEGER PRIMARY KEY, reference INTEGER,idli INTEGER,icecream INTEGER,cold_drinks INTEGER,burger INTEGER,french_fries INTEGER,pasta INTEGER,pizza INTEGER,tax TEXT, service_charge TEXT,net_amount TEXT)") 
                        
        self.conn.commit()
        

    def insert(self,reference,idli,icecream,cold_drinks,
                        burger,french_fries,pasta,pizza,tax,
                        service_charge,net_amount
                        ):
        
        self.cur.execute("INSERT INTO restaurant VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?)",(reference,idli,icecream,cold_drinks,
                        burger,french_fries,pasta,pizza,tax,
                        service_charge,net_amount))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM restaurant")
        rows = self.cur.fetchall()

        return rows

    def search(self,reference=""):#, net_amount="", service_charge="", tax="",pasta=""):
        self.cur.execute("SELECT * FROM restaurant WHERE reference = ?", (reference,))# net_amount, service_charge, tax, pasta )))# OR net_amount = ? OR service_charge = ? "OR tax = ? OR  pasta = ?"
                    
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,reference):
        self.cur.execute("DELETE FROM restaurant WHERE reference = ?", (reference,))
        self.conn.commit()
        #conn.close()

    def update(self,reference,idli,icecream,cold_drinks,
                        burger,french_fries,pasta,pizza,tax,
                        service_charge,net_amount):
        self.cur.execute("UPDATE restaurant SET reference = ?,idli =?,icecream =?,cold_drinks =?,burger =?,french_fries =?,pasta =?,pizza =?,tax =?, service_charge=?,net_amount=? WHERE reference = ? ", (reference,idli,icecream,cold_drinks,burger,french_fries,pasta,pizza,tax,service_charge,net_amount,reference))
        self.conn.commit()

    
    def __del__(self):
        self.conn.close()
