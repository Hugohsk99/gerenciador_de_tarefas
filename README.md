# Gerenciador de Tarefas
# Descrição

Um aplicativo de gerenciamento de tarefas simples, no qual os usuários podem adicionar, editar, excluir e marcar tarefas como concluídas. Além disso, o aplicativo pode ter um cronômetro para rastrear o tempo gasto em cada tarefa e um sistema de pontuação baseado no desempenho do usuário.
Requisitos
1 -  Registro de Usuário
O sistema deve fornecer uma funcionalidade que permita aos usuários criar uma nova conta, inserindo um nome de usuário e senha únicos. Os detalhes do usuário devem ser validados e armazenados em um banco de dados para uso futuro.
2 -  Login de Usuário
O sistema deve permitir que os usuários acessem suas contas inserindo suas credenciais válidas de nome de usuário e senha. O processo de autenticação deve ser seguro e eficiente.
3 - Adição de Tarefas
Os usuários devem poder adicionar novas tarefas à sua lista de tarefas. Cada tarefa deve ser armazenada de maneira segura no banco de dados e ser facilmente acessível para visualização e edição.
4 - Requisito de Edição de Tarefas
Os usuários devem ter a capacidade de editar as informações de qualquer tarefa existente em sua lista. Isso pode incluir a alteração do nome da tarefa, descrição, prazo ou qualquer outra informação relevante.
5 - Exclusão de Tarefas
Deve haver uma funcionalidade que permita aos usuários remover tarefas de sua lista. A exclusão deve ser permanente e não deve deixar nenhum resíduo de dados no banco de dados.
6 - Conclusão de Tarefas
O sistema deve fornecer uma opção para marcar as tarefas como concluídas. Isso pode envolver a alteração do estado da tarefa e a exibição de uma indicação visual na interface do usuário.
7 - Requisito de Cronômetro
O sistema deve fornecer um cronômetro para rastrear o tempo que o usuário passa em cada tarefa. O cronômetro deve ser fácil de iniciar, pausar e parar, e o tempo total gasto em cada tarefa deve ser armazenado no banco de dados.
8 - Sistema de Pontuação
Para incentivar a produtividade, o sistema deve ter um sistema de pontuação. Os pontos podem ser concedidos com base na conclusão de tarefas, tempo gasto e outras métricas relevantes. O total de pontos de cada usuário deve ser armazenado e exibido na interface do usuário.
9 - Interface de Usuário
A interface do usuário deve ser amigável, intuitiva e esteticamente agradável. Deve ser fácil para os usuários novos e existentes navegarem e interagirem com as funcionalidades do sistema.
10 - Persistência de Dados
O sistema deve ter um banco de dados robusto para armazenar todas as informações do usuário e as tarefas. Deve garantir a persistência de dados entre as sessões e proteger a integridade e segurança dos dados.


# Prototipação
Casos de Uso

    -Usuários podem se registrar no sistema
    -    O usuário pode fornecer um nome de usuário e senha para criar uma nova conta.
-
    -Usuários podem fazer login no sistema
    -    Os usuários podem inserir suas credenciais de usuário para acessar o sistema.
-
    -Usuários podem adicionar novas tarefas
    -    Os usuários podem adicionar novas tarefas à lista de tarefas, fornecendo um nome para a tarefa.
-
    -Usuários podem editar tarefas existentes
    -    Os usuários podem editar o nome de uma tarefa existente selecionando a tarefa e fornecendo um novo nome.
-
    -Usuários podem excluir tarefas existentes
    -    Os usuários podem excluir uma tarefa existente selecionando a tarefa e pressionando o botão "Excluir Tarefa".
-
    -Usuários podem marcar tarefas como concluídas
    -    Os usuários podem marcar uma tarefa como concluída selecionando a tarefa e pressionando o botão "Marcar como Concluída". A tarefa será então atualizada para indicar que foi concluída.

# Mapeamento de Processos
1 - Registro de usuário:
Solicitação de detalhes do usuário
Fornecimento de detalhes pelo usuário
Validação dos detalhes do usuário
Criação da nova conta de usuário
Armazenamento dos detalhes do usuário no banco de dados
2 - Autenticação: 
Solicitação de credenciais do usuário
Fornecimento de credenciais pelo usuário
Validação das credenciais do usuário
Autenticação e concessão de acesso ao sistema

3 - Adição de Novas Tarefas
Solicitação de detalhes da nova tarefa
Fornecimento de detalhes da tarefa pelo usuário
Validação dos detalhes da tarefa
Adição da tarefa à lista de tarefas do usuário
Armazenamento da tarefa no banco de dados

4 - Edição de Tarefas Existentes
Seleção da tarefa a ser editada
Fornecimento dos detalhes atualizados da tarefa pelo usuário
Validação dos detalhes atualizados
Atualização dos detalhes da tarefa no banco de dados

5 - Exclusão de Tarefas
Seleção da tarefa a ser excluída
Confirmação da exclusão da tarefa pelo usuário
Remoção da tarefa da lista de tarefas do usuário no banco de dados

6 -  Conclusão de Tarefas
Seleção da tarefa a ser marcada como concluída
Marcação da tarefa como concluída pelo usuário
Atualização do status da tarefa no banco de dados
Cálculo dos pontos com base no tempo gasto e outras métricas
Atualização da pontuação do usuário

7 - Uso do Cronômetro
Início do cronômetro ao iniciar a tarefa
Parada do cronômetro ao concluir a tarefa
Cálculo do tempo total gasto na tarefa
Armazenamento do tempo gasto na tarefa no banco de dado

8 - Sistema de Pontuação
Conclusão de uma tarefa pelo usuário
Cálculo dos pontos com base no tempo gasto e outras métricas
Adição dos pontos ao total do usuário
Atualização da pontuação do usuário no banco de dados

# Codificação
React JS: Usado para construir a interface de usuário e seus componentes.
TypeScript: Garante a segurança de tipo no código para evitar possíveis erros.
Tailwind CSS: Fornece estilos e design para a interface do usuário.
Redux Toolkit: Gerencia o estado do aplicativo (como detalhes do usuário, lista de tarefas, etc.).
React Router DOM: Gerencia a navegação entre as diferentes páginas do aplicativo.
HTML: Estrutura o conteúdo básico da interface do usuário.
Redux Persist: Usado no sistema para manter o estado do aplicativo entre as sessões do navegador, permitindo a persistência de tarefas e informações de login do usuário.
# Protótipo de Interface (CANVAS)
![image](https://github.com/Hugohsk99/gerenciador_de_tarefas/assets/68088380/05f13352-f927-45be-9aa1-5b4908c24f6a)
![image](https://github.com/Hugohsk99/gerenciador_de_tarefas/assets/68088380/20a06e61-7716-4ebe-af41-0e541a8f99ac)
![image](https://github.com/Hugohsk99/gerenciador_de_tarefas/assets/68088380/ad78f345-144b-4615-a960-1a165bef0009)
![image](https://github.com/Hugohsk99/gerenciador_de_tarefas/assets/68088380/6890cb47-4942-4704-8348-9b408204353e)

# Modelo de négocios
![image](https://github.com/Hugohsk99/gerenciador_de_tarefas/assets/68088380/b6eca0ef-5a8b-4add-8caa-dfbc27ef2fac)

