import sqlite3
# ini contoh sql database menggunakan python


class data_base:
    """Creting Data Base"""
# contoh python sql3 database menggunakan oop/object oriented programming

    def __init__(self, data_base_name):
        self.data_base_name = data_base_name
        self.conn = sqlite3.connect(
            f"/storage/emulated/0/{self.data_base_name}")
        self.cur = self.conn.cursor()

    # Creating table into database
    def create_db(self, name, *arg):
        initial = f"CREATE TABLE IF NOT EXISTS {name} {arg}"
        self.cur.execute(initial)
        self.conn.commit()
        # self.conn.close()

    # inserting value to table of database
    def insert_db(self, name, *arg):
        initial = f"INSERT INTO {name} VALUES{arg}"
        self.cur.execute(initial)
        self.conn.commit()
        # self.conn.close()

    # view data base
    def show_db(self, name):
        initial = f"SELECT * FROM {name}"
        self.cur.execute(initial)
        data = self.cur.fetchall()
        self.conn.close()
        return data

# creating data base


database = data_base("Sekolah.db")
# creating table siswa with name alamat and gender row
database.create_db("Siswa", "Nama", "Alamat", "Kelamin")

# inserting data into table Siswa

# database.insert_db("Siswa", "Ilma Hulwatuzzahra", "Sampang Tiga", "P")
# database.insert_db("Siswa", "Hulwa", "Sampang Tiga", "P")
# database.insert_db("Siswa", "Zahra", "Sampang Tiga", "P")
# database.insert_db("Siswa", "Yazid Anshori", "Lanjon", "L")

# showing database on terminal. becouse we don't have db viewer yet.
database_show = database.show_db("Siswa")

for data in database_show:
    # list(data)
    print(data[1])
    # for x, y, z in data:
    # print(x, y, z)
    # for name in x:
    # print(name)
