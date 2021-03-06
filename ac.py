import sqlite3
from pprint import pprint


# https://www.w3resource.com/sqlite/sqlite-strftime.php


# '2007-01-01 10:00:00'
# i.e. yyyy-MM-dd HH: mm: ss

# conn = sqlite3.connect('fish.db')
#
# c = conn.cursor()

# c.execute("""CREATE TABLE fishes(id INTEGER PRIMARY KEY, name TEXT, price INTEGER, location TEXT , size INTEGER, start DATETIME, end DATETIME) """)


# c.execute("""INSERT INTO fishes VALUES
#     (1001, 'Bitterling', 900, 'River', 1,'2020-01-01 00:00:00', '2050-03-31 24:00:00'),
#     (1002, 'Pale Chub', 200, 'River', 1,'2020-01-01 09:00:00', '2050-12-31 16:00:00'),
#     (1003, 'Crucian Carp', 160, 'River', 2,'2020-01-01 00:00:00', '2050-12-31 24:00:00'),
#     (1004, 'Dace', 240, 'River', 3,'2020-01-01 16:00:00', '2050-12-31 09:00:00'),
#     (1005, 'Carp', 300, 'Pond', 4,'2020-01-01 00:00:00', '2050-12-31 24:00:00'),
#     (1006, 'Koi', 4000, 'Pond', 4,'2020-01-01 16:00:00', '2050-12-31 09:00:00'),
#     (1007, 'Goldfish', 1300, 'Pond', 1,'2020-01-01 00:00:00', '2050-12-31 24:00:00'),
#     (1008, 'Pop-eyed goldfish', 1300, 'Pond', 1,'2020-01-01 09:00:00', '2050-12-31 16:00:00'),
#     (1009, 'Ranchu goldfish', 4500, 'Pond', 2,'2020-01-01 09:00:00', '2050-12-31 16:00:00'),
#     (1010, 'Killifish', 300, 'Pond', 1,'2020-04-01 00:00:00', '2050-08-31 24:00:00'),
#     (1011, 'Crawfish', 200, 'Pond', 2,'2020-04-01 00:00:00', '2050-09-31 24:00:00'),
#     (1012, 'Soft-shelled turtle', 3750, 'River', 4,'2020-08-01 16:00:00', '2050-09-31 09:00:00'),
#     (1013, 'Snapping Turtle', 5000, 'River', 5,'2020-04-01 21:00:00', '2050-10-31 04:00:00'),
#     (1014, 'Tadpole', 100, 'Pond', 1,'2020-03-01 00:00:00', '2050-07-31 24:00:00'),
#     (1015, 'Frog', 120, 'Pond', 2,'2020-05-01 00:00:00', '2050-08-31 24:00:00'),
#     (1016, 'Freshwater goby', 400, 'River', 2,'2020-01-01 16:00:00', '2050-12-31 09:00:00'),
#     (1017, 'Loach', 400, 'River', 2,'2020-03-01 00:00:00', '2050-05-31 24:00:00'),
#     (1018, 'Catfish', 800, 'Pond', 4,'2020-05-01 16:00:00', '2050-10-31 09:00:00'),
#     (1019, 'Giant snakehead', 5500, 'Pond', 5,'2020-06-01 09:00:00', '2050-08-31 16:00:00'),
#     (1020, 'Bluegill', 180, 'River', 2,'2020-01-01 09:00:00', '2050-12-31 16:00:00'),
#     (1021, 'Yellow perch', 300, 'River', 3,'2020-01-01 00:00:00', '2050-03-31 24:00:00'),
#     (1022, 'Black bass', 400, 'River', 4,'2020-01-01 00:00:00', '2050-12-31 24:00:00'),
#     (1023, 'Tilapia', 800, 'River', 3,'2020-06-01 00:00:00', '2050-10-31 24:00:00'),
#     (1024, 'Pike', 1800, 'River', 5,'2020-09-01 00:00:00', '2050-12-31 24:00:00'),
#     (1025, 'Pond smelt', 500, 'River', 2,'2020-12-01 00:00:00', '2050-12-31 24:00:00'),
#     (1026, 'Sweetfish', 900, 'River', 3,'2020-07-01 00:00:00', '2050-09-31 24:00:00'),
#     (1027, 'Cherry salmon', 800, 'River Cliftop', 3,'2020-03-01 16:00:00', '2050-06-31 09:00:00'),
#     (1028, 'Cherry salmon', 800, 'River Cliftop', 3,'2020-09-01 16:00:00', '2050-11-31 09:00:00'),
#     (1029, 'Char', 800, 'River Cliftop', 3,'2020-03-01 16:00:00', '2050-06-31 09:00:00'),
#     (1030, 'Char', 800, 'River Cliftop', 3,'2020-09-01 16:00:00', '2050-11-31 09:00:00'),
#     (1031, 'Golden trout', 15000, 'River Cliftop',3, '2020-03-01 16:00:00', '2050-05-31 09:00:00'),
#     (1032, 'Golden trout', 15000, 'River Cliftop',3, '2020-09-01 16:00:00', '2050-11-31 09:00:00'),
#     (1033, 'Stringfish', 15000, 'River Clifftop', 5,'2020-12-01 16:00:00', '2050-12-31 09:00:00'),
#     (1034, 'Salmon', 700, 'River Mouth', 4,'2020-09-01 00:00:00', '2050-09-31 24:00:00'),
#     (1035, 'King salmon', 1800	, 'River Mouth', 6,'2020-09-01 00:00:00', '2050-09-31 24:00:00'),
#     (1036, 'Mitten crab', 2000, 'River', 2,'2020-09-01 16:00:00', '2050-11-31 09:00:00'),
#     (1037, 'Guppy', 1300, 'River', 1,'2020-04-01 09:00:00', '2050-11-31 16:00:00'),
#     (1038, 'Nibble fish', 1500	, 'River', 1,'2020-05-01 09:00:00', '2050-09-31 16:00:00'),
#     (1039, 'Angelfish', 3000, 'River', 2,'2020-05-01 16:00:00', '2050-10-31 09:00:00'),
#     (1040, 'Betta', 2500, 'River', 2,'2020-05-01 09:00:00', '2050-10-31 16:00:00'),
#     (1041, 'Neon tetra', 500, 'River', 1,'2020-04-01 09:00:00', '2050-11-31 16:00:00'),
#     (1042, 'Rainbowfish', 800, 'River', 1,'2020-05-01 09:00:00', '2050-10-31 16:00:00'),
#     (1043, 'Piranha', 2500, 'River', 2,'2020-06-01 09:00:00', '2050-09-31 16:00:00'),
#     (1044, 'Piranha', 2500, 'River', 2,'2020-06-01 21:00:00', '2050-09-31 04:00:00'),
#     (1045, 'Arowana', 10000, 'River', 4,'2020-06-01 16:00:00', '2050-09-31 09:00:00'),
#     (1046, 'Dorado', 15000, 'River', 5,'2020-06-01 04:00:00', '2050-09-31 21:00:00'),
#     (1047, 'Gar', 6000, 'Pond', 6,'2020-06-01 16:00:00', '2050-09-31 09:00:00'),
#     (1048, 'Arapaima', 10000, 'River', 6,'2020-06-01 16:00:00', '2050-09-31 09:00:00'),
#     (1049, 'Saddled bichir', 4000, 'River', 4,'2020-06-01 21:00:00', '2050-09-31 04:00:00'),
#     (1050, 'Sturgeon', 10000, 'River Mouth', 6,'2020-09-01 00:00:00', '2050-12-31 24:00:00'),
#     (1051, 'Sea butterfly', 1000, 'Sea', 1	,'2020-12-01 00:00:00', '2050-12-31 24:00:00'),
#     (1052, 'Sea horse', 1100, 'Sea',	1,'2020-04-01 00:00:00', '2050-11-31 24:00:00'),
#     (1053, 'Clown fish', 650, 'Sea', 1,'2020-04-01 00:00:00', '2050-09-31 24:00:00'),
#     (1054, 'Surgeonfish', 1000	, 'Sea', 2,'2020-04-01 00:00:00', '2050-09-31 24:00:00'),
#     (1055, 'Butterfly fish', 1000,	'Sea', 2,'2020-04-01 00:00:00', '2050-09-31 24:00:00'),
#     (1056, 'Napoleonfish', 10000, 'Sea', 6,'2020-07-01 04:00:00', '2050-08-31 21:00:00'),
#     (1057, 'Zebra turkeyfish', 500	, 'Sea', 3,'2020-04-01 00:00:00', '2050-11-31 24:00:00'),
#     (1058, 'Blowfish', 5000, 'Sea', 3,'2020-11-01 21:00:00', '2050-12-31 04:00:00'),
#     (1059, 'Puffer fish', 250,	'Sea', 3,'2020-07-01 00:00:00', '2050-09-31 24:00:00'),
#     (1060, 'Anchovy', 200, 'Sea', 2,'2020-01-01 04:00:00', '2050-12-31 21:00:00'),
#     (1061, 'Horse mackerel', 150,	'Sea', 2,'2020-01-01 00:00:00', '2050-12-31 24:00:00'),
#     (1062, 'Barred knifejaw', 5000	, 'Sea', 3,'2020-03-01 00:00:00', '2050-11-31 24:00:00'),
#     (1063, 'Sea bass', 400, 'Sea'	, 5	,'2020-01-01 00:00:00', '2050-12-31 24:00:00'),
#     (1064, 'Red snapper', 3000, 'Sea', 4,'2020-01-01 00:00:00', '2050-12-31 24:00:00'),
#     (1065, 'Dab', 300,	'Sea', 3,'2020-10-01 00:00:00', '2050-12-31 24:00:00'),
#     (1066, 'Olive flounder', 800, 'Sea', 5,'2020-01-01 00:00:00', '2050-12-31 24:00:00'),
#     (1067, 'Squid', 500, 'Sea', 3,'2020-12-01 00:00:00', '2050-12-31 24:00:00'),
#     (1068, 'Moray eel', 2000, 'Sea', 0,'2020-08-01 00:00:00', '2050-10-31 24:00:00'),
#     (1069, 'Ribbon eel', 600, 'Sea', 0,'2020-06-01 00:00:00', '2050-10-31 24:00:00'),
#     (1070, 'Tuna', 7000, 'Pier',	6,'2020-11-01 00:00:00', '2050-12-31 24:00:00'),
#     (1071, 'Blue marlin', 10000, 'Pier', 6,'2020-01-01 00:00:00', '2050-04-31 24:00:00'),
#     (1072, 'Giant trevally', 4500, 'Pier', 5,'2020-05-01 00:00:00', '2050-10-31 24:00:00'),
#     (1073, 'Mahi-mahi', 6000, 'Pier', 5,'2020-05-01 00:00:00', '2050-10-31 24:00:00'),
#     (1074, 'Ocean sunfish', 4000, 'Sea', 6,'2020-07-01 04:00:00', '2050-09-31 21:00:00'),
#     (1075, 'Ray', 3000	, 'Sea', 5,'2020-08-01 04:00:00', '2050-11-31 21:00:00'),
#     (1076, 'Saw shark', 12000, 'Sea', 6,'2020-06-01 16:00:00', '2050-09-31 09:00:00'),
#     (1077, 'Hammerhead shark', 8000, 'Sea', 6,'2020-06-01 16:00:00', '2050-09-31 09:00:00'),
#     (1078, 'Great white shark', 15000, 'Sea', 6,'2020-06-01 16:00:00', '2050-09-31 09:00:00'),
#     (1079, 'Whale shark', 13000, 'Sea', 6,'2020-06-01 00:00:00', '2050-09-31 24:00:00'),
#     (1080, 'Suckerfish', 1500,	'Sea', 4,'2020-06-01 00:00:00', '2050-09-31 24:00:00'),
#     (1081, 'Football fish', 2500, 'Sea', 4,'2020-11-01 16:00:00', '2050-12-31 09:00:00'),
#     (1082, 'Oarfish', 9000, 'Sea', 6,'2020-01-01 00:00:00', '2050-05-31 24:00:00'),
#     (1083, 'Barreleye', 15000,	'Sea', 2,'2020-01-01 21:00:00', '2050-12-31 04:00:00'),
#     (1084, 'Coelacanth', 15000	, 'Sea', 6,'2020-01-01 00:00:00', '2050-12-31 24:00:00'),
#     (1085, 'Blue marlin', 10000, 'Pier', 6,'2020-07-01 00:00:00', '2050-09-31 24:00:00'),
#     (1086, 'Bitterling', 900, 'River', 1,'2020-11-01 00:00:00', '2050-12-31 24:00:00'),
#     (1087, 'Yellow perch', 300, 'River', 3,'2020-10-01 00:00:00', '2050-12-31 24:00:00'),
#     (1088, 'Pond smelt', 500, 'River', 2,'2020-01-01 00:00:00', '2050-02-31 24:00:00'),
#     (1089, 'Stringfish', 15000, 'River Clifftop', 5,'2020-01-01 16:00:00', '2050-03-31 09:00:00'),
#     (1090, 'Sturgeon', 10000, 'River Mouth', 6,'2020-01-01 00:00:00', '2050-03-31 24:00:00'),
#     (1091, 'Sea butterfly', 1000, 'Sea', 1	,'2020-01-01 00:00:00', '2050-03-31 24:00:00'),
#     (1092, 'Blowfish', 5000, 'Sea', 3,'2020-01-01 21:00:00', '2050-02-31 04:00:00'),
#     (1093, 'Dab', 300,	'Sea', 3,'2020-01-01 00:00:00', '2050-04-31 24:00:00'),
#     (1094, 'Squid', 500, 'Sea', 3,'2020-01-01 00:00:00', '2050-08-31 24:00:00'),
#     (1095, 'Tuna', 7000, 'Pier',	6,'2020-01-01 00:00:00', '2050-04-31 24:00:00'),
#     (1096, 'Blue marlin', 10000, 'Pier', 6,'2020-11-01 00:00:00', '2050-12-31 24:00:00'),
#     (1097, 'Football fish', 2500, 'Sea', 4,'2020-01-01 16:00:00', '2050-03-31 09:00:00'),
#     (1098, 'Oarfish', 9000, 'Sea', 6,'2020-12-01 00:00:00', '2050-12-31 24:00:00')""")


# c.execute(""" UPDATE fishes SET start = '2020-11-01 00:00:00' WHERE id = 1096""")

# conn.commit()


# # print all
# c.execute("""SELECT * FROM fishes""")
# print(c.fetchall())
# #




# # updated to fix time issue (would show fish that exceded hour)
# # # example - would show anchovy at current time 21:38 when fish set to stop spawning at 21
# SELECT id, name, price, location, start, end, strftime('%H %M', 'now', 'localtime')
# FROM 'fishes'
# WHERE strftime('%m', 'now', 'localtime') BETWEEN strftime('%m', start) AND  strftime('%m', end)
# AND strftime('%H %M', 'now', 'localtime') BETWEEN strftime('%H %M', start) AND strftime('%H %M', end)
# # #

conn = sqlite3.connect('fish.db')

c = conn.cursor()


def printFish():
    # conn = sqlite3.connect('fish.db')

    # c = conn.cursor()

    c.execute(""" SELECT id, name, price, location, start, end, strftime('%H %M', 'now', 'localtime')
    FROM 'fishes'
    WHERE strftime('%m', 'now', 'localtime') BETWEEN strftime('%m', start) AND  strftime('%m', end)
    AND strftime('%H %M', 'now', 'localtime') BETWEEN strftime('%H %M', start) AND strftime('%H %M', end) """)


    return c.fetchall()

a = printFish()

print(a)

conn.commit()
conn.close()


#
# def printstuff():
#     a = (""" #     (1082, 'Oarfish', 9000, 'Sea', 6,'2020-01-01 00:00:00', '2050-05-31 24:00:00'),
# #     (1083, 'Barreleye', 15000,	'Sea', 2,'2020-01-01 21:00:00', '2050-12-31 04:00:00'),
# #     (1084, 'Coelacanth', 15000	, 'Sea', 6,'2020-01-01 00:00:00', '2050-12-31 24:00:00'),
# #     (1085, 'Blue marlin', 10000, 'Pier', 6,'2020-07-01 00:00:00', '2050-09-31 24:00:00'),
# #     (1086, 'Bitterling', 900, 'River', 1,'2020-11-01 00:00:00', '2050-12-31 24:00:00'),
# #     (1087, 'Yellow perch', 300, 'River', 3,'2020-10-01 00:00:00', '2050-12-31 24:00:00'),
# #     (1088, 'Pond smelt', 500, 'River', 2,'2020-01-01 00:00:00', '2050-02-31 24:00:00'),
# #     (1089, 'Stringfish', 15000, 'River Clifftop', 5,'2020-01-01 16:00:00', '2050-03-31 09:00:00'),
# #     (1090, 'Sturgeon', 10000, 'River Mouth', 6,'2020-01-01 00:00:00', '2050-03-31 24:00:00'),
# #     (1091, 'Sea butterfly', 1000, 'Sea', 1	,'2020-01-01 00:00:00', '2050-03-31 24:00:00'),
# #     (1092, 'Blowfish', 5000, 'Sea', 3,'2020-01-01 21:00:00', '2050-02-31 04:00:00'),
# #     (1093, 'Dab', 300,	'Sea', 3,'2020-01-01 00:00:00', '2050-04-31 24:00:00'),
# #     (1094, 'Squid', 500, 'Sea', 3,'2020-01-01 00:00:00', '2050-08-31 24:00:00'),
# #     (1095, 'Tuna', 7000, 'Pier',	6,'2020-01-01 00:00:00', '2050-04-31 24:00:00'),
# #     (1096, 'Blue marlin', 10000, 'Pier', 6,'2020-11-01 00:00:00', '2050-12-31 24:00:00'),
# #     (1097, 'Football fish', 2500, 'Sea', 4,'2020-01-01 16:00:00', '2050-03-31 09:00:00'),
# #     (1098, 'Oarfish', 9000, 'Sea', 6,'2020-12-01 00:00:00', '2050-12-31 24:00:00')""")
#     return a
#
# henlo = printstuff()
# print (henlo)