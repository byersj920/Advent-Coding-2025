def has_pattern(ID):
    stringy_ID = str(ID)
    id_size = len(stringy_ID)
    chunk_list = []
    pattern_check_results = False

    for num in range (1, id_size):
        number_check = id_size/num
        if number_check % 1 == 0:
            chunk_list.append(num)

    for num in chunk_list:
        chunk_start = 0
        chunk_end = num
        list_of_chunks = []
        has_pattern = True

        for chunk in range (0, id_size//num):
            added_chunk = stringy_ID[chunk_start: chunk_end]
            list_of_chunks.append(added_chunk)
            chunk_start += num
            chunk_end += num

        for chunk in list_of_chunks:
            if chunk != list_of_chunks[0]:
                has_pattern = False
        
        if has_pattern == True:
            pattern_check_results = True

    return pattern_check_results