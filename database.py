import sqlite3

def create_table():
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS funcionarios (
                        cpf TEXT PRIMARY KEY,
                        nome TEXT,
                        idade INTEGER,
                        funcao TEXT,
                        admissao TEXT,
                        remuneracao TEXT,
                        observacoes TEXT)''')
    conn.commit()
    conn.close()

def cpf_exists(cpf):
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM funcionarios WHERE cpf = ?', (cpf,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def add_func(cpf, nome, idade, funcao, admissao, remuneracao, observacoes):
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO funcionarios VALUES (?, ?, ?, ?, ?, ?, ?)', (cpf, nome, idade, funcao, admissao, remuneracao, observacoes))
    conn.commit()
    conn.close()

def select_func():
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM funcionarios')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_func(cpf):
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM funcionarios WHERE cpf = ?', (cpf,))
    conn.commit()
    conn.close()

def update_func(cpf, nome, idade, funcao, admissao, remuneracao, observacoes):
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE funcionarios SET nome = ?, idade = ?, funcao = ?, admissao = ?, remuneracao = ?, observacoes = ? 
                      WHERE cpf = ?''', (nome, idade, funcao, admissao, remuneracao, observacoes, cpf))
    conn.commit()
    conn.close()
