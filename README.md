#  Backend Django - Instruções de Uso

Este documento contém as instruções para instalar, configurar e executar o backend do projeto desenvolvido em [Django](https://www.djangoproject.com/).

## Pré-requisitos

Antes de começar, certifique-se de que você tenha as seguintes ferramentas instaladas:

- [Python (versão 3.8 ou superior)](https://www.python.org/)
- [pip](https://pip.pypa.io/) (gerenciador de pacotes do Python)

## Clonando o Projeto

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/fundamentos-devops/to-do-backend.git
cd to-do-backend/
```

## Criando o Ambiente Virtual

Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS

venv\Scripts\activate  # Windows
```

## Instalando Dependências

Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## Configurando o Projeto

No diretório `contrib/`, você encontrará arquivos e exemplos úteis para configuração do ambiente.

Certifique-se de configurar as seguintes variáveis de ambiente:

- `DEBUG`: Define se o ambiente está em modo de desenvolvimento (`True`) ou produção (`False`).
- `ALLOWED_HOSTS`: Lista de domínios/IPs permitidos para acessar a aplicação.
- `DATABASE_URL`: URL de conexão com o banco de dados (por exemplo, PostgreSQL).

Você pode criar um arquivo `.env` na raiz do projeto com essas variáveis.  
Exemplo:

```env
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

> Dica: use o arquivo de exemplo disponível em `contrib/` para facilitar essa configuração.

## Executando o Projeto

Para rodar o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

O backend estará disponível por padrão em: [http://127.0.0.1:8000/api/v1/](http://127.0.0.1:8000/api/v1/)
