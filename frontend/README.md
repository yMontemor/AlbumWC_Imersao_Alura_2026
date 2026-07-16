# 🏆 Alura Album - Copa do Mundo 2026

Um álbum de figurinhas virtual interativo em 3D celebrando as quatro seleções semifinalistas da **Copa do Mundo FIFA de 2026** (Argentina, Inglaterra, Espanha e França), além de uma seção especial dedicada aos craques da tecnologia e educadores da Alura (**Brasil - Seleção Tech**). Este projeto foi desenvolvido como parte da **Imersão Alura: Arquitetura Web 2026**.

O projeto conta com uma interface moderna e futurista de alta fidelidade visual, com efeitos de virada de página realista (Page Flip), áudio interativo e integração dinâmica via API com um backend em FastAPI.

---

## 🚀 Tecnologias Utilizadas

* **HTML5:** Estruturação semântica das páginas e dos slots das figurinhas.
* **CSS3 (Vanilla):** Sistema de design moderno com variáveis customizadas (temas por país), gradientes lineares e radiais, efeitos holográficos, animações e responsividade.
* **JavaScript (ES6):** Manipulação de DOM, integração assíncrona com o backend via Fetch API e controle de áudio.
* **[St.PageFlip](https://github.com/Nodlik/StPageFlip):** Biblioteca JS para simulação realista de livro/álbum 3D com física de arrastar e virar folhas.
* **FastAPI (Backend):** Servidor local responsável por disponibilizar os dados e as imagens das figurinhas.

---

## 📁 Estrutura de Páginas do Álbum

* **Página 0: Capa** - Design estilizado com efeitos de glitch nos títulos, silhuetas de cards flutuantes e esfera 3D.
* **Página 1: Argentina (ARG)** - Apresenta jogadores como Lionel Messi (Estrela), Lautaro Martínez, Julián Álvarez, Emiliano Martínez e o técnico Lionel Scaloni.
* **Página 2: Inglaterra (ENG)** - Apresenta Jude Bellingham (Estrela), Harry Kane, Bukayo Saka, Pickford e o técnico Thomas Tuchel.
* **Página 3: Espanha (ESP)** - Apresenta Lamine Yamal (Estrela), Rodri, Nico Williams, Dani Olmo e o técnico Luis de La Fuente.
* **Página 4: França (FRA)** - Apresenta Kylian Mbappé (Estrela), Michael Olise, Ousmane Dembélé, Dayot Upamecano e o técnico Didier Deschamps.
* **Páginas 5 e 6: Brasil - Seleção Tech (BRA)** - Seção especial trazendo a equipe da Alura, criadores e educadores de tecnologia (Paulo Silveira, Guilherme Silveira, Gustavo Guanabara, Maurício Aniche, Andre David, Guilherme Lima, Gi Space Coding, Vinicius Neves, Rafaela Ballerini, e você!).
* **Página 7: Contracapa** - Finalização do álbum com código de barras simulado, resumo da edição especial e design temático com gradientes e curvas geométricas.

---

## 📁 Arquivos Principais

* **[index.html](index.html):** Estrutura HTML do álbum com todas as páginas, cabeçalhos, rodapés e os slots (`.sticker-slot`) de figurinhas numerados de #01 a #30.
* **[style.css](style.css):** Identidade visual premium baseada nas cores oficiais da FIFA 2026, com temas personalizados para cada página de acordo com a seleção correspondente, tipografia refinada e sombras profundas.
* **[app.js](app.js):** Lógica da aplicação, inicializando a biblioteca de virada de página, controlando a reprodução de efeitos sonoros, e realizando o consumo da API REST para colar as figurinhas coletadas em tempo real.

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
* ⚡ **Efeitos Visuais Premium:** Títulos com estilo de falha digital (glitch art) na capa e gradiente dourado na contracapa para melhor legibilidade contra o fundo temático.
* 🔌 **Alimentação Dinâmica:** Se o servidor backend estiver ativo, o álbum preenche os slots automaticamente com as fotos oficiais dos jogadores e educadores correspondentes aos números indicados nos slots.
