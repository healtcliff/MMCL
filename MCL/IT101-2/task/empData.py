from datetime import datetime

empRecords="""201911007,James,Butt,Accounting,365,30,2/15/1956;
201203008,Josephine,Darakjy,Marketing,365,15,7/15/1988;
199710014,Art,Venere,Human Resources,750,30,3/10/1988;
201612010,Lenna,Paprocki,Marketing,565,16,9/11/1991;
201710017,Donette,Foller,Admin,450,28,6/1/1955;
201701013,Simona,Morasca,Finance,450,18,1/26/1995;
201011003,Mitsue,Tollner,Marketing,750,16,8/27/1970;
201409015,Leota,Dilliard,Finance,365,27,7/3/1981;
199512017,Sage,Wieser,MIS,750,15,5/11/1959;
199708003,Kris,Marrier,Admin,750,16,12/19/1983;
200705019,Minna,Amigon,Accounting,1050,28,1/22/1985;
199805018,Abel,Maclead,Accounting,565,18,5/13/2000;
201007003,Kiley,Caldarera,MIS,450,23,2/19/1992;
200606016,Graciela,Ruta,Purchasing,565,18,6/24/1985;
200609015,Cammy,Albares,Finance,750,19,4/27/1995;
200204019,Mattie,Poquette,Finance,565,25,9/2/1987;
199506019,Meaghan,Garufi,Human Resources,750,18,9/12/1998;
201811019,Gladys,Rim,Accounting,565,15,1/2/1985;
199503015,Yuki,Whobrey,MIS,450,15,2/9/1989;
200405012,Fletcher,Flosi,Finance,750,27,12/27/1997;
201403012,Bette,Nicka,Accounting,450,30,1/6/1987;
200109018,Veronika,Inouye,MIS,565,17,4/25/1997;
202002018,Willard,Kolmetz,Purchasing,450,22,11/23/1981;
199608007,Maryann,Royster,Marketing,750,15,10/2/1984;
201302012,Alisha,Slusarski,Admin,565,28,10/13/1960;
200006017,Allene,Iturbide,MIS,750,21,4/19/1998;
200606018,Chanel,Caudy,Admin,750,27,6/21/1960;
200210009,Ezekiel,Chui,Human Resources,450,17,3/15/1963;
201010011,Willow,Kusko,Accounting,750,16,1/21/1984;
201911014,Bernardo,Figeroa,Purchasing,800,20,1/17/1981;
200908015,Ammie,Corrio,Marketing,750,22,3/21/1979;
200004001,Francine,Vocelka,Finance,1050,26,2/10/1969;
201701016,Ernie,Stenseth,MIS,800,26,4/8/1998;
201305005,Albina,Glick,MIS,1050,27,12/15/1988;
201506006,Alishia,Sergi,Marketing,450,29,7/26/2001;
201006011,Solange,Shinko,MIS,800,27,11/8/1984;
202004014,Jose,Stockham,Finance,1050,30,2/19/2000;
201711018,Rozella,Ostrosky,Admin,800,21,5/17/2001;
201906004,Valentine,Gillian,Admin,565,25,8/6/1962;
200512015,Kati,Rulapaugh,Finance,1050,25,7/9/2001;
200002015,Youlanda,Schemmer,Admin,365,24,2/14/1962;
200511001,Dyan,Oldroyd,MIS,365,22,11/23/2000;
201001001,Roxane,Campain,Marketing,450,19,6/25/1978;
201504020,Lavera,Perin,Finance,565,21,5/7/1965;
201304010,Erick,Ferencz,Accounting,365,16,12/21/1967;
200307011,Fatima,Saylors,Marketing,450,22,1/3/1956;
200009012,Jina,Briddick,Marketing,365,18,12/19/1985;
199703001,Kanisha,Waycott,Marketing,750,16,5/5/1981;
200409010,Emerson,Bowley,Human Resources,800,23,1/18/1963;
200903010,Blair,Malet,Human Resources,565,23,1/23/1969;
200607008,Brock,Bolognia,Accounting,1050,22,2/16/1982;
199712007,Lorrie,Nestle,Finance,565,20,10/21/1984;
199709005,Sabra,Uyetake,Accounting,800,19,3/2/1995;
199710013,Marjory,Mastella,Marketing,365,27,1/25/1983;
201801012,Karl,Klonowski,Accounting,365,22,5/16/2002;
200802011,Tonette,Wenner,Admin,800,15,6/15/1957;
200610007,Amber,Monarrez,Purchasing,565,21,11/12/1979;
201408004,Shenika,Seewald,MIS,800,23,10/28/1972;
199804005,Delmy,Ahle,MIS,450,24,8/17/1960;
200503006,Deeanna,Juhas,Human Resources,800,18,9/23/1959;
200211020,Blondell,Pugh,Admin,750,27,9/17/1986;
201304019,Jamal,Vanausdal,Finance,565,15,11/3/1983;
201202003,Cecily,Hollack,MIS,800,23,5/6/1977;
199509006,Carmelina,Lindall,Accounting,365,16,2/28/1999;
201711010,Maurine,Yglesias,MIS,365,28,9/18/1967;
201708012,Tawna,Buvens,MIS,450,17,7/28/1970;
200808004,Penney,Weight,Marketing,565,25,6/7/1979;
200508019,Elly,Morocco,Marketing,1050,28,2/3/1973;
200107012,Ilene,Eroman,Human Resources,365,19,12/7/1958;
201404015,Vallie,Mondella,Accounting,450,19,7/21/1964;
201312008,Kallie,Blackwood,Marketing,800,28,2/9/1999;
200008001,Johnetta,Abdallah,Admin,1050,15,4/20/1996;
199608011,Bobbye,Rhym,MIS,1050,21,9/13/2001;
200410002,Micaela,Rhymes,Admin,365,30,10/24/1966;
200310002,Tamar,Hoogland,Finance,565,26,4/19/1959;
201808002,Moon,Parlato,Accounting,750,18,2/5/1978;
201904001,Laurel,Reitler,Admin,450,30,12/10/1956;
200804019,Delisa,Crupi,Human Resources,800,21,8/21/1961;
200604005,Viva,Toelkes,MIS,750,23,9/10/1985;
200202004,Elza,Lipke,Marketing,1050,29,2/12/1982;
201212011,Devorah,Chickering,Human Resources,565,25,8/27/1962;
201404006,Timothy,Mulqueen,Marketing,450,19,8/8/1960;
199607002,Arlette,Honeywell,Accounting,365,25,12/28/1991;
201709011,Dominque,Dickerson,Accounting,1050,20,12/27/1992;
201810008,Lettie,Isenhower,Human Resources,800,18,7/4/1997;
199505019,Myra,Munns,Human Resources,750,18,7/7/1974;
201301006,Stephaine,Barfield,Marketing,450,21,9/10/1956;
201001008,Lai,Gato,Admin,1050,20,1/23/1975;
201405007,Stephen,Emigh,Finance,800,30,3/14/1969;
202003014,Tyra,Shields,Marketing,565,30,12/16/1987;
200909011,Tammara,Wardrip,Accounting,365,25,3/10/1985;
199807020,Cory,Gibes,Admin,565,17,7/10/1994;
200705015,Danica,Bruschke,Purchasing,750,27,8/21/1999;
200311004,Wilda,Giguere,Admin,1050,16,10/27/1956;
201805014,Elvera,Benimadho,MIS,800,19,12/14/1961;
200810007,Carma,Vanheusen,Finance,1050,23,12/22/1985;
201910017,Malinda,Hochard,Marketing,750,21,9/3/1969;
201909008,Natalie,Fern,Finance,750,27,6/6/1991;
201401005,Lisha,Centini,Finance,750,26,1/16/1978;
201703003,Arlene,Klusman,Purchasing,365,29,1/4/1961;
200111005,Alease,Buemi,Purchasing,800,26,7/7/1980;
201904005,Louisa,Cronauer,Purchasing,750,22,10/24/1963;
200609005,Angella,Cetta,Finance,365,28,2/26/1980;
200806015,Cyndy,Goldammer,Marketing,365,15,4/5/2000;
201012006,Rosio,Cork,Marketing,1050,20,7/15/1970;
201401019,Celeste,Korando,Admin,365,30,7/27/1961;
200005012,Twana,Felger,Finance,565,26,5/15/1994;
200212006,Estrella,Samu,Marketing,565,20,12/17/1998;
199905012,Donte,Kines,Finance,800,15,12/16/1983;
200304020,Tiffiny,Steffensmeier,MIS,450,24,3/9/1978;
199905016,Edna,Miceli,Admin,800,27,2/3/1988;
201805003,Sue,Kownacki,MIS,450,15,7/7/1989;
199504007,Jesusa,Shin,Marketing,365,22,9/8/1958;
201312018,Rolland,Francescon,Marketing,800,20,1/4/1992;
202001016,Pamella,Schmierer,Finance,1050,23,6/6/1955;
200704014,Glory,Kulzer,Purchasing,565,23,6/21/1976;
200509005,Shawna,Palaspas,Admin,1050,27,3/24/1992;
200203009,Brandon,Callaro,Marketing,1050,20,2/2/1987;
200601003,Scarlet,Cartan,Marketing,365,27,12/1/1985;
201704010,Oretha,Menter,Admin,750,16,12/26/1968;
201902001,Ty,Smith,Accounting,450,18,7/17/1961;
200801015,Xuan,Rochin,Accounting,800,29,1/1/1983;
201906013,Lindsey,Dilello,Accounting,565,24,12/23/1958;
200207015,Devora,Perez,Marketing,365,18,7/16/1960;
201907008,Herman,Demesa,Admin,565,21,8/25/1966;
200001007,Rory,Papasergi,MIS,1050,17,10/19/1999;
199610005,Talia,Riopelle,Accounting,800,30,3/15/1958;
200111020,Van,Shire,Accounting,565,18,2/22/1962;
200708002,Lucina,Lary,Finance,750,24,5/7/1973;
202005017,Bok,Isaacs,Finance,365,16,5/27/1956;
201005017,Rolande,Spickerman,Admin,365,27,10/19/1982;
199707013,Howard,Paulas,MIS,750,30,4/9/1970;
199607006,Kimbery,Madarang,Admin,450,21,8/16/1973;
201912011,Thurman,Manno,Human Resources,450,26,3/20/2001;
199806013,Becky,Mirafuentes,Finance,1050,19,10/24/1982;
200506017,Beatriz,Corrington,Purchasing,450,15,11/1/1963;
201407017,Marti,Maybury,Human Resources,800,30,6/2/1986;
200202008,Nieves,Gotter,Admin,450,23,10/20/2000;
201702011,Leatha,Hagele,Finance,565,20,1/6/1990;
199804016,Valentin,Klimek,Purchasing,450,20,10/15/1994;
201106004,Melissa,Wiklund,Human Resources,365,20,9/8/2000;
201704002,Sheridan,Zane,Marketing,450,21,3/3/1992;
200406016,Bulah,Padilla,Accounting,750,23,10/9/1965;
200406017,Audra,Kohnert,Finance,450,17,6/20/1986;
199504018,Daren,Weirather,Accounting,365,30,3/2/1962;
201802013,Fernanda,Jillson,Finance,750,19,7/18/1982;
200112015,Gearldine,Gellinger,Marketing,565,26,7/6/1958;
199712001,Chau,Kitzman,MIS,750,23,10/7/1994;
200109017,Theola,Frey,Admin,1050,19,9/27/1984;
200604013,Cheryl,Haroldson,Purchasing,450,28,3/23/1989;
200211003,Laticia,Merced,Finance,750,28,4/19/1986;
201803006,Carissa,Batman,Marketing,450,29,11/7/1965;
201311008,Lezlie,Craghead,Purchasing,750,22,12/27/1990;
201409017,Ozell,Shealy,MIS,1050,25,10/19/1990;
201005002,Arminda,Parvis,Human Resources,450,30,2/14/1981;
200910014,Reita,Leto,MIS,565,24,12/15/1989;
201805020,Yolando,Luczki,Finance,450,20,8/27/1961;
200711012,Lizette,Stem,Human Resources,1050,25,7/24/1955;
201603014,Gregoria,Pawlowicz,Finance,450,28,4/6/1982;
199910016,Carin,Deleo,MIS,800,26,9/15/1971;
201107005,Chantell,Maynerich,Marketing,365,18,7/12/1978;
201703006,Dierdre,Yum,Finance,565,23,10/12/1985;
201005012,Larae,Gudroe,Purchasing,450,30,10/20/1979;
200102003,Latrice,Tolfree,Marketing,800,29,6/5/1981;
201003006,Kerry,Theodorov,Accounting,750,22,10/22/1967;
199906006,Dorthy,Hidvegi,Human Resources,565,29,10/22/1979;
200802015,Fannie,Lungren,Finance,565,24,1/4/1988;
201209007,Evangelina,Radde,Accounting,1050,21,2/17/1963;
199610007,Novella,Degroot,Admin,800,21,2/7/1988;
200907014,Clay,Hoa,Finance,450,15,6/19/1970;
201805008,Jennifer,Fallick,Admin,450,21,2/17/1984;
200309011,Irma,Wolfgramm,Admin,750,15,2/9/1986;
200209018,Eun,Coody,Admin,450,28,4/2/1978;
200109019,Sylvia,Cousey,Marketing,1050,20,7/2/1992;
201212001,Nana,Wrinkles,Admin,800,28,8/9/1965;
201902013,Layla,Springe,Purchasing,450,30,11/22/1997;
201211001,Joesph,Degonia,Purchasing,750,15,8/24/1984;
199508015,Annabelle,Boord,Accounting,365,26,9/24/1996;
199907017,Stephaine,Vinning,Marketing,365,30,12/4/1977;
201206013,Nelida,Sawchuk,Human Resources,750,22,5/9/1964;
200101020,Marguerita,Hiatt,Purchasing,1050,15,3/1/1960;
200306001,Carmela,Cookey,Marketing,365,18,7/17/1979;
201001007,Junita,Brideau,Accounting,565,23,10/4/1962;
199501003,Claribel,Varriano,Purchasing,800,28,8/18/1992;
199905003,Benton,Skursky,MIS,565,22,1/5/1984;
199705017,Hillary,Skulski,MIS,800,29,12/5/1989;
200409012,Merilyn,Bayless,MIS,800,22,12/26/1997;
200311010,Teri,Ennaco,Finance,565,25,2/11/1976;
201011005,Merlyn,Lawler,Human Resources,450,18,9/11/1961;
201412001,Georgene,Montezuma,Accounting,450,26,7/12/1974;
201810016,Jettie,Mconnell,Purchasing,365,17,2/20/2001;
199502007,Lemuel,Latzke,Admin,1050,18,2/15/1976;
200903005,Melodie,Knipp,Human Resources,565,18,3/22/1989;
199802006,Candida,Corbley,Admin,365,18,4/12/1977;
199509013,Karan,Karpin,Marketing,1050,26,12/12/1978;
201512019,Andra,Scheyer,Purchasing,450,20,10/18/1993;
201810009,Felicidad,Poullion,Marketing,1050,25,10/12/1980;
200907003,Belen,Strassner,Purchasing,750,20,8/25/1960;
201710020,Gracia,Melnyk,Admin,750,21,9/27/1986;
200401014,Jolanda,Hanafan,Human Resources,750,17,11/6/1986;
199612006,Barrett,Toyama,Finance,1050,28,9/25/1981;
200609001,Helga,Fredicks,Human Resources,750,22,5/15/1986;
200505016,Ashlyn,Pinilla,Accounting,1050,15,6/25/1972;
199612009,Fausto,Agramonte,Purchasing,800,27,4/16/1977;
199503005,Ronny,Caiafa,Human Resources,365,22,9/22/1957;
200012015,Marge,Limmel,Purchasing,1050,20,4/23/1979;
199906020,Norah,Waymire,Finance,565,17,7/2/1959;
200807016,Aliza,Baltimore,Admin,800,17,6/26/2002;
202003020,Mozell,Pelkowski,Marketing,450,28,5/22/1971;
201103009,Viola,Bitsuie,Finance,750,17,8/24/1980;
200909015,Franklyn,Emard,Purchasing,565,30,8/20/1979;
200612013,Willodean,Konopacki,Accounting,1050,27,1/5/1969;
201808012,Beckie,Silvestrini,Finance,565,18,5/20/1968;
199612011,Rebecka,Gesick,Purchasing,450,21,3/25/1976;
199912008,Frederica,Blunk,Purchasing,450,20,8/22/2000;
201812017,Glen,Bartolet,Human Resources,450,26,4/12/1984;
200905005,Freeman,Gochal,Marketing,450,15,11/21/1987;
201804013,Vincent,Meinerding,Admin,365,20,4/24/1968;
200109016,Rima,Bevelacqua,Human Resources,565,29,10/26/1971;
200106004,Glendora,Sarbacher,Finance,565,29,9/26/1963;
200211013,Avery,Steier,Marketing,450,26,5/20/2001;
200802007,Cristy,Lother,Admin,450,30,3/9/1984;
201002017,Nicolette,Brossart,Human Resources,450,20,11/11/1985;
199609016,Tracey,Modzelewski,Finance,1050,19,4/19/1971;
201804014,Virgina,Tegarden,Marketing,365,20,3/22/1986;
199808013,Tiera,Frankel,Accounting,450,28,10/15/1991;
201805016,Alaine,Bergesen,Admin,1050,18,1/26/1980;
199705014,Earleen,Mai,MIS,1050,25,1/28/2000;
201201009,Leonida,Gobern,MIS,750,16,8/6/1974;
200706018,Ressie,Auffrey,Human Resources,750,23,3/18/1984;
200206009,Justine,Mugnolo,MIS,800,29,1/13/1958;
201508010,Eladia,Saulter,Finance,750,18,7/16/1961;
200811016,Chaya,Malvin,Purchasing,750,21,12/6/1955;
200810017,Gwenn,Suffield,Accounting,365,30,8/17/1986;
200202001,Salena,Karpel,Finance,365,26,7/22/1988;
202002008,Yoko,Fishburne,MIS,800,27,10/20/1964;
201207016,Taryn,Moyd,MIS,750,26,6/19/1955;
201407010,Katina,Polidori,Human Resources,750,30,8/3/1962;
199912016,Rickie,Plumer,Finance,450,18,9/12/1995;
201904015,Alex,Loader,Purchasing,450,27,1/22/2002;
202004005,Lashon,Vizarro,MIS,800,24,1/23/1970;
201605015,Lauran,Burnard,Finance,365,29,10/10/1996;
200002009,Ceola,Setter,Marketing,365,28,6/24/1973;
201606014,My,Rantanen,MIS,565,22,2/23/1963;
200610015,Lorrine,Worlds,Human Resources,800,19,12/5/1990;
201802007,Peggie,Sturiale,Accounting,450,17,6/20/1967;
201312012,Marvel,Raymo,Human Resources,450,28,6/10/1976;
201808014,Daron,Dinos,Accounting,750,30,12/23/1996;
201208007,An,Fritz,Marketing,365,17,11/9/1973;
201712008,Portia,Stimmel,Finance,450,15,2/13/1986;
200512014,Rhea,Aredondo,Accounting,800,26,9/6/1976;
200207017,Benedict,Sama,Marketing,1050,20,4/28/1964;
200509006,Alyce,Arias,Accounting,450,23,3/12/1980;
200101004,Heike,Berganza,MIS,450,27,12/13/2001;
200107020,Carey,Dopico,Finance,800,23,8/15/1998;
199702001,Dottie,Hellickson,Marketing,365,15,7/12/1958;
200602012,Deandrea,Hughey,Finance,800,25,2/13/1979;
200011005,Kimberlie,Duenas,Finance,800,27,8/3/1985;
201603004,Martina,Staback,Admin,800,24,8/10/1970;
200211012,Skye,Fillingim,Human Resources,365,22,7/14/1962;
201003017,Jade,Farrar,Purchasing,565,20,7/11/1960;
200707003,Charlene,Hamilton,MIS,800,20,2/20/1989;
200911008,Geoffrey,Acey,MIS,750,17,9/5/1983;
201512002,Stevie,Westerbeck,Purchasing,365,18,8/19/1978;
199602010,Pamella,Fortino,Marketing,450,22,11/9/1969;
200307002,Harrison,Haufler,Marketing,750,22,1/23/1966;
199903019,Johnna,Engelberg,Admin,800,27,11/23/1991;
201112008,Buddy,Cloney,MIS,750,20,2/17/1964;
200811006,Dalene,Riden,Admin,1050,16,11/1/1972;
201104015,Jerry,Zurcher,Admin,565,26,1/20/1984;
199712018,Haydee,Denooyer,Human Resources,565,25,12/5/1995;
201910018,Joseph,Cryer,Purchasing,565,29,8/27/1971;
201310015,Deonna,Kippley,Finance,800,28,2/6/1989;
201102017,Raymon,Calvaresi,Human Resources,800,26,7/27/1979;
201202020,Alecia,Bubash,Admin,1050,17,12/15/2000;
200404017,Ma,Layous,Marketing,565,20,7/16/1974;
200306002,Detra,Coyier,MIS,450,18,4/21/1994;
200411019,Terrilyn,Rodeigues,Marketing,565,27,3/15/1990;
200506001,Salome,Lacovara,Human Resources,365,29,12/8/1981;
200202013,Garry,Keetch,Admin,1050,29,11/8/1960;
200703006,Matthew,Neither,MIS,800,30,4/8/1976;
200403002,Theodora,Restrepo,Marketing,450,21,12/26/1986;
199605016,Noah,Kalafatis,Accounting,565,29,2/10/1970;
201812014,Carmen,Sweigard,Human Resources,800,16,9/6/1965;
201603001,Lavonda,Hengel,Finance,1050,16,9/15/1972;
201110015,Junita,Stoltzman,Finance,365,20,11/11/1975;
200705005,Herminia,Nicolozakes,Finance,750,22,3/16/1974;
200502016,Casie,Good,Finance,1050,23,12/16/1962;
201405015,Reena,Maisto,Admin,1050,19,9/11/1994;
200807012,Mirta,Mallett,MIS,1050,15,5/20/1981;
200110019,Cathrine,Pontoriero,Accounting,800,26,9/8/1998;
199706005,Filiberto,Tawil,Finance,565,25,5/3/1972;
200612010,Raul,Upthegrove,Accounting,365,15,5/26/1958;
200406009,Sarah,Candlish,Human Resources,450,26,8/23/1981;
200903004,Lucy,Treston,Admin,800,27,3/6/1966;
201011010,Judy,Aquas,Finance,800,17,8/5/1962;
199708013,Yvonne,Tjepkema,Human Resources,800,27,12/28/1975;
200910020,Kayleigh,Lace,Accounting,800,26,12/20/1971;
200009010,Felix,Hirpara,Admin,450,29,1/13/1978;
200010008,Tresa,Sweely,Human Resources,450,26,9/27/1971;
201709002,Kristeen,Turinetti,Admin,450,30,4/16/1977;
199503006,Jenelle,Regusters,Marketing,450,26,7/15/2002;
201808010,Renea,Monterrubio,MIS,750,23,9/27/2000;
200412020,Olive,Matuszak,Admin,1050,18,7/4/2001;
201103018,Ligia,Reiber,Finance,565,21,3/26/1976;
199611018,Christiane,Eschberger,Finance,800,19,5/19/1992;
199609020,Goldie,Schirpke,MIS,750,15,1/15/1958;
201607011,Loreta,Timenez,Human Resources,800,18,1/23/1986;
199707012,Fabiola,Hauenstein,Purchasing,800,25,12/8/1997;
200501006,Amie,Perigo,Marketing,365,26,9/15/1967;
200307015,Raina,Brachle,Admin,365,23,2/4/1965;
201106016,Erinn,Canlas,Marketing,750,30,6/18/1961;
201303009,Cherry,Lietz,Accounting,750,23,11/17/1979;
200401006,Kattie,Vonasek,MIS,365,28,3/12/1964;
199606007,Lilli,Scriven,Finance,450,16,11/21/2001;
201103001,Whitley,Tomasulo,Finance,565,29,2/4/1981;
200602015,Barbra,Adkin,Marketing,750,27,8/19/1974;
200108018,Hermila,Thyberg,Human Resources,565,26,1/8/1988;
199610011,Jesusita,Flister,Finance,565,30,11/18/1996;
199611017,Caitlin,Julia,Human Resources,800,26,12/12/1997;
200505017,Roosevelt,Hoffis,MIS,800,19,3/24/2002;
201305016,Helaine,Halter,Finance,365,18,4/11/1993;
201308018,Lorean,Martabano,MIS,365,15,1/23/1986;
199507006,France,Buzick,Finance,450,29,6/25/1995;
201105019,Justine,Ferrario,MIS,565,29,10/1/1975;
199507018,Adelina,Nabours,Admin,450,30,6/18/1986;
200410008,Derick,Dhamer,Admin,750,29,1/27/2002;
199602012,Jerry,Dallen,Human Resources,565,26,8/21/1959;
201707008,Leota,Ragel,Human Resources,1050,15,9/22/1985;
200605008,Jutta,Amyot,Marketing,565,18,1/14/1987;
201212007,Aja,Gehrett,MIS,365,30,9/27/1960;
200404004,Kirk,Herritt,Accounting,450,21,6/16/1964;
201006006,Leonora,Mauson,Finance,1050,18,11/12/1962;
200405001,Winfred,Brucato,MIS,750,23,11/12/1991;
199903017,Tarra,Nachor,Finance,800,23,4/28/1980;
200102009,Corinne,Loder,Finance,365,16,9/11/1960;
201202009,Dulce,Labreche,Human Resources,565,30,5/21/1962;
202001008,Kate,Keneipp,Marketing,1050,26,12/20/1959;
199805007,Kaitlyn,Ogg,Accounting,365,25,7/13/1972;
199801016,Sherita,Saras,Purchasing,800,16,7/21/1996;
200702001,Lashawnda,Stuer,Marketing,1050,27,11/21/1989;
199709014,Ernest,Syrop,Accounting,450,15,7/15/2000;
201810006,Nobuko,Halsey,MIS,1050,17,8/20/1999;
200509010,Lavonna,Wolny,Accounting,1050,22,7/25/1961;
200108014,Lashaunda,Lizama,Admin,800,29,1/8/1958;
201012004,Mariann,Bilden,Accounting,1050,17,4/2/1967;
201604003,Helene,Rodenberger,MIS,365,22,8/8/1960;
201112004,Roselle,Estell,Human Resources,450,27,9/14/1964;
202004019,Samira,Heintzman,Admin,365,19,9/24/2001;
200105017,Margart,Meisel,Accounting,1050,28,12/21/1984;
200502015,Kristofer,Bennick,MIS,800,28,2/13/1996;
200504005,Weldon,Acuff,Purchasing,565,18,2/2/1998;
200909010,Shalon,Shadrick,Accounting,1050,28,3/4/1965;
199508013,Denise,Patak,Marketing,565,26,1/11/1973;
200107019,Louvenia,Beech,Accounting,800,29,4/16/1971;
201202012,Audry,Yaw,MIS,750,17,11/26/2002;
200806007,Kristel,Ehmann,Accounting,800,21,7/23/1996;
200010018,Vincenza,Zepp,Marketing,365,16,4/13/2002;
200710014,Elouise,Gwalthney,Marketing,565,17,6/15/1966;
200404013,Venita,Maillard,Marketing,365,19,12/26/1975;
199712014,Kasandra,Semidey,Accounting,1050,16,1/19/1984;
201505011,Xochitl,Discipio,Admin,1050,19,10/22/1984;
200512007,Maile,Linahan,MIS,365,20,10/23/1981;
200402009,Krissy,Rauser,Marketing,750,15,10/14/1975;
200507004,Pete,Dubaldi,Purchasing,365,28,7/17/1990;
200210007,Linn,Paa,Accounting,800,21,7/23/1980;
200006018,Paris,Wide,Finance,450,29,2/22/1978;
200402005,Wynell,Dorshorst,MIS,565,22,4/11/1972;
201807017,Quentin,Birkner,Purchasing,750,23,10/7/1999;
201206011,Regenia,Kannady,Accounting,750,18,3/2/1961;
199908014,Sheron,Louissant,Purchasing,800,25,2/2/1956;
201511012,Izetta,Funnell,Admin,1050,18,12/21/1969;
200103016,Rodolfo,Butzen,Purchasing,565,25,3/23/1980;
201601015,Zona,Colla,Purchasing,565,18,6/18/1959;
199807015,Serina,Zagen,Finance,750,30,10/26/1988;
201311019,Paz,Sahagun,Marketing,565,30,8/28/1993;
201907016,Markus,Lukasik,Accounting,750,16,5/20/1982;
201107020,Jaclyn,Bachman,Purchasing,750,20,7/13/1981;
200212008,Cyril,Daufeldt,Admin,565,20,6/14/1970;
199807013,Gayla,Schnitzler,MIS,800,29,3/27/1960;
200201002,Erick,Nievas,Admin,800,15,11/24/1997;
200510013,Jennie,Drymon,Finance,365,23,11/23/1971;
200102012,Mitsue,Scipione,Finance,565,23,7/9/1971;
201910011,Ciara,Ventura,Purchasing,450,23,1/18/1968;
201906012,Galen,Cantres,Marketing,1050,27,8/19/1956;
201409005,Truman,Feichtner,Admin,450,18,6/26/1957;
201409018,Gail,Kitty,MIS,1050,29,1/28/1969;
199510009,Dalene,Schoeneck,Finance,1050,18,12/3/1962;
201207015,Gertude,Witten,Human Resources,365,15,11/15/1976;
201601020,Lizbeth,Kohl,MIS,450,22,8/11/1971;
200107017,Glenn,Berray,Finance,565,19,4/2/1988;
200205014,Lashandra,Klang,Admin,565,28,8/10/1955;
200906014,Lenna,Newville,Marketing,800,27,7/25/1993;
200410004,Laurel,Pagliuca,Human Resources,565,30,4/4/1971;
199612001,Mireya,Frerking,Accounting,565,15,4/3/1964;
201601016,Annelle,Tagala,Human Resources,565,24,9/9/1987;
199707008,Dean,Ketelsen,Marketing,800,27,8/22/1984;
199703015,Levi,Munis,Admin,800,16,3/3/1972;
199507013,Sylvie,Ryser,Admin,365,25,4/23/2001;
199704020,Sharee,Maile,Finance,565,15,2/22/1978;
201808009,Cordelia,Storment,Accounting,800,21,10/17/1972;
200405015,Mollie,Mcdoniel,Marketing,565,19,2/28/1957;
199808016,Brett,Mccullan,MIS,565,15,3/27/2001;
200705003,Teddy,Pedrozo,Finance,565,19,6/3/1993;
200010009,Tasia,Andreason,Admin,365,24,10/25/1974;
199708020,Hubert,Walthall,Admin,365,21,6/17/1967;
200511010,Arthur,Farrow,Human Resources,565,21,9/22/1984;
199904003,Vilma,Berlanga,Marketing,450,16,7/20/1996;
201403016,Billye,Miro,Finance,365,23,3/19/1983;
201507014,Glenna,Slayton,Finance,750,26,2/15/1970;
199502009,Mitzie,Hudnall,Purchasing,800,19,3/4/1990;
201711020,Bernardine,Rodefer,Human Resources,1050,26,8/7/1989;
200906001,Staci,Schmaltz,Marketing,750,21,3/23/1980;
201310008,Nichelle,Meteer,Finance,365,18,10/20/1984;
200505006,Janine,Rhoden,Admin,750,28,2/10/1991;
200605005,Ettie,Hoopengardner,Purchasing,750,24,4/23/1959;
200508007,Eden,Jayson,Human Resources,800,30,9/17/1979;
200205010,Lynelle,Auber,Finance,750,17,1/15/1976;
200905019,Merissa,Tomblin,Marketing,365,23,1/27/1984;
201009015,Golda,Kaniecki,Human Resources,365,17,6/16/1960;
199810014,Catarina,Gleich,Human Resources,1050,15,6/3/1961;
199901016,Virgie,Kiel,Accounting,450,17,2/26/1995;
200807014,Jolene,Ostolaza,Marketing,565,29,9/8/1994;
199601016,Keneth,Borgman,Accounting,750,30,4/1/1992;
199504020,Rikki,Nayar,Admin,565,15,12/8/1971;
201211005,Elke,Sengbusch,Accounting,800,29,6/4/1988;
200608009,Hoa,Sarao,Purchasing,1050,29,12/10/1982;
201203014,Trinidad,Mcrae,Admin,750,16,2/2/1994;
200502008,Mari,Lueckenbach,MIS,365,30,3/16/1972;
199609013,Selma,Husser,Admin,750,27,3/12/1995;
199602009,Antione,Onofrio,Accounting,450,27,3/16/1958;
200401003,Luisa,Jurney,Accounting,800,21,4/8/2002;
200208006,Clorinda,Heimann,Accounting,1050,15,5/21/1994;
200307014,Dick,Wenzinger,Admin,565,15,10/13/1973;
200901005,Ahmed,Angalich,Purchasing,750,20,2/10/1973;
200704013,Iluminada,Ohms,Marketing,750,16,7/13/1972;
201701018,Joanna,Leinenbach,Finance,1050,15,11/6/1980;
201003007,Caprice,Suell,Admin,750,18,6/28/1992;
200205001,Stephane,Myricks,Human Resources,800,30,1/8/1978;
199809001,Quentin,Swayze,Marketing,365,17,7/16/1955;
200810009,Annmarie,Castros,Accounting,1050,19,12/14/1993;
201908014,Shonda,Greenbush,Purchasing,450,17,7/24/1957;
200607005,Cecil,Lapage,Purchasing,1050,27,1/9/1965;
201806017,Jeanice,Claucherty,Marketing,800,24,1/16/1981;
199609015,Josphine,Villanueva,Admin,450,16,12/13/1963;
201207014,Daniel,Perruzza,Admin,1050,27,12/11/1963;
201202018,Cassi,Wildfong,Admin,365,28,5/21/1962;
200007007,Britt,Galam,Marketing,450,15,12/6/1997;
199903020,Adell,Lipkin,Marketing,365,29,6/5/1963;
200001006,Jacqueline,Rowling,Finance,365,16,2/1/1975;
200709010,Lonny,Weglarz,Purchasing,365,18,5/22/1959;
200610011,Lonna,Diestel,Admin,800,25,12/8/1994;
201606003,Cristal,Samara,Purchasing,565,16,12/25/1980;
199510004,Kenneth,Grenet,Marketing,365,24,4/7/1967;
199507005,Elli,Mclaird,Purchasing,800,23,7/15/1999;
201512003,Alline,Jeanty,Purchasing,365,30,7/28/1987;
201502014,Sharika,Eanes,Human Resources,800,26,1/25/1992;
200112005,Nu,Mcnease,Human Resources,800,18,6/21/1999;
201206006,Daniela,Comnick,Accounting,565,29,7/16/1989;
199701002,Cecilia,Colaizzo,Purchasing,450,24,9/2/1969;
200310017,Leslie,Threets,Accounting,365,22,3/14/1978;
199509019,Nan,Koppinger,Marketing,800,27,9/1/1986;
200812015,Izetta,Dewar,MIS,750,23,1/11/1980;
199909010,Tegan,Arceo,Human Resources,800,30,3/25/1970;
199705013,Ruthann,Keener,Admin,565,29,4/26/1955;
201912012,Joni,Breland,Admin,365,17,1/24/1991;
201905017,Vi,Rentfro,Purchasing,365,19,2/1/1959;
200109015,Colette,Kardas,Admin,1050,24,3/21/1982;
199908006,Malcolm,Tromblay,Human Resources,565,19,4/18/1990;
199612013,Ryan,Harnos,Finance,750,19,9/24/1959;
200808013,Jess,Chaffins,MIS,750,29,4/16/1971;
199509002,Sharen,Bourbon,Human Resources,1050,26,9/24/1971;
200304017,Nickolas,Juvera,Purchasing,565,16,2/15/1962;
200901001,Gary,Nunlee,Purchasing,750,30,2/16/1966;
199808003,Diane,Devreese,Marketing,800,16,8/4/1963;
201412002,Roslyn,Chavous,MIS,365,15,1/7/1992;
201209005,Glory,Schieler,Human Resources,800,30,10/14/2000;
200709011,Rasheeda,Sayaphon,Admin,1050,29,10/7/1957;
200612020,Alpha,Palaia,Human Resources,1050,24,12/4/1965;
201909015,Refugia,Jacobos,Purchasing,750,30,8/5/1971;
200510003,Shawnda,Yori,Admin,565,30,10/7/1960;
201401020,Mona,Delasancha,Human Resources,450,30,6/14/1983;
201609008,Gilma,Liukko,Finance,450,28,12/3/1957;
201301014,Janey,Gabisi,Admin,450,28,12/4/1996;
199911003,Lili,Paskin,Purchasing,365,25,4/19/1993;
201101018,Loren,Asar,Human Resources,750,15,8/17/1990;
200903012,Dorothy,Chesterfield,Accounting,450,17,4/28/1975;
200110016,Gail,Similton,Marketing,1050,20,10/7/2000;
201907013,Catalina,Tillotson,Purchasing,1050,21,1/2/1987;
201504001,Lawrence,Lorens,Human Resources,750,18,5/28/1978;
199601011,Carlee,Boulter,MIS,800,24,8/1/1999;
200301006,Thaddeus,Ankeny,Accounting,800,17,1/17/1979;
200003014,Jovita,Oles,Finance,450,19,6/14/1965;
199506006,Alesia,Hixenbaugh,Finance,750,17,3/3/2000;
201311016,Lai,Harabedian,Accounting,1050,29,1/5/2000;
201106010,Brittni,Gillaspie,Marketing,1050,25,11/28/1974;
201601005,Raylene,Kampa,Purchasing,365,15,12/19/2001;
200909005,Flo,Bookamer,Human Resources,800,28,12/19/1957;
200512016,Jani,Biddy,Human Resources,565,20,8/7/1966;
199806004,Chauncey,Motley,Admin,450,24,3/1/2000"""

#How many employees are there
employees = empRecords.strip().split(';')

num_employees = len(employees)
print(f"Number of employees: {num_employees}")


#Which department has the highest number of employees
departments = {}
for emp in employees:
    emp_data = emp.split(',')
    department = emp_data[3].strip()

    # Checking if department already exists in the dictionary
    if department in departments:
        departments[department] += 1
    # Adding the department to the dictionary with count as 1
    else:
        departments[department] = 1
    #Finding the department with the highest count
max_department = max(departments, key=departments.get)  
print(f"Department with the highest number of employees: {max_department}")

# Counter for employees celebrating their birthday in December
december_birthdays = 0
# Process each record
for record in employees:
    # Split the record into fields
    birth = record.split(",")
    # Extract the date of birth field
    date_of_birth = datetime.strptime(birth[6], "%m/%d/%Y")
    # Check if the birth month is December
    if date_of_birth.month == 12:
        december_birthdays += 1

print(f"The number of employees celebrating their birthday in December: {december_birthdays}")

#What is the Employee number of the highest earning employee
highest_earning = 0
highest_earning_employee_id = ""

# Iterate through the records
for record in employees:
    fields = record.split(",")
    salary = int(fields[4])
    workDays = record.split(",")
    days = int(workDays[5])
    #multiply the salary with the days the have been working 
    salarys = salary * days
    # Check if the current salary is higher than the previous highest earning
    if salarys > highest_earning:
        highest_earning = salarys
        highest_earning_employee_id = fields[0]

print(f"Employee ID with the highest earning: {highest_earning_employee_id}")

#How many employees are senior citizen 
current_date = datetime.now()

# Initialize the count of senior employees
senior_employee_count = 0

# Iterate through the records
for record in employees:
    fields = record.split(",")
    date_of_birth = datetime.strptime(fields[6], "%m/%d/%Y")

    # Calculate the age of the employee
    age = current_date.year - date_of_birth.year

    # Check if the employee is a senior (age 60 and above)
    if age >= 60:
        senior_employee_count += 1

print(f"Number of senior employees: {senior_employee_count}")

#How many employees are in their 15th year of service
fifteen_years_service_count = 0

# Iterate through the records
for record in employees:
    workDays = record.split(",")
    days = int(workDays[5])

    # Check if the employee has completed 15 years of service
    if days >= 365 * 15:
        fifteen_years_service_count += 1

print(f"Number of employees with 15 years of service: {fifteen_years_service_count}")