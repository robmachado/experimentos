import sqlite3
import json
import sys
import os
import rest

con = sqlite3.conect('ops.db')
cur = con.cursor()

# Este metodo deve atualizar os dados das tabelas locais op e tecelões
def update():
    data = rest.getAllOps()
    for linha in data:
        