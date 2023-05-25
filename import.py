import sqlite3, csv
con = sqlite3.connect("C:\Users\Public\database.db")
cur = con.cursor()

with open('c:\obmen\import.csv', newline='') as csvfile:
    csvdata = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in csvdata:
        marka=row[0]
        sp2=row[1]
        alkokode=row[2]
        if (sp2):
            res = cur.execute("SELECT * FROM excise_stamp WHERE number='" + marka +"' LIMIT 1")
            #if (res.fetchone() is None):
            massiv=res.fetchall()
            try:
                print(massiv[0])
            except:
                cur.execute("INSERT INTO excise_stamp (number, inform_f2_reg_id, alc_code, piece) VALUES ('" + marka + "', '" + sp2 + "', '" + alkokode + "', 1)")
                cur.execute("INSERT INTO excise_stamp_transaction (number, state, action, stamp, note, status) VALUES ('" + marka + "', 1, 1, '2023-05-19T17:09:00', 'На основании документа запроса марок №20230519170004-SR-9290', 16)")
con.commit()