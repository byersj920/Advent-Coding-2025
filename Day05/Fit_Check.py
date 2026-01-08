def Fit_Check (id_range, golden_range):

    if id_range['min'] <= golden_range['min'] and id_range['max'] >= golden_range['max']:
        golden_range = id_range
        return golden_range
    
    if id_range['min'] < golden_range['min'] and id_range['max'] <= golden_range['max'] and id_range['max'] >= golden_range['min']:
        golden_range['min'] = id_range['min']
        return golden_range
    
    if id_range['max'] > golden_range['max'] and id_range['min'] <= golden_range['max'] and id_range['min'] >= golden_range['min']:
        golden_range['max'] = id_range['max']
        return golden_range

    return 'Outside Range!'