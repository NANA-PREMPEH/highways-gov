from datetime import datetime
from trial import db
upgrade_data = {
    "all contract": [
        {
            "name_of_contract": "SANTASI - BEKWAI BYPASS",
            "length": 20,
            "lot": None,
            "contract_sum": 71231085.21,
            "contractor": "NORTHEN MINES & QUARRIES LTD",
            "date_commenced": datetime.strptime("01-03-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("01-03-2021", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "NSUTA - BEPOSO",
            "length": 7,
            "lot": 3,
            "contract_sum": 25960940.06,
            "contractor": "MEMPHIS METROPOLITAN CO. LTD",
            "date_commenced": datetime.strptime("09-11-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("09-11-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "AWIAM KWANTA - OBUASI ROAD",
            "length": 30,
            "lot": 7,
            "contract_sum": 32199853.71,
            "contractor": "JOSHOB CONSTRUCTION CO.",
            "date_commenced": datetime.strptime("09-11-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("09-11-2022", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "TRABUOM - NWIMSO",
            "length": 16,
            "lot": 1,
            "contract_sum": 57350585.11,
            "contractor": "HALLMARK CIVIL ENGINEERING",
            "date_commenced": datetime.strptime("24-05-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("24-05-2021", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "BANKA JUNCTION - GYADEM ROAD",
            "length": 7,
            "lot": None,
            "contract_sum": 3165763.42,
            "contractor": None,
            "date_commenced": datetime.strptime("07-09-2016", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-03-2018", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "BEKWAI TOWN ROADS",
            "length": 5.2,
            "lot": None,
            "contract_sum": 119707049.60,
            "contractor": "ATTACHY CONSTRUCTION LTD.",
            "date_commenced": datetime.strptime("24-05-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("24-05-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "BEKWAI TOWN ROADS",
            "length": 5,
            "lot": None,
            "contract_sum": 13808534.38,
            "contractor": "KENSTEP LTD.",
            "date_commenced": datetime.strptime("30-01-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-01-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "MAMPONG - KOFIASE",
            "length": 14,
            "lot": 2,
            "contract_sum": 53637690.76,
            "contractor": "KOFI JOB COMPANY LTD.",
            "date_commenced": datetime.strptime("09-11-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("09-11-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "OBUASI - DATANO",
            "length": 15,
            "lot": 5,
            "contract_sum": 52671409.49,
            "contractor": "JOSHOB CONSTRUCTION CO.",
            "date_commenced": datetime.strptime("09-11-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("09-11-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "GYABEM - BANKU JUNCTION",
            "length": 9,
            "lot": None,
            "contract_sum": 15920540.64,
            "contractor": "COMET CONSTRUCTION LTD.",
            "date_commenced": datetime.strptime("08-02-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("08-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "EFFIDUASE - SENCHI - JUANSA ROAD",
            "length": 8,
            "lot": 2,
            "contract_sum": 28282726.22,
            "contractor": "AGYAKOT COMPANY LTD.",
            "date_commenced": datetime.strptime("26-12-2014", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-06-2018", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KOKOBEN - ADJAMENSU",
            "length": 9,
            "lot": None,
            "contract_sum": 36627481.83,
            "contractor": "M. GYEBI COMPANY LTD.",
            "date_commenced": datetime.strptime("10-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("10-02-2021", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "ADUAMOAH - ADUMANSAKESE ROAD",
            "length": None,
            "lot": 1,
            "contract_sum": 31840330.48,
            "contractor": "HARDWICK LTD.",
            "date_commenced": datetime.strptime("09-11-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("09-11-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KONONGO - AGOGO",
            "length": 8,
            "lot": None,
            "contract_sum": 20461155.10,
            "contractor": "MYK CONSTRUCTION LTD.",
            "date_commenced": datetime.strptime("24-05-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("24-02-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "OBUASI - DATANO",
            "length": 15,
            "lot": 4,
            "contract_sum": 51694966.68,
            "contractor": "RESOURCE ACCESS LTD.",
            "date_commenced": datetime.strptime("09-11-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("09-11-2020", "%d-%m-%Y").strftime("%Y-%m-%d")
        } 
    ]
}

def update_upgrade(upgrade_data):
    entries = []
    for contract in upgrade_data["all contract"]:
        new_entry = Upgrading(name_of_contract=contract['name_of_contract'], length=contract['length'], lot=contract['lot'],
                    contract_sum=contract['contract_sum'], contractor=contract['contractor'], 
                    date_commenced=contract['date_commenced'], date_completed=contract['date_completed'])
        entries.append(new_entry)
        db.session.add_all(entries)
        db.session.commit()