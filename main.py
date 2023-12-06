import rest
import label

# verifica se está on line
# se sim
# busca dados de todas as ops pendentes e grava localmente em sqllite
# aguarda seleção da OP
# localiza os dados remotamente
data = rest.getop(4)

# se não
# localiza os dados localmente

# popula dados na interface

# recupera peso da balança
# salva os dados no servidor se estiver on line
# 


data["op_id"] = "4"
data["tecelao"] = "ROGERIO"
data["fio"] = "ZUNZIANG"
data["faccionista"] = "FIMACOM"
data["pL"] = "16.26"
data["pB"] = "16.26"

etiq = label.label(data)
print(etiq)