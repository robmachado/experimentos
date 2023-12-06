import sqlite3

con = sqlite3.conect('ops.db')
cur = con.cursor()


# Este método de sincronizar os dados das peças com o ERP e remover os registros já sincronizados
def sync():
    # procurar registros ainda não sincronizados
    query = """ SELECT * FROM label WHERE flag_sync = 0; """
    cur.execute(query)
    for linha in cur.fetchall():
        # para cada linha enviar para o ERP