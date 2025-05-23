# -projeto-final-qa-washington
1. Apresentação
Nome completo

Washington Luiz farias da silva junior

Curso e semestre

gti 5° semestre


Um parágrafo com uma breve descrição da sua experiência com a disciplina
eu achei muito interessante a materia, gostei muito da parte de automação ci/cd, as exteções do google e de mexer com o github
gostei muito de partes de fazer os teste

2. O que é Quality Assurance (QA)?
Explique com suas palavras o conceito de QA e sua importância no desenvolvimento de software
é a garantia de qualidade, A QA garante que o softwere estara em comformidade com os requisitos pré definidos 

Use uma linguagem simples e acessível, como se estivesse explicando para alguém leigo


3. Conceitos Aprendidos Durante o Semestre
Escreva um parágrafo explicando o que você aprendeu sobre:
Qualidade em software e cultura de qualidade

eu aprendi que não é somente criar um site ou softwere e lançar ele para rodar precisa haver teste antes para garantir que o produdo esta realmente como as expectativas do cliente aprendi sobre teste autimatizados, teste de carga para ver quanto o site aguenta aprendi a criar um plano de teste contendo o excopo, o que o teste ira fazer, qual o resultado esperado

Tipos de testes (unitário, integração, sistema, aceitação, regressão e exploratório)

testes unitarios são aqueles que verificam uma parte especifica do codigo, teste de sistema são aqueles que verificam o sistema como um todo verificando as funcionalidades, teste de aceitação são aqueles que verificam se o sistema esta em confomridade com o espoerado antes de seu lançamento, teste de regressão são aqueles que verificam se o sistema esta rodando apos uma alteração, teste exploratorio são aqueles feitos para procurar defeitos dento de um site ou sistema e por fim os teste de integração são aquele que verificam a comunicação entre os sistemas.

Planejamento de testes (critérios de aceitação, planos e casos de teste)

planejamento de teste são feitos antes da aplicação dos teste e serve para dizer o que o teste faz, qual o resultado esperado, quais ferramentas serão utilizadas, qual o resultado obtido apos o teste e um caso de teste que descreve o senario pelo qual o teste irá passar 

Ferramentas de testes utilizadas durante o semestre (Colab, GitHub, etc.)
usamos o Fake Filler para automatizar teste como preencher um formulario com dados falsos
o weve para identificar problemas páginas web
O gost inpector Ele funciona como um gravador de testes, onde você pode registrar as interações de um usuário em um site
o postman para teste de Apis 

Automação de testes e integração com CI/CD
o ci/cd serve para automação de mudança no codigo e implantação de atualizações no ambiente de produção

Monitoramento e controle de qualidade (uso de métricas, rastreamento de bugs, observabilidade)
para um bom monitoramento e necessario verificar as seguites metricas:
Número total de casos de teste: Quantidade total de casos de teste criados.
Porcentagem de casos de teste executados: Percentual de casos de teste que foram executados.
Porcentagem de casos de teste aprovados: Percentual de casos de teste que passaram com sucesso.
Porcentagem de casos de teste reprovados: Percentual de casos de teste que falharam.
Número total de defeitos: A quantidade total de falhas encontradas durante o processo de teste.

4. Ferramentas e Sites Utilizados
Liste todos os sites e ferramentas que você usou durante o curso, por exemplo:
https://reqres.in/


https://colab.research.google.com/ 


https://github.com/


https://uptimerobot.com/
 eu não lembro de muita mas usamos o postman, fake filer, gost inspector, katalon, pytest, jmeter

(outros que desejar incluir)


5. Explicação dos Testes Entregues
Para cada um dos três testes obrigatórios entregues na pasta /testes, responda:
Nome do teste


Objetivo


Qual biblioteca Python foi utilizada


Qual resultado esperado


Link para o arquivo (ex: testes/teste_01.py)


Exemplo de formatação:

✅ Teste 01 – Verificação de status da API ReqRes
Biblioteca: Requests


Objetivo: Verificar se o endpoint retorna status HTTP 200


Resultado esperado: Teste passa com sucesso se o status for 200


Arquivo: testes/teste_01.py



6. Conclusão Final
Escreva um parágrafo com sua reflexão pessoal, respondendo:
O que você aprendeu de mais importante?


eu aprendi o quão grande é a importancia dos teste na criação de softweres sem a QA seria muito dificil construir um sistema funcional 

Como você enxerga a área de QA no seu futuro profissional?

a QA com certeza estara comigo por toda a minha carreira proficional, principalmente na area de automação de ci/ci e devOps Automatizando tarefas como integração, testes, implementação e monitoramento, acelerando o ciclo de desenvolvimento.


Qual ferramenta ou tema mais chamou sua atenção e por quê?
a ferramenta weve que mostra todas as falhas dentro de um site, isso facilita na solução dos problemas, dentre outras extençoes do goole que eu achei muito legais como o katalon que ele grava por onde voce passa no site e voce pode fazer alterações automatizadas.



teste 01 teste unitario
Objetivo
Verificar se as funções básicas da calculadora (soma, subtracao, multiplicacao, divisao) funcionam corretamente, incluindo casos de uso típicos e edge cases (como divisão por zero).

2. Biblioteca Python Utilizada
unittest: Biblioteca padrão do Python para criação e execução de testes unitários.

3. Resultado Esperado
Todos os testes devem passar (OK), confirmando que:

As operações matemáticas retornam os valores corretos
o resultado foi comforme o esperado, devolvel como resposta o "ok"


teste 02 teste de integração
Objetivo
Verificar se:

O cadastro impede usuários duplicados

O login só funciona com a senha correta

Os dados persistem entre as operações

Bibliotecas não foi utilizada

Apenas Python puro (sem dependências)

Resultado esperado
Saída no console: ✅ Teste passou - Fluxo completo validado!
rodou perfeitamente e deu o resultado esperado 


teste 03 teste de regressão
Objetivo
Garantir que mudanças futuras na função formatar_texto() não quebrem comportamentos já existentes que outros sistemas podem depender.

Bibliotecas não foi utilizada

Python puro (sem dependências)

Resultado esperado

✅ Todos os casos de teste passaram (sem regressões)
o codigo roudou sem erro e com o resultado esperado






