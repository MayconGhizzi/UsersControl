# UsersControl

Construir um programa "UsersControl" em modo console que, ao receber as seguintes entradas faça:
- add: Adiciona um novo User (Objeto User), pergunte "Nome" e  "Email" e se realizado com sucesso retorne o ID cadastrado;
- list: Lista os usuários cadastrados: ID | Nome | Email;
- rm: Apaga um usuário cadastrado, necessita do parâmetro ID para deletar um User;
- export: Exporta os dados para um arquivo físico no computador;
- import: Importa de um arquivo físico "previamente" exportado, nessa opção ele deve verificar se existem Users, caso sim: pergunte se deseja "substituir" os cadastros existentes ou se deseja "mesclar" à os Users já existentes;

Para termos um padrão nos arquivos que vamos exportar, vamos definir o seguinte:
- o nome do arquivo a ser gerado/importado sempre será users.txt;
- deverão ficar na mesma pasta onde o programa está sendo executado;
- para delimitar os atributos de um User, usaremos o caracter "," (vírgula);
- para delimitar um Objeto User inteiro usaremos ";" (ponto e vírgula) em um nova linha;
- ex.:
1,Jose,jose@gmail.com;
2,Maria,maria@gmail.com;
- espaços em branco serão ignorados nos atributos ID e Email, e ignorados no início e final do atributo Nome;
