# 💸 MoneyFlow

## 📌 Sobre

**MoneyFlow** é uma aplicação web simples desenvolvida em **Django** para controle financeiro pessoal. O sistema permite que cada usuário cadastre suas **categorias** e **transações**, organizando ganhos e gastos de forma clara e objetiva.

O projeto foi desenvolvido com foco **educacional e prático**, servindo como exercício de Django (models, forms, autenticação, views protegidas e templates), além de ser utilizável no dia a dia para controle básico de finanças.

Ideal para:

✅ Estudantes aprendendo Django
✅ Controle financeiro pessoal simples
✅ Projetos didáticos e portfólio

---
Funcionalidades

Autenticação

* Cadastro de usuário
* Login e logout
* Proteção de rotas com `login_required`
* Cada usuário vê **apenas seus próprios dados**

Categorias

* Cadastro de categorias personalizadas
* Descrição opcional definida pelo usuário
* Listagem apenas das categorias do usuário logado
* Mensagem amigável quando não há categorias cadastradas

Transações

* Cadastro de transações vinculadas a uma categoria
* Valores de entrada e saída
* Edição e exclusão de transações
* Proteção contra acesso a dados de outros usuários

---

Conceitos Aplicados

* Django ORM
* Relacionamento entre modelos (User → Categoria → Transações)
* `ModelForm`
* Views baseadas em função (FBV)
* Templates com `extends` e `block`
* CSS organizado por página
* Controle de acesso por usuário

---

## Conjunto de Tecnologias

| Camada         | Tecnologia   |
| -------------- | ------------ |
| Backend        | Django       |
| Linguagem      | Python 3.10+ |
| Frontend       | HTML5 + CSS3 |
| Banco de Dados | SQLite       |
| Autenticação   | Django Auth  |

---

## 🚀 Instalação

### Pré-requisitos

* Python 3.10+
* Git
* pip

### Passo 1: Clone o repositório

```bash
git clone https://github.com/seu-usuario/moneyflow.git
cd moneyflow
```

### Passo 2: Crie o ambiente virtual
Observação: o ambiente virtual (venv) não está versionado no repositório.
Recomenda-se criar um ambiente virtual antes de instalar as dependências.
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### Passo 3: Instale as dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Migrações

```bash
python manage.py migrate
```

### Passo 5: Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### Passo 6: Execute o servidor

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📖 Uso

1. Crie uma conta ou faça login
2. Cadastre suas categorias
3. Adicione transações vinculadas às categorias
4. Visualize, edite ou exclua seus registros

Cada usuário possui seu próprio ambiente isolado.

---


Segurança

* Proteção CSRF habilitada
* ORM do Django (previne SQL Injection)
* Acesso restrito por usuário
* Rotas protegidas por autenticação

---

Observações

Este projeto foi desenvolvido **para fins educacionais**, com foco em aprendizado prático de Django. O código pode ser reutilizado, adaptado e evoluído livremente.

---

Autor

Desenvolvido por Luis Carlos
Projeto de estudo com Django
