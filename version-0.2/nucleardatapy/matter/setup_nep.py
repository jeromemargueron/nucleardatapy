import os
import sys
import numpy as np  # 1.15.0
from scipy.interpolate import CubicSpline

#nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
#sys.path.insert(0, nucleardatapy_tk)

import nucleardatapy as nuda

def nep_models():
    """
    Return a list of models available in this toolkit and print them all on the prompt.

    :return: The list of models with can be 'Skyrme', 'GSkyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF'.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter pheno_models()")
    #
    models = [ 'Skyrme', 'GSkyrme', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF', 'xEFT' ]
    #models = [ 'Skyrme', 'GSkyrme', 'Skyrme2', 'ESkyrme', 'Gogny', 'Fayans', 'NLRH', 'DDRH', 'DDRHF', 'xEFT' ]
    #print('Phenomenological models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    #
    if nuda.env.verb: print("Exit pheno_models()")
    #
    return models, models_lower

def nep_params( model ):
    """
    Return a list with the parameterizations available in 
    this toolkit for a given model and print them all on the prompt.

    :param model: The type of model for which there are parametrizations. They should be chosen among the following options: 'Skyrme', 'NLRH', 'DDRH', 'DDRHF'.
    :type model: str.
    :return: The list of parametrizations. \
    If `models` == 'Skyrme': 'BSK14', \
        'BSK16', 'BSK17', 'BSK27', 'F-', 'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', \
        'NRAPR', 'RATP', 'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
        'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', 'SLY4', 'SLY5', \
        'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', 'UNEDF0', 'UNEDF1'. \
    If `model` == 'Skyrme2': 'SLy4', 'SkM*', 'SV-min', 'SV-bas', 'SV-K218', \
        'SV-K226', 'SV-K241', 'SV-mas07', 'SV-mas08', 'SV-mas10',\
        'SV-sym28', 'SV-sym32', 'SV-sym34', 'SV-kap00', 'SV-kap20', 'SV-kap60'. \
    If `model` == 'GSkyrme': 'SkK180', 'SkK200', 'SkK220', 'SkK240', 'SkKM'. \
    If `models` == 'ESkyrme': 'BSk22', 'BSk24', 'BSk25', 'BSk26', 'BSk31', 'BSk32', \
        'BSkG1', 'BSkG2', 'BSkG3'. \
    If `models` == 'Fayans': 'Fy(IVP)', 'Fy(Dr,HDB)', 'Fy(std)'. \
    If `models` == 'NLRH': 'NL-SH', 'NL3', 'NL3II', 'PK1', 'PK1R', 'TM1'. \
    If `models` == 'DDRH': 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99'. \
    If `models` == 'DDRHF': 'PKA1', 'PKO1', 'PKO2', 'PKO3'.
    If `models` == 'xEFT': 'H1MM', 'H2MM', 'H3MM', 'H4MM', 'H5MM', 'H6MM', 'H7MM'.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter nep_params()")
    #
    #print('For model:',model)
    if model.lower() == 'skyrme':
        params = [ 'BSK14', 'BSK16', 'BSK17', 'BSK27', 'BSkG1', 'BSkG2','F-', \
            'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', 'NRAPR', 'RATP', \
            'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
            'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', \
            'SLY4', 'SLY5', 'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', \
            'UNEDF0', 'UNEDF1' ]
    elif model.lower() == 'skyrme2':
        params = [ 'SLy4', 'SkM*', 'SV-min', 'SV-bas', 'SV-K218', \
            'SV-K226', 'SV-K241', 'SV-mas07', 'SV-mas08', 'SV-mas10',\
            'SV-sym28', 'SV-sym32', 'SV-sym34', 'SV-kap00', 'SV-kap20', 'SV-kap60']
    elif model.lower() == 'gskyrme':
        params = [ 'SkK180', 'SkK200', 'SkK220', 'SkK240', 'SkKM' ]
    elif model.lower() == 'eskyrme':
        params = [ 'BSk22', 'BSk24', 'BSk25', 'BSk26', 'BSk31', 'BSk32',  'BSkG3', 'BSkG4' ]
    elif model.lower() == 'gogny':
        params = [ 'D1S', 'D1', 'D250', 'D260', 'D280', 'D300' ]
    elif model.lower() == 'fayans':
        params = [ 'Fy(IVP)', 'Fy(Dr,HFB)', 'Fy(std)']
    elif model.lower() == 'nlrh':
        params = [ 'NL-SH', 'NL3', 'NL3II', 'PK1', 'PK1R', 'TM1' ]
    elif model.lower() == 'ddrh':
        params = [ 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99' ]
    elif model.lower() == 'ddrhf':
        params = [ 'PKA1', 'PKO1', 'PKO2', 'PKO3' ]
    elif model.lower() == 'xeft':
        params = [ 'H1MM', 'H2MM', 'H3MM', 'H4MM', 'H5MM', 'H6MM', 'H7MM' ]
    #print('For model:',model)
    #print('Parameters available in the toolkit:',params)
    params_lower = [ item.lower() for item in params ]
    #
    if nuda.env.verb: print("Exit nep_params()")
    #
    return params, params_lower

class setupNEP():
    """
    Instantiate the object with results based on phenomenological\
    interactions and choosen by the toolkit practitioner. \
    This choice is defined in the variables `model` and `param`.

    If `models` == 'Skyrme', `param` can be: 'BSK14', \
    'BSK16', 'BSK17', 'BSK27', 'F-', 'F+', 'F0', 'FPL', 'LNS', 'LNS1', 'LNS5', \
    'NRAPR', 'RATP', 'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
    'SKMS', 'SKO', 'SKOP', 'SKP', 'SKRSIGMA', 'SKX', 'Skz2', 'SLY4', 'SLY5', \
    'SLY230A', 'SLY230B', 'SV', 'T6', 'T44', 'UNEDF0', 'UNEDF1'. 

    If `models` == 'Skyrme2', `param` can be: 'SLy4', 'SkM*', \
    'SV-min', 'SV-bas', 'SV-K218', 'SV-K226', 'SV-K241', 'SV-mas07', \
    'SV-mas08', 'SV-mas10','SV-sym28', 'SV-sym32', 'SV-sym34', 'SV-kap00', \
    'SV-kap20', 'SV-kap60'.

    If `models` == 'GSkyrme', `param` can be: 'SkK180', 'SkK200', 'SkK220', 'SkK240', 'SkKM'. \

    If `models` == 'ESkyrme', `param` can be: 'BSk22', 'BSk24', 'BSk25', \
    'BSk26', 'BSk31', 'BSk32', 'BSkG1', 'BSkG2', 'BSkG3'.

    If `models` == 'Fayans', `param` can be: 'Fy(IVP)', 'Fy(Dr,HDB)', 'Fy(std)'.

    If `models` == 'NLRH', `param` can be: 'NL-SH', 'NL3', 'NL3II', 'PK1', 'PK1R', 'TM1'. 

    If `models` == 'DDRH', `param` can be: 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99'. 

    If `models` == 'DDRHF', `param` can be: 'PKA1', 'PKO1', 'PKO2', 'PKO3'. 

    If `models` == 'xEFT', `param` can be: 'H1MM', 'H2MM', 'H3MM', 'H4MM', 'H5MM', 'H6MM', 'H7MM'.
    
    :param model: Fix the name of model: 'Skyrme', 'NLRH', \
    'DDRH', 'DDRHF'. Default value: 'Skyrme'.
    :type model: str, optional. 
    :param param: Fix the parameterization associated to model. \
    Default value: 'SLY5'.
    :type param: str, optional. 

    **Attributes:**
    """
    #
    def __init__( self, model = 'Skyrme', param = 'SLY5' ):
        #
        if nuda.env.verb: print("\nEnter setupNEP()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        #print("-> model:",model)
        #: Attribute param.
        self.param = param
        if nuda.env.verb: print("param:",param)
        #print("-> param:",param)
        #
        self = setupNEP.init_self( self )
        #
        models, models_lower = nep_models( )
        #
        if model.lower() not in models_lower:
            print('setup_nep: The model name ',model,' is not in the list of models.')
            print('setup_nep: list of models:',models)
            print('setup_nep: -- Exit the code --')
            exit()
        #
        params, params_lower = nep_params( model = model )
        #
        if param.lower() not in params_lower:
            print('setup_nep: The param set ',param,' is not in the list of param.')
            print('setup_nep: list of param:',params)
            print('setup_nep: -- Exit the code --')
            exit()
        #
        if model.lower() == 'skyrme':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/NEPSkyrme.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            #print('Reads file:',file_in)
            #: Attribute providing the full reference to the paper to be citted.
            #self.ref = ''
            #: Attribute providing the label the data is references for figures.
            self.label = 'SKY-'+param
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this EOS."
            #name = np.loadtxt( file_in, usecols=(0), comments='#', unpack = True, dtype = str )
            names = []
            with open(file_in,"r") as file:
                for line in file:
                    if '#' in line:
                        continue
                    names.append( line.split()[0] )
            names = np.array( names, dtype = str )
            #print('name:',name)
            #
            #nsat, Esat, Ksat, Qsat, Esym, Lsym, Ksym, msat \
            #   = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8), comments='#', unpack = True, dtype = float )
            #kappas = 1./msat - 1.0
            #kappav = np.zeros( kappas.size )
            #Zsat = kappav.copy()
            #Qsym = kappav.copy()
            #Zsym = kappav.copy()
            nsat, Esat, Ksat, Qsat, Zsat, Esym, Lsym, Ksym, Qsym, Zsym, \
                msat, kappasat, kappav = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13), comments='#', unpack = True )
            kappasym = kappasat - kappav
            Dmsat = -2*kappasym/( (1+kappasat)**2-kappasym**2)
            #
            #print('param:',param)
            if param in names:
                self.nep = True
                ind = np.where( names == param )[0][0]
                self.nsat = nsat[ind]; self.Esat = Esat[ind]; self.Ksat = Ksat[ind]; self.Qsat = Qsat[ind]; self.Zsat = Zsat[ind]; 
                self.Esym = Esym[ind]; self.Lsym = Lsym[ind]; self.Ksym = Ksym[ind]; self.Qsym = Qsym[ind]; self.Zsym = Zsym[ind];
                self.msat = msat[ind]; self.kappas = kappasat[ind]; self.kappav = kappav[ind];
                self.kappasat = kappasat[ind]; self.kappasym = kappasym[ind]; self.Dmsat = Dmsat[ind]
            else:
                self.nep = False
        #
        elif model.lower() == 'skyrme2':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/NEPSkyrme2.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.label = 'Skyrme2-'+param
            self.note = "write here notes about this EOS."
            #name = np.loadtxt( file_in, usecols=(0), comments='#', unpack = True, dtype=str )
            names = []
            with open(file_in,"r") as file:
                for line in file:
                    if '#' in line:
                        continue
                    names.append( line.split()[0] )
            names = np.array( names, dtype = str )
            nsat, Esat, Ksat, Qsat, msat, Esym, Lsym, kappav \
                = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8), comments='#', unpack = True )
            kappasat = 1.0/msat - 1.0
            kappasym = kappasat - kappav
            Dmsat = -2*kappasym/( (1+kappasat)**2-kappasym**2)
            #
            if param in names:
                self.nep = True
                ind = np.where( names == param )[0][0]
                self.nsat = nsat[ind]; self.Esat = Esat[ind]; self.Ksat = Ksat[ind]; self.Qsat = Qsat[ind];
                self.Esym = Esym[ind]; self.Lsym = Lsym[ind];
                self.msat = msat[ind]; self.kappas = kappasat[ind]; self.kappav = kappav[ind];
                self.kappasat = kappasat[ind]; self.kappasym = kappasym[ind]; self.Dmsat = Dmsat[ind]
            else:
                self.nep = False
            #
        elif model.lower() == 'gskyrme':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/NEPGSkyrme.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            #: Attribute providing the full reference to the paper to be citted.
            #self.ref = 'In preparation'
            #: Attribute providing the label the data is references for figures.
            self.label = 'GSKY-'+param
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this EOS."
            names = []
            with open(file_in,"r") as file:
                for line in file:
                    if '#' in line:
                        continue
                    names.append( line.split()[0] )
            names = np.array( names, dtype = str )
            #name = np.loadtxt( file_in, usecols=(0), comments='#', unpack = True, dtype=str )
            kFsat, Esat, Ksat, Qsat, Esym, Lsym, Ksym, Qsym, \
                msat, mvec = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8,9,10), comments='#', unpack = True )
            nsat = 2.0 * kFsat**3 / ( 3.0 * nuda.cst.pi2 )
            kappasat = 1.0/msat - 1.0
            kappasym = 1.0/msat - 1.0/mvec
            kappav = kappasat - kappasat
            Zsat = np.zeros( kappasat.size )
            Zsym = Zsat.copy()
            Dmsat = -2*kappasym/( (1+kappasat)**2-kappasym**2)
            #
            if param in names:
                self.nep = True
                ind = np.where( names == param )[0][0]
                self.nsat = nsat[ind]; self.Esat = Esat[ind]; self.Ksat = Ksat[ind]; self.Qsat = Qsat[ind]; self.Zsat = None
                self.Esym = Esym[ind]; self.Lsym = Lsym[ind]; self.Ksym = Ksym[ind]; self.Qsym = Qsym[ind]; self.Zsym = None
                self.msat = msat[ind]; self.kappas = kappasat[ind]; self.kappav = kappav[ind];
                self.kappasat = kappasat[ind]; self.kappasym = kappasym[ind]; self.Dmsat = Dmsat[ind]
            else:
                self.nep = False
            #
        elif model.lower() == 'eskyrme':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/NEPESkyrme.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            #: Attribute providing the full reference to the paper to be citted.
            #self.ref = ''
            #: Attribute providing the label the data is references for figures.
            self.label = 'ESKY-'+param
            #: Attribute providing additional notes about the data.
            self.note = "write here notes about this EOS."
            names = []
            with open(file_in,"r") as file:
                for line in file:
                    if '#' in line:
                        continue
                    names.append( line.split()[0] )
            names = np.array( names, dtype = str )
            #name = np.loadtxt( file_in, usecols=(0), comments='#', unpack = True, dtype=str )
            nsat, Esat, Ksat, Qsat, Esym, Lsym, Ksym, msat = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8), comments='#', unpack = True )
            kappasat = 1.0/msat - 1.0
            kappav = np.zeros( kappasat.size )
            Zsat = kappav.copy()
            Qsym = kappav.copy()
            Zsym = kappav.copy()
            kappasym = kappasat - kappav
            Dmsat = -2*kappasym/( (1+kappasat)**2-kappasym**2)
            #
            if param in names:
                self.nep = True
                ind = np.where( names == param )[0][0]
                self.nsat = nsat[ind]; self.Esat = Esat[ind]; self.Ksat = Ksat[ind]; self.Qsat = Qsat[ind]; self.Zsat = None
                self.Esym = Esym[ind]; self.Lsym = Lsym[ind]; self.Ksym = Ksym[ind]; self.Qsym = None; self.Zsym = None
                self.msat = msat[ind]; self.kappas = kappasat[ind]; self.kappav = None;
                self.kappasat = kappasat[ind]; self.kappasym = None; self.Dmsat = None
            else:
                self.nep = False
            #
        elif model.lower() == 'gogny':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/NEPGogny.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.label = 'Gogny-'+param
            self.note = "write here notes about this EOS."
            #name = np.loadtxt( file_in, usecols=(0), comments='#', unpack = True, dtype=str )
            names = []
            with open(file_in,"r") as file:
                for line in file:
                    if '#' in line:
                        continue
                    names.append( line.split()[0] )
            names = np.array( names, dtype = str )
            Ksat, Qsat = np.loadtxt( file_in, usecols=(1,2), comments='#', unpack = True )
            #
            if param in names:
                self.nep = True
                ind = np.where( names == param )[0][0]
                self.Ksat = Ksat[ind]; self.Qsat = Qsat[ind];
                self.nsat = None; self.Esat = None; self.Zsat = None
                self.Esym = None; self.Lsym = None; self.Ksym = None; self.Qsym = None; self.Zsym = None
                self.msat = None; self.kappas = None; self.kappav = None;
                self.kappasat = None; self.kappasym = None; self.Dmsat = None
            else:
                self.nep = False
#            pass
            #
        elif model.lower() == 'fayans':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/NEPFayans.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            self.label = 'Fayans-'+param
            self.note = "write here notes about this EOS."
            #name = np.loadtxt( file_in, usecols=(0), comments='#', unpack = True, dtype=str )
            names = []
            with open(file_in,"r") as file:
                for line in file:
                    if '#' in line:
                        continue
                    names.append( line.split()[0] )
            names = np.array( names, dtype = str )
            nsat, Esat, Ksat, Qsat, msat, Esym, Lsym, kappav \
                = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8), comments='#', unpack = True )
            kappasat = 1.0/msat - 1.0
            kappasym = kappasat - kappav
            Dmsat = -2*kappasym/( (1+kappasat)**2-kappasym**2)
            #
            if param in names:
                self.nep = True
                ind = np.where( names == param )[0][0]
                self.nsat = nsat[ind]; self.Esat = Esat[ind]; self.Ksat = Ksat[ind]; self.Qsat = Qsat[ind];
                self.Esym = Esym[ind]; self.Lsym = Lsym[ind];
                self.msat = msat[ind]; self.kappas = kappasat[ind]; self.kappav = kappav[ind];
                self.kappasat = kappasat[ind]; self.kappasym = kappasym[ind]; self.Dmsat = Dmsat[ind]
            else:
                self.nep = False
            #
        elif model.lower() == 'nlrh':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/NEPnlrh.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            #self.ref = ''
            self.label = 'NLRH-'+param
            self.note = "write here notes about this EOS."
            #name = np.loadtxt( file_in, usecols=(0), comments='#', unpack = True, dtype=str )
            names = []
            with open(file_in,"r") as file:
                for line in file:
                    if '#' in line:
                        continue
                    names.append( line.split()[0] )
            names = np.array( names, dtype = str )
            nsat, Esat, Ksat, Qsat, Zsat, Esym, Lsym, Ksym, Qsym, Zsym, \
                msat, kappasat, kappav = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13), comments='#', unpack = True )
            kappasym = kappasat - kappav
            Dmsat = -2*kappasym/( (1+kappasat)**2-kappasym**2)
            #
            if param in names:
                self.nep = True
                ind = np.where( names == param )[0][0]
                self.nsat = nsat[ind]; self.Esat = Esat[ind]; self.Ksat = Ksat[ind]; self.Qsat = Qsat[ind]; self.Zsat = Zsat[ind]; 
                self.Esym = Esym[ind]; self.Lsym = Lsym[ind]; self.Ksym = Ksym[ind]; self.Qsym = Qsym[ind]; self.Zsym = Zsym[ind];
                self.msat = msat[ind]; self.kappas = kappasat[ind]; self.kappav = kappav[ind];
                self.kappasat = kappasat[ind]; self.kappasym = kappasym[ind]; self.Dmsat = Dmsat[ind]
            else:
                self.nep = False
            #
        elif model.lower() == 'ddrh':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/NEPddrh.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            #self.ref = ''
            self.label = 'DDRH-'+param
            self.note = "write here notes about this EOS."
            #name = np.loadtxt( file_in, usecols=(0), comments='#', unpack = True, dtype=str )
            names = []
            with open(file_in,"r") as file:
                for line in file:
                    if '#' in line:
                        continue
                    names.append( line.split()[0] )
            names = np.array( names, dtype = str )
            nsat, Esat, Ksat, Qsat, Zsat, Esym, Lsym, Ksym, Qsym, Zsym, \
                msat, kappasat, kappav = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13), comments='#', unpack = True )
            kappasym = kappasat - kappav
            Dmsat = -2*kappasym/( (1+kappasat)**2-kappasym**2)
            #
            if param in names:
                self.nep = True
                ind = np.where( names == param )[0][0]
                self.nsat = nsat[ind]; self.Esat = Esat[ind]; self.Ksat = Ksat[ind]; self.Qsat = Qsat[ind]; self.Zsat = Zsat[ind];
                self.Esym = Esym[ind]; self.Lsym = Lsym[ind]; self.Ksym = Ksym[ind]; self.Qsym = Qsym[ind]; self.Zsym = Zsym[ind];
                self.msat = msat[ind]; self.kappas = kappasat[ind]; self.kappav = kappav[ind];
                self.kappasat = kappasat[ind]; self.kappasym = kappasym[ind]; self.Dmsat = Dmsat[ind]
            else:
                self.nep = False
            #
        elif model.lower() == 'ddrhf':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/NEPddrhf.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            #self.ref = ''
            self.label = 'DDRHF-'+param
            self.note = "write here notes about this EOS."
            #name = np.loadtxt( file_in, usecols=(0), comments='#', unpack = True, dtype=str )
            names = []
            with open(file_in,"r") as file:
                for line in file:
                    if '#' in line:
                        continue
                    names.append( line.split()[0] )
            names = np.array( names, dtype = str )
            nsat, Esat, Ksat, Qsat, Zsat, Esym, Lsym, Ksym, Qsym, Zsym, \
                msat, kappasat, kappav = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13), comments='#', unpack = True )
            kappasym = kappasat - kappav
            Dmsat = -2*kappasym/( (1+kappasat)**2-kappasym**2)
            #
            if param in names:
                self.nep = True
                ind = np.where( names == param )[0][0]
                self.nsat = nsat[ind]; self.Esat = Esat[ind]; self.Ksat = Ksat[ind]; self.Qsat = Qsat[ind]; self.Zsat = Zsat[ind];
                self.Esym = Esym[ind]; self.Lsym = Lsym[ind]; self.Ksym = Ksym[ind]; self.Qsym = Qsym[ind]; self.Zsym = Zsym[ind];
                self.msat = msat[ind]; self.kappas = kappasat[ind]; self.kappav = kappav[ind];
                self.kappasat = kappasat[ind]; self.kappasym = kappasym[ind]; self.Dmsat = Dmsat[ind];
            else:
                self.nep = False
            #
        elif model.lower() == 'xeft':
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/NEPxEFT.dat')
            if nuda.env.verb: print('Reads file:',file_in)
            #self.ref = ''
            self.label = 'xEFT-'+param
            self.note = "write here notes about this EOS."
            #name = np.loadtxt( file_in, usecols=(0), comments='#', unpack = True, dtype=str )
            names = []
            with open(file_in,"r") as file:
                for line in file:
                    if '#' in line:
                        continue
                    names.append( line.split()[0] )
            names = np.array( names, dtype = str )
            Esat, Esym, nsat, Lsym, Ksat, Ksym, Qsat, Qsym, Zsat, Zsym, Pressure, Ktau,\
                = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8,9,10,11,12), comments='#', unpack = True )
            kappas = np.zeros( Esat.size )
            kappav = np.zeros( Esat.size )
            kappasat = np.zeros( Esat.size )
            kappasym = np.zeros( Esat.size )
            msat = np.zeros( Esat.size )
            Dmsat = np.zeros( Esat.size )
            #
            if param in names:
                self.nep = True
                ind = np.where( names == param )[0][0]
                self.nsat = nsat[ind]; self.Esat = Esat[ind]; self.Ksat = Ksat[ind]; self.Qsat = Qsat[ind]; self.Zsat = Zsat[ind];
                self.Esym = Esym[ind]; self.Lsym = Lsym[ind]; self.Ksym = Ksym[ind]; self.Qsym = Qsym[ind]; self.Zsym = Zsym[ind];
                self.msat = None; self.kappas = None; self.kappav = None;
                self.kappasat = None; self.kappasym = None; self.Dmsat = None;
            else:
                self.nep = False
            #
        self.den_unit = 'fm$^{-3}$'
        self.kfn_unit = 'fm$^{-1}$'
        self.e2a_unit = 'MeV'
        self.pre_unit = 'MeV fm$^{-3}$'
        self.gap_unit = 'MeV'
        #
        if nuda.env.verb: print("Exit SetupNEP()")
    #
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        print("")
        #
        if nuda.env.verb: print("Enter print_outputs()")
        #
        print("- Print output:")
        print("   model:",self.model)
        print("   param:",self.param)
        #print("   ref:",self.ref)
        print("   label:",self.label)
        #print("   note:",self.note)
        if any(self.sm_den): print(f"   sm_den: {np.round(self.sm_den,2)} in {self.den_unit}")
        if any(self.sm_kfn): print(f"   sm_kfn: {np.round(self.sm_kfn,2)} in {self.kfn_unit}")
        if any(self.sm_e2a): print(f"   sm_e2a: {np.round(self.sm_e2a,2)} in {self.e2a_unit}")
        if any(self.nm_den): print(f"   nm_den: {np.round(self.nm_den,2)} in {self.den_unit}")
        if any(self.nm_kfn): print(f"   nm_kfn: {np.round(self.nm_kfn,2)} in {self.kfn_unit}")
        if any(self.nm_e2a): print(f"   nm_e2a: {np.round(self.nm_e2a,2)} in {self.e2a_unit}")
        if any(self.nm_gap): print(f"   nm_gap: {np.round(self.nm_gap,2)} in {self.gap_unit}")
        print(' NEP:')
        if self.nep:
            print(' sat:',self.Esat,self.nsat,self.Ksat,self.Qsat,self.Zsat)
            print(' sym:',self.Esym,self.Lsym,self.Ksym,self.Qsym,self.Zsym)
            print(' ms:',self.msat,self.kappasat,self.kappav)
        #
        if nuda.env.verb: print("Exit print_outputs()")
        #
    def init_self( self ):
        """
        Initialize variables in self.
        """
        #
        if nuda.env.verb: print("Enter init_self()")
        #
        #: Attribute the plot linestyle.
        self.linestyle = 'solid'
        #: Attribute providing the full reference to the paper to be citted.
        self.ref = ''
        #: Attribute providing additional notes about the data.
        self.note = ''
        #: Attribute the plot label data.
        self.label = ''
        #: Attribute the plot marker.
        self.marker = None
        #: Attribute the NEP.
        self.Esat = None; self.nsat = None; self.Ksat = None; self.Qsat = None; self.Zsat = None;
        self.Esym = None; self.Lsym = None; self.Ksym = None; self.Qsym = None; self.Zsym = None;
        self.msat = None; self.kappasat = None; self.kappav = None; 
        self.kappasym = None; self.Dmsat = None;
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self
