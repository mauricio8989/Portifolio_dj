# Portifolio

Neste projeto Apresentarei tudo que aprendi no decorrer desses anos. <br>
Aqui eu apresento meus principais projetos representando as principais tecnologias que domino até o momento.

## Índice

- [Portifolio](#portifolio)
  - [Índice](#índice)
  - [Instalação](#instalação)
  - [Estrutura de Pastas](#estrutura-de-pastas)
  - [Descrição](#descrição)
  - [Dependências](#dependências)
  - [Contribuições](#contribuições)

## Instalação

Para configurar este projeto em sua máquina local, siga estes passos:

1. Clone o repositório:

   ```bash
   git clone https://github.com/mauricio8989/portifolio_dj.git
   ```

2. Navegue até o diretório do projeto:

    ```bash
    cd portifolio_dj
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt

4. Aplique as migrações:

    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário (opcional):

    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

## Estrutura de Pastas

Este é um projeto Django básico que inclui um aplicativo de blog. Aqui está a estrutura de pastas do projeto:

## Descrição

- `manage.py`: É um utilitário de linha de comando que permite interagir com o projeto Django de várias maneiras.
- `portifolio/__init__.py`: Este é um arquivo vazio que diz ao Python que este diretório deve ser considerado um pacote Python.
- `portifolio/settings.py`: Configurações para o projeto Django.
- `portifolio/urls.py`: As declarações de URL para este projeto Django.
- `portifolio/asgi.py`: Ponto de entrada para servidores ASGI compatíveis para servir seu projeto.
- `portifolio/wsgi.py`: Ponto de entrada para servidores WSGI compatíveis para servir seu projeto.
- `blog/`: Esta pasta contém o aplicativo de blog que criamos.
- `blog/migrations/`: Esta pasta inclui arquivos de migração do banco de dados.
- `blog/__init__.py`: Este é um arquivo vazio que diz ao Python que este diretório deve ser considerado um pacote Python.
- `blog/admin.py`: Aqui você pode registrar seus modelos para que eles sejam incluídos no site de administração do Django.
- `blog/apps.py`: Este é um arquivo de configuração para o aplicativo de blog.
- `blog/models.py`: Aqui você define os dados do seu aplicativo.
- `blog/tests.py`: Aqui você pode adicionar testes para o seu aplicativo.
- `blog/views.py`: Aqui você define as visualizações para o seu aplicativo.

Espero que isso ajude a entender a estrutura do projeto Django!

## Dependências

asgiref==3.8.1 <br>
Django==5.0.6 <br>
sqlparse==0.5.0 <br>
tzdata==2024.1

## Contribuições

Contribuições são bem-vindas! Siga estes passos para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie um novo branch (`git checkout -b feature`)
3. Faça suas alterações
4. Faça o commit das suas alterações (`git commit -am 'Adicionar nova funcionalidade'`)
5. Envie o branch (`git push origin feature`)
6. Crie um pull request
