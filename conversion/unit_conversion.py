#!/usr/bin/env python3
'''Convert a variable with a given unit to another unit
Usage:
    ./unit_conversion.py input_value input_unit
    ./unit_conversion.py input_value input_unit output_unit

Example:
    ./unit_conversion.py 1 N kg*m/s/s 
'''
import sys


# The dictionary of units. Each unit is defined as 
# a tuple (value, kg, m, s), where value is the magnitude
# of the unit in the standard unit and kg, m and s are 
# the dimensions of the unit under standard units.
units = {
        'kg' : (1, 1, 0, 0),
        'm' : (1, 0, 1, 0),
        's' : (1, 0, 0, 1),

        'g' : (0.001, 1, 0, 0),
        'N' : (1, 1, 1, -2),
        }

def to_standard_units(value, positive_units, negative_units):
    '''Convert a value in a list of positive units
    and a list of negative units to the standard units.
    Return a tuple (value, kg, m, s).
    '''
    value_and_units_std = [value, 0, 0, 0]

    for u in positive_units:
        value_and_units_std[0] *= units[u][0]
        value_and_units_std[1] += units[u][1]
        value_and_units_std[2] += units[u][2]
        value_and_units_std[3] += units[u][3]

    for u in negative_units:
        value_and_units_std[0] /= units[u][0]
        value_and_units_std[1] -= units[u][1]
        value_and_units_std[2] -= units[u][2]
        value_and_units_std[3] -= units[u][3]

    return tuple(value_and_units_std)

def to_custom_unit(value_and_units_std, positive_units, negative_units):
    '''Convert a tuple (value, kg, m, s) to the
    value under a custom unit defined a list of positive_units
    and a list of negative_units.

    Return the value under the custom unit.
    '''
    value_and_units_std_rest = list(value_and_units_std) 
    value = value_and_units_std[0]

    for u in positive_units:
        value /= units[u][0]
        value_and_units_std_rest[1] -= units[u][1]
        value_and_units_std_rest[2] -= units[u][2]
        value_and_units_std_rest[3] -= units[u][3]

    for u in negative_units:
        value *= units[u][0]
        value_and_units_std_rest[1] += units[u][1]
        value_and_units_std_rest[2] += units[u][2]
        value_and_units_std_rest[3] += units[u][3]

    assert(value_and_units_std_rest[1] == 0)
    assert(value_and_units_std_rest[2] == 0)
    assert(value_and_units_std_rest[3] == 0)

    return value

def split_unit_string_to_positive_and_negative_lists(unit_string):
    '''Split a unit string to a list of positive and 
    negative units.
    '''
    # Add padding to the unit_string

    if not unit_string[0] in ['*', '/']:
        unit_string = '*' + unit_string

    # Get positive and negative units

    positive_units = []
    negative_units = []

    for start in range(len(unit_string)):
        if not unit_string[start] in ['*', '/']:
            continue

        stop = start + 1
        while stop < len(unit_string) and (not unit_string[stop] in ['*', '/']):
            stop += 1

        if unit_string[start] == '*':
            positive_units.append(unit_string[start + 1:stop])
        else:
            negative_units.append(unit_string[start + 1:stop])

    return positive_units, negative_units
   
def unit_number_to_string(unit, unit_number):
    '''Return a string of an unit given the 
    number of occurance of an unit.
    '''
    s = ''
    if unit_number > 0:
        for i in range(unit_number):
            s += '*' + unit
    elif unit_number < 0:
        for i in range(-unit_number):
            s += '/' + unit

    return s

if __name__ == '__main__':
    input_value = float(sys.argv[1])
    input_unit = sys.argv[2]
    output_unit = '' if len(sys.argv) < 4 else sys.argv[3]

    # Convert input unit to standard units

    input_positive_units, input_negative_units = split_unit_string_to_positive_and_negative_lists(input_unit)
    value_and_units_std = to_standard_units(input_value, input_positive_units, input_negative_units)

    if output_unit == '':
        output_unit += unit_number_to_string('kg', value_and_units_std[1])
        output_unit += unit_number_to_string('m', value_and_units_std[2])
        output_unit += unit_number_to_string('s', value_and_units_std[3])

    # Covert standard units to output unit

    output_positive_units, output_negative_units = split_unit_string_to_positive_and_negative_lists(output_unit)
    output_value = to_custom_unit(value_and_units_std, output_positive_units, output_negative_units)
    
    print('{0} {1} = {2} {3}'.format(input_value, input_unit, output_value, output_unit))
