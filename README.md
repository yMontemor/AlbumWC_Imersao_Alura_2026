# 🏆 Alura Album - Copa do Mundo 2026

Um álbum de figurinhas virtual interativo em 3D que celebra as quatro seleções semifinalistas da **Copa do Mundo FIFA de 2026** (Argentina, Inglaterra, Espanha e França), além de seções dedicadas aos palcos das decisões (estádios) e símbolos oficiais do torneio. Este projeto foi desenvolvido durante a **Imersão Alura: Arquitetura Web 2026**.

O projeto conta com uma interface moderna de alta fidelidade visual, com efeitos de virada de página realista, áudio interativo e integração dinâmica via API com backend usando FastAPI.

---

## 🚀 Tecnologias Utilizadas

* **HTML5:** Estruturação semântica das páginas e dos slots das figurinhas.
* **CSS3:** Sistema de design moderno com variáveis customizadas (temas por país), gradientes lineares e radiais, efeitos holográficos, animações e responsividade.
* **JavaScript:** Manipulação do DOM, consumo da API REST via Fetch API, renderização dinâmica das figurinhas, controle de áudio e interações do álbum.
* **[St.PageFlip](https://github.com/Nodlik/StPageFlip):** Biblioteca JS para simulação realista de livro/álbum 3D com física de arrastar e virar folhas.
* **FastAPI (Backend):** Servidor REST desenvolvido em FastAPI responsável por disponibilizar os dados e as imagens das figurinhas consumidas pelo frontend.

---

## 📁 Estrutura de Páginas do Álbum

* **Página 0: Capa** - Design estilizado com efeitos de glitch nos títulos, silhuetas de cards flutuantes e esfera 3D.
* **Página 1: Argentina (ARG)** - Apresenta jogadores como Lionel Messi (Estrela), Lautaro Martínez, Julián Álvarez, Emiliano Martínez e o técnico Lionel Scaloni.
* **Página 2: Inglaterra (ENG)** - Apresenta Jude Bellingham (Estrela), Harry Kane, Bukayo Saka, Pickford e o técnico Thomas Tuchel.
* **Página 3: Espanha (ESP)** - Apresenta Lamine Yamal (Estrela), Rodri, Nico Williams, Dani Olmo e o técnico Luis de La Fuente.
* **Página 4: França (FRA)** - Apresenta Kylian Mbappé (Estrela), Michael Olise, Ousmane Dembélé, Dayot Upamecano e o técnico Didier Deschamps.
* **Página 5: Palcos de Decisão (ROAD TO THE FINAL)** - Traz estádios que receberão os jogos das semifinais e final da Copa do Mundo (AT&T Stadium, Atlanta Stadium, MetLife Stadium, Hard Rock Stadium e o Logo Oficial).
* **Página 6: Mascotes e Símbolos (WORLD CUP 2026)** - Traz mascotes e símbolos do torneio (Maple do Canadá, Zayu do México, Clutch dos EUA, Troféu da Copa do Mundo FIFA e a bola oficial Trionda).
* **Página 7: Contracapa** - Finalização do álbum com código de barras simulado, resumo da edição especial e design temático com gradientes e curvas geométricas.

---

## 📁 Arquivos Principais

* **[index.html](frontend/index.html):** Estrutura HTML do álbum com todas as páginas, cabeçalhos, rodapés e os slots (`.sticker-slot`) de figurinhas numerados de #01 a #30.
* **[style.css](frontend/style.css):** Identidade visual premium baseada nas cores oficiais da FIFA 2026, com temas personalizados para cada página de acordo com a seleção correspondente, tipografia refinada e sombras profundas.
* **[app.js](frontend/app.js):** Lógica da aplicação, inicializando a biblioteca de virada de página, controlando a reprodução de efeitos sonoros, e realizando o consumo da API REST para carregar dinamicamente as figurinhas no álbum.

---

## 📂 Estrutura do Projeto

```text
backend/
├── figurinhas/
├── main.py
└── requirements.txt

frontend/
├── index.html
├── style.css
└── app.js
```

---

## ⚙️ Como Executar o Projeto

### 1. Iniciar o Backend (FastAPI)
O frontend consome as figurinhas a partir do servidor FastAPI local. Para executá-lo, acesse a pasta do backend no terminal, instale as dependências (caso não tenha feito ainda) e inicie o servidor:

```bash
# Entre na pasta do backend
cd backend

# Instale as dependências do projeto
pip install -r requirements.txt

# Inicie o servidor com Uvicorn
python -m uvicorn main:app --reload
```
> O servidor rodará por padrão em `http://localhost:8000`.

### 2. Executar o Frontend
Abra a pasta `frontend` utilizando uma extensão como o **Live Server** (VS Code/Antigravity) ou outro servidor HTTP local e acesse o arquivo `index.html`.

---

## 🎨 Funcionalidades Destacadas

* 📖 **Simulação Física de Páginas:** Arraste com o mouse ou clique nas setas laterais para virar as páginas do álbum com som de papel realista.
* ⚡ **Efeitos Visuais Premium:** Títulos com estilo de falha digital (glitch art) na capa e gradiente dourado na contracapa para melhor legibilidade contra o fundo temático.
* 🔌 **Alimentação Dinâmica:** Se o servidor backend estiver ativo, o álbum preenche os slots automaticamente com as fotos oficiais dos jogadores, estádios, mascotes e símbolos correspondentes aos números indicados nos slots.
* 🖼️ **Backend Dinâmico:** As imagens das figurinhas são disponibilizadas por uma API FastAPI, permitindo atualizar as figurinhas sem necessidade de modificar o código do frontend.
* 🌍 **Temas por Seleção:** Cada página utiliza uma identidade visual inspirada nas cores da seleção representada.

---

## 👨‍💻 Autor

Desenvolvido por **Gabriel Montemor** durante a **Imersão Alura – Arquitetura Web 2026**, com foco na aplicação prática de HTML, CSS, JavaScript e FastAPI na construção de uma aplicação web interativa.