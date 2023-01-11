def circulate_through_array(array_position, array_length):
    if array_position > array_length-1:
        array_position = 0
    elif array_position < 0:
        array_position = array_length-1
    return array_position