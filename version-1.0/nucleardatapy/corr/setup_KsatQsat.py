import os
import sys
import numpy as np  # 1.15.0
import random

import nucleardatapy as nuda

def KsatQsat_constraints():
    """
    Return a list of constraints available in this toolkit in the \
    following list: 
    '1991-Pearson', '2025-MK', \
    'EDF-SKY', 'EDF-GSKY', 'EDF-ESKY', 'EDF-DDRH', \
    'EDF-NLRH', 'EDF-DDRHF', 'EDF-Gogny', 'EDF-xEFT'; \
    and print them all on the prompt.

    :return: The list of constraints.
    :rtype: list[str].
    """
    constraints = [ '1991-Pearson', '2025-MK-95', '2025-MK-90', '2025-MK-67', \
    'EDF-SKY', 'EDF-GSKY', 'EDF-ESKY', 'EDF-Fayans' , 'EDF-Gogny', 'EDF-DDRH', \
    'EDF-NLRH', 'EDF-DDRHF', 'EDF-xEFT' ]
    #constraints = [ '1991-Pearson', '2025-MK-67', '2025-MK-90', '2025-MK-95', \
    #'EDF-SKY', 'EDF-SKY2', 'EDF-ESKY', 'EDF-DDRH', \
    #'EDF-NLRH', 'EDF-DDRHF', 'EDF-Fayans' , 'EDF-Gogny', 'EDF-xEFT' ]
    #print('Constraints available in the toolkit:',constraints)
    constraints_lower = [ item.lower() for item in constraints ]
    return constraints, constraints_lower

def flinear(xi, m, c):
    return float(m) * np.array(xi, dtype=float) + float(c)*np.ones(len(xi))

class setupKsatQsat():
    """
    Instantiate the values of Esym and Lsym from the constraint.

    The name of the constraint to be chosen in the \
    following list: '1991-Pearson', '2025-MK', \
    'EDF-SKY', 'EDF-ESKY', 'EDF-DDRH', \
    'EDF-NLRH', 'EDF-DDRHF', 'EDF-Gogny', 'EDF-xEFT'.
    :param constraint: Fix the name of `constraint`. Default value: 'EDF-SKY'.
    :type constraint: str, optional.

    **Attributes:**
    """
    #
    def __init__( self, constraint = 'EDF-SKY' ):
        #
        if nuda.env.verb: print("Enter setupKsatQsat()")
        #: Attribute constraint.
        self.constraint = constraint
        if nuda.env.verb: print("constraint:",constraint)
        #
        self = setupKsatQsat.init_self( self )
        #
        constraints, constraints_lower = KsatQsat_constraints()
        #
        if constraint.lower() not in constraints_lower:
            print('setup_KsatQsat: The constraint ',constraint,' is not in the list of constraints.')
            print('setup_KsatQsat: list of constraints:',constraints)
            print('setup_KsatQsat: -- Exit the code --')
            exit()
        #
        if constraint.lower() == '1991-pearson':
            #
            # pearson correlation
            #
            #: Attribute providing the label the data is references for figures.
            self.label = '1991-Pearson'
            #: Attribute providing additional notes about the constraint.
            self.note = "Experimental constraints from Pearson."
            # fix the marker style
            self.marker = 's'
            #
            self.Ksat_band = np.linspace(100,400,num=30)
            alpha = 0.082
            beta1 = -17.5
            beta2 = -22.5
            Q2K_up = alpha * self.Ksat_band + beta1
            Q2K_lo = alpha * self.Ksat_band + beta2
            self.Qsat_up = Q2K_up * self.Ksat_band
            self.Qsat_lo = Q2K_lo * self.Ksat_band
            self.Qsat_band = 0.5 * ( self.Qsat_up + self.Qsat_lo )
            self.Qsat_err = 0.5 * np.abs( self.Qsat_up - self.Qsat_lo )
            self.Ksat_lin = None
            self.Qsat_lin = None
            #
        elif constraint.lower() == '2025-mk-67':
            #
            # best models (95%) from Margueron, Khan paper 2025
            #
            #: Attribute providing the label the data is references for figures.
            self.label = '2025-MK (67%)'
            #: Attribute providing additional notes about the constraint.
            self.note = "Exploration with DD Skyrme."
            # fix the marker style
            self.marker = 's'
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/best67DDSkyrme.dat')
            t00, x00, t01, x01, t02, x02, sig1, sig2, t1, x1, t2, x2, self.Ksat, self.Qsat, \
                = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14), comments='#', delimiter=',', unpack = True )
            #
        elif constraint.lower() == '2025-mk-90':
            #
            # best models (95%) from Margueron, Khan paper 2025
            #
            #: Attribute providing the label the data is references for figures.
            self.label = '2025-MK (90%)'
            #: Attribute providing additional notes about the constraint.
            self.note = "Exploration with DD Skyrme."
            # fix the marker style
            self.marker = 's'
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/best90DDSkyrme.dat')
            t00, x00, t01, x01, t02, x02, sig1, sig2, t1, x1, t2, x2, self.Ksat, self.Qsat, \
                = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14), comments='#', delimiter=',', unpack = True )
            #
        elif constraint.lower() == '2025-mk-95':
            #
            # best models (95%) from Margueron, Khan paper 2025
            #
            #: Attribute providing the label the data is references for figures.
            self.label = '2025-MK (95%)'
            #: Attribute providing additional notes about the constraint.
            self.note = "Exploration with DD Skyrme."
            # fix the marker style
            self.marker = 's'
            #
            file_in = os.path.join(nuda.param.path_data,'matter/nep/best95DDSkyrme.dat')
            t00, x00, t01, x01, t02, x02, sig1, sig2, t1, x1, t2, x2, self.Ksat, self.Qsat, \
                = np.loadtxt( file_in, usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14), comments='#', delimiter=',', unpack = True )
            #
        elif 'edf-' in constraint.lower():
            #
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = ''
            #
            if constraint.lower() == 'edf-sky':
                #: Attribute providing the label the data is references for figures.
                self.label = 'Skyrme'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from Skyrme."
                # fix the marker style
                self.marker = '*'
                # fix model variable
                model = 'Skyrme'
            elif constraint.lower() == 'edf-sky2':
                #: Attribute providing the label the data is references for figures.
                self.label = 'Skyrme2'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from other set of Skyrme EDF."
                # fix the marker style
                self.marker = '*'
                # fix model variable
                model = 'Skyrme2'
            elif constraint.lower() == 'edf-gsky':
                #: Attribute providing the label the data is references for figures.
                self.label = 'GSkyrme'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from Generalized Skyrme."
                # fix the marker style
                self.marker = '*'
                # fix model variable
                model = 'GSkyrme'
            elif constraint.lower() == 'edf-esky':
                #: Attribute providing the label the data is references for figures.
                self.label = 'ESkyrme'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from ESkyrme DFT."
                # fix the marker style
                self.marker = '*'
                # fix model variable
                model = 'ESkyrme'
            elif constraint.lower() == 'edf-ddrh':
                #: Attribute providing the label the data is references for figures.
                self.label = 'DDRH'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from DDRH DFT."
                # fix the marker style
                self.marker = '+'
                # fix model variable
                model = 'DDRH'
            elif constraint.lower() == 'edf-nlrh':
                #: Attribute providing the label the data is references for figures.
                self.label = 'NLRH'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from NLRH DFT."
                # fix the marker style
                self.marker = '+'
                # fix model variable
                model = 'NLRH'
            elif constraint.lower() == 'edf-ddrhf':
                #: Attribute providing the label the data is references for figures.
                self.label = 'DDRHF'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from DDRHF DFT."
                # fix the marker style
                self.marker = '+'
                # fix model variable
                model = 'DDRHF'
            elif constraint.lower() == 'edf-fayans':
                #: Attribute providing the label the data is references for figures.
                self.label = 'Fayans'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from Fayans DFT."
                # fix the marker style
                self.marker = 'x'
                # fix model variable
                model = 'Fayans'
            elif constraint.lower() == 'edf-gogny':
                #: Attribute providing the label the data is references for figures.
                self.label = 'Gogny'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from Gogny DFT."
                # fix the marker style
                self.marker = 'x'
                # fix model variable
                model = 'Gogny'
            elif constraint.lower() == 'edf-xeft':
                #: Attribute providing the label the data is references for figures.
                self.label = 'xEFT'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from xEFT DFT."
                # fix the marker style
                self.marker = 'o'
                # fix model variable
                model = 'xeft'
                #
            #print('model:',model)
            params, params_lower = nuda.matter.nep_params( model = model )
            #print('params:',params)
            #
            Ksat = []; Qsat = [];
            for param in params:
                #
                #print('param:',param)
                nep = nuda.matter.setupNEP( model = model, param = param )
                #print('param:',param,' Ksat:',nep.Ksat)
                if nep.nep:
                    Ksat.append( nep.Ksat ); Qsat.append( nep.Qsat ); 
            self.Ksat = np.array( Ksat, dtype=float ).tolist()
            self.Qsat = np.array( Qsat, dtype=float ).tolist()
            #
            #print('Ksat:',self.Ksat)
            #print('Qsat:',self.Qsat)
            #
            # Compute linear fit:
            #
            sum1 = 0.0; sum2 = 0.0; sum3 = 0.0; sum4 = 0.0; sum5 = 0.0;
            for i,xi in enumerate(self.Ksat):
                wi = 1.0
                yi = self.Qsat[i]
                sum1 += wi
                sum2 += wi * xi * yi
                sum3 += wi * xi
                sum4 += wi * yi
                sum5 += wi * xi**2
            self.m = ( sum1 * sum2 - sum3 * sum4 ) / ( sum1 * sum5 - sum3**2 )
            self.c = ( sum5 * sum4 - sum3 * sum2 ) / ( sum1 * sum5 - sum3**2 )
            #
            Ksat_min = min(self.Ksat)
            Ksat_max = max(self.Ksat)
            #
            self.Ksat_lin = np.linspace( Ksat_min, Ksat_max, num = 10 )
            self.Qsat_lin = nuda.corr.flinear( self.Ksat_lin , self.m, self.c )
            #
        else:
            #
            print('setup_KsatQsat: The variable constraint:',constraint)
            print('setup_KsatQsat: does not fit with the options in the code')
        #
        if nuda.env.verb: print("Exit setupKsatQsat()")
        #
    #
    def print_outputs( self ):
        """
        Method which print outputs on terminal's screen.
        """
        print("")
        #
        if nuda.env.verb: print("Enter print_outputs()")
        #
        print("   constraint:",self.constraint)
        print("   ref:",self.ref)
        print("   label:",self.label)
        print("   note:",self.note)
        print("   plot:",self.plot)
        print("   Ksat:",self.Ksat)
        print("   Qsat:",self.Qsat)
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
        #: Attribute providing the full reference to the paper to be citted.
        self.ref = None
        #: Attribute providing the label the data is references for figures.
        self.label = None
        #: Attribute providing additional notes about the constraint.
        self.note = None
        #: Attribute the plot alpha
        self.alpha = 0.5
        self.plot = None
        #
        #: Attribute Ksat.
        self.Ksat = None
        self.Ksat_band = None
        self.Ksat_err = None
        self.Ksat_up = None
        self.Ksat_lo = None
        self.Ksat_lin = None
        #: Attribute Qsat.
        self.Qsat = None
        self.Qsat_band = None
        self.Qsat_err = None
        self.Qsat_up = None
        self.Qsat_lo = None
        self.Qsat_lin = None
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        
