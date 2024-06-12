                                            Orsay, December 17, 1993

        Dear Colleague,

        Thank  you for  your message  and for  your interest  in the
        evaluated atomic masses of nuclei.

        Please find below  the procedures on how to  access and copy
        the files  of "The  1993 Atomic  Mass Evaluation"  from NNDC
        (USA and  Canada), NEA-DB(Western Europe and  Japan) or IAEA
        (other countries).

        I hope everything will work out well.  If it does'nt, please
        contact me  or contact the  person in  charge in one  of the
        Nuclear Data  Centers.  Of  course if  you need  any special
        information, please  ask, it will  be my pleasure to  try to
        provide it to you.

        Best regards,
        Georges Audi


        *********         A -  GENERAL INFORMATION         *********
        *********         A -  GENERAL INFORMATION         *********

                               (December 6, 1993)

        I - INTRODUCTION

        The  table of  masses  (part  I) and  the  table of  nuclear
        reaction and separation energies (part II) of:
                     "THE 1993 ATOMIC MASS EVALUATION"
                         by G.Audi and A.H.Wapstra
                    Nuclear Physics A565 (1993) 1 and 66.
                            (December 6, 1993)
        are available electronically at the Nuclear Data Centers.

        A  total of  six files  can  be obtained.   The first  file,
        mass_exp.mas93, contains  the table of masses  as printed in
        part  I.  The  next two  files  correspond to  the table  of
        reaction and separation  energies in two parts  of 6 entries
        each, as in part II:
           rct1_exp.mas93 for S2n, S2p, Q(a), Q(2B),  Q(ep),  Q(B-n)
           rct2_exp.mas93 for Sn,  Sp, Q(4B), Q(d,a), Q(p,a), Q(n,a)
        The   last   three    files   with   names   mass_rmd.mas93,
        rct1_rmd.mas93 and rct2_rmd.mas93 are identical to the first
        three files  except that the  values resulting from  the few
        experimental  data, listed  in  table  B of  part  I of  our
        publication, are replaced by  values that we recommend based
        upon estimates from systematic trends.

        Values  in these  files are  exact (unrounded)  copy of  the
        published ones.
           * They can conveniently be used for calculations.
           * None of them should be copied in a publication as given
             in  these  files,  but   instead,  the  rounded  values
             published in the above Journal should be used.


        II - VALUES FOR THE MOST PRECISE MASSES:

                      Mass excess (keV)        Atomic mass (micro-u)

          1  n      8071.32311  0.00221       1008664.92358  0.00229
          1 H       7288.96917  0.00077       1007825.03190  0.00057
          2 H      13135.71957  0.00114       2014101.77795  0.00062
          3 H      14949.79430  0.00170       3016049.26767  0.00136
          3 He     14931.20331  0.00161       3016029.30942  0.00123
          4 He      2424.91111  0.00141       4002603.24970  0.00150
         13 C       3125.01132  0.00457      13003354.83834  0.00490
         14 C       3019.89432  0.00396      14003241.99059  0.00425
         14 N       2863.41905  0.00171      14003074.00743  0.00183
         16 O      -4736.99810  0.00239      15994914.62231  0.00253
         20 Ne     -7041.92927  0.00283      19992440.17639  0.00298
         40 Ar    -35039.88949  0.00539      39962383.12350  0.00505


        III - REFERENCES:

        "THE 1993 ATOMIC MASS EVALUATION"  by G.Audi and A.H.Wapstra

        Part  I:  Nuclear Physics A565 (1993) 1.
          for files:
              mass_exp.mas93  masses experimental
              mass_rmd.mas93  masses recommended

        Part II:  Nuclear Physics A565 (1993) 66
          for files:
              rct1_exp.mas93  reaction energies experimental,table 1
              rct2_exp.mas93  reaction energies experimental,table 2
              rct1_rmd.mas93  reaction energies recommended, table 1
              rct2_rmd.mas93  reaction energies recommended, table 2


        IV - FORMAT:

        All files  are 2650 lines  long with 124 character  per line
        (originally in fixed format).  Headers are 40 lines long.

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


        V - CORRECTIONS AND SUGGESTIONS

        If   you   find  errors   or   omissions   in  the   present
        documentation,  or, if  you  have a  suggestion  to make  it
        clearer, please  send a message to  the following electronic
        address.  Thanks in advance.
              internet : audi@frcpn11.in2p3.fr
              bitnet   : audi@frcpn11



        *********        B -  NNDC (USA and Canada)        *********
        *********        B -  NNDC (USA and Canada)        *********


        I - COPYING OF FILES THROUGH NETWORKS:

        The six mass files may  be obtained via an anonymous account
        on the  NNDC VAX  Alpha computer,  through TCP/IP  or DECNET
        networks.

        These   six  files,   along   with   a  documentation   file
        "READMASS.ME",    are    located   in    the    subdirectory
        SA0:[SCR.MASSES].  These may then be copied on to the user's
        computer using the  FTP "GET" command, or  the DECNET "COPY"
        command.

        The user name of the anonymous account is BNLNDC.

        * TCP/IP:  use the  `FTP'  command,  to  connect to  BNLND2:
           ex: ftp bnlnd2.dne.bnl.gov (or 130.199.112.132)
               User (identify yourself to the host): bnlndc
               Command: cd masses
               Command: get mass_exp.mas93
               Command: quit

        * DECNET:  use the DEC  `DIRECTORY' and `COPY' commands, for
                   bnlnd2 (or 44436 or 43.404).
           ex:$dir bnlnd2"bnlndc"::sa0:[scr.masses]
              $copy bnlnd2"bnlndc"::sa0:[scr.masses]mass_exp.mas93 *


        II - ATOMIC MASSES FROM NNDC ON-LINE SYSTEM:

        1 - Access to the On-Line service:

        One  can  access the  NNDC  (National  Nuclear Data  Center,
        Brookhaven National Laboratory, USA) On-Line service through
        a network or a remote modem.  The service is available on an
        NNDC VAX Alpha computer.  Presently,  there is no charge for
        the On-Line service.

        Via modem:
             The NNDC VAX  Alpha computer can be  accessed via modem
             using the telephone number 516-282-5390.
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
                         nndc@bnl     (bitnet)
                         bnl::nndc    (hepnet)

        Please  give   your  name,  postal  and   e-mail  addresses,
        telephone number,  your affiliation, and a  personal code of
        six   or  fewer   characters  which   will  serve   as  your
        authorization code.



        *********  C -  NEA-DB (Western Europe and Japan)  *********
        *********  C -  NEA-DB (Western Europe and Japan)  *********


        I - COPYING OF FILES THROUGH NETWORKS:

        File transfer options
           Upload   Kermit protocol to transfer files to NEA
           Download Kermit protocol to transfer files from NEA
           Capture  Screen capture to transfer ASCII files from NEA
           Binary Bitnet
                    To send binary files through BITNET
           Binary Internet (FTP)
                    To send or receive binary files through INTERNET


        II - ATOMIC MASSES FROM NEA ON-LINE SERVICES:

        1 - Access to the On-Line service:

        Logging on: logon as NEADB  and give your assigned user name
                    and password or use the GUEST name for a limited
                    time.
              Internet: DB.NEA.FR old  (numeric = 130.84.216.5)
                                  new  (numeric = 193.51.64.1)
              X25     : (2080) 921607751 or in France: (1) 921607751


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


        4 - Authorization:

              Address:   Nuclear Energy Agency - Data Bank
                         O.E.C.D.
                         Le Seine Saint Germain
                         12, boulevard des Iles
                         92130 Issy-les-Moulineaux
                         France

              Telephone: +33 (1) 45.24.10.71
              Telefax:   +33 (1) 45.24.11.10

              E-mail:    nea@nea.fr   (internet)
                         nea@frneab51 (earn/bitnet)



        *********       D -  IAEA (other countries)        *********
        *********       D -  IAEA (other countries)        *********


        I - COPYING OF FILES THROUGH NETWORKS:

        The six mass files may  be obtained via an anonymous account
        on the  NDS VAX  4200 computer through TCP/IP network.

        These   six  files,   along   with   a  documentation   file
        "README.MAS93",    are   located    in   the    subdirectory
        {SCR.MASSES}.  These may then be copied on to the user's
        computer using the FTP "GET" command.

        Use the 'FTP' command to connect to:
                       iaeand.iaea.or.at (or 161.5.2.2)

        The user name of the anonymous account is "NDSOPEN".

        Ex: ftp iaeand.iaea.or.at (or 161.5.2.2)
            User (identify yourself to the host): ndsopen
            Command: cd masses
            Command: get mass_exp.mas93
            Command: quit


        II - ATOMIC MASSES FROM IAEA ON-LINE SERVICES:

               ==============================================
              /  Note: This service will not be available  /
             /         until spring/summer 1994.          /
            ==============================================

        1 - Access to the On-Line service:

        Use the TCP/IP (internet) network.
             TELNET iaeand.iaea.or.at
             Username: IAEANDS
             Enter NDS assigned authorization code (or GUEST): GUEST
                    (or your authorization code if you have one)


        2 - Retrievals or Copying of files:

        Identical to the system of the US National Data Center.
        (see B - II - 2  above)


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
