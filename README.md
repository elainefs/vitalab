# VitaLab

## 📘 Sobre

Aplicação para gerenciamento de exames e consultas em clínicas médicas.

## 💻️ Tecnologias

- Python
- Django
- SQLite

## ✅ Funcionalidade

- [x] Solicitar exames
- [x] Visualizar resultados de exames
- [x] Cadastro de usuários

## ⚙️ Como usar

Para executar essa aplicação siga os seguintes passos:

1. Clone o repositório

```bash
git clone https://github.com/elainefs/vitalab.git

cd vitalab
```

2. Crie e ative um ambiente virtual

```bash
python3 -m venv .venv # Para Windows use: python -m venv .venv
source .venv/bin/activate  # Para Windows use: .venv\Scripts\activate
```

3. Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

4. Execute as migrações no banco de dados

```bash
python3 manage.py migrate
```

5. Crie um super usuário

```bash
python3 manage.py createsuperuser
```

6. Execute a aplicação

```bash
python3 manage.py runserver
```

A aplicação estará disponível em `http://localhost:8000`.

O gerenciamento pode ser feito através da interface do Django Admin em: `http://localhost:8000/admin/`

## 📄 Licença

Este projeto está sobre a licença MIT. Veja o arquivo LICENSE para mais informações.

---

Made with ❤️ by Elaine Ferreira
