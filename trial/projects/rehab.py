from datetime import datetime
from trial.models import Rehabilitation
from trial import db

rehab_data = {
    "all contract": [
        {
            "name_of_contract": "Anwiankwanta-Obuasi",
            "length": 0.3,
            "lot": 1,
            "contract_sum": 23000,
            "contractor": "Joshob Construction Limited",
            "date_commenced": datetime.strptime("17-04-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-05-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        },
        {
            "name_of_contract": "KODIE - ADUMAN",
            "length": 9,
            "lot": None,
            "contract_sum": 39090694.69,
            "contractor": "KNAPO CONSTRUCTION LTD",
            "date_commenced": datetime.strptime("30-05-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("28-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        },
        {
            "name_of_contract": "KOFIASI - ANYINASU ROAD",
            "length": 15,
            "lot": 1,
            "contract_sum": 49974126.72,
            "contractor": "PRIVATE MAIL BAG 30",
            "date_commenced": datetime.strptime("17-09-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": None
        },
        {
            "name_of_contract": "MAMPONG KOFIASE ROAD",
            "length": 14,
            "lot": 2,
            "contract_sum": None,
            "contractor": "KOFI JOB COMPANY LTD",
            "date_commenced": datetime.strptime("16-03-2020", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("09-09-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        },
        {
            "name_of_contract": "M/S GLOBAL INNOVATION CONSTRUCTION LTD",
            "length": 11.4,
            "lot": None,
            "contract_sum": 87839992.87,
            "contractor": "M/S GLOBAL INNOVATION CONSTRUCTION LTD",
            "date_commenced": datetime.strptime("24-05-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("24-05-2021", "%d-%m-%Y").strftime("%Y-%m-%d")
        },
        {
            "name_of_contract": "ADANKWAME - NTESERE ROAD",
            "length": 4,
            "lot": None,
            "contract_sum": 9926540.49,
            "contractor": "M/S ABOVE HEIGHTS CONSTRUCTION LTD",
            "date_commenced": datetime.strptime("22-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("22-02-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        },
        {
            "name_of_contract": "WIAWSO - MOSEASO ROADS",
            "length": 20,
            "lot": 2,
            "contract_sum": 58253608.50,
            "contractor": "HALL MARK CIVIL ENG.",
            "date_commenced": datetime.strptime("24-05-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("24-05-2021", "%d-%m-%Y").strftime("%Y-%m-%d")
        },
        {
            "name_of_contract": "TRABUOM - TOASE ROAD",
            "length": 9,
            "lot": None,
            "contract_sum": 54452268.67,
            "contractor": "A. KANNIN LTD",
            "date_commenced": datetime.strptime("26-11-2015", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("25-07-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        },
        {
            "name_of_contract": "OYOKO - EFFIDUASE ROAD",
            "length": 17,
            "lot": 6,
            "contract_sum": 26099968.85,
            "contractor": "JAH NICORF LIMITED",
            "date_commenced": datetime.strptime("09-11-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": None
        } 
    ]
}

def update_rehab(rehab_data):
    entries = []
    for contract in rehab_data["all contract"]:
        new_entry = Rehabilitation(name_of_contract=contract['name_of_contract'], length=contract['length'], lot=contract['lot'],
                    contract_sum=contract['contract_sum'], contractor=contract['contractor'], 
                    date_commenced=contract['date_commenced'], date_completed=contract['date_completed'])
        entries.append(new_entry)
        db.session.add_all(entries)
        db.session.commit()
