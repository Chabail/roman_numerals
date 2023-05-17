def roman_num(num):

    result = "I" * num
    result=result.replace("IIIII","V")
    result=result.replace("IIII","IV")
    
    return result
