# 🩺 MediFlow - Sistema Inteligente de Agendamento

> **Gestão de Consultas Médicas com Verificação de Conflitos e UI Moderna**

![Badge Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![Badge Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Badge FastAPI](https://img.shields.io/badge/FastAPI-Performance-009688?style=for-the-badge&logo=fastapi)
![Badge Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap%205-purple?style=for-the-badge&logo=bootstrap)

O **MediFlow** é um sistema completo para clínicas médicas que resolve o problema crítico de "double booking" (duplo agendamento). Com uma interface baseada em **Glassmorphism** e **Dark Mode**, ele oferece uma experiência visual limpa e tecnológica, garantindo que dois pacientes nunca sejam marcados para o mesmo médico no mesmo horário.

---

## 🚀 Funcionalidades Principais

### 📅 Agendamento Inteligente (Smart Booking)
* **Trava de Conflito:** O Backend verifica automaticamente se o médico já possui compromisso no horário solicitado antes de salvar.
* **Feedback Visual:** Alertas claros informam sucesso ou erro de conflito instantaneamente.

### 🎨 UI/UX Medical Clean
* **Glassmorphism:** Cards com efeito de vidro fosco e sombras suaves.
* **Dark Mode Completo:** Alternância de tema com um clique (persistência via LocalStorage).
* **Responsividade:** Funciona perfeitamente em Desktop e Mobile.

### 👨‍⚕️ Gestão de Profissionais
* **CRUD Completo:** Cadastre, Edite e Exclua médicos.
* **Interface Dinâmica:** Menus dropdown e formulários que se adaptam ao contexto (criação vs edição).

---

## 🛠️ Stack Tecnológica

### Backend
* **Python 3.x**
* **FastAPI:** Framework moderno e de alta performance.
* **SQLAlchemy:** ORM para manipulação do banco de dados SQLite.
* **Pydantic:** Validação de dados robusta.

### Frontend
* **HTML5 / CSS3:** Variáveis CSS para temas e efeitos de Blur.
* **Jinja2:** Renderização de templates no servidor.
* **Bootstrap 5:** Grid system e componentes visuais.
* **JavaScript (Vanilla):** Fetch API para comunicação assíncrona com o Backend.

---

## ⚙️ Como Rodar o Projeto

### Pré-requisitos
* Python 3.9 ou superior instalado.

### Passo a Passo

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/SEU-USUARIO/MediFlow.git](https://github.com/SEU-USUARIO/MediFlow.git)
    cd MediFlow
    ```

2.  **Crie o ambiente virtual (Recomendado)**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicie o Servidor**
    ```bash
    python -m uvicorn app.main:app --reload
    ```

5.  **Acesse no navegador**
    * **Sistema:** [http://localhost:8000](http://localhost:8000)
    * **Docs API:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📂 Estrutura do Projeto

```text
MediFlow/
│
├── app/
│   ├── main.py       # Rotas (API e Frontend)
│   ├── models.py     # Tabelas do Banco
│   ├── schemas.py    # Validação Pydantic
│   ├── crud.py       # Lógica de Banco e Conflitos
│   └── database.py   # Conexão SQLite
│
├── static/
│   ├── css/
│   │   └── style.css # Estilos (Dark Mode, Glassmorphism)
│   └── img/
│       └── favicon.png
│
├── templates/        # Telas HTML
│   ├── base.html
│   ├── index.html
│   ├── agendar.html
│   └── medicos.html
│
└── requirements.txt
```

👨‍💻 Autor
<div align="center">

<h3>Hiann Alexander Mendes de Oliveira</h3>

<p> 🎓 Estudante de Sistemas de Informação - IF Goiano (Campus Urutaí)


💻 Desenvolvedor Backend 


📍 Goiânia, Goiás </p>

<a href="https://www.linkedin.com/in/hiann-alexander" target="_blank"> <img src="https://img.shields.io/badge/LinkedIn-Conectar-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"> </a>

</div>
