# 🏆 Alura Album - Copa do Mundo Tech

Um álbum de figurinhas virtual interativo em 3D celebrando os gigantes e pioneiros da tecnologia (Inteligência Artificial, Linguagens de Programação, Sistemas Operacionais, etc.). Este projeto foi desenvolvido como parte da **Imersão Alura: Arquitetura Web 2026**.

O projeto conta com uma interface moderna e futurista de alta fidelidade visual, com efeitos de virada de página realista (Page Flip), áudio interativo e integração dinâmica via API com um backend em FastAPI.

---

## 🚀 Tecnologias Utilizadas

* **HTML5:** Estruturação semântica das páginas e dos slots das figurinhas.
* **CSS3 (Vanilla):** Sistema de design moderno com variáveis customizadas, gradientes neon, efeitos holográficos, animações e responsividade.
* **JavaScript (ES6):** Manipulação de DOM, integração assíncrona com o backend via Fetch API e controle de áudio.
* **[St.PageFlip](https://github.com/Nodlik/StPageFlip):** Biblioteca JS para simulação realista de livro/álbum 3D com física de arrastar e virar folhas.
* **FastAPI (Backend):** Servidor local responsável por disponibilizar os dados e as imagens das figurinhas.

---

## 📁 Estrutura de Arquivos Principais

* **[index.html](index.html):** Contém toda a estrutura HTML do álbum, definindo a capa, contracapa e as páginas internas de cada categoria técnica com seus respectivos slots (`.sticker-slot`) de figurinhas.
* **[style.css](style.css):** Define a identidade visual premium (tema escuro, sombras dinâmicas, tipografia do Google Fonts e animações fluidas).
* **[app.js](app.js):** Controla a lógica da aplicação, inicializando a biblioteca de virada de página, controlando a reprodução de efeitos sonoros, e realizando o consumo da API REST para colar as figurinhas coletadas em tempo real.

---

## ⚙️ Como Executar o Projeto

### 1. Iniciar o Backend (FastAPI)
O frontend consome as figurinhas a partir do servidor FastAPI local. Para executá-lo, acesse a pasta do backend no terminal e inicie o servidor:

```bash
# Entre na pasta correspondente ao dia/etapa do backend
cd backend/dia-3

# Inicie o servidor com Uvicorn
uvicorn main:app --reload
```
> O servidor rodará por padrão em `http://localhost:8000`.

### 2. Executar o Frontend
Basta abrir o arquivo **[index.html](index.html)** diretamente no seu navegador ou utilizar uma extensão como o **Live Server** no VS Code para servir os arquivos estáticos.

---

## 🎨 Funcionalidades Destacadas

* 📖 **Simulação Física de Páginas:** Arraste com o mouse ou clique nas setas laterais para virar as páginas do álbum com som de papel realista.
* ⚡ **Efeitos Visuais Premium:** Títulos com estilo de falha digital (glitch art) e gradientes lineares com compatibilidade total entre navegadores.
* 🔌 **Alimentação Dinâmica:** Se o servidor backend estiver ativo, o álbum preenche os slots automaticamente com as fotos oficiais dos pioneiros da tecnologia correspondentes aos números indicados nos slots.
