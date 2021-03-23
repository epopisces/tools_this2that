#!/usr/bin/env python3
__doc__ = """

This2ThatTitle - a toolkit for converting one entity to another

Paragraph describing

Usage:
    ./this2that.py arg1 [optionalarg2]

Parameters
    param1          Thing 1 (required). 6 chars starting with Thing
    param2          Thing 2 (optional)

Output:
    string_output   Thing 3.  6 chars starting with Thing

Examples:
    ./this2that.py                              prompts for all args
    ./this2that.py InputType                    prompts for 2 args, OutputType and the input entity
    ./this2that.py InputType OutputType         prompts for 1 arg, the input entity
    ./this2that.py InputType OutputType Input   produces OutputType from the 'Input' entity of InputType
    ./this2that.py help                         outputs this help doc

"""
__author__ = "epopisces"
__date__ = "2021.03.22"
__version__ = 0.1

import argparse, os, re

#TODO Well, interesting conundrum.  Some T2T functions will only need one input. 
#TODO Some need two (some dependency of the output, eg a filepath).  
#TODO Is there a good way to designate when a func is one vs the other?

#region #####     Validation                                              #####
###############################################################################
def validate_json():
    return

def validate_filepath():
    return

def validate_dirpath():
    return
#endregion

#region #####     to_file                                                 #####
###############################################################################

def json_to_filename(json_input, output_filename, validate=True):
    import json
    if validate:
        validate_json()

    return

def json_to_absolutepath(json_input, absolutepath, validate=True):
    return

def json_to_relativepath(json_input, relativepath, validate=True):
    return

#endregion to_file
class ObjectClass():
    """A quick description of the class

    Attributes:
        var1 (bool):          used for this thing
        var2 (str, optional): used for that thing
    """    

    def __init__(self, var1, var2=False):
        self.var1 = var1
        self.var2 = var2

        # maybe call another function here to help setup things

        return

    def this_func(self):
        # do the thing here
        return


if __name__ == "__main__":
    #? Remove this section if not accepting arguments from CLI
    #region  #####     Argparse                                                     #####
    #####################################################################################
    parser = argparse.ArgumentParser(description='short description of the module')
    parser.add_argument('-v','--var2', default=False, type=str, help='describe arg for when man or help is used')
    parser.add_argument('--var1', action='store_true', help='describe arg for when man or help is used')

    args = parser.parse_args()
    #endregion

    # Uncomment for testing setup   
    var1 = True
    oc = ObjectClass(var1, var2=args.var2)