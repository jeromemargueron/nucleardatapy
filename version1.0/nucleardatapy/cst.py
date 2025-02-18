"""
Instantiate a few constants for the nucleardatapy toolkit.
"""
#
# fundamental constants:
#
hbc  = 197.3269804 # in MeV.fm
pi = 3.141592653589793
pi2 = pi*pi
mec2 = 0.510998949 # electron mass in MeV
mmuc2= 105.6583745 # muon mass in MeV
mnc2 = 939.565346 # neutron mass in MeV
mpc2 = 938.272013 # proton mass in MeV
mnuc2 = 0.5*(mnc2 + mpc2)
mnuc2_approx = 939.0
h2m = hbc**2 / mnuc2
nsat = 0.16 # in fm-3
e = 1.602176634e-19 # electron charge in Coulomb
c = 299.792458e6 # speed of light in m s^-1
c2 = c*c
Nc = 3 # Number of colors
#
# astrophysics
#
G_cgs    = 6.67259e-8  # Grav. const in cm^3/g/s^2
G_si     = 6.67259e-11 # Grav. const in m^3/Kg/s^2
Msol_cgs = 1.99e33     # solar mass in g
Msol_si  = 1.99e30     # solar mass in Kg
Rsol_cgs = 6.96e10     # solar radius in cm
Rsol_si  = 6.96e8      # solar radius in m
rshsol_si = 2 * G_si * Msol_si / c2 # Schw. radius of the sun in m
#
# integers
#
one = 1.0
two = 2.0
three = 3.0
four = 4.0
five = 5.0
half = 0.5
third = 1.0/3.0
twoThird = 2.0/3.0
threeFifth = 3.0 / 5.0
fiveThird = 5.0 / 3.0
#
# convertion constants:
#
MeV2J = e*10**6
MeV2kg = (10**6*e)/c2
MeVfm32gcm3=10**48*e/c**2
MeVfm32dyncm2=c2*MeV2kg/10**-46

#


#class constants():
#    """
#    Instantiate a few constants for the nucleardatapy toolkit.
#    """
#    # convertion constants:

#    def __init__(self):
#        self.hbc = 197.32705 # in MeV.fm
#        self.mec2 = 0.510998928 # electron mass in MeV
#        self.mnc2 = 939.565346 # neutron mass in MeV
#        self.mpc2 = 938.272013 # proton mass in MeV
#        self.mnucc2 = 0.5*(self.mnc2 + self.mpc2)
#        self.MeV2J = 1.0545717/6.5821193*1.e-12
#        self.MeV2kg = 1.672621/939.272*1.e-27
#        self.c = 299.782458e6 # in m s^-1
#        self.c2 = c*c
#
