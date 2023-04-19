import random
import random
import random


TUPLES = [[(a, random.randint(1, 200)) for a in range(1, 201)] for _ in range(3)]


PASSWORDS = [
    "kLka34Gf1b",
    "GQYLcHB1PC",
    "pmvn6pw5in",
    "hKCgYKHztA",
    "C1oNoDJ1Kq",
    "DS71pUpzaA",
    "lAjblcnzpA",
    "YCF20FC0bP",
    "P1sskwkYHi",
    "aqI96XPx3J",
    "EdpN66ZCwT",
    "MBiZK0lHRG",
    "IcdOmSDdDn",
    "70kyfsXdbF",
    "x16LTRgf3z",
    "ROA9cpGRFm",
    "04rVGT4ARN",
    "Droit1VIsV",
    "q7yxMI9GkE",
    "lMsyobgpU8",
    "at72xWbVpO",
    "GEnHVjjX69",
    "Fg48YJurRs",
    "53PCfxvv4Z",
    "2OeaAhrJK2",
    "yVCsFhAmAi",
    "6DQpa3RAOd",
    "ol8HbWo9ZL",
    "VRIYJMM8B8",
    "RyxGvs8g0h",
    "2TxWsRKqGn",
    "jCaaGGQS6P",
    "EW1U0NWrPr",
    "etCqCTRAkq",
    "sapZxHMOkC",
    "bjyCj3WGfE",
    "VEr1TrrSeF",
    "uJC7ndhvh1",
    "IQkqEpEyaJ",
    "yLfA9LTCj7",
    "DjCcbleKo3",
    "zzmQpfqWyY",
    "JLQmsFKXnh",
    "fTUvdczQao",
    "IYixxKbaJx",
    "NlzSDpiw3s",
    "BLfegpG2sK",
    "BRwLVPOlr5",
    "9HWa7Li03n",
    "oylHkZy5gs",
    "gxY3agKlQ9",
    "OM4aPuYHUB",
    "jqHD1MDyDa",
    "b7OdHM9Kbu",
    "zUmAShpia9",
    "AnDvpsIAWB",
    "hyIj1QInyQ",
    "EIs3SDuafK",
    "dZd4Mc1oXD",
    "ENyWbT2zWT",
    "P6px6P0OoK",
    "y4cW804Dcy",
    "KfZcW3UEjX",
    "vG9LuXY2jv",
    "Py0wKfQ5uC",
    "aZYDp5GPwR",
    "7IFYYcEgcU",
    "DmYIexMzxX",
    "e1sXpTgHbQ",
    "6oTohUiNX8",
    "FGL8i4kteR",
    "YBPjIzneW0",
    "LysJx3sewW",
    "5Alf1dfGeW",
    "si5JpqA9YF",
    "4bGnBWNJ22",
    "SDHCPt7yOI",
    "1aqNBVMAbC",
    "V4AZNV6B5g",
    "PGdjjE5S3z",
    "yBfOQ4Z7yL",
    "gV4VpPqeUJ",
    "IhYGTdINRm",
    "kmXK7yEJgV",
    "vuYhtwL3wU",
    "yNGosLGlzY",
    "WNcpDlw1DK",
    "yJEBgrWGVV",
    "0cqkBGLcuZ",
    "YakkOE1XEl",
    "zE4b0O91Ht",
    "f5Z69VyHPb",
    "rEtor5JXi1",
    "VT2xqRSeb8",
    "sSIdoXI53u",
    "2QvzMpUK0s",
    "kBsyZcJjAp",
    "1sef4hybT3",
    "vokZ9LJS4o",
    "6eDgQyTRjT",
    "BZ2PJseg0o",
    "JSCglcmWWt",
    "QkYXECS6b0",
    "hJtDvBsVBe",
    "XWbd2ikyGj",
    "jMfoDZ1rx5",
    "JMDQox5UI0",
    "jm9Sqpfa8z",
    "zEEyxtQ2Yb",
    "5KoTnm3KGB",
    "bsvXd051Wx",
    "x5R14WOvWb",
    "mz0lTo3Gii",
    "5UaUhZbX5e",
    "pi8Nlxe8Sm",
    "scu45p0dHB",
    "ICmXCBtdct",
    "SYsfzlED2X",
    "vOK2VIAq7i",
    "kAVr0vWZDX",
    "x8TkO10cxE",
    "KpGsiKGBjW",
    "pxpn8QzX9c",
    "rfs3cHQePX",
    "Dl89d7QHz4",
    "tIPuVK2ZLf",
    "AasTyeGwTs",
    "umuToQRBEG",
    "6snEpVckF0",
    "w4t1UIgZNP",
    "rx6jhPB7pZ",
    "pu8maXbuDJ",
    "vePfJk3Ulu",
    "rgF4E9Cyhf",
    "Edj0ZzGLcD",
    "MGQTsR42Dy",
    "t42hpKQJOG",
    "Jbx1vkUZST",
    "wDGZKfh5Xi",
    "BCq4dGJVPM",
    "EyzOnZWIiX",
    "hy7pFPvWaT",
    "eVxo79aflL",
    "HyiPitDYfC",
    "shdCi8pmMT",
    "k4nBvHU4m5",
    "p2MQCJAmXg",
    "C7SRNU0Oe6",
    "tC8oSG1PeF",
    "eNTWp55ch5",
    "YuxqPMZ4IL",
    "bcaaaFAzIo",
    "CbAb8jeYWu",
    "cr9u9x4U0Z",
    "EEC3OrQjNk",
    "O3O9Q5eM6W",
    "EKftJyotS1",
    "L6P8T9WThc",
    "NhEKTo4bad",
    "DiIN2v2dvs",
    "hvjwsbMKSb",
    "4RAyN4dnvU",
    "gveUbgsuyk",
    "M9GYExqmEN",
    "kSG7ZTqb8t",
    "2k24BEUQ02",
    "V92Qp5KvTx",
    "twg5syodBj",
    "XuaNOuwgQp",
    "M0IsDIR0xq",
    "PcZStZNLqJ",
    "mWLJQ9SrxD",
    "PR9neZqSbC",
    "msvny07YsA",
    "5jpZQNL2Zt",
    "mMQF8qFMMQ",
    "7bcK8x9Vsh",
    "FqH9ueekGr",
    "acJqT95SLA",
    "nU4BwLSoBY",
    "kIIPmO0e58",
    "tE6I9pJ9er",
    "w6Qx2tsz9B",
    "1YZkOLsVwW",
    "WAyKDfOmKS",
    "DffGqGC2mc",
    "HQAxItCfgo",
    "7uduxVR9NT",
    "JIwLmIUrF9",
    "I1C01QKqO3",
    "X8QepaXdVe",
    "EVpzFk0PjT",
    "WTp6LTFxnP",
    "g7oZGT9TYt",
    "jZ49LuzkBS",
    "rDDTtMhRLw",
    "42ekids5qp",
    "L3ALLZro4h",
    "mGb0N7Zase",
    "AULCqcTxii",
]


def generate_account_data():
    sql_statements = []
    for i in range(1, 201):
        account_id = i
        travel_miles = random.randint(1, 200)
        password = PASSWORDS[i - 1]
        credit_card_number = "".join(str(random.randint(0, 9)) for _ in range(16))
        cvv = str(random.randint(100, 999))
        fk_passenger_id = f"P{i:0>3}"

        sql_statements.append(
            f"({account_id}, {travel_miles}, '{password}', '{credit_card_number}', '{cvv}', '{fk_passenger_id}')"
        )

    return (
        "INSERT INTO account (AccountID, TravelMiles, Password, CreditCardNumber, CVV, FK_PassengerID)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


AIRLINE = [
    "Baker, Neal and Allen",
    "Bailey PLC",
    "Navarro, Montes and Lambert",
    "Smith, Brady and Griffith",
    "Cameron, Rice and Davis",
    "Rodriguez-Aguilar",
    "Garcia-Decker",
    "Miller and Sons",
    "James-Reed",
    "Stevens-West",
    "Newton-King",
    "Fleming, Erickson and Bryant",
    "Hunter-Mccoy",
    "Stevens, Horton and Cook",
    "Valdez-Jordan",
    "Rush, Gray and Cline",
    "Landry, Cunningham and Sullivan",
    "Valenzuela, Simmons and Gomez",
    "Robinson, Ortiz and Thompson",
    "Mora Inc",
    "Sutton and Sons",
    "Martinez-Gray",
    "Duarte-Wood",
    "Rodriguez-Frey",
    "Walters-Turner",
    "Sanchez, Castaneda and Cooper",
    "Roberts, Stokes and Abbott",
    "King-Barnett",
    "Nielsen Ltd",
    "Diaz Group",
    "Bullock-Odonnell",
    "Williams, Anderson and Miller",
    "Welch-Saunders",
    "Powell, Ramos and Carlson",
    "Oneill-Fischer",
    "Allen-Cox",
    "Hamilton-Freeman",
    "Conway, Bryant and Brown",
    "Long Ltd",
    "Barrera, Hamilton and Berry",
    "Craig-Hensley",
    "Williams Ltd",
    "Fields, Crawford and Mitchell",
    "Bishop, Griffin and Macias",
    "Key and Sons",
    "Myers, Nguyen and Mcgrath",
    "Best Ltd",
    "Moore PLC",
    "Stevens, Fuller and Sexton",
    "Gutierrez, Moran and Merritt",
    "Porter-Choi",
    "Wilson, Brown and Riddle",
    "Silva Inc",
    "Obrien, Morrison and Morrison",
    "Buck-Macias",
    "Lam Ltd",
    "Hill-Rodriguez",
    "Bowman and Sons",
    "Frazier-Vasquez",
    "Lewis-Sandoval",
    "Young Group",
    "Martin, Heath and Hicks",
    "Wagner, Bernard and Mcdonald",
    "Nguyen, Davidson and Houston",
    "Johnson-Ramirez",
    "Munoz PLC",
    "Herrera PLC",
    "Soto-Johnson",
    "Williams, Kennedy and Wright",
    "Brewer, Thompson and Powers",
    "Adams-Lynch",
    "Peterson, Hughes and Holmes",
    "Foster-Taylor",
    "Shelton, Robertson and Smith",
    "Montes, Marshall and Horn",
    "Martinez, Porter and Henry",
    "Vargas-House",
    "Myers and Sons",
    "Thompson Group",
    "Mccarthy, Benson and Mathis",
    "Stevens-Pena",
    "Michael-Burns",
    "Vasquez LLC",
    "Harper-Phillips",
    "Lopez Ltd",
    "Gonzalez-Mora",
    "Ruiz-Rodriguez",
    "Payne, Gregory and Hall",
    "Mcpherson LLC",
    "Wilson Inc",
    "Trevino-James",
    "Burns, Page and Tanner",
    "Wilson Ltd",
    "Rocha and Sons",
    "White, Jenkins and Lopez",
    "Garcia, Camacho and Moore",
    "Crawford, Fletcher and Grant",
    "Reyes Inc",
    "Norman-Weaver",
    "Hernandez PLC",
    "Erickson, Cuevas and Johnston",
    "Meyer, Flores and Coleman",
    "Parrish and Sons",
    "Fields-Mcdaniel",
    "Carroll, Lucero and Allen",
    "Lopez-Franco",
    "Wilson-Thomas",
    "Clark, Brooks and Anderson",
    "Gonzales-Hardy",
    "Reynolds and Sons",
    "White, Alvarez and Allen",
    "Rowe PLC",
    "Pierce, Williams and Peterson",
    "Powers-Jones",
    "Meadows Inc",
    "Serrano Inc",
    "Kramer-Smith",
    "Gray, Dillon and Cross",
    "Erickson Inc",
    "Strickland, Patel and Cole",
    "Shields PLC",
    "Williams, Greer and Strickland",
    "Hall-Garcia",
    "Hodges-Hughes",
    "Vang, Palmer and Gonzalez",
    "Garcia-Lawson",
    "Miller, Hill and Flores",
    "Petty-White",
    "Lopez Group",
    "Hall Ltd",
    "Rodriguez-Robles",
    "Cox, Davis and Sexton",
    "Dyer, Zimmerman and Rodriguez",
    "Rodriguez PLC",
    "Johnson, Lopez and Murphy",
    "Morgan, Adams and Pearson",
    "Waters-Thompson",
    "Hernandez LLC",
    "Mullins and Sons",
    "Wagner and Sons",
    "Brown, Baker and Lloyd",
    "Mitchell, Harris and Munoz",
    "Williams, Rangel and Turner",
    "Glass-Carrillo",
    "Jones LLC",
    "Cameron-Jacobs",
    "Terry LLC",
    "Bowen Ltd",
    "Burns, Bridges and Sanchez",
    "Hughes LLC",
    "Leach-Higgins",
    "Velazquez-Ferguson",
    "Bradshaw Inc",
    "Meyer Group",
    "Davis, Smith and Owens",
    "Murray-Villegas",
    "Ritter, Greer and Smith",
    "Greene-Allen",
    "Jackson LLC",
    "Parker PLC",
    "Contreras LLC",
    "Merritt, Brown and Taylor",
    "Burns, Davis and Williams",
    "Williams, Trujillo and Hamilton",
    "Hubbard and Sons",
    "Stokes Group",
    "Nelson, Douglas and Soto",
    "Dixon and Sons",
    "Barnes LLC",
    "Marsh LLC",
    "Johnson-Haney",
    "Oliver, Adkins and Hoover",
    "Conway-Williams",
    "Little, Schaefer and Kerr",
    "Mckenzie Ltd",
    "Shelton Inc",
    "Koch Inc",
    "Jefferson, Gray and Howard",
    "Moore LLC",
    "Scott-Greene",
    "Lynch, Coleman and Goodman",
    "Johnston, Matthews and Walker",
    "Walker, Mcgrath and Long",
    "Smith LLC",
    "Nichols, Jimenez and Johnson",
    "Griffith, Rojas and Welch",
    "Stewart-Ross",
    "Torres-Whitney",
    "Armstrong-Williams",
    "Martin-Oliver",
    "Taylor-Byrd",
    "Bell-Snyder",
    "Williams Ltd",
    "Smith Inc",
    "Kelly, Benjamin and Rodriguez",
    "Lopez, Andrews and Torres",
    "Larsen, Walsh and Clark",
    "Dickerson Group",
    "Sparks, Castro and Dean",
    "Larson Inc",
]


def generate_airline_data():
    sql_statements = []
    for i in range(1, 201):
        name = AIRLINE[i - 1]
        airline_id = i
        sql_statements.append(f"('{name}', {airline_id})")

    return (
        "INSERT INTO airline (Name, AirlineID)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


AIRPORT_NAME_AND_LOCATION = [
    ("Ondores", "Charyshskoye"),
    ("Furong", "Berlin"),
    ("Yongshan", "Paobokol"),
    ("Kavajë", "Chãos"),
    ("Mazeikiai", "Damietta"),
    ("Botou", "Farroupilha"),
    ("San Antonio", "Dublin"),
    ("Gelemso", "Daba"),
    ("Hidalgo", "Garibaldi"),
    ("Nardaran", "Gueltat Zemmour"),
    ("Dunyāpur", "Karanlukh"),
    ("Lincheng", "Watthana Nakhon"),
    ("San Lorenzo", "Steinkjer"),
    ("Aguas del Padre", "Huangcun"),
    ("Khujirt", "Shibirghān"),
    ("Quy Đạt", "Simões Filho"),
    ("Ngamba", "Ózd"),
    ("Bernardo de Irigoyen", "Vis"),
    ("Glencoe", "Kuroda"),
    ("Xuefeng", "Berezivka"),
    ("Changbu", "Soltsy"),
    ("Santa Ignacia", "Dongdong"),
    ("Čeladná", "Hexi"),
    ("Date", "Zharkent"),
    ("Turrialba", "Buta"),
    ("Pucangkrajan", "Niort"),
    ("Beauharnois", "Sruni"),
    ("Sila", "Springfield"),
    ("Gaopai", "Llano de Piedra"),
    ("Batticaloa", "Maha Sarakham"),
    ("Kompóti", "Jelsa"),
    ("Chekmagush", "Jovellanos"),
    ("Veselynove", "Anping"),
    ("Veracruz", "Komyshany"),
    ("Abeokuta", "Allacapan"),
    ("Ad Dann", "Namayingo"),
    ("Guozhai", "Oetutulul"),
    ("Nueva Germania", "Zhangjiahe"),
    ("Wasquehal", "Guanban"),
    ("Oka", "Dayangzhou"),
    ("Mỹ Xuyên", "Biryulëvo"),
    ("Além Paraíba", "Pacobamba"),
    ("Fengyang", "Hūn"),
    ("Červené Pečky", "Yuandianhui"),
    ("Žandov", "Al Ghuwayrīyah"),
    ("Xintang", "Frutal"),
    ("Thị Trấn Mường Lát", "Fulu"),
    ("Terter", "Altona"),
    ("Tujing", "Chanuman"),
    ("Rossosh", "Wang Muang"),
    ("Sacanche", "Huikou"),
    ("Zhongba", "Honglu"),
    ("Haoshui", "Kryevidh"),
    ("Binan", "Itapuí"),
    ("Fais", "Nikolskoye"),
    ("Shakīso", "Izazi"),
    ("Myaydo", "Laimuda"),
    ("Panyarang", "Huashan"),
    ("Gubat", "Fullerton"),
    ("Melaka", "Foxton"),
    ("Lunen", "Mamedkala"),
    ("Sławatycze", "Cantilan"),
    ("Ha", "Columbus"),
    ("Xinshi", "Lipník nad Bečvou"),
    ("Orimattila", "São Miguel do Araguaia"),
    ("Wenquan", "Māymay"),
    ("Touho", "Qifang"),
    ("Cachoeira", "Sadabe"),
    ("Iriga City", "Caucasia"),
    ("Xuelu", "Shuangqiao"),
    ("Xiagong", "Belleville"),
    ("Porto-Novo", "Mabalacat"),
    ("Alung", "Gumalang"),
    ("Gambēla", "Amherst"),
    ("Fangyan", "Lianyun"),
    ("Toulouse", "Ursynów"),
    ("Wangpu", "Rasūlnagar"),
    ("Tegalsari", "Qitao"),
    ("Belfast", "Águas"),
    ("Matadi", "Mingcheng"),
    ("Tombu", "Mets Parni"),
    ("Nantes", "Guocun"),
    ("Dresden", "Samphanthawong"),
    ("Talitsy", "Quzhou"),
    ("Vydreno", "Lansing"),
    ("Zapala", "Sere"),
    ("Želetava", "Siso"),
    ("Polovinnoye", "Langsa"),
    ("Brodósqui", "Quwa"),
    ("Maracanã", "Tekikbanyuurip"),
    ("Marxog", "Xia Zanggor"),
    ("Huangjin", "Geneng"),
    ("Fornos", "San Miguel"),
    ("Buenos Aires", "Lafiagi"),
    ("Toužim", "Prokhladnyy"),
    ("Stockholm", "Ruyigi"),
    ("Bohutín", "Lam Plai Mat"),
    ("Lewotola", "Scranton"),
    ("Sunjia Buzi", "Kurihashi"),
    ("Gose", "Jiexiu"),
    ("Candon", "Siennica Różana"),
    ("Salamá", "Khodzha-Maston"),
    ("Pagatan", "Mijiang"),
    ("Qinjiang", "Pokrovskoye"),
    ("Irbid", "Mirriah"),
    ("Kalibaru", "Chemal"),
    ("Sukaraharja", "Santa Rosa"),
    ("Baracoa", "Reshetylivka"),
    ("Lanling", "Franco da Rocha"),
    ("Quillabamba", "Lakbok"),
    ("Mitrovicë", "Jincheng"),
    ("Sanjiang", "Rangxi"),
    ("Whittier", "Panaoti"),
    ("Cergy-Pontoise", "Tarhuna"),
    ("Smithers", "Buenlag"),
    ("Brodnica", "Toulouse"),
    ("Daogao", "Nouna"),
    ("Béré", "Pangascasan"),
    ("Gjilan", "Mahalapye"),
    ("Stanowice", "Juyuan"),
    ("Changjiang", "La Gacilly"),
    ("Mongo", "Bulusari"),
    ("Kamwenge", "Pingding"),
    ("Leipzig", "Hikkaduwa"),
    ("Omišalj", "Cabaritan East"),
    ("Dongzaogang", "Varna"),
    ("Belsk Duży", "Taiyu"),
    ("Penelas", "Rejanegara"),
    ("Ajdabiya", "Krajan"),
    ("Gebang", "Trảng Bom"),
    ("Koktokay", "Banhā"),
    ("Laojiangjunjie", "Rumilly"),
    ("Kebonan", "Ozerki"),
    ("Libato", "Destrnik"),
    ("New York City", "Cabinda"),
    ("Huazhou", "El Charco"),
    ("Tlučná", "Mandesan"),
    ("Capayán", "Ignacio Zaragoza"),
    ("Mâcon", "Honolulu"),
    ("Karangboyo", "Harhorin"),
    ("Puerto Mayor Otaño", "Osan"),
    ("Dolno Palčište", "Seidu"),
    ("Boyarka", "Šavnik"),
    ("Vidoši", "Port Elizabeth"),
    ("Pajoreja", "Maraã"),
    ("Zhenlai", "Laowobao"),
    ("Lazaro Cardenas", "Looc"),
    ("Valence", "Huaping"),
    ("Ronneby", "Kumba"),
    ("Grugul", "Aix-les-Bains"),
    ("Xinmin", "Chiclayo"),
    ("Anambongan", "Ai Tu"),
    ("Lydenburg", "Kang-neung"),
    ("Kuwayris Sharqī", "Rūjayb"),
    ("Červená Voda", "Maiac"),
    ("Kamień Pomorski", "Karinë"),
    ("Qongirot Shahri", "Prakhon Chai"),
    ("Youzha", "Hājīganj"),
    ("Sembungin", "Pale"),
    ("Vukatanë", "Koryukivka"),
    ("Calizo", "Tabora"),
    ("Hukeng", "Bukbatang"),
    ("Dijon", "Kakuda"),
    ("Huazhai", "Domampot"),
    ("Chuncheon", "Rio Meão"),
    ("Jinqiao", "Parfino"),
    ("Jacareí", "Tejen"),
    ("Nīkshahr", "Małdyty"),
    ("Gyumri", "Ivanec"),
    ("Phu Luang", "Jishui"),
    ("Palma De Mallorca", "Nakhon Pathom"),
    ("Skuratovskiy", "Skopje"),
    ("Sabang", "Tenjolaya"),
    ("Moncton", "Dawung"),
    ("Huurch", "Nurabelen"),
    ("Mošorin", "Panyam"),
    ("Rubiataba", "Wenshao"),
    ("Manizales", "Szczecin"),
    ("Tawaramoto", "Shurugwi"),
    ("Yugawara", "Tangjia"),
    ("Guangyi", "Yuanping"),
    ("Gelgaudiškis", "Bāfq"),
    ("Datuan", "Temorlorong"),
    ("Jiucaizhuang", "Kolonia Town"),
    ("Ozerki", "Ängelholm"),
    ("Fuxing", "Sigli"),
    ("Zgornje Pirniče", "Avelar"),
    ("Duozhu", "Farshūţ"),
    ("Shuishi", "Santiago de Cao"),
    ("Pangantocan", "Boconó"),
    ("Balong Wetan", "Amarete"),
    ("Panaytayon", "Bourges"),
    ("Hradec nad Moravici", "Sangumata"),
    ("San Nicolas", "Tayzhina"),
    ("Moa", "Palestina de los Altos"),
    ("Jiuli", "Burgos"),
    ("Jeffreys Bay", "Asaita"),
    ("Barberena", "Qanlikol"),
    ("Karasuyama", "Lyon"),
    ("Silab", "Tinumpuk"),
]


def generate_airport_data():
    sql_statements = []
    for i in range(1, 201):
        airport_id = i
        name, location = AIRPORT_NAME_AND_LOCATION[i - 1]
        size = random.randint(3000, 20000)

        sql_statements.append(f"({airport_id}, '{name}', '{location}', {size})")

    return (
        "INSERT INTO airport (AirportID, Name, Location, Size)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


RANDOM_SEAT_NUMBERS = list(range(1, 601))

random.shuffle(RANDOM_SEAT_NUMBERS)

FIRST_CLASS_SEATS = RANDOM_SEAT_NUMBERS[:200]
BUSINESS_CLASS_SEATS = RANDOM_SEAT_NUMBERS[200:400]
OTHER_FLIGHT_CLASS_SEATS = RANDOM_SEAT_NUMBERS[400:]


def generate_business_data():
    sql_statements = []
    for _, (seat_number, fk_flight_id) in enumerate(TUPLES[2]):
        availability = random.choice([True, False])
        is_reclining = random.choice([True, False])

        sql_statements.append(
            f"({seat_number},{availability},{fk_flight_id},{is_reclining})"
        )

    return (
        "INSERT INTO business (SeatNumber , Availability , FK_FlightID , Is_Reclining)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


CARGO_TYPE = ["Perishable", "Non-Perishable", "Fragile", "Heavy", "Light", "Hazardous"]


def generate_cargo_airliner_data():
    sql_statements = []
    for i in range(1, 201):
        flight_id = i
        cargo_type = random.choice(CARGO_TYPE)
        sql_statements.append(f"({flight_id},'{cargo_type}')")

    return (
        "INSERT INTO cargoairliner (FlightID , CargoType)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


def generate_first_class_data():
    sql_statements = []
    for _, (seat_number, fk_flight_id) in enumerate(TUPLES[0]):
        availability = random.choice([True, False])
        has_lounge_access = random.choice([True, False])
        priority_boarding = random.choice([True, False])

        sql_statements.append(
            f"({seat_number},{availability},{fk_flight_id},{has_lounge_access},{priority_boarding})"
        )

    return (
        "INSERT INTO firstclass (SeatNumber , Availability , FK_FlightID , HasLoungeAccess , PriorityBoarding)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


FLIGHT_MODELS = [
    "Bombardier 561",
    "Embraer 126",
    "Tupolev 685",
    "Boeing 864",
    "Boeing 423",
    "Airbus 740",
    "Boeing 781",
    "Embraer 421",
    "Tupolev 844",
    "Bombardier 945",
    "Tupolev 556",
    "Bombardier 528",
    "Boeing 670",
    "Tupolev 722",
    "Tupolev 804",
    "Bombardier 574",
    "Tupolev 166",
    "Airbus 955",
    "Tupolev 191",
    "Boeing 309",
    "Embraer 386",
    "Bombardier 167",
    "Embraer 170",
    "Boeing 306",
    "Boeing 605",
    "Tupolev 252",
    "Airbus 211",
    "Airbus 184",
    "Bombardier 880",
    "Bombardier 111",
    "Embraer 190",
    "Embraer 486",
    "Airbus 895",
    "Embraer 731",
    "Bombardier 554",
    "Boeing 788",
    "Boeing 405",
    "Airbus 142",
    "Boeing 606",
    "Boeing 531",
    "Airbus 511",
    "Airbus 452",
    "Tupolev 676",
    "Tupolev 238",
    "Bombardier 546",
    "Bombardier 679",
    "Bombardier 366",
    "Embraer 915",
    "Embraer 976",
    "Tupolev 660",
    "Bombardier 620",
    "Airbus 471",
    "Tupolev 230",
    "Boeing 858",
    "Tupolev 435",
    "Bombardier 332",
    "Bombardier 641",
    "Embraer 230",
    "Embraer 960",
    "Bombardier 998",
    "Tupolev 214",
    "Tupolev 654",
    "Embraer 233",
    "Bombardier 613",
    "Embraer 992",
    "Bombardier 263",
    "Airbus 608",
    "Airbus 683",
    "Tupolev 696",
    "Bombardier 357",
    "Tupolev 381",
    "Embraer 944",
    "Tupolev 610",
    "Boeing 938",
    "Embraer 762",
    "Boeing 307",
    "Tupolev 162",
    "Airbus 442",
    "Bombardier 307",
    "Boeing 167",
    "Airbus 202",
    "Bombardier 431",
    "Airbus 259",
    "Boeing 654",
    "Bombardier 483",
    "Tupolev 820",
    "Embraer 468",
    "Airbus 554",
    "Boeing 381",
    "Boeing 703",
    "Tupolev 761",
    "Tupolev 272",
    "Embraer 476",
    "Tupolev 878",
    "Bombardier 213",
    "Embraer 788",
    "Bombardier 962",
    "Boeing 670",
    "Tupolev 797",
    "Tupolev 576",
    "Tupolev 442",
    "Airbus 663",
    "Airbus 992",
    "Airbus 819",
    "Airbus 302",
    "Embraer 269",
    "Bombardier 207",
    "Embraer 484",
    "Boeing 594",
    "Bombardier 777",
    "Bombardier 841",
    "Airbus 992",
    "Tupolev 409",
    "Airbus 127",
    "Tupolev 804",
    "Tupolev 627",
    "Tupolev 399",
    "Embraer 133",
    "Bombardier 448",
    "Bombardier 296",
    "Embraer 169",
    "Tupolev 739",
    "Tupolev 980",
    "Boeing 915",
    "Bombardier 314",
    "Tupolev 220",
    "Airbus 636",
    "Boeing 586",
    "Airbus 477",
    "Bombardier 859",
    "Bombardier 550",
    "Tupolev 338",
    "Boeing 231",
    "Bombardier 870",
    "Airbus 166",
    "Airbus 747",
    "Embraer 130",
    "Airbus 595",
    "Airbus 928",
    "Airbus 402",
    "Boeing 255",
    "Tupolev 166",
    "Tupolev 310",
    "Bombardier 592",
    "Boeing 130",
    "Boeing 626",
    "Airbus 408",
    "Boeing 882",
    "Airbus 862",
    "Tupolev 770",
    "Tupolev 872",
    "Embraer 111",
    "Bombardier 415",
    "Embraer 333",
    "Boeing 357",
    "Tupolev 916",
    "Boeing 879",
    "Airbus 549",
    "Airbus 531",
    "Airbus 530",
    "Tupolev 804",
    "Airbus 658",
    "Tupolev 632",
    "Bombardier 859",
    "Bombardier 140",
    "Tupolev 396",
    "Bombardier 707",
    "Tupolev 377",
    "Boeing 424",
    "Tupolev 434",
    "Airbus 975",
    "Airbus 535",
    "Boeing 595",
    "Boeing 343",
    "Bombardier 409",
    "Bombardier 855",
    "Embraer 622",
    "Boeing 990",
    "Bombardier 406",
    "Boeing 339",
    "Airbus 857",
    "Bombardier 990",
    "Airbus 896",
    "Embraer 757",
    "Airbus 495",
    "Embraer 303",
    "Tupolev 728",
    "Boeing 963",
    "Tupolev 248",
    "Airbus 720",
    "Tupolev 398",
    "Bombardier 720",
    "Embraer 908",
    "Boeing 296",
    "Tupolev 301",
    "Embraer 626",
    "Boeing 715",
    "Embraer 880",
    "Tupolev 809",
    "Embraer 573",
]


def generate_flight_data():
    sql_statements = []
    for i in range(1, 201):
        flight_id = i
        max_passengers = random.randint(50, 500)
        max_weight = random.uniform(10000.0, 100000.0)
        model = FLIGHT_MODELS[i - 1]
        fk_airline_id = random.randint(1, 200)

        sql_statements.append(
            f"({flight_id},{max_passengers},{max_weight:.2f},'{model}',{fk_airline_id})"
        )

    return (
        "INSERT INTO flight (FlightID , MaxPassengers , MaxWeight , Model , FK_AirlineID)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


LUGGAGE_TYPES = [
    "Suitcase",
    "Backpack",
    "Duffel bag",
    "Garment bag",
    "Tote bag",
    "Briefcase",
    "Carry-on bag",
    "Rolling suitcase",
    "Travel backpack",
    "Laptop bag",
    "Messenger bag",
    "Shoulder bag",
    "Hiking backpack",
    "Satchel",
    "Waist pack",
    "Weekender bag",
    "Trunk",
    "Hardshell suitcase",
    "Softshell suitcase",
    "Spinner suitcase",
]

HANDLING_INSTRUCTIONS = [
    "Fragile",
    "Handle with care",
    "Do not stack",
    "This side up",
    "Keep dry",
    "Keep away from heat",
    "Do not bend",
    "Do not crush",
    "Perishable",
    "Hazardous material",
    "Do not expose to sunlight",
    "Keep frozen",
    "Flammable",
    "Explosive",
    "Corrosive",
    "Toxic",
    "Radioactive",
    "Oxidizing agent",
    "Compressed gas",
]

DESCRIPTIONS = [
    "Electronics",
    "Clothing",
    "Sports equipment",
    "Musical instrument",
    "Food items",
    "Medication",
    "Toiletries",
    "Jewelry",
    "Documents",
    "Books",
    "Toys",
    "Art supplies",
    "Shoes",
    "Accessories",
    "Home goods",
    "Office supplies",
    "Cosmetics",
    "Furniture",
    "Tools",
    "Pet supplies",
]

CARGO_CLASSES = [
    "Economy",
    "Business",
    "First Class",
    "Premium Economy",
    "Comfort Plus",
    "Upper Class",
    "Basic Economy",
    "Standard Economy",
    "Deluxe Economy",
    "Executive Class",
    "Royal Class",
    "Presidential Suite",
]


def generate_luggage_data():
    sql_statements = []
    for i in range(1, 201):
        luggage_id = f"L{i:0>3}"
        price = random.uniform(10.0, 500.0)
        weight = random.uniform(1.0, 50.0)
        fk_passenger_id = f"P{i:0>3}"
        fk_flight_id = random.randint(1, 200)
        true_flag_index = random.randint(0, 2)
        if true_flag_index == 0:
            carry_on_flag = True
            luggage_type = f"'{random.choice(LUGGAGE_TYPES)}'"
            liquid_limit = random.randint(0, 1000)
            check_in_flag = False
            cargo_class = "NULL"
            specialized_flag = False
            description = "NULL"
            fragility = "NULL"
            handling_instructions = "NULL"
        elif true_flag_index == 1:
            carry_on_flag = False
            luggage_type = "NULL"
            liquid_limit = "NULL"
            check_in_flag = True
            cargo_class = f"'{random.choice(CARGO_CLASSES)}'"
            specialized_flag = False
            description = "NULL"
            fragility = "NULL"
            handling_instructions = "NULL"
        else:
            carry_on_flag = False
            luggage_type = "NULL"
            liquid_limit = "NULL"
            check_in_flag = False
            cargo_class = "NULL"
            specialized_flag = True
            description = f"'{random.choice(DESCRIPTIONS)}'"
            fragility = random.choice([False, True])
            handling_instructions = (
                f"'{random.choice(HANDLING_INSTRUCTIONS)}'" if fragility else "NULL"
            )

        sql_statements.append(
            f"('{luggage_id}',{price:.2f},{weight:.2f},'{fk_passenger_id}',{fk_flight_id},{carry_on_flag},{luggage_type},{liquid_limit},{check_in_flag},{cargo_class},{specialized_flag},{description},{fragility},{handling_instructions})"
        )

    return (
        "INSERT INTO luggage (LuggageID , Price , Weight , FK_PassengerID , FK_FlightID , CarryOnFlag , Type , LiquidLimit , CheckInFlag , CargoClass , SpecializedFlag , Description , Fragility , HandlingInstructions)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


def generate_other_flight_class_data():
    sql_statements = []
    for _, (seat_number, fk_flight_id) in enumerate(TUPLES[1]):
        availability = random.choice([True, False])
        is_standing_seat = random.choice([True, False])

        sql_statements.append(
            f"({seat_number},{availability},{fk_flight_id},{is_standing_seat})"
        )

    return (
        "INSERT INTO otherflightclass (SeatNumber , Availability , FK_FlightID , IsStandingSeat)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


NAMES = [
    ("Matthew", "Myers"),
    ("Tara", "Miller"),
    ("Carol", "Stanton"),
    ("Trevor", "Lee"),
    ("Carrie", "Castillo"),
    ("Taylor", "Lopez"),
    ("Cindy", "Mccall"),
    ("Matthew", "Bass"),
    ("Norma", "Daugherty"),
    ("Jacob", "Wong"),
    ("Christine", "Adams"),
    ("Erin", "Butler"),
    ("James", "Martinez"),
    ("Danielle", "Lyons"),
    ("Jillian", "Olsen"),
    ("Mary", "Williamson"),
    ("Jonathan", "Lopez"),
    ("Gabriella", "Waters"),
    ("Thomas", "Anderson"),
    ("Anthony", "Jones"),
    ("Patrick", "Ramos"),
    ("Heidi", "Porter"),
    ("Melissa", "Bates"),
    ("Sarah", "Nash"),
    ("Micheal", "Lewis"),
    ("Richard", "Herrera"),
    ("Madeline", "Hamilton"),
    ("Kenneth", "Clark"),
    ("Christopher", "Ward"),
    ("Brianna", "Malone"),
    ("Lee", "Olsen"),
    ("Kathryn", "Dean"),
    ("Timothy", "Jones"),
    ("Edwin", "Miller"),
    ("Ryan", "Escobar"),
    ("Jennifer", "Long"),
    ("Mallory", "Ramirez"),
    ("Justin", "Hogan"),
    ("Richard", "Miller"),
    ("Barry", "Compton"),
    ("Michael", "Chavez"),
    ("Amanda", "Ramos"),
    ("Benjamin", "Sullivan"),
    ("Mary", "Jackson"),
    ("Steven", "Holmes"),
    ("Shannon", "Mcneil"),
    ("Jill", "Taylor"),
    ("Christine", "Wilson"),
    ("Victoria", "Roberson"),
    ("Jacqueline", "Moore"),
    ("Paul", "Brown"),
    ("Vanessa", "Farmer"),
    ("Maxwell", "Leblanc"),
    ("James", "Alvarez"),
    ("April", "Gomez"),
    ("Cory", "Jackson"),
    ("Michael", "Brooks"),
    ("Kathryn", "Ramos"),
    ("William", "Taylor"),
    ("Cathy", "Price"),
    ("Haley", "Perez"),
    ("Gabriel", "Brown"),
    ("Manuel", "Schmidt"),
    ("Brandon", "Martinez"),
    ("Anthony", "Lee"),
    ("Kyle", "Archer"),
    ("Jacqueline", "Morse"),
    ("Lori", "Brown"),
    ("Matthew", "Cameron"),
    ("Christina", "Matthews"),
    ("Adrian", "Reynolds"),
    ("Carol", "Williams"),
    ("Kathleen", "May"),
    ("David", "Martinez"),
    ("Briana", "Cox"),
    ("Cynthia", "Mccarty"),
    ("Jesse", "Stokes"),
    ("Susan", "Kennedy"),
    ("Stephanie", "Hubbard"),
    ("Mallory", "Parker"),
    ("Melinda", "Mason"),
    ("Jerome", "Rogers"),
    ("Jacqueline", "Anderson"),
    ("Jennifer", "Carter"),
    ("Brianna", "Sanchez"),
    ("Leslie", "Lee"),
    ("Stephanie", "Rogers"),
    ("Kevin", "Dawson"),
    ("Ricky", "Ferguson"),
    ("Troy", "Jones"),
    ("Laura", "Hicks"),
    ("Kenneth", "Beard"),
    ("David", "Phillips"),
    ("Mariah", "Gutierrez"),
    ("Benjamin", "Contreras"),
    ("Christopher", "Rivera"),
    ("David", "Webster"),
    ("Kathryn", "Pham"),
    ("Jacob", "Johnson"),
    ("John", "Harris"),
    ("Amber", "Hammond"),
    ("Jennifer", "Robinson"),
    ("Elizabeth", "Padilla"),
    ("Nancy", "Moore"),
    ("Kathleen", "Bell"),
    ("Ralph", "Giles"),
    ("Dawn", "Wilson"),
    ("Jillian", "Allen"),
    ("Robert", "Foster"),
    ("Justin", "Andersen"),
    ("Kathleen", "Harris"),
    ("Joan", "Blevins"),
    ("Ricky", "Wells"),
    ("Christopher", "Mendoza"),
    ("Steven", "Martin"),
    ("Victor", "Castro"),
    ("Diana", "Yates"),
    ("Brian", "Mendez"),
    ("John", "Moran"),
    ("Chelsea", "Myers"),
    ("Larry", "Martin"),
    ("Charles", "Miller"),
    ("Dennis", "White"),
    ("Alexander", "Cole"),
    ("Amy", "Ellison"),
    ("Amanda", "Coffey"),
    ("Jessica", "Wagner"),
    ("Valerie", "Hughes"),
    ("Kevin", "Gonzalez"),
    ("Bethany", "Valdez"),
    ("Jason", "Spencer"),
    ("Lauren", "Cantrell"),
    ("Jeremy", "Fields"),
    ("Catherine", "Garcia"),
    ("Rachel", "Yu"),
    ("Lisa", "Nelson"),
    ("Erin", "Alvarez"),
    ("Theresa", "Clark"),
    ("Kenneth", "Roberts"),
    ("Lisa", "Estrada"),
    ("Joshua", "Casey"),
    ("Melinda", "Jackson"),
    ("Connie", "Hicks"),
    ("William", "Moore"),
    ("Christopher", "Hanson"),
    ("Caitlin", "Howard"),
    ("Megan", "Mitchell"),
    ("Derrick", "Torres"),
    ("Carol", "Chambers"),
    ("Christopher", "Rosario"),
    ("Cody", "Baird"),
    ("Rebekah", "Brown"),
    ("Kathy", "Kim"),
    ("Lisa", "Murphy"),
    ("Brian", "Cohen"),
    ("Shelby", "Koch"),
    ("Joseph", "Barnes"),
    ("Christine", "Christensen"),
    ("Amy", "Knox"),
    ("Courtney", "Rice"),
    ("Richard", "Freeman"),
    ("Bryan", "Wilson"),
    ("Lauren", "Horton"),
    ("Cynthia", "Stewart"),
    ("Paul", "Miller"),
    ("Tracey", "Anderson"),
    ("Michael", "Ellis"),
    ("William", "Turner"),
    ("Christina", "Mason"),
    ("Jim", "Williams"),
    ("David", "Clark"),
    ("Kimberly", "French"),
    ("Richard", "Santiago"),
    ("Ruth", "Allen"),
    ("Carrie", "Taylor"),
    ("Shawn", "Cortez"),
    ("Matthew", "Orr"),
    ("Sierra", "Tucker"),
    ("John", "Smith"),
    ("Kimberly", "Green"),
    ("Daniel", "Wolfe"),
    ("Terrance", "Chandler"),
    ("Craig", "Harper"),
    ("John", "Martin"),
    ("Heather", "Noble"),
    ("Steven", "Moody"),
    ("Justin", "Murphy"),
    ("Anthony", "Newman"),
    ("Bobby", "Benson"),
    ("Mary", "Galvan"),
    ("Richard", "Fisher"),
    ("David", "Mueller"),
    ("Brian", "Dougherty"),
    ("Maria", "Rodriguez"),
    ("Anne", "Clayton"),
    ("Thomas", "Anderson"),
    ("Madison", "Lee"),
    ("Jamie", "Juarez"),
    ("Kimberly", "Robinson"),
    ("Allison", "Smith"),
]


def generate_passenger_data():
    sql_statements = []
    for i in range(1, 201):
        passenger_id = f"P{i:0>3}"
        first_name, last_name = NAMES[i - 1]
        dob = f"{random.randint(1950,2010)}-{random.randint(1,12):0>2}-{random.randint(1,28):0>2}"

        sql_statements.append(
            f"('{passenger_id}','{first_name}','{last_name}','{dob}')"
        )

    return (
        "INSERT INTO passenger (PassengerID , FirstName , LastName , DOB)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


def generate_passenger_airliner_data():
    sql_statements = []
    for i in range(1, 201):
        flight_id = i
        number_of_flight_attendants = random.randint(1, 10)

        sql_statements.append(f"({flight_id},{number_of_flight_attendants})")

    return (
        "INSERT INTO passengerairliner (FlightID , NumberOfFlightAttendants)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


OWNERS = [
    "Cindy Bates",
    "Chelsea Kennedy",
    "Amy Mcdaniel",
    "Dorothy Short",
    "Michael Hernandez",
    "Teresa Maynard",
    "Robert Cunningham",
    "Chase Cabrera",
    "Jennifer Zamora",
    "Melanie Fisher",
    "Thomas Miller",
    "Jacqueline Robinson",
    "Stephanie Clayton",
    "Edward Tucker",
    "Jesse Mitchell",
    "Brenda Campbell",
    "Gregory Blackwell",
    "Susan Jones",
    "Stephen Carter",
    "Denise Porter",
    "Maria Rodriguez",
    "Eric Caldwell",
    "Amber Jones",
    "John Alexander",
    "Nicholas Pitts",
    "Michael Oneal",
    "Ashley Nichols",
    "Paul Wright",
    "Adam Grant",
    "Rhonda Knight",
    "Jerry Wood",
    "Austin Carter",
    "Denise Graham",
    "Nancy Carter",
    "Russell Kelley",
    "Sean Bryant",
    "Brianna Fernandez",
    "James Hansen",
    "Alexander Mcdaniel",
    "Troy Reyes",
    "Megan Brady",
    "Daniel Richardson",
    "Rhonda Miller",
    "Heather White",
    "Timothy Lutz",
    "Denise Atkinson",
    "Bruce Parrish",
    "Pamela Holmes",
    "Arthur Harding",
    "Lorraine Austin",
    "Alexandra Montoya",
    "Catherine Johnson",
    "Sonya Dyer",
    "Jeff Zuniga",
    "Emily Holland",
    "Zachary Watson",
    "Jill Powell",
    "Antonio Barnes",
    "Michelle Harris",
    "Jennifer Jensen",
    "Christina Hull",
    "Dennis Acosta",
    "Mr. Samuel Hull",
    "Patricia Ortega",
    "Robert Collins",
    "Logan Osborn",
    "Michele Palmer",
    "Karen Thompson",
    "Julia Lowe",
    "Natasha Montgomery",
    "Rebecca Weaver",
    "Michelle Long",
    "Janet Kaufman",
    "Howard Tran",
    "Emily Spencer",
    "Joshua Johnson",
    "Melissa Arnold",
    "Benjamin Harris",
    "John Medina",
    "Samantha Todd",
    "Ronald Ortega",
    "Donald Miller",
    "Cheryl Vega",
    "Timothy Simmons",
    "James Lewis",
    "James Gilbert",
    "Tara Marshall",
    "Tina West",
    "Carrie Kelly",
    "Gregory Gregory",
    "Chad Weber",
    "Stephanie Rogers",
    "Deborah Peterson",
    "Steven Smith",
    "Kurt Little",
    "Andrew Pratt",
    "Christopher Douglas",
    "James Smith",
    "Jesus Figueroa",
    "Patrick Parker",
    "Deanna Orozco",
    "Melissa Burke",
    "Nicholas Roberts",
    "Andrew Cunningham",
    "Eric Hernandez",
    "Michael Green",
    "Briana Munoz",
    "Tara Thomas",
    "Derek Romero",
    "Michael Thomas",
    "Trevor Fields",
    "Stephen Smith",
    "Jennifer Perez",
    "Patrick Reynolds",
    "Danielle Welch",
    "Alexandria Brown",
    "Kayla Bowman",
    "Stephanie Day",
    "Cody Wilson",
    "Debra Michael",
    "Richard Hernandez",
    "Abigail Stout",
    "Jenny Lowery",
    "Amanda Gonzalez",
    "Kathryn Carr",
    "Austin Preston",
    "Joseph Lowery",
    "Tammy Campbell",
    "Victoria Russell",
    "Jeffrey Hamilton",
    "Brittany Harris",
    "Jorge George",
    "Jeremy Moon",
    "Austin Bruce",
    "Theresa Gordon",
    "Timothy Floyd",
    "Stephanie Garcia",
    "Kathryn Chambers",
    "Daniel Kelly",
    "Ian Johnson",
    "Kenneth Odom",
    "Angela Dunlap",
    "Kathleen Solis",
    "Heather Ward",
    "Brooke Sampson",
    "Hannah Berger",
    "Gary Grant",
    "Raymond Clayton",
    "Natasha Baker",
    "Adam Price",
    "Nicholas Johnson",
    "Christopher Miller",
    "Joshua Ross",
    "James Sampson",
    "Todd Lamb",
    "Madison Raymond",
    "Lisa Lee",
    "Sean Webb",
    "Samuel Burke",
    "David Richardson",
    "Thomas Johnson",
    "Xavier Trujillo",
    "Richard Mcbride",
    "William Edwards",
    "Zachary Roth",
    "Dustin Nelson",
    "Charles Stephens",
    "Jesus Murphy",
    "Emily Warren",
    "Amanda Ballard",
    "Cathy Walker",
    "Lori Holmes",
    "Thomas Long",
    "Diana Molina",
    "Haley Jones",
    "Amber Marshall",
    "Heather Ayala",
    "Tonya Kaufman",
    "Jessica Williams",
    "Jesse Brown",
    "Amanda Collins",
    "Martin Walton",
    "April Torres",
    "Stephen Hull",
    "Nicole Alvarado",
    "Timothy Gentry",
    "Thomas Singleton",
    "Mr. Rick Young",
    "Joseph Fisher",
    "Jessica Anderson",
    "Sarah Wells",
    "Brooke Farmer",
    "Brandon Joyce",
    "Richard Cardenas",
    "Michael Torres",
    "Deborah Zavala",
    "Debra Carpenter",
    "Alexandra Mcfarland",
    "Roger Simmons",
    "Chelsea Lane",
]


def generate_private_jet_data():
    sql_statements = []
    for i in range(1, 201):
        flight_id = i
        owner = OWNERS[i - 1]

        sql_statements.append(f"({flight_id},'{owner}')")

    return (
        "INSERT INTO privatejet (FlightID , Owner)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


STATUS = [
    ("Lake Jose", "Windy"),
    ("North Timothy", "Cloudy"),
    ("Lake Rodneybury", "Rainy"),
    ("Davidside", "Rainy"),
    ("Port Nicholas", "Windy"),
    ("Lake Mariatown", "Cloudy"),
    ("Mullinstown", "Rainy"),
    ("Port Christopherhaven", "Foggy"),
    ("North Patriciafort", "Snowy"),
    ("Phillipsshire", "Rainy"),
    ("South Emilyfurt", "Sunny"),
    ("Brewerhaven", "Sunny"),
    ("Fernandezburgh", "Rainy"),
    ("Clarkeview", "Snowy"),
    ("New Stevenborough", "Foggy"),
    ("Weissmouth", "Sunny"),
    ("Amyton", "Rainy"),
    ("North Lindafurt", "Windy"),
    ("New Jessica", "Snowy"),
    ("Lake Dakota", "Sunny"),
    ("Guerraview", "Rainy"),
    ("East Alejandromouth", "Sunny"),
    ("Port Jack", "Sunny"),
    ("South Jenniferview", "Cloudy"),
    ("Murphyshire", "Cloudy"),
    ("Smithfurt", "Snowy"),
    ("Lewisberg", "Foggy"),
    ("Bryanport", "Foggy"),
    ("Patriciaberg", "Foggy"),
    ("Daveland", "Cloudy"),
    ("New Jerry", "Windy"),
    ("Woodwardfurt", "Windy"),
    ("West Teresa", "Snowy"),
    ("North Gabrielle", "Snowy"),
    ("Lake Pamelaport", "Sunny"),
    ("Davidfurt", "Windy"),
    ("Wrighthaven", "Sunny"),
    ("East Kevin", "Snowy"),
    ("East Tiffanyside", "Foggy"),
    ("Andrewside", "Cloudy"),
    ("North Christopherside", "Rainy"),
    ("North Wesley", "Foggy"),
    ("Delgadotown", "Snowy"),
    ("Pattersonborough", "Sunny"),
    ("Danielshire", "Cloudy"),
    ("East Darrenmouth", "Sunny"),
    ("Murraymouth", "Windy"),
    ("Port Paulton", "Foggy"),
    ("East Jacob", "Sunny"),
    ("North Ashleytown", "Cloudy"),
    ("West Trevorview", "Sunny"),
    ("Timothymouth", "Snowy"),
    ("East Eric", "Sunny"),
    ("South Edwardview", "Rainy"),
    ("North Toddfurt", "Cloudy"),
    ("West Veronica", "Cloudy"),
    ("North Ronaldfort", "Cloudy"),
    ("Port Danielleview", "Sunny"),
    ("Hollyfort", "Snowy"),
    ("Munozmouth", "Foggy"),
    ("Orozcoville", "Cloudy"),
    ("Rachelshire", "Foggy"),
    ("East Valerieburgh", "Foggy"),
    ("Sherrytown", "Sunny"),
    ("Victoriafurt", "Cloudy"),
    ("Hammondberg", "Cloudy"),
    ("South Leahmouth", "Windy"),
    ("Port Katie", "Foggy"),
    ("Cruzshire", "Sunny"),
    ("West Kellybury", "Windy"),
    ("West Jennifer", "Cloudy"),
    ("Browntown", "Rainy"),
    ("Brendaland", "Foggy"),
    ("East Melissa", "Windy"),
    ("South Sheila", "Snowy"),
    ("Hutchinsonbury", "Snowy"),
    ("Danielton", "Foggy"),
    ("Williamstad", "Cloudy"),
    ("Port Daniel", "Foggy"),
    ("Hudsonchester", "Cloudy"),
    ("Davidbury", "Rainy"),
    ("West Matthew", "Snowy"),
    ("North Jenny", "Snowy"),
    ("West Amandaland", "Sunny"),
    ("Mariaville", "Foggy"),
    ("New Ianland", "Rainy"),
    ("Langside", "Foggy"),
    ("Karenfort", "Foggy"),
    ("South Jacob", "Foggy"),
    ("Ruizton", "Snowy"),
    ("West Christopherport", "Snowy"),
    ("Gordonville", "Snowy"),
    ("West Juliehaven", "Sunny"),
    ("West Christinechester", "Rainy"),
    ("South Davidside", "Foggy"),
    ("Elizabethton", "Snowy"),
    ("West Jeffrey", "Windy"),
    ("North Elizabeth", "Sunny"),
    ("Port Michaelmouth", "Cloudy"),
    ("Allisonstad", "Foggy"),
    ("East Dominique", "Sunny"),
    ("North Leslie", "Sunny"),
    ("Simpsonville", "Windy"),
    ("Ramirezfurt", "Sunny"),
    ("Vincentstad", "Sunny"),
    ("East Earltown", "Foggy"),
    ("Jamesstad", "Snowy"),
    ("Wilkersonfurt", "Sunny"),
    ("Stacyshire", "Rainy"),
    ("Patriciaton", "Sunny"),
    ("South Marissatown", "Cloudy"),
    ("Garciachester", "Snowy"),
    ("Michaelhaven", "Foggy"),
    ("South Jaredton", "Windy"),
    ("South Ernest", "Foggy"),
    ("Lake Wesleyside", "Foggy"),
    ("Raymondberg", "Windy"),
    ("East Karen", "Windy"),
    ("Lake Elizabeth", "Cloudy"),
    ("Port Thomasview", "Snowy"),
    ("North Suzanne", "Windy"),
    ("Seanshire", "Snowy"),
    ("South Regina", "Cloudy"),
    ("East Connor", "Cloudy"),
    ("New Karenside", "Rainy"),
    ("Lake Janet", "Windy"),
    ("Louisport", "Snowy"),
    ("West Teresashire", "Rainy"),
    ("Dunlapside", "Foggy"),
    ("Jasonchester", "Cloudy"),
    ("Baileyberg", "Foggy"),
    ("Lauraland", "Cloudy"),
    ("Jamesville", "Sunny"),
    ("East Kaylaburgh", "Cloudy"),
    ("Baileyberg", "Foggy"),
    ("Lake Garyport", "Rainy"),
    ("Tonymouth", "Cloudy"),
    ("West Kyle", "Windy"),
    ("Monicamouth", "Snowy"),
    ("Jasonberg", "Foggy"),
    ("Feliciaton", "Foggy"),
    ("West Monique", "Sunny"),
    ("Port Judy", "Foggy"),
    ("Faithbury", "Rainy"),
    ("Amberberg", "Foggy"),
    ("North Carrietown", "Foggy"),
    ("Nancyville", "Snowy"),
    ("Greenville", "Snowy"),
    ("Kramerburgh", "Windy"),
    ("New Rhondatown", "Sunny"),
    ("Taylorfort", "Sunny"),
    ("North Frank", "Cloudy"),
    ("Victoriaborough", "Cloudy"),
    ("Lake Ryan", "Windy"),
    ("East Jessica", "Foggy"),
    ("Kaylaside", "Rainy"),
    ("Port George", "Sunny"),
    ("New Austin", "Windy"),
    ("Sanchezstad", "Windy"),
    ("Port Jodyside", "Rainy"),
    ("Lake Nathanhaven", "Rainy"),
    ("Jamesstad", "Windy"),
    ("New Michaelberg", "Sunny"),
    ("South Julie", "Windy"),
    ("New Meaganside", "Foggy"),
    ("West Robertmouth", "Rainy"),
    ("North Lindaville", "Cloudy"),
    ("East Crystalfort", "Cloudy"),
    ("West Ronaldfort", "Rainy"),
    ("East Christopherton", "Cloudy"),
    ("Port Bethany", "Foggy"),
    ("Garciatown", "Rainy"),
    ("North Jeremy", "Foggy"),
    ("Lake Tiffany", "Cloudy"),
    ("Barnettstad", "Rainy"),
    ("Alexisview", "Snowy"),
    ("Hernandezstad", "Cloudy"),
    ("New Whitney", "Foggy"),
    ("Wilsonville", "Foggy"),
    ("Swansonland", "Foggy"),
    ("Blackwellberg", "Windy"),
    ("West Jessicatown", "Snowy"),
    ("Moorechester", "Windy"),
    ("Cannonburgh", "Rainy"),
    ("Garciaside", "Sunny"),
    ("North Zacharymouth", "Rainy"),
    ("East Julia", "Foggy"),
    ("East Scott", "Cloudy"),
    ("West Carolyn", "Rainy"),
    ("West Brett", "Snowy"),
    ("East Matthew", "Sunny"),
    ("North Carrie", "Snowy"),
    ("Elizabethburgh", "Foggy"),
    ("North Edwardchester", "Snowy"),
    ("Colestad", "Windy"),
    ("West Jonathanville", "Rainy"),
    ("Kempchester", "Windy"),
    ("Katieport", "Sunny"),
    ("Galvanfurt", "Cloudy"),
    ("West Jennifershire", "Snowy"),
]


def generate_status_data():
    sql_statements = []
    for i in range(1, 201):
        arrival_location, weather_condition = STATUS[i - 1]
        departure_time = f"{random.randint(2000,2025)}-{random.randint(1,12):0>2}-{random.randint(1,28):0>2} {random.randint(0,23):0>2}:{random.randint(0,59):0>2}:{random.randint(0,59):0>2}"
        current_time = f"{random.randint(2000,2025)}-{random.randint(1,12):0>2}-{random.randint(1,28):0>2} {random.randint(0,23):0>2}:{random.randint(0,59):0>2}:{random.randint(0,59):0>2}"
        fk_flight_id = i

        sql_statements.append(
            f"('{arrival_location}','{weather_condition}','{departure_time}','{current_time}',{fk_flight_id})"
        )

    return (
        "INSERT INTO status (ArrivalLocation , WeatherCondition , DepartureTime , CurrentTime , FK_FlightID)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


def generate_services_data():
    sql_statements = []
    pairs = set()
    while len(pairs) < 200:
        airline_id = random.randint(1, 200)
        airport_id = random.randint(1, 200)
        pair = (airline_id, airport_id)
        if pair not in pairs:
            pairs.add(pair)
            sql_statements.append(f"({airline_id},{airport_id})")

    return (
        "INSERT INTO services (AirlineID , AirportID)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n"
    )


def generate_ticket_data():
    sql_statements = []
    for i in range(1, 201):
        ticket_price = random.randint(50, 1000)
        ticket_number = f"T{i:0>3}"
        fk_seat_number = TUPLES[0][i-1][0]
        fk_passenger_id = f"P{i:0>3}"

        sql_statements.append(
            f"({ticket_price},'{ticket_number}',{fk_seat_number},'{fk_passenger_id}')"
        )

    return (
        "INSERT INTO ticket (TicketPrice , TicketNumber , FK_SeatNumber , FK_PassengerID)\nVALUES\n"
        + ",\n".join(sql_statements)
        + ";\n\n\n"
    )


with open("mock_data.sql", "w", encoding="utf-8") as f:
    f.write(generate_airport_data())
    f.write(generate_airline_data())
    f.write(generate_services_data())
    f.write(generate_flight_data())
    f.write(generate_passenger_data())
    f.write(generate_luggage_data())
    f.write(generate_status_data())
    f.write(generate_account_data())

    f.write(generate_business_data())
    f.write(generate_first_class_data())
    f.write(generate_other_flight_class_data())

    f.write(generate_ticket_data())

    f.write(generate_cargo_airliner_data())
    f.write(generate_passenger_airliner_data())
    f.write(generate_private_jet_data())


print("SQL script generated and saved to 'mock_data.sql'")
