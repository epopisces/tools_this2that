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

import argparse, os, re, csv

import gallery

#TODO Well, interesting conundrum.  Some T2T functions will only need one input. 
#TODO Some need two (some dependency of the output, eg a filepath).  
#TODO Is there a good way to designate when a func is one vs the other?

# the below is a thought exercise for another time.  Right now I am focused on 'Entity' for conversion,
# not master_entity for correlation (which is what I started to brainstorm)
# master_entity = {
#     'descendant_entities': [entity1: {ancestor_entity: master_entity, attrib1: value, attrib2: value}, entity2]
# }

class Entity():
    """
    Represents an entity with a defined type (cde)
    Includes a number of helpful retrieval, output, validation, and conversion utilities
    
    Arguments:
        entity (str, optional):     the entity object passed during init
        cde (str, optional):        the cde of the entity object passed during init
    
    Attributes:
        entity              (str)   the current entity object being handled
        cde                 (str)   the cde of the current entity object
        init_entity         (str)   the entity object passed during init
        init_cde            (str)   the cde of the entity object passed during init
    """

    def __init__(self, entity=False, cde=False):
        self.entity = self.init_entity = entity
        self.cde = self.init_cde = cde

        self.cde_index = self.load_cde_index()
        return
    
    def load_cde_index(self):
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

        #TODO put the below code in a wrapper that auto-converts.  Call it 'resolve' or something like that
        # def resolve(self): # could go in init, once resolving is something we want to do every time
        #     if self.term_cde == self.master_cde:
        #         self.master_term = self.term

        #     else:
        #         self.obj_attrs[self.term_cde] = self.term
        
        # if self.cde_index_list[origin_cde]['master_cde'].split(";")[0] == "Tail" or "":
        #     print(f"{origin_entity} has no currently derivable master") #TODO error logging
        #     return "error"


    @staticmethod
    def retrieve(origin_entity, origin_cde="string", validate=False):
        """"""
        #TODO logging debug here f"retreiving {origin_cde} from {origin_etntity}"

        func_name = f'from_{origin_cde}'
        gallery_func = getattr(gallery, func_name, None)

        try:
            retrieved_obj, operation = gallery_func(origin_entity)
        except TypeError:
            print(f"{func_name} not yet defined in the gallery module") #TODO error logging
            status = 0
            raise NotImplementedError(f"{func_name} not yet defined in the gallery module")
            pass
        else:
            if operation == 0:
                print(f"{func_name} threw an error, unable to retrieve {origin_cde}") #TODO error logging

        return retrieved_obj

    @staticmethod
    def output(origin_entity, target_cde, origin_cde='string', validate=False):
        """"""
        #TODO logging debug here f"received {origin_cde} targeting {target_cde}"

        func_name = f'to_{target_cde}'
        gallery_func = getattr(gallery, func_name, None)

        try:
            derived_cdes, operation = gallery_func(origin_entity)
        except TypeError:
            print(f"{func_name} not yet defined in the gallery module") #TODO error logging
            status = 0
            raise NotImplementedError(f"{func_name} not yet defined in the gallery module")
            pass
        else:
            if operation == 0:
                print(f"{func_name} threw an error, unable to derive {target_cde}") #TODO error logging

        return(derived_cdes)
  
    @staticmethod
    def convert(origin_entity, origin_cde, target_cde, validate=False):
        """converts origin_entity of type origin_cde to type target_cde, returning [target_entity]"""
        #TODO logging debug here f"received {origin_cde} targeting {target_cde}"

        func_name = f'to_{target_cde}'
        gallery_func = getattr(gallery, func_name, None)

        try:
            derived_cdes, operation = gallery_func(origin_entity)
        except TypeError:
            print(f"{func_name} not yet defined in the gallery module") #TODO error logging
            status = 0
            raise NotImplementedError(f"{func_name} not yet defined in the gallery module")
            pass
        else:
            if operation == 0:
                print(f"{func_name} threw an error, unable to derive {target_cde}") #TODO error logging

        return derived_cdes


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
    entity = "test_string"
    cde = "string"
    eo = Entity(entity, cde)
    eo.convert(eo.entity, eo.cde, 'json')