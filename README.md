# 🗳️ Simulador de Urna Eletrônica

Um simulador de urna eletrônica desenvolvido em Python que oferece duas experiências de uso: uma votação manual interativa (voto a voto) e uma simulação automatizada de larga escala utilizando a biblioteca `random`.

---

## 🚀 Funcionalidades

* **Modo Manual:** Menu interativo estruturado para registrar votos individualmente para 5 candidatos, além de computar votos brancos e nulos.
* **Modo Automático:** Geração automatizada de votos em alta escala. O usuário define os limites mínimo e máximo, e o sistema distribui os votos aleatoriamente.
* **Apuração Dinâmica:** Processamento instantâneo dos resultados após o encerramento da votação, apresentando dados detalhados e um anúncio cronometrado do vencedor.
* **Interface Otimizada:** Gerenciamento do console por meio de uma função dedicada de limpeza de tela (`limpar()`), garantindo uma navegação fluida e organizada para o usuário.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.14.5 (Stable)
* **Bibliotecas Nativas:**
  * `os` & `subprocess`: Integração com o sistema operacional para controle do console.
  * `sys`: Gerenciamento do fluxo de encerramento do script.
  * `time`: Criação de pausas dramáticas e temporização da interface.
  * `random`: Simulação estatística dos votos automatizados.

---

## 📝 Aprendizados Adquiridos

O desenvolvimento deste projeto permitiu a consolidação de conceitos fundamentais da programação:

1. **Estrutura de Dados:** Manipulação avançada de dicionários (`dict`) para persistência e contagem dos votos de forma centralizada.
2. **Controle de Fluxo:** Implementação de loops de repetição aninhados (`while True`) e interrupções condicionais (`break`, `sys.exit`).
3. **Tratamento de Entradas:** Higienização de strings com `.lower()` para garantir a resiliência do menu contra variações de caixa (letras maiúsculas/minúsculas).
4. **Lógica e Formatação:** Aplicação de expressões matemáticas para cálculo de proporções e formatação de casas decimais em *f-strings*.

DD/MM/YYYY > 05/06/2026 15pm
