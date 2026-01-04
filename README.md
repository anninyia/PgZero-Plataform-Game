# PgZero Platform Game

## 📌 Descrição do Projeto

Este projeto foi desenvolvido como parte do **Teste de Python para Tutores (2029)**. Trata-se de um jogo do gênero **Platformer**, criado utilizando exclusivamente a biblioteca **PgZero**, respeitando todas as regras e restrições definidas no teste. Além disso, tem fins de estudo pessoal.

O jogo apresenta um menu principal interativo, música de fundo, efeitos sonoros, animações de sprites e inimigos com comportamento próprio, demonstrando domínio de lógica de jogos, organização de código e boas práticas em Python.

Todos os arquivos de sons foram retirados do jogo DELTARUNE, criado por Toby Fox.

Todos os sprites são autorais.

---

## 🎮 Funcionalidades

- Menu principal com botões clicáveis:
  - Iniciar jogo;
  - Ligar/Desligar sons e música;
  - Sair do jogo.
- Música de fundo;
- Efeito sonoro de pulo;
- Personagem principal com:
  - Gravidade;
  - Pulo;
  - Movimento lateral;
  - Animação idle e de caminhada.
- Inimigos perigosos:
  - Movimento automático;
  - Limitação de território;
  - Animação contínua.
- Colisão entre herói e inimigos (reinicia o jogo).

---

## 🕹️ Controles

- **A** → mover para a esquerda
- **D** → mover para a direita
- **ESPAÇO** → pular
- **Mouse** → interagir com o menu

---

## 🗂️ Estrutura do Projeto

```bash
Python/
├── main.py
├── images/
│   ├── background.png
│   ├── hero_idle_0.png
│   ├── hero_idle_1.png
│   ├── hero_walk_0.png
│   ├── hero_walk_1.png
│   ├── enemy_idle_0.png
│   ├── enemy_idle_1.png
│   ├── enemy_walk_0.png
│   └── enemy_walk_1.png
├── sounds/
│   └── jump.wav
└── music/
    └── music.mp3
```

---

## 🧰 Tecnologias Utilizadas

- **Python 3**
- **PgZero**
- Bibliotecas permitidas:
  - `random`
  - `math`
  - `pygame.Rect` (exceção permitida)

Nenhuma outra biblioteca externa foi utilizada.

---

## ▶️ Como Executar

1. Certifique-se de ter o PgZero instalado:

   ```bash
   pip install pgzero
   ```

2. Navegue até a pasta do projeto

3. Execute o jogo com:

   ```bash
   pgzrun main.py
   ```

---

## 🎨 Sprites e Sons

- Todos os sprites foram criados em **pixel art** de forma autoral no **Piskel** e organizados em animações cíclicas extremamente simples;
- Os sons e músicas foram editados e convertidos para **WAV (16-bit PCM)** ou **MP3** utilizando o **Audacity**, garantindo compatibilidade com o PgZero. Todos os sons foram retirados do jogo DELTARUNE, por Toby Fox.

---

## 📜 Observações Finais

- O código é **100% autoral**;
- O projeto atende integralmente aos requisitos do teste;
- Estrutura e complexidade compatíveis com projetos finais de alunos;
- O jogo contém bugs que ainda não foram corrigidos (exemplo: *hitbox* dos inimigos está errada), mas serão no decorrer dos estudos.

---

## 👩‍💻 Autoria

Projeto desenvolvido de forma independente para fins de estudo e avaliação técnica no teste de tutores de Python (2026).
