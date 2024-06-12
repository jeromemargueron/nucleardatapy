            A T O M I C       M A S S       E V A L U A T I O N
 
 
        *********         A -  GENERAL INFORMATION         *********
        *********         A -  GENERAL INFORMATION         *********
 
                             (November 28, 1995)
 
        I - INTRODUCTION
 
        The table  of masses and  the table of nuclear  reaction and
        separation energies resulting  from the evaluation published
        in:
             -------------------------------------------------
            | "THE 1995 UPDATE TO THE ATOMIC MASS EVALUATION" |
            |                                                 |
            |                    (Ame'95)                     |
            |                                                 |
            |           by G. Audi and A.H. Wapstra           |
            |                                                 |
            |       Nuclear Physics A595 (1995) 409-480.      |
            |                                                 |
            |               (December 25, 1995)               |
             -------------------------------------------------
 
        are  available  electronically  at the  ``Atomic  Mass  Data
        Center" (AMDC) and at the Nuclear Data Centers.
 
        Six files from this evaluation can be obtained:
            mass_rmd.mas95   Recommended  masses
            rct1_rmd.mas95   Recommended  reaction energies, table 1
            rct2_rmd.mas95   Recommended  reaction energies, table 2
            mass_exp.mas95   Experimental masses
            rct1_exp.mas95   Experimental reaction energies, table 1
            rct2_exp.mas95   Experimental reaction energies, table 2
        Most  readers can  best use  the set  of recommended  tables
        (labelled  with `rmd')  whereas  the  more specialized  user
        could  with  benefit  analyze  the second  set  (with  label
        `exp').
 
        The first file, mass_rmd.mas95, contains the table of masses
        as  printed  in  the   reference  above,  plus  the  binding
        energies,  the beta-decay  energies and  the atomic  masses.
        The next two  files correspond to the table  of reaction and
        separation energies (cf. "The  1993 Atomic Mass Evaluation",
        part II) in two parts of 6 entries each:
           rct1_rmd.mas95 for S2n, S2p, Q(a), Q(2B),  Q(ep),  Q(B-n)
           rct2_rmd.mas95 for Sn,  Sp, Q(4B), Q(d,a), Q(p,a), Q(n,a)
        The   last   three    files   with   names   mass_exp.mas95,
        rct1_exp.mas95 and rct2_exp.mas95 are identical to the first
        three files except for the  values resulting from the use of
        the few  deviating experimental  data, listed in  Table~B of
        Ame'93 and updated in Table~IV-a of Ame'95.
 
        Values  in these  files are  exact (unrounded)  copy of  the
        published ones.
           *  They can conveniently be used for calculations.
           *  They should not be copied in a publication as given in
              these files, but instead, rounded values, as published
              in the above Journal should be used.
 
        References: Ame'93 =   "The 1993 atomic mass evaluation"
                                   by G.Audi and A.H.Wapstra
                               Nuclear Physics A565 (1993) 1-397.
 
 
        II - VALUES FOR THE MOST PRECISE CALCULATIONS:
 
        a - values for the most precise masses:
 
                      Mass excess (keV)        Atomic mass (micro-u)
 
          1  n      8071.32281  0.00215       1008664.92326  0.00221
          1 H       7288.96940  0.00064       1007825.03214  0.00035
          2 H      13135.71961  0.00104       2014101.77799  0.00036
          3 H      14949.79417  0.00149       3016049.26753  0.00106
          3 He     14931.20356  0.00138       3016029.30970  0.00086
          4 He      2424.91109  0.00095       4002603.24968  0.00100
         13 C       3125.01081  0.00095      13003354.83780  0.00099
         14 C       3019.89233  0.00374      14003241.98845  0.00400
         14 N       2863.41701  0.00083      14003074.00524  0.00086
         15 N        101.43823  0.00085      15000108.89844  0.00092
         16 O      -4736.99828  0.00147      15994914.62211  0.00153
         20 Ne     -7041.92974  0.00192      19992440.17589  0.00198
         28 Si    -21492.79309  0.00244      27976926.53273  0.00196
         40 Ar    -35039.88974  0.00387      39962383.12324  0.00305
 
        b - values for the correlation coefficients (in nano-amu**2)
 
            n          H         D         3H        3He      4He
 
         4.899380
        -0.083048   0.123414
         0.092465   0.040200  0.132764
         0.014840  -0.000165  0.014699  1.114100
         0.006104   0.002664  0.008774  0.446509  0.733021
        -0.000036   0.000001 -0.000001  0.000000  0.000000  0.999982
 
        c - values for precise  mass differences (in keV)  of use in
            deriving  reaction energies  other than  those given  in
            files rct1.... and rct2.... (cf.  Ame'93, p.68-69):
 
                   a-2d       : -23846.5281  0.0021
                   3He-t      :    -18.5906  0.0009
                   p-n        :   -782.3534  0.0021
                   p+n-d      :   2224.5726  0.0020
                   p+2n-t     :   8481.8209  0.0043
                   p-a+t      :  19813.8525  0.0020
                   p+d-3He    :   5493.4854  0.0010
                   2p+n-3He   :   7718.0580  0.0023
                   -a+n+3He   :  20577.6153  0.0029
                   d+n-t      :   6257.2483  0.0024
                   a-d-p-n    : -26071.1007  0.0030
                   a-d+p-3He  : -18353.0427  0.0019
                   a-d+n-t    : -17589.2799  0.0028
 
 
        III - FORMAT:
 
        All files  are 2931 lines  long with 124 character  per line
        (originally in fixed format).  Headers are 39 lines long.
 
        Record Format:
 
        1 - For mass-files:
 
           Column       Format        Quantity
 
             1:1        a1            fortran control character (a)
             2:4        i3            N-Z neutron excess
             5:9        i5            N  neutron number
            10:14       i5            Z  atomic number
            15:19       i5            A  mass number
            20:20       1x
            21:23       a3            Chem Symbol
            24:27       a4            origin
            28:28       1x
            29:39       f11.3         mass
            40:48       f9.3          mass accuracy
            49:59       f11.3         binding energy
            60:68       f9.3          binding energy accuracy
            69:72       4x
            73:74       a2            B+ or B-
            75:85       f11.3         beta decay energy
            86:94       f9.3          beta decay energy accuracy
            95:96       2x
            97:110      i3,1x,f10.3   atomic_mass
           111:119      f9.3          atomic mass accuracy
 
 
        2 - For rct-files :
 
           Column       Format        Quantity
 
             1:1        a1            fortran control character (a)
             2:4        i3            A mass number
             5:5        1x
             6:8        a3            Chem Symbol
             9:11       i3            Z atomic number
            12:12       1x
            13:30       f10.2,f8.2    energy 1, accuracy 1
            31:48       f10.2,f8.2    energy 2, accuracy 2
            49:66       f10.2,f8.2    energy 3, accuracy 3
            67:84       f10.2,f8.2    energy 4, accuracy 4
            85:102      f10.2,f8.2    energy 5, accuracy 5
           103:120      f10.2,f8.2    energy 6, accuracy 6
 
        Notes:
          a- Fortran control character: 1 = page feed
                                        0 = line feed
          b- decimal point is replaced by  # for values derived from
                  systematical trends (see publications).
          c- * in place of value means `not calculable'
 
 
        IV - CORRECTIONS AND SUGGESTIONS
 
        If   you   find  errors   or   omissions   in  the   present
        documentation,  or, if  you  have a  suggestion  to make  it
        clearer, please  send a message to  the following electronic
        address.  Thanks in advance.
              internet : audi@frcpn11.in2p3.fr
 
 
 
        *********             B -  A.M.D.C.                *********
        *********             B -  A.M.D.C.                *********
 
 
        COPYING OF FILES THROUGH NETWORKS:
 
        The six files of the Ame'95, along with a documentation file
        "readme.mas95", may be obtained  via an anonymous account on
        the  Atomic  Masses  Data  Center  (AMDC)  HP-Unix  computer
        through TCP/IP network protocol.
 
        These files are located  in the subdirectory pub/AMDC.  They
        may be copied on to the  user's computer using the FTP "get"
        command.   The  user  name   of  the  anonymous  account  is
        "anonymous" (enter your e-mail address as the password).
        Example:
               ftp csn-hp.in2p3.fr
               user:      anonymous
               password:  your electronic address
               cd pub
               cd AMDC                (please type AMDC in capitals)
               get readme.mas95
               get mass_rmd.mas95
               quit
 
 
        II - ADDRESS
 
        Address:   Atomic  Mass  Data  Center
                   C.S.N.S.M. (IN2P3-CNRS)
                   Batiment 108
                   91405 Orsay campus
                   (France)
 
        Telephone: +33 (1) 69.41.52.23
        Telefax:   +33 (1) 69.41.52.68
 
        E-mail:    audi@frcpn11.in2p3.fr  (internet)
 
 
        *********        C -  NNDC (USA and Canada)        *********
        *********        C -  NNDC (USA and Canada)        *********
 
 
        I - COPYING OF FILES THROUGH NETWORKS:
 
        The six mass files may  be obtained via an anonymous account
        on  the  NNDC  DEC  Alpha computer  through  TCP/IP  network
        protocol.
 
        These   six  files,   along   with   a  documentation   file
        "README.MAS95",    are   located    in   the    subdirectory
        SA2:[PUBLIC.MASSES].   These may  then be  copied on  to the
        user's computer using the FTP "GET" command.
 
        The user name  of the anonymous account  is ANONYMOUS (Enter
        your e-mail address as the password):
           ex: ftp bnlnd2.dne.bnl.gov
               User (identify yourself to the host): anonymous
               Password: enter your e-mail address as the password
               Command: cd masses
               Command: get mass_rmd.mas95
               Command: quit
 
 
        II - ATOMIC MASSES FROM NNDC ON-LINE SYSTEM:
 
        1 - Access to the On-Line service:
 
        One  can  access the  NNDC  (National  Nuclear Data  Center,
        Brookhaven National Laboratory, USA) On-Line service through
        a network or a remote modem.  The service is available on an
        NNDC VAX Alpha computer.  Presently,  there is no charge for
        the On-Line service.
 
        Via modem:
             The NNDC VAX  Alpha computer can be  accessed via modem
             using the telephone number 516-282-2002.
             After  getting  the  connect signal,  type  a  carriage
             return, wait  and then  type a second  carriage return.
             The  VAX  login  prompt  should  then  appear  on  your
             terminal.
 
        Via networks:
           * TCP/IP (internet):  use the `TELNET' command  to access
                    the  computer  node  BNLND2.  Its  address   is
                    BNLND2.DNE.BNL.GOV (or 130.199.112.132)
           * DECNET:  use  the  `SET   HOST'  command  with  address
                    BNLND2 (or 44436 or 43.404)
 
        The VAX login  prompt will appear and you  should proceed as
        follows:
           * Username: NNDC
           * Enter NNDC assigned authorization code (or GUEST):GUEST
                (or your authorization code if you have one)
 
        The  authorization code  "GUEST" allows  a new  user limited
        amount of CPU time to become acquainted with the system.
 
 
        2 - Retrievals or Copying of files:
 
        Once  you  are  logged  into NNDC  online  service  you  can
        retrieve from  various different numerical  or bibliographic
        data bases, or simply  copy files containing computer codes,
        documentation, or mass tables.
 
        In  order to  copy  files containing  mass  tables you  will
        proceed as the following:
 
        After successful login select the option FILES.  Within this
        option select the data item MASSES and indicate which of the
        six files  and documentation you  will like to copy  over to
        your  computer.  After  the  selection of  file(s) you  will
        automatically be in SEND option  and you will be asked which
        network  you will  want  to use  to  transfer your  file(s).
        After that the system will  query you about your destination
        address, your password (it does not echo), and the file name
        that you are  transferring.  The system will  respond if the
        transfer was successful.  You can  then choose to do further
        retrievals or logout.
 
 
        3 - Logout:
 
        When  terminating  a  retrieval  session,  enter  or  select
        LOGOUT.
 
 
        4 - Authorization:
 
        For authorization  for access  to NNDC online  service, user
        can supply  the necessary  information while logged  in with
        'GUEST' authorization as indicated above or write to NNDC at
        the following address:
 
              Address:   On-Line access
                         National Nuclear Data Center
                         Brookhaven National Laboratory
                         Building 197D
                         P.O. Box 5000
                         Upton, NY 11973-5000 (U.S.A.)
 
              Telephone: 516-282-2901.
              Telefax:   516-282-2806
 
              E-mail:    nndc@bnl.gov (internet)
                         bnl::nndc    (hepnet)
 
        Please  give   your  name,  postal  and   e-mail  addresses,
        telephone number,  your affiliation, and a  personal code of
        six   or  fewer   characters  which   will  serve   as  your
        authorization code.
 
 
        III - ATOMIC MASSES FROM NNDC WORLD WIDE WEB SITE:
 
        1 - URL:  http://www.dne.bnl.gov/nndc.html
 
        2 - Select 1995 Audi-Wapstra  Atomic  Masses under Programs,
            Data Files and Manuals.
 
        3 - Click on a file name  to view it or shift-click to down-
            load the file.
 
 
 
        **** D -  NEA-DB (Western Europe, Mexico, Korea, Japan) ****
        **** D -  NEA-DB (Western Europe, Mexico, Korea, Japan) ****
 
 
        I - WORLD WIDE WEB
 
              URL: http://www.nea.fr/
              Select Data Bank
              Select Experimental data (EXFOR, ... MASSES)
              Select File(s) required
 
        II - FTP
 
              Ftp to ftp.nea.fr
              login ANONYMOUS
              password is user's e-mail address
              cd data
              mget mass*  or  mget rct*     (file names are given in
                                                        Section A-I)
              exit
 
 
        III - E-MAIL
 
        Send an e-mail to:  nearobot@nea.fr
 
        In the body of the message type
               "index"            to get the list of filenames
            or "get filename"     where filename is one of:
                                        masses-info.txt
                                        mass_rmd_mas95.txt
                                        rct1_rmd_mas95.txt
                                        rct2_rmd_mas95.txt
                                        mass_exp_mas95.txt
                                        rct1_exp_mas95.txt
                                        rct2_exp_mas95.txt
 
        IV - TELNET
 
        1 - Access to the On-Line service:
 
        Logging on: logon as NEADB  and give your assigned user name
                    and password or use the GUEST name for a limited
                    time.
              Internet: DB.NEA.FR   (numeric = 193.51.64.1)
 
 
        2 - Retrievals or Copying of files:
 
        On logging-on to our On-Line service, the user has to select
        first the option "Nuclear Data".  Under "Nuclear Data" there
        is a menu called MASSES.   When this option is selected, the
        description of  the files and  their content will  appear on
        the screen,  ending with a  question asking: "Which  file or
        files would you  like to retrieve?" The  selected files will
        automatically be transmitted to the user home computer.
 
 
        3 - Logout:
 
        When  terminating  a  retrieval  session,  enter  or  select
        LOGOUT.
 
 
        4 - Authorization (not required):
 
              Address:   Nuclear Energy Agency - Data Bank
                         O.E.C.D.
                         Le Seine Saint Germain
                         12, boulevard des Iles
                         92130 Issy-les-Moulineaux
                         France
 
              Telephone: +33 (1) 45.24.10.71
              Telefax:   +33 (1) 45.24.11.10
 
              E-mail:    nea@nea.fr   (internet)
 
 
        *********       E -  IAEA (other countries)        *********
        *********       E -  IAEA (other countries)        *********
 
 
        I - COPYING OF FILES THROUGH NETWORKS:
 
        The six mass files may  be obtained via an anonymous account
        on the  NDS AlphaServer  2100-4/275 computer  through TCP/IP
        network.
 
        These   six  files,   along   with   a  documentation   file
        "README.MAS95",    are   located    in   the    subdirectory
        {SCR.MASSES}.  These may then be copied on to the user's
        computer using the FTP "GET" command.
 
        Use the 'FTP' command to connect to:
                       iaeand.iaea.or.at
 
        The user name of the anonymous account is "NDSOPEN".
 
        Ex: ftp iaeand.iaea.or.at
            user (identify yourself to the host): ndsopen
            cd masses
            get mass_rmd.mas95
            quit
 
 
        II - ATOMIC MASSES FROM IAEA ON-LINE SERVICES:
 
        1 - Access to the On-Line service:
 
        Use the TCP/IP (internet) network.
             TELNET iaeand.iaea.or.at
             Username: IAEANDS
             Enter NDS assigned authorization code (or GUEST): GUEST
                    (or your authorization code if you have one)
 
 
        2 - Retrievals or Copying of files:
 
        Identical to the system of the US National Data Center.
        (see C - II - 2  above)
 
 
        3 - Logout:
 
        When  terminating  a  retrieval  session,  enter  or  select
        LOGOUT.
 
 
        4 - Authorization:
 
        As a "GUEST", you will have 30 seconds of CPU allocated.  At
        the end of a GUEST session,  you may sign up directly for an
        authorization  code for  full  access service.   Or you  may
        contact the IAEA  Nuclear Data Section for  assignment of an
        authorization code.
 
              Address:   Nuclear Data Section
                         NDIS Manager
                         International Atomic Energy Agency
                         P.O.Box 100
                         A-1400 Vienna, Austria
 
              Telephone: +43 1  2360 1715
              Telefax:   +43 1  2345 64
              Telex:     1-12645 ATOM A
 
              E-mail:    online@iaeand.iaea.or.at (internet)
