from datetime import datetime
from trial.models import Construction
from trial import db

construc_data = {
    "all contract": [
        {
            "name_of_contract": "KUMASI-EJISU (BY PASS)",
            "length": 0.9,
            "lot": 9,
            "contract_sum": 198771.21,
            "contractor": "BREWECKS COMPANY",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-12-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-ACCRA ROAD",
            "length": 0.01,
            "lot": 6,
            "contract_sum": 191277.81,
            "contractor": "BANQE GH LTD.",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "NKWANTA ON  JUASO",
            "length": 0.3,
            "lot": 26,
            "contract_sum": 198882.20,
            "contractor": "YAKAB PRESTIGE LTD.",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "HIGHWAY VILLAGE",
            "length": 0.9,
            "lot": 14,
            "contract_sum": 195057.63,
            "contractor": "BAKAG VENTURES",
            "date_commenced": datetime.strptime("07-07-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-11-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-EJISU (BY PASS)",
            "length": 0.3,
            "lot": 11,
            "contract_sum": 196825.27,
            "contractor": "BREWECKS COMPANY",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KONONGO-AGOGO ROAD",
            "length": 1.2,
            "lot": 5,
            "contract_sum": 19049182,
            "contractor": "BILLS CONSTRUCTION WORKS",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-09-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-EJISU",
            "length": 0.9,
            "lot": 8,
            "contract_sum": 193802.21,
            "contractor": "BREWECKS COMPANY",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-11-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "ABUAKWA-BIBIANI ROAD",
            "length": 0.6,
            "lot": 14,
            "contract_sum": 199602.61,
            "contractor": "BUTUMENS VENTURES",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-11-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "NKWANTA -TUTUKA ROAD",
            "length": 0.12,
            "lot": 23,
            "contract_sum": 176790.69,
            "contractor": "AMS AND SONS LTD.",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-TECHIMAN (BY PASS)",
            "length": 0.6,
            "lot": 29,
            "contract_sum": 189218.27,
            "contractor": "ABROSARP COMPANY",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "MAMPONG-EJURA ROAD",
            "length": 0.1,
            "lot": 18,
            "contract_sum": 191998.48,
            "contractor": "AGEROP LTD.",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "HWERESO-KUMASI",
            "length": 0.2,
            "lot": 70,
            "contract_sum": 189713.46,
            "contractor": "AMS AND SONS LTD.",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-ACCRA ROAD",
            "length": 1,
            "lot": 5,
            "contract_sum": 190685.65,
            "contractor": "LOMENFI COMPANY LTD",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "BEKWAI-KUNTANASE ROAD",
            "length": 0.6,
            "lot": 25,
            "contract_sum": 198658.64,
            "contractor": "KUMASAP GOLD LIMITED",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2018", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "MAMPONG-KUMASI ROAD",
            "length": 0.019,
            "lot": 15,
            "contract_sum": 187826.14,
            "contractor": "KWAKU APAU LTD.",
            "date_commenced": datetime.strptime("07-07-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-11-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "BEKWAI-ASSIN PRASO ROAD",
            "length": None,
            "lot": None,
            "contract_sum": 195404.14,
            "contractor": "KWAKU APAU LTD.",
            "date_commenced": datetime.strptime("27-10-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("27-04-2018", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KONONGO-AGOGO ROAD",
            "length": 0.6,
            "lot": 2,
            "contract_sum": 197710.35,
            "contractor": "KENDYMAY",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-12-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-TECHIMAN",
            "length": 0.2,
            "lot": 28,
            "contract_sum": 188541.38,
            "contractor": "KYEREWAA MM GH LTD.",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMAWU-BODOMASE ROAD",
            "length": 0.18,
            "lot": 17,
            "contract_sum": 198121.95,
            "contractor": "KYEREWAA MM GH LTD.",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "NSUTA-MAMPONG ROAD",
            "length": 0.6,
            "lot": 19,
            "contract_sum": 187116.19,
            "contractor": "HINRA ENTERPRISE",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMAWU-BODOMASE",
            "length": 0.6,
            "lot": 20,
            "contract_sum": 197064.46,
            "contractor": "NIMROT COMPANY LTD.",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-ANWIANKWANTA ROAD",
            "length": 0.25,
            "lot": 12,
            "contract_sum": 187837.86,
            "contractor": "GAVKT ENTERPRISE",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-11-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "AGOGO-DOME (BY PASS)",
            "length": 0.6,
            "lot": 1,
            "contract_sum": 198460.64,
            "contractor": "GIRDERS ENTERPRISE",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-11-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "BEKWAI-ADANSI PRASO ROAD",
            "length": 0.1,
            "lot": 25,
            "contract_sum": 192604.28,
            "contractor": "FREE FALL COMPANY LTD.",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "NSUTA-KWAMANG ATONSU ROAD",
            "length": 0.6,
            "lot": 27,
            "contract_sum": 199090.33,
            "contractor": "MYK CONSTRUCTION LTD.",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMAWU-BODOMASE",
            "length": 0.6,
            "lot": 18,
            "contract_sum": 199341.44,
            "contractor": "HRO CONSTRUCTION&ENG SERVICE",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-ACCRA ROAD",
            "length": 2,
            "lot": 1,
            "contract_sum": 188182.33,
            "contractor": "HAMLERA ENTERPRISE",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-02-2018", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "EJISU-EFFIDUASE ROAD",
            "length": 0.9,
            "lot": 29,
            "contract_sum": 189279.42,
            "contractor": "FLORTONY COMPANY LTD.",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "ABUAKWA-BIBIANI ROAD",
            "length": 0.6,
            "lot": 17,
            "contract_sum": 198013.57,
            "contractor": "FREEWAY KEEPERS VENTURES",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-11-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-ANWIANKWANTA ROAD",
            "length": 0.15,
            "lot": 3,
            "contract_sum": 198884.74,
            "contractor": "ELBAFF VENTURES",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-11-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "BOANKRA (HIGHWAY VILLAGE)",
            "length": 1.2,
            "lot": 15,
            "contract_sum": 197264.11,
            "contractor": "EBONY CONCEPT ENTERPRISE",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-11-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "ANWIANKWANTA-ADUMASA ROAD",
            "length": 0.9,
            "lot": 7,
            "contract_sum": 192038.03,
            "contractor": "EASTMAIDAS COMPANY LTD.",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "MAMPONG TOWN ROAD",
            "length": 3.6,
            "lot": 20,
            "contract_sum": 47188.37,
            "contractor": "DEHAWK VENTURES",
            "date_commenced": datetime.strptime("30-06-2015", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("26-04-2016", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-SUNYANI RAOD",
            "length": 1,
            "lot": 22,
            "contract_sum": 195830.62,
            "contractor": "DEX ENTERPRISE",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-02-2018", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KWADASO-TRABUOM ROAD",
            "length": 1.2,
            "lot": 10,
            "contract_sum": 195692.51,
            "contractor": "DUFFEROO CONSTRUCTION LTD.",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "MAMPONG-KUMASI (TRANODUMSI ZONGO)",
            "length": 0.0185,
            "lot": 16,
            "contract_sum": 172507.76,
            "contractor": "DONCROSS LIMITED",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "NSUTA-KWAMANG",
            "length": 0.6,
            "lot": 21,
            "contract_sum": 187038.28,
            "contractor": "DEANSGATE COMPANY LIMITED",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "EFFIDUASE-KUMAWU",
            "length": 0.6,
            "lot": 30,
            "contract_sum": 199018.80,
            "contractor": "DOORMAN COMPANY LTD.",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-SUNYANI RAOD",
            "length": 0.6,
            "lot": 7,
            "contract_sum": 199383.98,
            "contractor": "LEELB ENTERPRISE",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-11-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "EJISU-KUNTENASE ROAD",
            "length": 0.6,
            "lot": 18,
            "contract_sum": 199645.50,
            "contractor": "LESSE COMPANY LTD",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-11-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "AMANTIA-OBUASEWA ROAD",
            "length": 1.2,
            "lot": 22,
            "contract_sum": 198784.67,
            "contractor": "LIZEL VENTURES",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "BEKWAI-ASIWA ROAD",
            "length": 0.9,
            "lot": 16,
            "contract_sum": 198305.93,
            "contractor": "LEELB ENTERPRISE",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-11-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI ROAD",
            "length": 0.6,
            "lot": 23,
            "contract_sum": 187705.85,
            "contractor": "LIKEL VENTURES",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-EJISU BY PASS",
            "length": 0.6,
            "lot": 11,
            "contract_sum": 199802.75,
            "contractor": "MULTIWAVES CONSTRUCTION WORKS",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-11-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "AGYENKWASO-ANOMABA",
            "length": 0.1,
            "lot": 1,
            "contract_sum": 195526.77,
            "contractor": "MYK CONSTRUCTION LTD",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-AMANKWANTA ROAD",
            "length": 0.3,
            "lot": 2,
            "contract_sum": 198878.63,
            "contractor": "MICANDY CONSTRUCTION COM LTD",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-AMANKWANTA ROAD",
            "length": 0.6,
            "lot": 4,
            "contract_sum": 193776.90,
            "contractor": "MIDIONE ENTERPRISE",
            "date_commenced": datetime.strptime("30-07-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("30-11-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "BEKWAI-ASIWA ROAD",
            "length": 0.3,
            "lot": 1,
            "contract_sum": 163164.52,
            "contractor": "LINSBA COMPANY LTD",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-ANWIANKWANTA ROAD",
            "length": 0.3,
            "lot": 1,
            "contract_sum": 198875.29,
            "contractor": "MIDIONE ENTERPRISE",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-SUNYANI RAOD",
            "length": 0.3,
            "lot": 14,
            "contract_sum": 180580.40,
            "contractor": "M-EDINAM VENTURES",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "OFOASE PRA-RIVER ROAD",
            "length": 0.9,
            "lot": 6,
            "contract_sum": 162926.02,
            "contractor": "NICH HANKO CO. LTD",
            "date_commenced": datetime.strptime("17-09-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2018", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "BEKWAI-ADANSI PRASO ROAD",
            "length": 0.05,
            "lot": 24,
            "contract_sum": 189923.90,
            "contractor": "NUDANA GH. LTD",
            "date_commenced": None,
            "date_completed": None
         }, 
        {
            "name_of_contract": "KUMASI-AMANKWANTA ROAD",
            "length": 0.6,
            "lot": 3,
            "contract_sum": 198953.97,
            "contractor": "OFBAFF LTD",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-TECHIMAN",
            "length": 0.2,
            "lot": 30,
            "contract_sum": 187391.33,
            "contractor": "OFBAFF LTD",
            "date_commenced": datetime.strptime("07-08-2017", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("07-12-2017", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "NKWANTA ON  JUASO",
            "length": 0.18,
            "lot": 15,
            "contract_sum": 196784.79,
            "contractor": "OAK SPHERE ENG.SOLU",
            "date_commenced": datetime.strptime("17-09-2018", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("17-02-2019", "%d-%m-%Y").strftime("%Y-%m-%d")
        }, 
        {
            "name_of_contract": "KUMASI-KUNTENASE ROAD",
            "length": 8.7,
            "lot": None,
            "contract_sum": 195979084.90,
            "contractor": "KOFI JOB COM. LTD",
            "date_commenced": datetime.strptime("01-03-2019", "%d-%m-%Y").strftime("%Y-%m-%d"),
            "date_completed": datetime.strptime("01-03-2021", "%d-%m-%Y").strftime("%Y-%m-%d")
        } 
    ]
}

def update_construc(construc_data):
    entries = []
    for contract in construc_data["all contract"]:
        new_entry = Construction(name_of_contract=contract['name_of_contract'], length=contract['length'], lot=contract['lot'],
                    contract_sum=contract['contract_sum'], contractor=contract['contractor'], 
                    date_commenced=contract['date_commenced'], date_completed=contract['date_completed'])
        entries.append(new_entry)
        db.session.add_all(entries)
        db.session.commit()