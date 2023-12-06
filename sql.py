from datetime import datetime
from peewee import *

class Label(Model):
    id = IntegerField(),
    codprod = TextField(),
    produto = TextField(),
    instrucao = TextField(),
    comentarios = TextField(),
    maquina = TextField(),
    qtdsol = FloatField(),
    qtdprod = FloatField(),
    sequencial = IntegerField(default=1),
    numero = IntegerField(),
    faccionista = TextField(),
    fio = TextField()


def create(cur):
    
    conn = sqlite3.conect('ops.db')
    cur = conn.cursor()
    
    #id integer PRIMARY KEY, //ordem_producao.id
    #codprod text NOT NULL, //produtos.codigo
    #produto text NOT NULL, //produtos.resumido
    #instrucao text, //produto_producoes.instrucao
    #comentarios text, //ordem_producao.comentarios
    #maquina text NOT NULL, //maquinas.codigo
    #qtdsol real NOT NULL, //ordem_producao.qtdade_produzir
    #qtdprod real DEFAULT 0 NOT NULL, //ordem_producao.qtdade_produzida
    #sequencial integer DEFAULT 1 NOT NULL, //ordem_producao_pecas.sequencial (max)
    #numero integer NOT NULL, //op + ??? (seq)
    #faccionista text NOT NULL, //parceiros.fantasia (substr)
    #fio text //????

    # trazer todas as op em aberto
    sql_create_op = """ CREATE TABLE IF NOT EXISTS ops (
        id integer NOT NULL,
        codprod text NOT NULL,
        produto text NOT NULL,
        instrucao text,
        comentarios text,
        maquina text NOT NULL,
        qtdsol real NOT NULL,
        qtdprod real DEFAULT 0 NOT NULL,
        sequencial integer DEFAULT 1 NOT NULL,
        numero integer NOT NULL,
        faccionista text NOT NULL,
        fio text
    );
    
    CREATE UNIQUE uop ON ops(id);
    
    """

    # trazer os tecelões apenas os ativos id e nome
    sql_create_tecelao = """ CREATE TABLE IF NOT EXISTS teceloes ( 
        id integer NOT NULL,
        nome text NOT NULL
    );
    
    CREATE UNIQUE utec ON teceloes(id);
    
    """

    # salvar antes de enviar para a API 
    sql_create_label = """ CREATE TABLE IF NOT EXISTS labels (
        op_id integer NOT NULL,
        numero integer NOT NULL,
        sequencial integer DEFAULT 1 NOT NULL,
        codprod text NOT NULL,
        produto text NOT NULL,
        maquina text NOT NULL,
        tecelao_id integer NOT NULL,
        tecelao text NOT NULL,
        defeitos integer DEFAULT 0,
        comentario text,
        posicao text,
        pL real NOT NULL,
        tara real DEFAULT 0,
        pB real NOT NULL,
        fio text,
        flag_print BOOLEAN DEFAULT FALSE,
        flag_sync BOOLEAN DEFAULT FALSE
    ); 
    
    CREATE UNIQUE unum ON labels(numero);
    CREATE INDEX isync ON labels(flag_sync);
    CREATE INDEX iprint ON labels(flag_print);
    
    """

    cur.execute(sql_create_op)
    cur.execute(sql_create_tecelao)
    cur.execute(sql_create_label)
    conn.close()
    
# registra a peça localmente    
def salvarLabel(data):
    conn = sqlite3.conect('ops.db')
    cur = conn.cursor()
    query = """ INSERT INTO labels (op_id, numero, sequencial, codprod, produto, maquina, tecelao_id, tecelao, defeitos, comentario, posicao, pL, tara, pB, fio, flag_print, flag_sync)
    VALUES (?,?,?,?,?,?,?,?,??,?,?,?,?,?,?); """
    cur.execute(query, data["op_id"],data["numero"],data["sequencial"],data["codprod"],data["produto"],data["maquina"],data["tecelao_id"],data["tecelao"],data["defeitos"],data["comentario"],data["posicao"],data["pL"],data["tara"],data["pB"],data["fio"],data["flag_print"],data["flag_sync"])
    conn.commit()
    conn.close()

# recupera os dados das peças conforme o filtro aplicado
def getLabel(filter):
    conn = sqlite3.conect('ops.db')
    cur = conn.cursor()
    query = """ SELECT * FROM labels WHERE """
    