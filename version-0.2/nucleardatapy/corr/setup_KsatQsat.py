import os
import sys
import numpy as np  # 1.15.0
import random

import nucleardatapy as nuda

def KsatQsat_constraints():
    """
    Return a list of constraints available in this toolkit in the \
    following list: '2024-DFT-SKY', '2024-DFT-ESKY', '2024-DFT-DDRH', \
    '2024-DFT-NLRH', '2024-DFT-DDRHF', '2024-DFT-Gogny', '2024-DFT-xEFT'; \
    and print them all on the prompt.

    :return: The list of constraints.
    :rtype: list[str].
    """
    constraints = [ '2024-DFT-SKY', '2024-DFT-SKY2', '2024-DFT-ESKY', '2024-DFT-DDRH', \
    '2024-DFT-NLRH', '2024-DFT-DDRHF', '2024-DFT-Fayans' , '2024-DFT-Gogny' ]
    #print('Constraints available in the toolkit:',constraints)
    constraints_lower = [ item.lower() for item in constraints ]
    return constraints, constraints_lower

def flinear(xi, m, c):
    return float(m) * np.array(xi, dtype=float) + float(c)*np.ones(len(xi))

class setupKsatQsat():
    """
    Instantiate the values of Esym and Lsym from the constraint.

    The name of the constraint to be chosen in the \
    following list: '2024-DFT-SKY', '2024-DFT-ESKY', '2024-DFT-DDRH', \
    '2024-DFT-NLRH', '2024-DFT-DDRHF', '2024-DFT-Gogny', '2024-DFT-xEFT'.
    :param constraint: Fix the name of `constraint`. Default value: '2024-DFT-SKY'.
    :type constraint: str, optional.

    **Attributes:**
    """
    #
    def __init__( self, constraint = '2024-DFT-SKY' ):
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
        if '2024-dft' in constraint.lower():
            #
            #: Attribute providing the full reference to the paper to be citted.
            self.ref = ''
            #
            if constraint.lower() == '2024-dft-sky':
                #: Attribute providing the label the data is references for figures.
                self.label = 'Skyrme-2024'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from Skyrme DFT."
                # fix the marker style
                self.marker = '*'
                # fix model variable
                model = 'Skyrme'
            elif constraint.lower() == '2024-dft-sky2':
                #: Attribute providing the label the data is references for figures.
                self.label = 'Skyrme2-2024'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from Skyrme DFT."
                # fix the marker style
                self.marker = '+'
                # fix model variable
                model = 'Skyrme2'
            elif constraint.lower() == '2024-dft-esky':
                #: Attribute providing the label the data is references for figures.
                self.label = 'ESkyrme-2024'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from ESkyrme DFT."
                # fix the marker style
                self.marker = 'x'
                # fix model variable
                model = 'ESkyrme'
            elif constraint.lower() == '2024-dft-ddrh':
                #: Attribute providing the label the data is references for figures.
                self.label = 'DDRH-2024'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from DDRH DFT."
                # fix the marker style
                self.marker = 'o'
                # fix model variable
                model = 'DDRH'
            elif constraint.lower() == '2024-dft-nlrh':
                #: Attribute providing the label the data is references for figures.
                self.label = 'NLRH-2024'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from NLRH DFT."
                # fix the marker style
                self.marker = '*'
                # fix model variable
                model = 'NLRH'
            elif constraint.lower() == '2024-dft-ddrhf':
                #: Attribute providing the label the data is references for figures.
                self.label = 'DDRHF-2024'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from DDRHF DFT."
                # fix the marker style
                self.marker = 'x'
                # fix model variable
                model = 'DDRHF'
            elif constraint.lower() == '2024-dft-fayans':
                #: Attribute providing the label the data is references for figures.
                self.label = 'Fayans-2024'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from Fayans DFT."
                # fix the marker style
                self.marker = '^'
                # fix model variable
                model = 'Fayans'
            elif constraint.lower() == '2024-dft-gogny':
                #: Attribute providing the label the data is references for figures.
                self.label = 'Gogny-2024'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from Gogny DFT."
                # fix the marker style
                self.marker = '<'
                # fix model variable
                model = 'Gogny'
            elif constraint.lower() == '2024-dft-xeft':
                #: Attribute providing the label the data is references for figures.
                self.label = 'xEFT-2024'
                #: Attribute providing additional notes about the constraint.
                self.note = "constraints from xEFT DFT."
                # fix the marker style
                self.marker = 'D'
                # fix model variable
                model = '2016-MBPT-AM'
                #
            #
        else:
            #
            print('setup_KsatQsat: The variable constraint:',constraint)
            print('setup_KsatQsat: does not fit with the options in the code')
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
        #: Attribute Qsat.
        self.Qsat = None
        #
        if nuda.env.verb: print("Exit init_self()")
        #
        return self        
