from tarefas import adicionar_tarefa, listar_tarefas, atualizar_status, excluir_tarefa, init_db

def menu():
    print("\n=== Sistema de Controle de Tarefas ===")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Atualizar Status")
    print("4. Excluir Tarefa")
    print("5. Sair")

if __name__ == '__main__':
    init_db()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                titulo = input("Título: ")
                descricao = input("Descrição: ")
                adicionar_tarefa(titulo, descricao)
                print("Tarefa adicionada com sucesso.")

            elif opcao == '2':
                tarefas = listar_tarefas()
                for t in tarefas:
                    print(f"[ID: {t[0]}] {t[1]} - {t[2]} | Status: {t[3]} | Criado em: {t[4]}")

            elif opcao == '3':
                id_tarefa = int(input("ID da Tarefa: "))
                novo_status = input("Novo status (pendente, em andamento, concluída): ")
                atualizar_status(id_tarefa, novo_status)
                print("Status atualizado.")

            elif opcao == '4':
                id_tarefa = int(input("ID da Tarefa: "))
                excluir_tarefa(id_tarefa)
                print("Tarefa excluída.")

            elif opcao == '5':
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print(f"Erro: {e}")
