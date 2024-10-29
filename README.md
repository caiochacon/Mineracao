# 📊 Projeto de Mineração com Streamlit

Bem-vindo ao repositório do projeto de Mineração Estatística de Dados! Este projeto foi desenvolvido para rodar um Dashboard que foi feito usando streamlit e plotly. Siga as instruções abaixo para configurar o ambiente e iniciar o projeto.

## Alunos

<table width=100%>
  <tr>
    <td align="center"><a href="https://github.com/caiochacon"><img style="border-radius: 50%;" src="assets\caio.jpeg" width="100px;" alt=""/><br /><sub><b>Caio Lucas</b></sub></a><br /><a href="https://github.com/caiochacon" title=""></a></td>
    <td align="center"><a href="https://github.com/talesnobre"><img style="border-radius: 50%;" src="assets\tales.png" width="100px;" alt=""/><br /><sub><b>Epitácio Neto</b></sub></a><br /><a href="https://github.com/talesnobre" title=""></a></td>
  </tr>
</table>

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


     - Criando a venv:
       ```bash
       python -m venv venv
       ```

     - Ativando a venv no Windows:

       ```bash
       .\venv\Scripts\activate
       ```

     - Ativando a venv no Linux/macOS:

       ```bash
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
