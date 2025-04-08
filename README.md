# 🔧 Previsão de Preço de Pistões com Machine Learning

Este projeto tem como objetivo prever o preço de pistões com base no seu peso utilizando modelos de regressão linear robusta com `scikit-learn`. A aplicação foi desenvolvida tanto para testes no Google Colab quanto para uma interface interativa com `Streamlit`.

---

## 🧠 Tecnologias Utilizadas

- Python 3.x  
- Pandas  
- Scikit-learn  
- Streamlit  
- Openpyxl (para leitura de arquivos `.xlsx`)  
- Google Colab (para prototipagem e testes rápidos)

---

## 📁 Estrutura do Projeto

```
📂 projeto-pistoes/
├── StreamLit.py         # App interativo com Streamlit
├── Estudo.xlsx          # Base de dados de exemplo
├── ML.ipynb             # Versão do projeto testada no Google Colab
├── requirements.txt     # Lista de dependências
└── README.md            # Este arquivo
```

---

## ⚙️ Como Executar o Projeto

### 🖥️ Localmente (com Streamlit)

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode o app:
```bash
streamlit run app.py
```

4. O navegador será aberto automaticamente (ou acesse `http://localhost:8501`)

---

## 📊 Funcionalidades

- Upload de arquivos `.xlsx` com dados de peso e preço
- Limpeza automática de dados ausentes (NaN)
- Treinamento de modelo de regressão robusta (RANSAC)
- Previsão do preço com base em peso informado pelo usuário
- Interface intuitiva e responsiva com Streamlit

---

## 💡 Exemplo de Uso

```
Digite o peso do pistão (em kg): 1.850
→ O preço estimado do pistão é: R$ 36.42
```

---

## 🔬 Testes no Google Colab

Caso prefira testar online, o projeto também possui uma versão `.ipynb` compatível com Google Colab (`modelo_colab.ipynb`).

---

## 📦 Requisitos

Para garantir o funcionamento do projeto, instale as bibliotecas:

```bash
pip install pandas scikit-learn streamlit openpyxl
```

Ou utilize diretamente o `requirements.txt`.

---

## 👨‍💻 Autor

Desenvolvido por **Seu Nome Aqui**  
📧 Email: gabroreis@gmail.com 
🔗 [LinkedIn](https://www.linkedin.com/in/gabriel-reis-2457a5186/)

---

## 📝 Licença

Este projeto está sob a licença MIT.  
Consulte o arquivo `LICENSE` para mais informações.

