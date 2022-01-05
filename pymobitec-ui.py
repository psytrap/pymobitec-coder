import eel


eel.init('web')

@eel.expose    
def decode_python(encoded):
    print("Decoding")
    ret = "Decodeing" +"\n"
    ret += encoded + "\n"
    return ret

eel.start('main.html')
