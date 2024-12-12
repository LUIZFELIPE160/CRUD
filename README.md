Cadastro de Funcionários

![Captura de tela 2024-12-12 100301](https://github.com/user-attachments/assets/0c3ac549-44bb-4876-b878-f0f9f5511ccc)

Este é um projeto de gerenciamento de funcionários, utilizando PyQt5 para a interface gráfica e SQLite para o banco de dados.

Funcionalidades

Adicionar Funcionário: Permite adicionar novos funcionários ao banco de dados, incluindo informações como CPF, nome, idade, função, data de admissão, remuneração e observações.

Visualizar Funcionários: Mostra uma lista de todos os funcionários cadastrados no banco de dados.

Atualizar Dados: Atualiza informações de um funcionário selecionado.

Deletar Funcionário: Remove um funcionário do banco de dados.

Validação de CPF: Garante que o CPF digitado seja válido, com 11 dígitos formatados corretamente.

Tecnologias Utilizadas
Python: Linguagem principal do projeto.

PyQt5: Biblioteca para criação da interface gráfica.

SQLite: Banco de dados utilizado para armazenar os dados dos funcionários.

Instalação
Clone o repositório: git clone https://github.com/LUIZFELIPE160/CRUD.git
Navegue até o diretório do projeto: cd crud
Instale as dependências necessárias: pip install PyQt5
Execute o aplicativo: python main.py

Uso
Insira as informações do funcionário nos campos apropriados.

Clique no botão "Adicionar" para salvar o funcionário no banco de dados.

Selecione um funcionário na lista para atualizar ou deletar seus dados.

Use os botões "Atualizar" ou "Deletar" conforme necessário.

Validações Implementadas

CPF: O CPF deve conter exatamente 11 números. Caso contrário, uma mensagem de erro será exibida.

![Captura de tela 2024-12-12 134843](https://github.com/user-attachments/assets/9eddc9a1-7431-48f3-bd3c-788ce9b6185f)

Idade: Deve ser um número inteiro. Entradas inválidas também geram mensagens de erro.

![Captura de tela 2024-12-12 135104](https://github.com/user-attachments/assets/7b1bff86-479e-4434-acfa-d1262427d580)

Verificação de Existência: Antes de adicionar um funcionário, o sistema verifica se o CPF já está cadastrado no banco de dados.

![Captura de tela 2024-12-12 135242](https://github.com/user-attachments/assets/75364b4c-609d-4825-973c-02e75bb028da)



Contribuições são bem-vindas! Para contribuir:

Faça um fork do projeto.

Crie uma branch para sua funcionalidade ou correção:

git checkout -b minha-feature

Commit suas alterações:

git commit -m "Adiciona minha funcionalidade"

Envie para o repositório remoto:

git push origin minha-feature

Abra um Pull Request.
