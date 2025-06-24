import numpy as np  # 1.15.0
import os
from scipy.interpolate import CubicSpline

import nucleardatapy as nuda

def rnp_theo_models():
    """
    Return a the neutron skin values of the models available in this toolkit and print them all on the prompt.

    :return: The list of models with can be 'Skyrme', 'NLRH', 'DDRH'.
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter rnp_theo_models()")
    #
    models = [ 'Skyrme', 'NLRH', 'DDRH' ]
    #print('Phenomenological models available in the toolkit:',models)
    models_lower = [ item.lower() for item in models ]
    #
    if nuda.env.verb: print("Exit rnp_theo_models()")
    #
    return models, models_lower

# def rnp_theo_nucleus():
#     #
#     if nuda.env.verb: print("\nEnter rnp_theo_nucleus()")
#     #
#     nucleus = [ '48Ca', '208Pb']
#     nucleus_lower = [ item.lower() for item in nucleus ]
#     #
#     if nuda.env.verb: print("Exit rnp_theo_nucleus()")
#     #
#     return nucleus, nucleus_lower
# 

def rnp_theo_params( model ):
    """
    Return a list with the parameterizations available in 
    this toolkit for a given model and print them all on the prompt.

    :param model: The type of model for which there are parametrizations. \
    They should be chosen among the following options: 'Skyrme', 'NLRH', \
    'DDRH', 'DDRHF'.
    :type model: str.
    :return: The list of parametrizations. \
    If `models` == 'skyrme': 'BSK14', \
    'BSK16', 'BSK17', 'F-', 'F+', 'F0', 'LNS1', 'LNS5', \
    'NRAPR', 'RATP', 'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
    'SKMS', 'SKO', 'SKOP', 'SKRSIGMA', 'SKX', 'Skz2', 'SLY4', 'SLY5', \
    'SLY230A', 'SLY230B', 'T6', 'UNEDF0', 'UNEDF1'. \
    If `models` == 'NLRH': 'NL-SH', 'NL3', 'NL3II', 'PK1', 'TM1'. \
    If `models` == 'DDRH': 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99'. \
    :rtype: list[str].
    """
    #
    if nuda.env.verb: print("\nEnter rnp_theo_params()")
    #
    #print('For model:',model)
    if model.lower() == 'skyrme':
        params = [ 'BSK14', 'BSK16', 'BSK17', 'F-', 'F+', 'F0',\
            'LNS1', 'LNS5', 'NRAPR', 'RATP', 'SAMI', 'SGII', 'SIII', \
            'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP','SKMS', 'SKO', 'SKOP', \
            'SKRSIGMA', 'SKX', 'Skz2', 'SLY4', 'SLY5', 'SLY230A', \
            'SLY230B', 'T6', 'UNEDF0', 'UNEDF1']
        nucleus = ['48Ca', '208Pb']    
    elif model.lower() == 'nlrh':
        params = [ 'NL-SH', 'NL3', 'NL3II', 'PK1', 'TM1' ]
        nucleus = ['48Ca', '208Pb']
    elif model.lower() == 'ddrh':
        params = [ 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99' ]
        nucleus = ['48Ca', '208Pb']
    #print('Parameters available in the toolkit:',params)
    params_lower = [ item.lower() for item in params ]
    #
    if nuda.env.verb: print("Exit rnp_theo_params()")
    #
    return params, params_lower

class setupRnpTheo():
    """
    Instantiate the object with results based on phenomenological\
    interactions and choosen by the toolkit practitioner. \
    This choice is defined in the variables `model` and `param`.

    If `models` == 'skyrme', `param` can be: 'BSK14', \
    'BSK16', 'BSK17', 'F-', 'F+', 'F0', 'LNS1', 'LNS5', \
    'NRAPR', 'RATP', 'SAMI', 'SGII', 'SIII', 'SKGSIGMA', 'SKI2', 'SKI4', 'SKMP', \
    'SKMS', 'SKO', 'SKOP', 'SKRSIGMA', 'SKX', 'Skz2', 'SLY4', 'SLY5', \
    'SLY230A', 'SLY230B', 'T6', 'UNEDF0', 'UNEDF1'. 

    If `models` == 'NLRH', `param` can be: 'NL-SH', 'NL3', 'NL3II', 'PK1', 'TM1'. 

    If `models` == 'DDRH', `param` can be: 'DDME1', 'DDME2', 'DDMEd', 'PKDD', 'TW99'. 

    
    :param model: Fix the name of model: 'Skyrme', 'NLRH', \
    'DDRH', 'DDRHF'. Default value: 'Skyrme'.
    :type model: str, optional. 
    :param param: Fix the parameterization associated to model. \
    Default value: 'SLY5'.
    :type param: str, optional. 

    **Attributes:**
    """
    #
    def __init__( self, model = 'Skyrme', param = 'SLY5', nucleus = '208Pb' ):
        #
        if nuda.env.verb: print("\nEnter setupRnpTheo()")
        #
        #: Attribute model.
        self.model = model
        if nuda.env.verb: print("model:",model)
        print("-> model:",model)
        #: Attribute param.
        self.param = param
        if nuda.env.verb: print("param:",param)
        print("-> param:",param)
        #
        #: Attribute nucleus.
        self.nucleus = nucleus
        if nuda.env.verb: print("nucleus:",nucleus)
        print("-> nucleus:",nucleus)
        # 
        self = nuda.nuc.setupRnpTheo.init_self( self )
        #
        models, models_lower = rnp_theo_models( )
        #
        if model.lower() not in models_lower:
            print('The model name ',model,' is not in the list of models.')
            print('list of models:',models)
            print('-- Exit the code --')
            exit()
        #
        params, params_lower = rnp_theo_params( model = model )
        #
        if param.lower() not in params_lower:
            print('The param set ',param,' is not in the list of param.')
            print('list of param:',params)
            print('-- Exit the code --')
            exit()
        #
        # nucleus, nucleus_lower = rnp_theo_nucleus( )
        # #
        # if nucleus.lower() not in nucleus_lower:
        #     print('The param set ',nucleus,' is not in the list of param.')
        #     print('list of param:',nucleus)
        #     print('-- Exit the code --')
        #     exit()
        # #            
        if model.lower() == 'skyrme':
            #
             file_in1 = os.path.join(nuda.param.path_data,'rnp/skyrmernp-'+nucleus+'.dat')
             if nuda.env.verb: print('Reads file1:',file_in1)
             name = np.loadtxt( file_in1, usecols=(0), comments='#', unpack = True, dtype=str )
             Rn, Rp, Rnp = np.loadtxt( file_in1, usecols=(1,2,3), comments='#', unpack = True )
             #: Attribute providing the label the data is references for figures.
             self.label = 'SKY-'+param
             #: Attribute providing additional notes about the data.
             self.note = "write here notes about this EOS."
             #
             if param in name:
                 self.rnp = True
                 ind = np.where(name == param )
                 self.Rn = Rn[ind][0]; 
                 self.Rp = Rp[ind][0]; 
                 self.Rnp = Rnp[ind][0];
             else:
                 self.rnp = False
            #
        elif model.lower() == 'nlrh':
            #
             file_in1 = os.path.join(nuda.param.path_data,'rnp/nlrhrnp-'+nucleus+'.dat')
             if nuda.env.verb: print('Reads file1:',file_in1)
             name = np.loadtxt( file_in1, usecols=(0), comments='#', unpack = True, dtype=str )
             Rn, Rp, Rnp = np.loadtxt( file_in1, usecols=(1,2,3), comments='#', unpack = True )
             #: Attribute providing the label the data is references for figures.
             self.label = 'NLRH-'+param
             #: Attribute providing additional notes about the data.
             self.note = "write here notes about this EOS."
             #
             if param in name:
                 self.rnp = True
                 ind = np.where(name == param )
                 self.Rn = Rn[ind][0]; 
                 self.Rp = Rp[ind][0]; 
                 self.Rnp = Rnp[ind][0];
             else:
                 self.rnp = False
            #
        elif model.lower() == 'ddrh':
            #
             file_in1 = os.path.join(nuda.param.path_data,'rnp/ddrhrnp-'+nucleus+'.dat')
             if nuda.env.verb: print('Reads file1:',file_in1)
             name = np.loadtxt( file_in1, usecols=(0), comments='#', unpack = True, dtype=str )
             Rn, Rp, Rnp = np.loadtxt( file_in1, usecols=(1,2,3), comments='#', unpack = True )
             #: Attribute providing the label the data is references for figures.
             self.label = 'DDRH-'+param
             #: Attribute providing additional notes about the data.
             self.note = "write here notes about this EOS."
             #
             if param in name:
                 self.rnp = True
                 ind = np.where(name == param )
                 self.Rn = Rn[ind][0]; 
                 self.Rp = Rp[ind][0]; 
                 self.Rnp = Rnp[ind][0];
             else:
                 self.rnp = False
            #
        # 
        self.Rn_unit = 'fm'
        self.Rp_unit = 'fm'
        self.Rnp_unit = 'fm'
        #
        if nuda.env.verb: print("Exit setupRnpTheo()")
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
        print("   nucleus:",self.nucleus)
        print("   model:",self.model)
        print("   param:",self.param)
        #
        print(f"   Rn: {np.round(self.Rn,4)} in {self.Rn_unit}")
        print(f"   Rp: {np.round(self.Rn,4)} in {self.Rp_unit}")
        print(f"   Rnp: {np.round(self.Rnp,4)} in {self.Rnp_unit}")
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
        #: Attribute the neutron matter density.
        self.Rn = []
        #: Attribute the symmetric matter density.
        self.Rp = []
        #: Attribute the neutron matter neutron Fermi momentum.
        self.Rnp = []
        #: Attribute the plot linestyle.
        self.linestyle = None
        #: Attribute the plot marker.
        self.marker = 'o'
        #: Attribute the plot every data.
        self.every = 1
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        
