Simulador simples de Urna Eletrônica.

Um simulador de urna eletrônica em Python que permite tanto uma votação manual (voto a voto) quanto uma simulação automatizada com uso da biblioteca `random`.
---------------------------------------------------------------------------------------------------------
>> Funcionalidades: 

1. Modo manual: menu interativo com 7 opções de votos que são registrados individualmente.
2. Modo automático: o usuário define um intervalo de votos que cada candidato receberá, e será gerado votos alatórios dentro desse intervalo.
3. Apuração em tempo-real: após a votação será feito a apuração no mesmo instante, e, de maneira dinamica, será revelado o vencedor.
4. Interface limpa: com o uso de uma função de limpar a tela `limpar()` feita a partir da biblioteca `sys` e `subprocess`, é possível manter uma organização a cada escolha feita.

---------------------------------------------------------------------------------------------------------
>> Tecnologias usadas:

1. Python 3.14.5 (stable)
2. Bibliotecas nativas: `os`, `sys`, `time`, `random`, `subprocess`.
---------------------------------------------------------------------------------------------------------
>> Aprendizados adquiridos:

1. Manipulação e estruturação de dados complexos utilizando dicionários 'dict'.
2. Uso de Controle de fluxo e loops de repetição (`while`, `break`).
3. Tratamento de strings (uso de `.lower()` para validação de entradas).
4. Lógica matemática para cálculo e formatação de porcentagens em f-strings.
