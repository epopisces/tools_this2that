#!/usr/bin/env python3
#? The gallery is made up of several sections of helper methods.
#?                      origin_entity   origin_cde  target_entity   target_cde
#? Validate methods     input           input       N/A             [return]
#? Input methods        input           [input]     return          return
#? Output methods       input           [input]     output          input
#? Convert methods      input           input       return          input
#? Separate into submodules in the future

#* The gallery should

import csv

from classifier import classify
import validator

def load_cde_index():
    cde_index = {}
    with open("data/cde_index.csv", newline='') as csvfile:
        cde_index_list = list(csv.reader(csvfile))
    for row in cde_index_list:
        cde_index[row[0]] = {
            'index': row[2],
            'cde_name': row[3],
            'relevance': row[5],
            'sphere': row[7],
            'rex': row[13],
            'rex_confidence': row[14],
            'descendant_cdes': row[18],
            'ancestor_cdes': row[19],
            'master_cde': row[20],
            'default_extension': row[22],
        }
    return cde_index


#region #####     VALIDATE                                                #####
###############################################################################
def validate(origin_entity, origin_cde):
        """"""
        #TODO logging debug here f"validating {origin_entity} is of type {origin_cde}"

        func_name = f'validate_{origin_cde}'
        gallery_func = getattr(validator, func_name, None)

        try:
            validated, operation = gallery_func(origin_entity)
        except TypeError:
            print(f"{func_name} not yet defined in the validator module") #TODO error logging
            status = 0
            raise NotImplementedError(f"{func_name} not yet defined in the validator module")
            pass
        else:
            if operation == 0:
                print(f"{func_name} threw an error, unable to validate {origin_cde}") #TODO error logging

        return validated
  
#endregion VALIDATE

#region #####     OUTPUT: to_filename                                     #####
###############################################################################

def to_filepath(origin_entity, output_dest, origin_cde='string', validate=True):
    """the default everyman for file output""" 
    # in future classifier should return pathtype
    if classify(output_dest) == False: #! == absolutefilepath
        status = to_absolutefilepath(origin_entity, output_dest, origin_cde=origin_cde, validate=validate)
    else:
        status = to_relativefilepath(origin_entity, output_dest, origin_cde=origin_cde, validate=validate)
    return status, 1

def to_absolutefilepath(origin_entity, output_dest, origin_cde='string', validate=True):
    """call appropriate to_<filetype> CONVERT method, then output to output_dest
    output_dest must be an absolutefilepath, if no extension default to .txt"""
    if validate:
        # dynamic validate method via origin_cde (eg 'validate_json', where cde = json)
        if not validate(origin_entity, origin_cde):
            raise ValueError(f"{origin_entity} is not a {origin_cde}")

    return True, 1

def to_relativefilepath(origin_entity, output_dest, origin_cde='string', validate=True):
    """call appropriate to_<filetype> CONVERT method, then output to output_dest
    output_dest must be a relativefilepath, if no extension default to .txt"""
    if validate:
        # dynamic validate method via origin_cde (eg 'validate_json', where cde = json)
        if not validate(origin_entity, origin_cde):
            raise ValueError(f"{origin_entity} is not a {origin_cde}")
    return True, 1

# Aliases
to_filename = to_filepath
to_file     = to_filepath

#endregion OUTPUT: to_file

#region #####     INPUT: from_file                                        #####
###############################################################################

def from_filename(origin_entity, origin_cde="text", validate=True):
    """origin_entity must be a filename"""
    if validate:
        # dynamic validate method via origin_cde (eg 'validate_json', where cde = json)
        validate_standin()

    return

def from_absolutefilepath(origin_entity, origin_cde="text", validate=True):
    """origin_entity must be a absolutefilepath"""
    if validate:
        # dynamic validate method via origin_cde (eg 'validate_json', where cde = json)
        validate_standin()
    return

def from_relativefilepath(origin_entity, origin_cde="text", validate=True):
    """origin_entity must be a relativefilepath"""
    if validate:
        # dynamic validate method via origin_cde (eg 'validate_json', where cde = json)
        validate_standin()
    return

#endregion INPUT: from_file

#region #####     CONVERT: to_json                                        #####
###############################################################################
def to_json(origin_entity, origin_cde="text", validate=True):
    if 'json' in cde_index[origin_cde]['descendant_cdes']:
        return True, 1
    else:
        return False, 0

#endregion CONVERT: to_json

cde_index = load_cde_index()