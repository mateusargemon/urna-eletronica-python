# Simulador de Urna Eletrônica

Um simulador de urna eletrônica desenvolvido em Python que oferece duas experiências de uso: uma votação manual interativa (voto a voto) e uma simulação automatizada de larga escala utilizando a biblioteca `random`.

---

## Funcionalidades

* **Modo Manual:** Menu interativo estruturado para registrar votos individualmente para 5 candidatos, além de computar votos brancos e nulos.
* **Modo Automático:** Geração automatizada de votos em alta escala. O usuário define os limites mínimo e máximo, e o sistema distribui os votos aleatoriamente.
* **Apuração Dinâmica:** Processamento instantâneo dos resultados após o encerramento da votação, apresentando dados detalhados e um anúncio cronometrado do vencedor.
* **Interface Otimizada:** Gerenciamento do console por meio de uma função dedicada de limpeza de tela (`limpar()`), garantindo uma navegação fluida e organizada para o usuário.

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3.14.5 (Stable)
* **Bibliotecas Nativas:**

  * `os` & `subprocess`: Integração com o sistema operacional para controle do console.
  * `sys`: Gerenciamento do fluxo de encerramento do script.
  * `time`: Criação de pausas e temporização da interface.
  * `random`: Simulação estatística dos votos automatizados.

---

## Aprendizados Adquiridos

* Manipulação de dicionários (`dict`) para armazenamento e contagem centralizada dos votos.
* Controle de fluxo utilizando loops aninhados (`while True`) e interrupções condicionais (`break`, `sys.exit`).
* Tratamento de entradas com `.lower()` para tornar o menu resistente a variações entre letras maiúsculas e minúsculas.
* Aplicação de expressões matemáticas e formatação com *f-strings* para cálculos de porcentagem e exibição de valores.

DD/MM/YYYY > 05/06/2026 15pm UTC-4
