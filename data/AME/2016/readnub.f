      Program ReadNub
c                                                G.Audi       v 26 nov 2004
c  Read Masses in file amdc/nubase/nubtab03.asc
c
      real*8 qg,ug
c
      character linea*150
      character*25 filea,filec
      character cqug*20,cque*18
      filea='nubtab03.asc            '
      filec='nubtab03.mod            '
      open(unit=1,file=filea,form='formatted',status='old')
      open(unit=3,file=filec,form='formatted',status='new')
c
c
   10 read(1,1001,end=90,err=99) linea
      read(linea(1:8),'(i3,i4,i1)') iaa,iza,isa
      cqug=linea(19:38)
      if(cqug(7:7).eq.'.' .and. cqug(16:16).eq.'.') then
        read(cqug,'(f11.4,f9.4)') qg,ug
      else
        read(cqug,'(i6,5x,i4,5x)') iqg,iug
        qg=iqg
        ug=iug
      endif
      idsg=0
      if(cqug(7:7).eq.'#') idsg=1

      write(3,1020) iaa,iza,isa,qg,ug,idsg
      go to 10
c
 1001 format (a150)
 1020 format (i5,i5,i5,3x,f11.4,3x,f9.4,i5)
c
   90 write (3,1990)
 1990 format(1h0,'End of ReadNub')
      stop
   99 write(3,1999)
 1999 format(1h0,'Error in reading file')
      stop
      end
