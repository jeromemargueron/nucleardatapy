#
# EOS from Gandolfi, Carlson, Reddy, PRC 85, (2012)
#
# This is named with a at the end, because I expect to calculate
# the same thing for the other fit given in the paper.
# To be done...


# remove files
system("rm EP_GCR_sat.dat")
system("rm EP_GCR_NM.dat")


# variables
nsat=0.16
Esata=-15.5
Esatb=-16.5
Ksata=210
Ksatb=250


print "     Esat  Esym  Lsym  Ksat    Ksym"

# °°°°°°°°
#1: EOS 
# °°°°°°°°
#1 V2pi
a_1=12.7
alp_1=0.49
b_1=1.78
bet_1=2.26
#
# energy per nucleons
e2a_1(n)=a_1*(n/nsat)**alp_1+b_1*(n/nsat)**bet_1
#
# pressure                   
p_1(n)=n**2/nsat*( a_1*alp_1*(n/nsat)**(alp_1-1) + b_1*bet_1*(n/nsat)**(bet_1-1) )
#
eNM_1=a_1+b_1
lsym_1=3*( a_1*alp_1 + b_1*bet_1 )
kNM_1=9*( a_1*alp_1*(alp_1-1) + b_1*bet_1*(bet_1-1) )
qNM_1=9*( a_1*alp_1*(alp_1-1)*(alp_1-2) + b_1*bet_1*(bet_1-1)*(bet_1-2) )
zNM_1=9*( a_1*alp_1*(alp_1-1)*(alp_1-2)*(alp_1-3) + b_1*bet_1*(bet_1-1)*(bet_1-2)*(bet_1-3) )
#
Esyma=eNM_1-Esata
Esymb=eNM_1-Esatb
Ksyma=kNM_1-Ksata
Ksymb=kNM_1-Ksatb
#
#ktau_1=ksym_2-6*lsym_2-qsat_2*lsym_2/ksat_2
#
res_1NMa=sprintf("1a: %.2f %.2f %.1f %.0f %.0f",Esata,Esyma,lsym_1,Ksata,Ksyma)
res_1NMb=sprintf("1b: %.2f %.2f %.1f %.0f %.0f",Esatb,Esymb,lsym_1,Ksatb,Ksymb)
res_1NMc=sprintf("1c: %.2f %.1f %.0f %.0f %.0f",eNM_1,lsym_1,kNM_1,qNM_1,zNM_1)
print res_1NMa
print res_1NMb


# °°°°°°°°
#2: EOS
# °°°°°°°°
#2
a_2=12.7
alp_2=0.48
b_2=3.45
bet_2=2.12
#
# energy per nucleons
e2a_2(n)=a_2*(n/nsat)**alp_2+b_2*(n/nsat)**bet_2
#
# pressure                   
p_2(n)=n**2/nsat*( a_2*alp_2*(n/nsat)**(alp_2-1) + b_2*bet_2*(n/nsat)**(bet_2-1) )
#
eNM_2=a_2+b_2
lsym_2=3*( a_2*alp_2 + b_2*bet_2 )
kNM_2=9*( a_2*alp_2*(alp_2-1) + b_2*bet_2*(bet_2-1) )
qNM_2=9*( a_2*alp_2*(alp_2-1)*(alp_2-2) + b_2*bet_2*(bet_2-1)*(bet_2-2) )
zNM_2=9*( a_2*alp_2*(alp_2-1)*(alp_2-2)*(alp_2-3) + b_2*bet_2*(bet_2-1)*(bet_2-2)*(bet_2-3) )
#
Esyma=eNM_2-Esata
Esymb=eNM_2-Esatb
Ksyma=kNM_2-Ksata
Ksymb=kNM_2-Ksatb
#
#ktau_2=ksym_2-6*lsym_2-qsat_2*lsym_2/ksat_2
#
res_2NMa=sprintf("2a: %.2f %.2f %.1f %.0f %.0f",Esata,Esyma,lsym_2,Ksata,Ksyma)
res_2NMb=sprintf("2b: %.2f %.2f %.1f %.0f %.0f",Esatb,Esymb,lsym_2,Ksatb,Ksymb)
res_2NMc=sprintf("2c: %.2f %.1f %.0f %.0f %.0f",eNM_2,lsym_2,kNM_2,qNM_2,zNM_2)
print res_2NMa
print res_2NMb



# °°°°°°°°
#3: EOS
# °°°°°°°°
#3
a_3=12.8
alp_3=0.488
b_3=3.19
bet_3=2.20
#
# energy per nucleons
e2a_3(n)=a_3*(n/nsat)**alp_3+b_3*(n/nsat)**bet_3
#
# pressure                   
p_3(n)=n**2/nsat*( a_3*alp_3*(n/nsat)**(alp_3-1) + b_3*bet_3*(n/nsat)**(bet_3-1) )
#
eNM_3=a_3+b_3
lsym_3=3*( a_3*alp_3 + b_3*bet_3 )
kNM_3=9*( a_3*alp_3*(alp_3-1) + b_3*bet_3*(bet_3-1) )
qNM_3=9*( a_3*alp_3*(alp_3-1)*(alp_3-2) + b_3*bet_3*(bet_3-1)*(bet_3-2) )
zNM_3=9*( a_3*alp_3*(alp_3-1)*(alp_3-2)*(alp_3-3) + b_3*bet_3*(bet_3-1)*(bet_3-2)*(bet_3-3) )
#
Esyma=eNM_3-Esata
Esymb=eNM_3-Esatb
Ksyma=kNM_3-Ksata
Ksymb=kNM_3-Ksatb
#
#ktau_3=ksym_2-6*lsym_2-qsat_2*lsym_2/ksat_2
#
res_3NMa=sprintf("3a: %.2f %.2f %.1f %.0f %.0f",Esata,Esyma,lsym_3,Ksata,Ksyma)
res_3NMb=sprintf("3b: %.2f %.2f %.1f %.0f %.0f",Esatb,Esymb,lsym_3,Ksatb,Ksymb)
res_3NMc=sprintf("3c: %.2f %.1f %.0f %.0f %.0f",eNM_3,lsym_3,kNM_3,qNM_3,zNM_3)
print res_3NMa
print res_3NMb

# °°°°°°°°
#4: EOS
# °°°°°°°°
#4
a_4=13.0
alp_4=0.49
b_4=3.21
bet_4=2.47
#
# energy per nucleons
e2a_4(n)=a_4*(n/nsat)**alp_4+b_4*(n/nsat)**bet_4
#
# pressure                   
p_4(n)=n**2/nsat*( a_4*alp_4*(n/nsat)**(alp_4-1) + b_4*bet_4*(n/nsat)**(bet_4-1) )
#
eNM_4=a_4+b_4
lsym_4=3*( a_4*alp_4 + b_4*bet_4 )
kNM_4=9*( a_4*alp_4*(alp_4-1) + b_4*bet_4*(bet_4-1) )
qNM_4=9*( a_4*alp_4*(alp_4-1)*(alp_4-2) + b_4*bet_4*(bet_4-1)*(bet_4-2) )
zNM_4=9*( a_4*alp_4*(alp_4-1)*(alp_4-2)*(alp_4-3) + b_4*bet_4*(bet_4-1)*(bet_4-2)*(bet_4-3) )
#
Esyma=eNM_4-Esata
Esymb=eNM_4-Esatb
Ksyma=kNM_4-Ksata
Ksymb=kNM_4-Ksatb
#
#ktau_4=ksym_2-6*lsym_2-qsat_2*lsym_2/ksat_2
#
res_4NMa=sprintf("4a: %.2f %.2f %.1f %.0f %.0f",Esata,Esyma,lsym_4,Ksata,Ksyma)
res_4NMb=sprintf("4b: %.2f %.2f %.1f %.0f %.0f",Esatb,Esymb,lsym_4,Ksatb,Ksymb)
res_4NMc=sprintf("4c: %.2f %.1f %.0f %.0f %.0f",eNM_4,lsym_4,kNM_4,qNM_4,zNM_4)
print res_4NMa
print res_4NMb

# °°°°°°°°
#5: EOS
# °°°°°°°°
#5
a_5=12.6
alp_5=0.475
b_5=5.16
bet_5=2.12
#
# energy per nucleons
e2a_5(n)=a_5*(n/nsat)**alp_5+b_5*(n/nsat)**bet_5
#
# pressure                   
p_5(n)=n**2/nsat*( a_5*alp_5*(n/nsat)**(alp_5-1) + b_5*bet_5*(n/nsat)**(bet_5-1) )
#
eNM_5=a_5+b_5
lsym_5=3*( a_5*alp_5 + b_5*bet_5 )
kNM_5=9*( a_5*alp_5*(alp_5-1) + b_5*bet_5*(bet_5-1) )
qNM_5=9*( a_5*alp_5*(alp_5-1)*(alp_5-2) + b_5*bet_5*(bet_5-1)*(bet_5-2) )
zNM_5=9*( a_5*alp_5*(alp_5-1)*(alp_5-2)*(alp_5-3) + b_5*bet_5*(bet_5-1)*(bet_5-2)*(bet_5-3) )
#
Esyma=eNM_5-Esata
Esymb=eNM_5-Esatb
Ksyma=kNM_5-Ksata
Ksymb=kNM_5-Ksatb
#
#ktau_5=ksym_2-6*lsym_2-qsat_2*lsym_2/ksat_2
#
res_5NMa=sprintf("5a: %.2f %.2f %.1f %.0f %.0f",Esata,Esyma,lsym_5,Ksata,Ksyma)
res_5NMb=sprintf("5b: %.2f %.2f %.1f %.0f %.0f",Esatb,Esymb,lsym_5,Ksatb,Ksymb)
res_5NMc=sprintf("5c: %.2f %.1f %.0f %.0f %.0f",eNM_5,lsym_5,kNM_5,qNM_5,zNM_5)
print res_5NMa
print res_5NMb


# °°°°°°°°
#6: EOS
# °°°°°°°°
#6
a_6=13.0
alp_6=0.50
b_6=4.71
bet_6=2.49
#
# energy per nucleons
e2a_6(n)=a_6*(n/nsat)**alp_6+b_6*(n/nsat)**bet_6
#
# pressure                   
p_6(n)=n**2/nsat*( a_6*alp_6*(n/nsat)**(alp_6-1) + b_6*bet_6*(n/nsat)**(bet_6-1) )
#
eNM_6=a_6+b_6
lsym_6=3*( a_6*alp_6 + b_6*bet_6 )
kNM_6=9*( a_6*alp_6*(alp_6-1) + b_6*bet_6*(bet_6-1) )
qNM_6=9*( a_6*alp_6*(alp_6-1)*(alp_6-2) + b_6*bet_6*(bet_6-1)*(bet_6-2) )
zNM_6=9*( a_6*alp_6*(alp_6-1)*(alp_6-2)*(alp_6-3) + b_6*bet_6*(bet_6-1)*(bet_6-2)*(bet_6-3) )
#
Esyma=eNM_6-Esata
Esymb=eNM_6-Esatb
Ksyma=kNM_6-Ksata
Ksymb=kNM_6-Ksatb
#
#ktau_6=ksym_2-6*lsym_2-qsat_2*lsym_2/ksat_2
#
res_6NMa=sprintf("6a: %.2f %.2f %.1f %.0f %.0f",Esata,Esyma,lsym_6,Ksata,Ksyma)
res_6NMb=sprintf("6b: %.2f %.2f %.1f %.0f %.0f",Esatb,Esymb,lsym_6,Ksatb,Ksymb)
res_6NMc=sprintf("6c: %.2f %.1f %.0f %.0f %.0f",eNM_6,lsym_6,kNM_6,qNM_6,zNM_6)
print res_6NMa
print res_6NMb



# °°°°°°°°
#7: EOS
# °°°°°°°°
#7
a_7=13.4
alp_7=0.514
b_7=5.62
bet_7=2.436
#
# energy per nucleons
e2a_7(n)=a_7*(n/nsat)**alp_7+b_7*(n/nsat)**bet_7
#
# pressure                   
p_7(n)=n**2/nsat*( a_7*alp_7*(n/nsat)**(alp_7-1) + b_7*bet_7*(n/nsat)**(bet_7-1) )
#
eNM_7=a_7+b_7
lsym_7=3*( a_7*alp_7 + b_7*bet_7 )
kNM_7=9*( a_7*alp_7*(alp_7-1) + b_7*bet_7*(bet_7-1) )
qNM_7=9*( a_7*alp_7*(alp_7-1)*(alp_7-2) + b_7*bet_7*(bet_7-1)*(bet_7-2) )
zNM_7=9*( a_7*alp_7*(alp_7-1)*(alp_7-2)*(alp_7-3) + b_7*bet_7*(bet_7-1)*(bet_7-2)*(bet_7-3) )
#
Esyma=eNM_7-Esata
Esymb=eNM_7-Esatb
Ksyma=kNM_7-Ksata
Ksymb=kNM_7-Ksatb
#
#ktau_7=ksym_2-6*lsym_2-qsat_2*lsym_2/ksat_2
#
res_7NMa=sprintf("7a: %.2f %.2f %.1f %.0f %.0f",Esata,Esyma,lsym_7,Ksata,Ksyma)
res_7NMb=sprintf("7b: %.2f %.2f %.1f %.0f %.0f",Esatb,Esymb,lsym_7,Ksatb,Ksymb)
res_7NMc=sprintf("7c: %.2f %.1f %.0f %.0f %.0f",eNM_7,lsym_7,kNM_7,qNM_7,zNM_7)
print res_7NMa
print res_7NMb



# °°°°°°°°°°°°°°°°°
# Analyse the files
# °°°°°°°°°°°°°°°°°
#
# properties at saturation density
#
set print "EP_GCR_sat.dat" append
print "#    Esat  Esym  nsat   Lsym  Ksat  Ksym"
print res_1NMa
print res_1NMb
print res_2NMa
print res_2NMb
print res_3NMa
print res_3NMb
print res_4NMa
print res_4NMb
print res_5NMa
print res_5NMb
print res_6NMa
print res_6NMb
print res_7NMa
print res_7NMb
unset print

stats "EP_GCR_sat.dat" u 2 prefix "Esat" nooutput
stats "EP_GCR_sat.dat" u 3 prefix "Esym" nooutput
stats "EP_GCR_sat.dat" u 4 prefix "Lsym" nooutput
stats "EP_GCR_sat.dat" u 5 prefix "Ksat" nooutput
stats "EP_GCR_sat.dat" u 6 prefix "Ksym" nooutput

res_sat1=sprintf("mean:   %.2f %.2f %.1f %.0f %.0f",Esat_mean,Esym_mean,Lsym_mean,Ksat_mean,Ksym_mean)
print res_sat1
res_sat2=sprintf("stddev:   %.2f  %.2f  %.1f  %.0f  %.0f",Esat_stddev,Esym_stddev,Lsym_stddev,Ksat_stddev,Ksym_stddev)
print res_sat2
res_sat3=sprintf("min:    %.2f %.2f %.1f %.0f %.0f",Esat_min,Esym_min,Lsym_min,Ksat_min,Ksym_min)
print res_sat3
res_sat4=sprintf("max:    %.2f %.2f %.1f %.0f %.0f",Esat_max,Esym_max,Lsym_max,Ksat_max,Ksym_max)
print res_sat4

set print "EP_GCR_sat.dat" append
print ""
print res_sat1
print res_sat2
print res_sat3

print res_sat4
unset print


set print "EP_GCR_NM.dat" append
print "#    ENM  Lsym  KNM  QNM  ZNM"
print res_1NMc
print res_2NMc
print res_3NMc
print res_4NMc
print res_5NMc
print res_6NMc
print res_7NMc
unset print

stats "EP_GCR_NM.dat" u 2 prefix "ENM" nooutput
stats "EP_GCR_NM.dat" u 3 prefix "Lsym" nooutput
stats "EP_GCR_NM.dat" u 4 prefix "KNM" nooutput
stats "EP_GCR_NM.dat" u 5 prefix "QNM" nooutput
stats "EP_GCR_NM.dat" u 6 prefix "ZNM" nooutput

res_NM1=sprintf("mean:   %.2f %.1f %.0f %.0f %.0f",ENM_mean,Lsym_mean,KNM_mean,QNM_mean,ZNM_mean)
print res_NM1
res_NM2=sprintf("stddev:   %.2f  %.1f  %.0f  %.0f  %.0f",ENM_stddev,Lsym_stddev,KNM_stddev,QNM_stddev,ZNM_stddev)
print res_NM2
res_NM3=sprintf("min:    %.2f %.1f %.0f %.0f %.0f",ENM_min,Lsym_min,KNM_min,QNM_min,ZNM_min)
print res_NM3
res_NM4=sprintf("max:    %.2f %.1f %.0f %.0f %.0f",ENM_max,Lsym_max,KNM_max,QNM_max,ZNM_max)
print res_NM4

set print "EP_GCR_NM.dat" append
print ""
print res_NM1
print res_NM2
print res_NM3
print res_NM4
unset print





# °°°°°°°°°°°°°°°°°
# Plot EOS
# °°°°°°°°°°°°°°°°°
#
set terminal pdf
set output "plot_GCR2014.pdf"

set grid xtics ytics

### Start multiplot (2x1 layout)
set multiplot layout 1,2 rowsfirst

set xrange [0.0:0.2]

# --- GRAPH a: E/A
set key top left
unset key
set ylabel "E/A (MeV)"
set xlabel "n_0 (fm^{-3})"
set yrange [0:25]
plot e2a_1(x) w l ls 11 not,\
     e2a_2(x) w l ls 12 not,\
     e2a_3(x) w l ls 13 not,\
     e2a_4(x) w l ls 14 not,\
     e2a_5(x) w l ls 15 not,\
     e2a_6(x) w l ls 16 not,\
     e2a_7(x) w l ls 17 not
# --- GRAPH c: pressure
set key top left
unset key
set ylabel "Pressure (MeV)"
set xlabel "n_0 (fm^{-3})"
set label 1 "Gandolfi et al.," at 0.01,4.2
set label 2 "PRC (2012)"     at 0.01,3.8
set yrange [0:6]
plot p_1(x) w l ls 11 not,\
     p_2(x) w l ls 12 not,\
     p_3(x) w l ls 13 not,\
     p_4(x) w l ls 14 not,\
     p_5(x) w l ls 15 not,\
     p_6(x) w l ls 16 not,\
     p_7(x) w l ls 17 not
unset label
unset multiplot
unset output