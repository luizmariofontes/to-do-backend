
# Backend Django - To-Do List

Este documento contém as instruções para instalar, configurar e executar o backend do projeto **To-Do List**, desenvolvido em **Django**.

---

## Pré-requisitos

Antes de começar, certifique-se de que você tenha as seguintes ferramentas instaladas:

- **Python** (versão 3.8 ou superior)
- **pip** (gerenciador de pacotes do Python)
- **Docker** (opcional, para execução em containers)

---

## Clonando o Projeto

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/luizmariofontes/to-do-backend.git
cd to-do-backend/
```

---

## Criando o Ambiente Virtual

Crie e ative um ambiente virtual:

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Instalando Dependências

Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

---

## Configurando o Projeto

Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias.  
### Exemplo de `.env`:

```env
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

---

## Executando o Projeto

### Ambiente de Desenvolvimento (Local)

Para rodar o servidor de desenvolvimento do Django:

```bash
python manage.py migrate
python manage.py runserver
```

O backend estará disponível em:  
`http://127.0.0.1:8000/api/v1/`

---

## 🐳 Executando com Docker

### Pré-requisitos:

- Docker

### Passos:

1. **Build da imagem Docker**

```bash
docker build -t to-do-backend .
```

2. **Executando o container**

```bash
docker run -p 8000:8000 --env-file .env to-do-backend
```

> **Obs:**  
O arquivo `.env` será utilizado para passar as variáveis de ambiente.

3. **Acessando a API**

A API estará disponível em:  
`http://localhost:8000/api/v1/`

---

## Banco de Dados

- **SQLite** é utilizado por padrão no ambiente de desenvolvimento.
- Para uso com PostgreSQL ou outro banco, modifique a variável `DATABASE_URL` no `.env`.

Exemplo de `DATABASE_URL` para PostgreSQL:

```env
DATABASE_URL=postgres://user:password@host:port/dbname
```

---

## Outras informações

- Para aplicar as migrações no Docker, o entrypoint do container já executa `python manage.py migrate`.
- Caso use banco externo (como PostgreSQL), certifique-se de que ele esteja acessível ao container.