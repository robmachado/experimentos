import sys

def label(array):
    
    
    text_file = open("./produto_cru.dat", "r")
    #read whole file to a string
    data = text_file.read()
    #close file
    text_file.close()

    data = data.replace("{peca}", array['numero'])
    data = data.replace("{cod_produto}", array['codprod'])
    data = data.replace("{lote}", array["op_id"])
    data = data.replace("{faccionista}", array["faccionista"])
    data = data.replace("{nometec}", array["tecelao"])
    data = data.replace("{pL}", array["pL"])
    data = data.replace("{pB}", array["pB"])
    data = data.replace("{marcafio}", array["fio"])

    return data