Este projeto utiliza FastAPI e SQLAlchemy para construir uma API REST que gerencia fornecedores, veículos, peças, compras e outros dados analíticos. Para começar a utilizar o projeto, siga as instruções abaixo.

# Requisitos

Certifique-se de ter os seguintes requisitos instalados no seu ambiente local:

- Python 3.7 ou superior
- PostgreSQL ou outro banco de dados compatível com SQLAlchemy

1. Clonar o repositório

Primeiro, clone o repositório para o seu ambiente local:

git clone <URL_DO_REPOSITORIO>

2. Criar e ativar um ambiente virtual

Para isolar as dependências do projeto, crie e ative um ambiente virtual:

No Windows:
bash
python -m venv venv
.\venv\Scripts\activate


No macOS/Linux:
python3 -m venv venv
source venv/bin/activate


3. Instalar as dependências

Instale as dependências do projeto:

pip install -r requirements.txt


4. Configurar variáveis de ambiente

Crie um arquivo .env na raiz do projeto para configurar suas variáveis de ambiente, como a string de conexão com o banco de dados. Um exemplo de conteúdo do arquivo .env:


CONN_STRING=postgresql+psycopg2://postgres:testeford@localhost:5432/postgres
SECRET_KEY=<SUA_CHAVE_SECRETA>


Substitua `<USUARIO>`, `<SENHA>`, `<BANCO_DE_DADOS>` e `<SUA_CHAVE_SECRETA>` pelas suas próprias configurações.

5. Executar o projeto:

Agora você pode iniciar o servidor de desenvolvimento com o Uvicorn.


uvicorn main:app --reload

Isso irá iniciar o servidor na URL http://127.0.0.1:8000 (Porta Padrão). Você poderá acessar a API diretamente no navegador ou através de ferramentas como Postman ou Insomnia.

Executar testes:

Se você desejar rodar os testes automatizados do projeto, execute o seguinte comando:

python -m pytest


Os testes serão executados e você verá o resultado no terminal.

# Endpoints disponíveis

- GET /suppliers/: Lista todos os fornecedores (com filtros opcionais).
- POST /suppliers/bulk: Cria múltiplos fornecedores de uma vez.
- GET /vehicles/: Lista todos os veículos.
- POST /vehicles/: Cria um novo veículo.
- GET /purchances/: Lista todas as compras.
- POST /purchances/: Cria uma nova compra.

Claro! Aqui está a continuação do texto:

---

Para mais detalhes sobre os endpoints, consulte a documentação automática da API acessando [http://127.0.0.1:8000/docs]. Dessa forma, o Swagger será exibido, permitindo que você visualize e interaja com os endpoints da API de maneira intuitiva. 

O Swagger oferece uma interface gráfica onde você pode testar as rotas diretamente no navegador, além de exibir informações detalhadas sobre cada uma delas, como parâmetros, respostas e códigos de status.


