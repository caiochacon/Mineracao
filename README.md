# 📊 Projeto de Mineração com Streamlit

Bem-vindo ao repositório do projeto de Mineração Estatística de Dados! Este projeto foi desenvolvido para rodar um Dashboard que foi feito usando streamlit e plotly. Siga as instruções abaixo para configurar o ambiente e iniciar o projeto.

## 🚀 Começando

Essas instruções ajudarão você a configurar o ambiente necessário para rodar o projeto em sua máquina local.

### 📋 Pré-requisitos

- **Python** versão 3.6 ou superior deve estar instalado.
- Um ambiente virtual é recomendado para isolar as dependências do projeto.

### 📦 Instalando

1. **Clone o repositório e configure o ambiente virtual:**

   - Clone o repositório:

     ```bash
     git clone https://github.com/caiochacon/Mineracao.git
     cd Mineracao
     ```

2. **Crie e ative o ambiente virtual para instalar as dependências apenas nele:**

     - No Windows:

       ```bash
       python -m venv venv
       .\venv\Scripts\activate
       ```

     - No Linux/macOS:

       ```bash
       python -m venv venv
       source venv/bin/activate
       ```

3. **Instale as dependências:**

     ```bash
     pip install -r requirements.txt
     ```

### ▶️ Rodando a Aplicação

Com as dependências instaladas, você pode iniciar a aplicação usando o comando:

```bash
streamlit run app.py
