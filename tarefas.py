import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT DEFAULT 'pendente',
            data_criacao TEXT
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_tarefa(titulo, descricao):
    if not titulo.strip():
        raise ValueError("O título da tarefa não pode estar vazio.")
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO tarefas (titulo, descricao, data_criacao) VALUES (?, ?, ?)', (titulo, descricao, data))
    conn.commit()
    conn.close()

def listar_tarefas():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tarefas')
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

def atualizar_status(id_tarefa, novo_status):
    if novo_status not in ['pendente', 'em andamento', 'concluída']:
        raise ValueError("Status inválido.")
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tarefas SET status = ? WHERE id = ?', (novo_status, id_tarefa))
    conn.commit()
    conn.close()

def excluir_tarefa(id_tarefa):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id_tarefa,))
    conn.commit()
    conn.close()
