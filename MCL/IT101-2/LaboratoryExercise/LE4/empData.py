#Ignore this file
empList="""201911007,James,Butt,Accounting,365;
201203008,Josephine,Darakjy,Marketing,365;
199710014,Art,Venere,Human Resources,750;
201612010,Lenna,Paprocki,Marketing,565;
201710017,Donette,Foller,Admin,450;
201701013,Simona,Morasca,Finance,450;
201011003,Mitsue,Tollner,Marketing,750;
201409015,Leota,Dilliard,Finance,365;
199512017,Sage,Wieser,MIS,750;
199708003,Kris,Marrier,Admin,750"""

empMR ="""201911007,1,28;
201203008,1,28;
199710014,1,28;
201612010,1,28;
201710017,1,28;
201701013,1,28;
201011003,1,28;
201409015,1,28;
199512017,1,28;
199708003,1,28;
201911007,2,28;
201203008,2,28;
199710014,2,28;
201612010,2,28;
201710017,2,28;
201701013,2,28;
201011003,2,28;
201409015,2,28;
199512017,2,28;
199708003,2,28;
201911007,3,10;
201203008,3,27;
199710014,3,28;
201612010,3,19;
201710017,3,11;
201701013,3,21;
201011003,3,22;
201409015,3,28;
199512017,3,28;
199708003,3,20;
201911007,4,20;
201203008,4,28;
199710014,4,26;
201612010,4,18;
201710017,4,12;
201701013,4,20;
201011003,4,24;
201409015,4,26;
199512017,4,28;
199708003,4,21"""


def createFiles():
    f = open("empList.txt","w")
    f.write(empList)
    f.close

    f = open("empMR.txt","w")
    f.write(empMR)
    f.close
