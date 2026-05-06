import pyodbc

conn = pyodbc.connect(
    "DRIVER={PostgreSQL Unicode};"
    "SERVER=localhost;"
    "PORT=5432;"
    "DATABASE=atividade_bd;"
    "UID=admin;"
    "PWD=admin;"
)

cursor = conn.cursor()

try:
    cursor.execute("""
        INSERT INTO projeto (nome, lider)
        VALUES (?, ?)
    """, ("Projeto Teste", "Líder Inicial"))

    conn.commit()
    print("✔ Projeto inserido com sucesso!")

except Exception as e:
    print("Erro ao inserir projeto:", e)

try:
    cursor.execute("""
        INSERT INTO atividade (titulo, descricao, projeto_id)
        VALUES (?, ?, ?)
    """, ("Nova atividade", "Descrição da atividade", 1))
    
    conn.commit()
    print("✔ Atividade inserida com sucesso!")

except Exception as e:
    print("Erro ao inserir:", e)

try:
    cursor.execute("""
        UPDATE projeto
        SET lider = ?
        WHERE id = ?
    """, ("João Silva", 1))
    
    conn.commit()
    print("✔ Líder atualizado com sucesso!")

except Exception as e:
    print("Erro ao atualizar:", e)

try:
    cursor.execute("""
        SELECT p.nome AS projeto, a.titulo AS atividade
        FROM projeto p
        LEFT JOIN atividade a ON a.projeto_id = p.id
        ORDER BY p.nome
    """)

    print("\n📋 Projetos e suas atividades:\n")

    for row in cursor.fetchall():
        print(f"Projeto: {row.projeto} | Atividade: {row.atividade}")

except Exception as e:
    print("Erro ao listar:", e)

conn.close()