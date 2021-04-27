from datetime import datetime
from trial import db

resurface_data = {
    "all contract": [
        {
            "name_of_contract": "EJURA-ANYINOFI ROAD",
            "length": 8,
            "lot": 3,
            "contract_sum": 7378176.78,
            "contractor": "TONY MACHINERIES LTD.",
            "date_commenced": datetime.strptime("31-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"), 
            "date_completed": datetime.strptime("31-07-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "EJURA-ANYINOFI-BONDASO ROAD",
            "length": 5,
            "lot": 1,
            "contract_sum": 2264594594,
            "contractor": "JULIAN LTD.",
            "date_commenced": datetime.strptime("15-04-2016", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("22-02-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "EJURA-ANYINOFI ROAD",
            "length": 12,
            "lot": 2,
            "contract_sum": 7164267.48,
            "contractor": "TRAFALKA LTD.",
            "date_commenced": datetime.strptime("31-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("31-07-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "AGOGO-ONYEMESO ROAD",
            "length": 11,
            "lot": None,
            "contract_sum": 5260545.50,
            "contractor": "TECHNOLIGHTS LTD.",
            "date_commenced": datetime.strptime("22-02-2010", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("22-02-2011", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "EJURA-ANYINOFI ROAD",
            "length": 10,
            "lot": 1,
            "contract_sum": 12698215.87,
            "contractor": "LOMENFI COMPANY LTD.",
            "date_commenced": datetime.strptime("31-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("31-07-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "EJURA-ANYINOFI -BONDASO ROAD",
            "length": 5,
            "lot": 3,
            "contract_sum": 2041866.12,
            "contractor": "LOMENFI COMPANY LTD.",
            "date_commenced": datetime.strptime("15-04-2016", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("22-05-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "EJURA-ANYINOFI ROAD",
            "length": 2,
            "lot": 4,
            "contract_sum": 7051773.12,
            "contractor": "ROUBMAP COMPANY LTD.",
            "date_commenced": datetime.strptime("31-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("31-07-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        } 
    ]
}

def update_resurface(resurface_data):
    entries = []
    for contract in resurface_data["all contract"]:
        new_entry = Resurfacing(name_of_contract=contract['name_of_contract'], length=contract['length'], lot=contract['lot'],
                    contract_sum=contract['contract_sum'], contractor=contract['contractor'], 
                    date_commenced=contract['date_commenced'], date_completed=contract['date_completed'])
        entries.append(new_entry)
        db.session.add_all(entries)
        db.session.commit()