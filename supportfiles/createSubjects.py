import sqlite3

SUBJECTLIST = {
    "subjects": [
        {
            "subject": "B1 Algoritmen",
            "domain": "B Grondslagen"
        },
        {
            "subject": "B2 Datastructuren",
            "domain": "B Grondslagen"
        },
        {
            "subject": "B3 Automaten",
            "domain": "B Grondslagen"
        },
        {
            "subject": "B4 Grammatica's",
            "domain": "B Grondslagen"
        },
        {
            "subject": "C1-2 Informatie en Data",
            "domain": "C Informatie"
        },
        {
            "subject": "C3 Representeren",
            "domain": "C Informatie"
        },
        {
            "subject": "C4 Datapresentaties",
            "domain": "C Informatie"
        },
        {
            "subject": "E1 Hard- en software",
            "domain": "E Architectuur"
        },
        {
            "subject": "E2 Security",
            "domain": "E Architectuur"
        }
    ]
}



conn = sqlite3.connect("../MCquizer.db")
DBoperator = conn.cursor()


for item in SUBJECTLIST["subjects"]:
    subject = item["subject"]
    domain = item["domain"]
    insertSubjectQuery = "INSERT INTO subject (subjectname, domain) VALUES (?, ?)"
    print (insertSubjectQuery)
    try:
        DBoperator = conn.cursor()
        DBoperator.execute(insertSubjectQuery, (subject, domain))
        conn.commit()
    except sqlite3.OperationalError as error:
        print(error)