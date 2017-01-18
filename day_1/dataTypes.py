def data_type(r):
  try:
    if  type(r) == str:
        return len(r)
    elif type (r) == bool:
        return r
    elif type (r) == int:
        if r>100:
            return 'more than 100'
        elif r<100:
            return  'less than 100'
        else:
            return 'equal to 100'

    elif type(r) ==list:
        if len(r) > 2:
            return r[2]
        else:
            return None
    else:
        return 'no value'
  except Exception as e:
    return 'Invalid entry'

    