MODULE input

 IMPLICIT NONE

 INTEGER :: NDQPSH = 5

 INTEGER :: NUMsphe, NUModd, NUMdefo, NUMd3n, NUMd3p, NUMsupd, NUMmono, NUMdipo, NUMtwop, NUMdvpn, NUMterm, NUMqpSH

 INTEGER , ALLOCATABLE :: IZsphe(:), INsphe(:)
 INTEGER , ALLOCATABLE :: IZdefo(:), INdefo(:), IsOKdefo(:)
 INTEGER , ALLOCATABLE :: IZd3n (:), INd3n (:), IsOKd3n(:), IZd3p(:), INd3p(:), IsOKd3p(:)
 INTEGER , ALLOCATABLE :: IZsupd(:), INsupd(:)
 INTEGER , ALLOCATABLE :: IZmono(:), INmono(:)
 INTEGER , ALLOCATABLE :: IZdipo(:), INdipo(:)
 INTEGER , ALLOCATABLE :: IZodd (:), INodd (:), IsOKodd(:)
 INTEGER , ALLOCATABLE :: IZqpSH(:), INqpSH(:)
 INTEGER , ALLOCATABLE :: IZtwop(:), INtwop(:)
 INTEGER , ALLOCATABLE :: IZdvpn(:), INdvpn(:)
 INTEGER , ALLOCATABLE :: IZterm(:), INterm(:)

 INTEGER , ALLOCATABLE :: IPodd(:)
 INTEGER , ALLOCATABLE :: IP1term(:), IP2term(:)
 INTEGER , ALLOCATABLE :: NQPqpSH(:),IPqpSH(:,:)

 DOUBLE PRECISION , ALLOCATABLE :: Bsphe(:),dBsphe(:),R0sphe(:),SIGsphe(:),RMSspheCharge(:), RMSspheProton(:)
 DOUBLE PRECISION , ALLOCATABLE :: Bdefo(:),dBdefo(:),b2defo(:)
 DOUBLE PRECISION , ALLOCATABLE :: DELd3n(:),ERRd3n(:),DELd3p(:),ERRd3p(:)
 DOUBLE PRECISION , ALLOCATABLE :: Bsupd(:),ESDsupd(:), b2supd(:)
 DOUBLE PRECISION , ALLOCATABLE :: Emono(:),dEmono(:)
 DOUBLE PRECISION , ALLOCATABLE :: Edipo(:)
 DOUBLE PRECISION , ALLOCATABLE :: SPINodd(:)
 DOUBLE PRECISION , ALLOCATABLE :: Etwop(:),dEtwop(:),BE2twop(:),dBE2twop(:)
 DOUBLE PRECISION , ALLOCATABLE :: ExcMASdvpn(:),ExcERRdvpn(:),BnucMASdvpn(:),BnucERRdvpn(:),DelVPNdvpn(:),DelERRdvpn(:)
 DOUBLE PRECISION , ALLOCATABLE :: SPINterm(:),Eterm(:),SPINdEterm(:),dEterm(:)
 DOUBLE PRECISION , ALLOCATABLE :: EqpSH(:,:),SPINqpSH(:,:)

 CHARACTER (LEN=5) , ALLOCATABLE :: LABqpSH(:,:)

 CONTAINS

    !
    !  The subroutine reads the database, allocates a number of arrays that
    !  are passed through the interface of this module, and fills out these
    !  arrays.
    !
    !  Version 01: - Reads ATOMIC masses from Audi Wapstra.
    !              - The electronic binding energy is removed in this
    !                routine but is present in the data contained in the
    !                file DataSet01.dat.
    !
    !  Version 02: - Reads NUCLEAR masses from a table that is a mix
    !                of Audi-Wapstra 2003 and new Jyvaskyla masses.
    !                The mass of a given nuclide is taken as the
    !                weighted average of the original Audi-Wapstra
    !                evaluation and the Jyvaskyla mass, see
    !
    !               J.R. Taylor, An Introduction to Error Analysis
    !               2nd Ed., University Science Books, 1997
    !
    !              - Electronic correction has been removed from the
    !                data contained in table DataSet02.dat. Also a bug
    !                relative to deltaVpn data has been fixed.
    !
    !  Version 03: - Adds proton radius for spherical nuclei.
    !              - Adds experimental error in binding energy of
    !                spherical nuclei
    !              - Adds flags for deformed nuclei, delta^(3)_n and
    !                delta^(3)_p, and odd g.s.,which indicate if the
    !                corresponding masses have been measured (1) or
    !                evaluated (0).
    !
    !  Version 04: - Adds rough estimate of axial deformation of SD states
    !              - Adds one nucleus in the list of SD states
    !
    !
    !                        ------------------
    !
    !  Spherical nuclei:
    !    - IZsphe, INsphe: proton number Z and neutron number N
    !    - Bsphe: experimental binding energy
    !    - dBsphe: experimental error in binding energy
    !    - R0sphe: experimental diffraction radius
    !    - SIGsphe: experimental surface thickness
    !    - RMSspheCharge: experimental r.m.s charge radius
    !    - RMSspheProton: r.m.s proton radius computed from the charge radius
    !
    !  Deformed nuclei:
    !    - IZdefo, INdefo: proton number Z and neutron number N
    !    - Bdefo: experimental binding energy
    !    - dBdefo: experimental error in binding energy
    !    - b2defo: beta_2 value of g.s. quadrupole deformation (SLY4 calculation)
    !    - IsOKdefo: status of binding energy: 1 = measured, 0 = evaluated
     !
    !  Odd-even mass differences:
    !    - IZd3n, INd3n: proton number and neutron number related to the
    !                    neutron odd-even mass difference
    !    - DELd3n, ERRd3n: delta3 (neutrons) and relative error
    !    - IsOKd3n: status of binding energy: 1 = measured, 0 = evaluated
    !    - IZd3p, INd3p: proton number and neutron number related to the
    !                    proton odd-even mass difference
    !    - DELd3p, ERRd3p: delta3 (protons) and relative error
     !   - IsOKd3p: status of binding energy: 1 = measured, 0 = evaluated
    !
    !  Super-deformed states and fission isomers:
    !    - IZsupd, INsupd: proton number Z and neutron number N
    !    - Bsupd: experimental binding energy
    !    - ESDsupd: energy of the SD bandhead or fission isomer
    !    - b2supd: rough estimate of the beta_2 value of the SD state
    !
    !  Giant monopole resonance
    !    - IZmono, INmono: proton number Z and neutron number N
    !    - Emono: experimental energy
    !
    !  Giant dipole resonance
    !    - IZdipo, INdipo: proton number Z and neutron number N
    !    - Emdipo: experimental energy
    !
    !  Odd-mass nuclei:
    !    - IZodd, INodd: proton number Z and neutron number N
    !    - SPINodd: experimental g.s. spin
    !    - IPodd: experimental g.s. parity
    !    - IsOKodd: status of binding energy: 1 = measured, 0 = evaluated
    !
    !  One quasi-particle state in Odd-mass superheavy nuclei:
    !    - IZqpSH, INqpSH: proton number Z and neutron number N
    !    - NQPqpSH: number of q.p. states
    !    - EqpSH: experimental excitation energy
    !    - LABqpSH: experimental Nilsson label
    !    - SPINqpSH: experimental spin
    !    - IPqpSH: experimental parity
    !
    !  Position of the first 2+ state
    !    - IZtwop, INtwop: proton number Z and neutron number N
    !    - Etwop: experimental energy of the 2+ state
    !    - dEtwop: error bar on the energy
    !    - BE2twop: experimental BE2
    !    - dBE2twop: error bar on the BE2
    !
    !  Delta Vpn
    !    - IZdvpn, INdvpn: proton number Z and neutron number N
    !    - ExcMASdvpn: Mass excess
    !    - ExcERRdvpn: Error on mass excess
    !    - BnucMASdvpn: binding energy per nucleon B/A
    !    - BnucERRdvpn: error (in %) on B/A
    !    - DelVPNdvpn: delta Vpn
    !    - DelERRdvpn: error on delta Vpn
    !
    !  Terminating states:
    !    - IZterm, INterm: proton number Z and neutron number N
    !    - SPINterm, IP1term: spin Imax and parity for the f7/2 state
    !    - Eterm: energy of the f7/2 state
    !    - SPINdEterm, IP2term: spin Imax and parity for the d3/2^(-1)*f7/2 state
    !    - dEterm: experimental energy difference between the two configurations
    !
    !  IMPORTANT REMARK
    !
    !      Experimental binding energies were extracted from Audi-Wapstra
    !      mass tables. BY DEFINITION, THEY DO INCLUDE A CONTRIBUTION FROM
    !      THE BINDING ENERGY OF THE ELECTRONS. To cancel out this effect
    !      and obtain the true NUCLEAR binding energy, a correction is added
    !      systematically, which goes (in MeV) as
    !
    !                CorrELEC * Z^(2.39), CorrELEC = 1.433.10^(-5)
    !

    SUBROUTINE GetData()

    INTEGER :: file_error, file_unit
    INTEGER :: i, j, PARdummy

    DOUBLE PRECISION :: Edummy, SPINdummy

    CHARACTER (LEN=8) :: Keyword
    CHARACTER (LEN=5) :: LABdummy

    OPEN (file_unit, FILE="DataSet04.dat", ACTION="READ", IOSTAT=file_error)
    IF (file_error .NE. 0) STOP "Impossible to read: ./DataSet04.dat"

    Keyword = "Initialization"

    ! Scanning of the database proceeds by keywords

    DO WHILE (Keyword .NE. "END_DATA")

        READ (file_unit,*) Keyword

        IF (Keyword == "SPHERICA") THEN

            READ (file_unit,*) NUMsphe

            IF (.NOT. ALLOCATED (IZsphe)) ALLOCATE (IZsphe(1:NUMsphe))
            IF (.NOT. ALLOCATED (INsphe)) ALLOCATE (INsphe(1:NUMsphe))
            IF (.NOT. ALLOCATED (Bsphe)) ALLOCATE (Bsphe(1:NUMsphe))
            IF (.NOT. ALLOCATED (dBsphe)) ALLOCATE (dBsphe(1:NUMsphe))
            IF (.NOT. ALLOCATED (R0sphe)) ALLOCATE (R0sphe(1:NUMsphe))
            IF (.NOT. ALLOCATED (SIGsphe)) ALLOCATE (SIGsphe(1:NUMsphe))
            IF (.NOT. ALLOCATED (RMSspheCharge)) ALLOCATE (RMSspheCharge(1:NUMsphe))
            IF (.NOT. ALLOCATED (RMSspheProton)) ALLOCATE (RMSspheProton(1:NUMsphe))

            DO i=1, NUMsphe
                READ (file_unit,*) IZsphe(i),INsphe(i),Bsphe(i),dBsphe(i), &
                                   R0sphe(i),SIGsphe(i),RMSspheCharge(i),RMSspheProton(i)
            END DO

        END IF

        IF (Keyword == "DEFORMED") THEN

            READ (file_unit,*) NUMdefo

            IF (.NOT. ALLOCATED (IZdefo)) ALLOCATE (IZdefo(1:NUMdefo))
            IF (.NOT. ALLOCATED (INdefo)) ALLOCATE (INdefo(1:NUMdefo))
            IF (.NOT. ALLOCATED (Bdefo)) ALLOCATE (Bdefo(1:NUMdefo))
            IF (.NOT. ALLOCATED (dBdefo)) ALLOCATE (dBdefo(1:NUMdefo))
            IF (.NOT. ALLOCATED (b2defo)) ALLOCATE (b2defo(1:NUMdefo))
            IF (.NOT. ALLOCATED (IsOKdefo)) ALLOCATE (IsOKdefo(1:NUMdefo))

            DO i=1, NUMdefo
                READ (file_unit,*) IZdefo(i),INdefo(i),Bdefo(i),dBdefo(i),b2defo(i),IsOKdefo(i)
            END DO

        END IF

        IF (Keyword == "DELTA3_N") THEN

            READ (file_unit,*) NUMd3n

            IF (.NOT. ALLOCATED (IZd3n)) ALLOCATE (IZd3n(1:NUMd3n))
            IF (.NOT. ALLOCATED (INd3n)) ALLOCATE (INd3n(1:NUMd3n))
            IF (.NOT. ALLOCATED (DELd3n)) ALLOCATE (DELd3n(1:NUMd3n))
            IF (.NOT. ALLOCATED (ERRd3n)) ALLOCATE (ERRd3n(1:NUMd3n))
            IF (.NOT. ALLOCATED (IsOKd3n)) ALLOCATE (IsOKd3n(1:NUMd3n))

            DO i=1, NUMd3n
                READ (file_unit,*) IZd3n(i),INd3n(i),DELd3n(i),ERRd3n(i),IsOKd3n(i)
            END DO

        END IF

        IF (Keyword == "DELTA3_P") THEN

            READ (file_unit,*) NUMd3p

            IF (.NOT. ALLOCATED (IZd3p)) ALLOCATE (IZd3p(1:NUMd3p))
            IF (.NOT. ALLOCATED (INd3p)) ALLOCATE (INd3p(1:NUMd3p))
            IF (.NOT. ALLOCATED (DELd3p)) ALLOCATE (DELd3p(1:NUMd3p))
            IF (.NOT. ALLOCATED (ERRd3p)) ALLOCATE (ERRd3p(1:NUMd3p))
            IF (.NOT. ALLOCATED (IsOKd3p)) ALLOCATE (IsOKd3p(1:NUMd3p))

            DO i=1, NUMd3p
                READ (file_unit,*) INd3p(i),IZd3p(i),DELd3p(i),ERRd3p(i),IsOKd3p(i)
            END DO

        END IF

        IF (Keyword == "SDSTATES") THEN

            READ (file_unit,*) NUMsupd

            IF (.NOT. ALLOCATED (IZsupd)) ALLOCATE (IZsupd(1:NUMsupd))
            IF (.NOT. ALLOCATED (INsupd)) ALLOCATE (INsupd(1:NUMsupd))
            IF (.NOT. ALLOCATED (Bsupd)) ALLOCATE (Bsupd(1:NUMsupd))
            IF (.NOT. ALLOCATED (ESDsupd)) ALLOCATE (ESDsupd(1:NUMsupd))
            IF (.NOT. ALLOCATED (b2supd)) ALLOCATE (b2supd(1:NUMsupd))

            DO i=1, NUMsupd
                READ (file_unit,*) IZsupd(i),INsupd(i),Bsupd(i),ESDsupd(i), b2supd(i)
            END DO

        END IF

        IF (Keyword == "MONOPRES") THEN

            READ (file_unit,*) NUMmono

            IF (.NOT. ALLOCATED (IZmono)) ALLOCATE (IZmono(1:NUMmono))
            IF (.NOT. ALLOCATED (INmono)) ALLOCATE (INmono(1:NUMmono))
            IF (.NOT. ALLOCATED (Emono)) ALLOCATE (Emono(1:NUMmono))
            IF (.NOT. ALLOCATED (dEmono)) ALLOCATE (dEmono(1:NUMmono))

            DO i=1, NUMmono
                READ (file_unit,*) IZmono(i),INmono(i),Emono(i),dEmono(i)
            END DO

        END IF

        IF (Keyword == "DIPOLRES") THEN

            READ (file_unit,*) NUMdipo

            IF (.NOT. ALLOCATED (IZdipo)) ALLOCATE (IZdipo(1:NUMdipo))
            IF (.NOT. ALLOCATED (INdipo)) ALLOCATE (INdipo(1:NUMdipo))
            IF (.NOT. ALLOCATED (Edipo)) ALLOCATE (Edipo(1:NUMdipo))

            DO i=1, NUMdipo
                READ (file_unit,*) IZdipo(i),INdipo(i),Edipo(i)
            END DO

        END IF

        IF (Keyword == "ODDNUCLE") THEN

            READ (file_unit,*) NUModd

            IF (.NOT. ALLOCATED (IZodd)) ALLOCATE (IZodd(1:NUModd))
            IF (.NOT. ALLOCATED (INodd)) ALLOCATE (INodd(1:NUModd))
            IF (.NOT. ALLOCATED (SPINodd)) ALLOCATE (SPINodd(1:NUModd))
            IF (.NOT. ALLOCATED (IPodd)) ALLOCATE (IPodd(1:NUModd))
            IF (.NOT. ALLOCATED (IsOKodd)) ALLOCATE (IsOKodd(1:NUModd))

            DO i=1, NUModd
                READ (file_unit,*) IZodd(i),INodd(i),SPINodd(i),IPodd(i),IsOKodd(i)
            END DO

        END IF

        IF (Keyword == "QPSHELEM") THEN

            READ (file_unit,*) NUMqpSH

            IF (.NOT. ALLOCATED (IZqpSH)) ALLOCATE (IZqpSH(1:NUMqpSH))
            IF (.NOT. ALLOCATED (INqpSH)) ALLOCATE (INqpSH(1:NUMqpSH))
            IF (.NOT. ALLOCATED (NQPqpSH)) ALLOCATE (NQPqpSH(1:NUMqpSH))
            IF (.NOT. ALLOCATED (EqpSH)) ALLOCATE (EqpSH(1:NUMqpSH,1:NDQPSH))
            IF (.NOT. ALLOCATED (LABqpSH)) ALLOCATE (LABqpSH(1:NUMqpSH,1:NDQPSH))
            IF (.NOT. ALLOCATED (SPINqpSH)) ALLOCATE (SPINqpSH(1:NUMqpSH,1:NDQPSH))
            IF (.NOT. ALLOCATED (IPqpSH)) ALLOCATE (IPqpSH(1:NUMqpSH,1:NDQPSH))

            DO i=1, NUMqpSH

                READ (file_unit,*) IZqpSH(i),INqpSH(i),NQPqpSH(i),EqpSH(i,1),LABqpSH(i,1),SPINqpSH(i,1),IPqpSH(i,1)

                DO j=2,NQPqpSH(i)
                   READ (file_unit,*) EqpSH(i,j),LABqpSH(i,j),SPINqpSH(i,j),IPqpSH(i,j)
                END DO

            END DO

        END IF

        IF (Keyword == "2+ENERGY") THEN

            READ (file_unit,*) NUMtwop

            IF (.NOT. ALLOCATED (IZtwop)) ALLOCATE (IZtwop(1:NUMtwop))
            IF (.NOT. ALLOCATED (INtwop)) ALLOCATE (INtwop(1:NUMtwop))
            IF (.NOT. ALLOCATED (Etwop)) ALLOCATE (Etwop(1:NUMtwop))
            IF (.NOT. ALLOCATED (dEtwop)) ALLOCATE (dEtwop(1:NUMtwop))
            IF (.NOT. ALLOCATED (BE2twop)) ALLOCATE (BE2twop(1:NUMtwop))
            IF (.NOT. ALLOCATED (dBE2twop)) ALLOCATE (dBE2twop(1:NUMtwop))

            DO i=1, NUMtwop
                READ (file_unit,*) IZtwop(i),INtwop(i),Etwop(i),dEtwop(i),BE2twop(i),dBE2twop(i)
            END DO

        END IF

        IF (Keyword == "DELTAVPN") THEN

            READ (file_unit,*) NUMdvpn

            IF (.NOT. ALLOCATED (IZdvpn)) ALLOCATE (IZdvpn(1:NUMdvpn))
            IF (.NOT. ALLOCATED (INdvpn)) ALLOCATE (INdvpn(1:NUMdvpn))
            IF (.NOT. ALLOCATED (ExcMASdvpn)) ALLOCATE (ExcMASdvpn(1:NUMdvpn))
            IF (.NOT. ALLOCATED (ExcERRdvpn)) ALLOCATE (ExcERRdvpn(1:NUMdvpn))
            IF (.NOT. ALLOCATED (BnucMASdvpn)) ALLOCATE (BnucMASdvpn(1:NUMdvpn))
            IF (.NOT. ALLOCATED (BnucERRdvpn)) ALLOCATE (BnucERRdvpn(1:NUMdvpn))
            IF (.NOT. ALLOCATED (DelVPNdvpn)) ALLOCATE (DelVPNdvpn(1:NUMdvpn))
            IF (.NOT. ALLOCATED (DelERRdvpn)) ALLOCATE (DelERRdvpn(1:NUMdvpn))

            DO i=1, NUMdvpn
                READ (file_unit,*) IZdvpn(i),INdvpn(i),ExcMASdvpn(i),ExcERRdvpn(i),BnucMASdvpn(i),BnucERRdvpn(i),DelVPNdvpn(i),DelERRdvpn(i)
            END DO

        END IF

        IF (Keyword == "TERMINAT") THEN

            READ (file_unit,*) NUMterm

            IF (.NOT. ALLOCATED (IZterm)) ALLOCATE (IZterm(1:NUMterm))
            IF (.NOT. ALLOCATED (INterm)) ALLOCATE (INterm(1:NUMterm))
            IF (.NOT. ALLOCATED (SPINterm)) ALLOCATE (SPINterm(1:NUMterm))
            IF (.NOT. ALLOCATED (IP1term)) ALLOCATE (IP1term(1:NUMterm))
            IF (.NOT. ALLOCATED (Eterm)) ALLOCATE (Eterm(1:NUMterm))
            IF (.NOT. ALLOCATED (SPINdEterm)) ALLOCATE (SPINdEterm(1:NUMterm))
            IF (.NOT. ALLOCATED (IP2term)) ALLOCATE (IP2term(1:NUMterm))
            IF (.NOT. ALLOCATED (dEterm)) ALLOCATE (dEterm(1:NUMterm))

            DO i=1, NUMterm
                READ (file_unit,*) IZterm(i),INterm(i),SPINterm(i),IP1term(i),Eterm(i),SPINdEterm(i),IP2term(i),dEterm(i)
            END DO

        END IF

    END DO

    CLOSE (file_unit)

    RETURN
    END SUBROUTINE GetData

    ! This subroutine only prints the data so that the user can verify that everything has
    ! been read properly.

    SUBROUTINE PrintData()

    INTEGER :: i, j
    CHARACTER (LEN=8) :: Keyword

    Keyword = "SPHERICA"
    WRITE (*,'(A8)') Keyword
    WRITE (*,'(9X,I5)') NUMsphe

    DO i=1, NUMsphe
       WRITE (*,'(9X,2I5,1X,6F11.5)') IZsphe(i),INsphe(i),Bsphe(i),dBsphe(i),R0sphe(i),SIGsphe(i),&
                                      RMSspheCharge(i),RMSspheProton(i)
    END DO

    Keyword = "DEFORMED"
    WRITE (6,'(A8)') Keyword
    WRITE (6,'(10X,I5)') NUMdefo

    DO i=1, NUMdefo
       WRITE (6,'(9X,2I5,F12.5,2F11.5,i4)') IZdefo(i),INdefo(i),Bdefo(i),dBdefo(i),b2defo(i),IsOKdefo(i)
    END DO

    Keyword = "DELTA3_N"
    WRITE (6,'(A8)') Keyword
    WRITE (6,'(10X,I5)') NUMd3n

    DO i=1, NUMd3n
       WRITE (6,'(9X,2I5,2F12.6,i4)') IZd3n(i),INd3n(i),DELd3n(i),ERRd3n(i),IsOKd3n(i)
    END DO

    Keyword = "DELTA3_P"
    WRITE (6,'(A8)') Keyword
    WRITE (6,'(10X,I5)') NUMd3p

    DO i=1, NUMd3p
       WRITE (6,'(9X,2I5,2F12.6,i4)') INd3p(i),IZd3p(i),DELd3p(i),ERRd3p(i),IsOKd3p(i)
    END DO

    Keyword = "SDSTATES"
    WRITE (*,'(A8)') Keyword
    WRITE (*,'(9X,I5)') NUMsupd

    DO i=1, NUMsupd
       WRITE (*,'(9X,2I5,F12.5,F9.3,F9.3)') IZsupd(i),INsupd(i),Bsupd(i),ESDsupd(i),b2supd(i)
    END DO

    Keyword = "MONOPRES"
    WRITE (*,'(A8)') Keyword
    WRITE (*,'(9X,I5)') NUMmono

    DO i=1, NUMmono
       WRITE (*,'(9X,2I5,1X,F9.2,F10.2)') IZmono(i),INmono(i),Emono(i),dEmono(i)
    END DO

    Keyword = "DIPOLRES"
    WRITE (*,'(A8)') Keyword
    WRITE (*,'(9X,I5)') NUMdipo

    DO i=1, NUMdipo
       WRITE (*,'(9X,2I5,1X,F9.2)') IZdipo(i),INdipo(i),Edipo(i)
    END DO

    Keyword = "ODDNUCLE"
    WRITE (*,'(A8)') Keyword
    WRITE (*,'(9X,I5)') NUModd

    DO i=1, NUModd
       WRITE (*,'(9X,2I5,F6.1,I5,i4)') IZodd(i),INodd(i),SPINodd(i),IPodd(i),IsOKodd(i)
    END DO

    Keyword = "QPSHELEM"
    WRITE (*,'(A8)') Keyword
    WRITE (*,'(9X,I5)') NUMqpSH

    DO i=1, NUMqpSH
       WRITE (*,'(9X,2I5,I4,F10.5,4X,A5,F8.1,5X,I2)') IZqpSH(i),INqpSH(i),NQPqpSH(i),EqpSH(i,1),LABqpSH(i,1),SPINqpSH(i,1),IPqpSH(i,1)
       DO j=2,NQPqpSH(i)
          WRITE (*,'(23X,F10.5,4X,A5,F8.1,5X,I2)') EqpSH(i,j),LABqpSH(i,j),SPINqpSH(i,j),IPqpSH(i,j)
       END DO
    END DO

    Keyword = "2+ENERGY"
    WRITE (*,'(A8)') Keyword
    WRITE (*,'(9X,I5)') NUMtwop

    DO i=1, NUMtwop
       WRITE (*,'(9X,2I5,4F11.5)') IZtwop(i),INtwop(i),Etwop(i),dEtwop(i),BE2twop(i),dBE2twop(i)
    END DO

    Keyword = "DELTAVPN"
    WRITE (*,'(A8)') Keyword
    WRITE (*,'(9X,I5)') NUMdvpn

    DO i=1, NUMdvpn
       WRITE (*,'(9X,2I5,F12.1,F10.1,F15.2,F10.2,F14.4,F12.4)') &
                  IZdvpn(i),INdvpn(i),ExcMASdvpn(i),ExcERRdvpn(i),BnucMASdvpn(i),BnucERRdvpn(i),DelVPNdvpn(i),DelERRdvpn(i)
    END DO

    Keyword = "TERMINAT"
    WRITE (*,'(A8)') Keyword
    WRITE (*,'(9X,I5)') NUMterm

    DO i=1, NUMterm
       WRITE (*,'(9X,2I5,F9.1,I10,F12.3,F8.1,I8,F9.3)') IZterm(i),INterm(i),SPINterm(i),IP1term(i),Eterm(i),SPINdEterm(i),IP2term(i),dEterm(i)
    END DO

    RETURN
    END SUBROUTINE PrintData

END MODULE input
