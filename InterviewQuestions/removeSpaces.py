def remove_special_character(s):
    return ''.join(char for char in s if char.isalnum() or char.isspace())
    
print(remove_special_character("vdhdic  ifjd938 sdsd@ sdif&  S#$%^&*()"))