import streamlit as st

st.title('**Introdução**')

tab1, tab2, tab3 = st.tabs(['Sobre a Passos Mágicos', 'Sobre o Projeto', 'Dicionário'])

with tab1:
    st.subheader('**Quem somos?**')
    st.write(""" A Associação Passos Mágicos possui uma história de 31 anos dedicada a transformar a vida de crianças e jovens de baixa renda, oferecendo-lhes melhores perspectivas de futuro. """)
    st.write(""" Essa iniciativa, idealizada por Michelle Flues e Dimetri Ivanoff, teve início em 1992, com atividades realizadas em orfanatos no município de Embu-Guaçu. """)
    st.write(""" Em 2016, após anos de experiência e aprendizado, decidiram expandir o alcance do programa para beneficiar um maior número de jovens. Essa transformação, baseada em uma abordagem que combina educação de qualidade, suporte psicológico e psicopedagógico, ampliação da visão de mundo e incentivo ao protagonismo, resultou na criação da Associação Passos Mágicos como um projeto social e educacional. """)
    st.divider()
    st.subheader('**O que fazemos?**')
    st.write(""" A Passos Mágicos transforma vidas por meio da educação, oferecendo aulas de alfabetização, língua portuguesa e matemática para crianças e adolescentes de 7 a 17 anos residentes em Embu-Guaçu. Os estudantes são organizados em turmas de acordo com seu nível de aprendizado, definido por uma avaliação diagnóstica realizada no momento da inscrição. """)
    st.write(""" Atualmente, a instituição impacta diretamente 1.000 alunos, distribuídos em diferentes etapas de aprendizado: """)
    st.write(""" - Fase Alfabetização: Para alunos em processo de alfabetização ou com dificuldades na leitura e escrita (20% dos alunos).\n
- Fases 1 e 2: Aprofundamento dos conteúdos do Ensino Fundamental 1 (37% dos alunos).\n
- Fases 3 e 4: Foco no Ensino Fundamental 2, com ênfase no aprofundamento de matérias (24% dos alunos).\n
- Fases 5 e 6: Voltadas para o Ensino Médio, atendendo jovens e adolescentes (8% dos alunos).\n
- Fases 7 e 8: Preparação intensiva para vestibulares e exames do último ano do Ensino Médio (11% dos alunos). """)
    st.write("""Além disso, a Passos Mágicos oferece programas educacionais inovadores, como: """)
    st.write(""" - Preparação para vestibulares e escolas técnicas por meio do programa Vem Ser.\n
- Cursos avançados em parceria com a USP, incluindo disciplinas como Sustentabilidade, Computação e Programação, oferecendo oportunidades únicas de aprendizado. """)
    st.write(""" Ciente de que o suporte emocional é essencial para o sucesso acadêmico, a Passos Mágicos também disponibiliza acompanhamento psicológico individual e em grupo para alunos e seus familiares, promovendo bem-estar e equilíbrio emocional para enfrentar os desafios da educação. """)
    st.divider()
    st.subheader('**Impacto (indicadores 2023)**')
    st.write(""" Pessoas Impactadas: **4400** (considerando a média de 4 familiares por aluno) """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(""" Alunos no programa de Aceleração do Conhecimento: **1100 alunos** """)
        st.write(""" - 20% na alfabetização """)
        st.write(""" - 37% nas turmas 1 e 2 """)
        st.write(""" - 24% nas turmas 3 e 4 """)
        st.write(""" - 8% nas turmas 5 e 6 """)
        st.write(""" - 11% nas turmas 7 e 8 """)

    with col2:
        st.write(""" Bolsistas em instituições de ensino particular: **98 alunos** """)
        st.write(""" - Colégio Evolução Arco Íris: 75 alunos """)
        st.write(""" - Albert Einstein: 8 alunos """)
        st.write(""" - Escola João Paulo II: 1 aluno """)
        st.write(""" - Colégio Poliedro: 2 alunos """)
        st.write(""" - FIAP: 12 alunos """)
    
    with col3:
        st.write(""" Universitários em instituições de ensino superior: **103 alunos** """)
        st.write(""" - ESPM: 4 alunos """)
        st.write(""" - Estácio: 5 alunos """)
        st.write(""" - FIAP: 46 alunos """)
        st.write(""" - UNISA: 39 alunos """)

with tab2:
    st.write(""" O objetivo do projeto é criar uma solução preditiva para monitorar o desempenho escolar dos alunos, identificando aqueles com resultados acima ou abaixo do esperado. A avaliação será baseada em indicadores como Desempenho Acadêmico, Psicopedagógico, Engajamento, Autoavaliação, Adequação de Nível e Ponto da Virada. Para isso, será empregado o modelo de machine learning que apresentou o melhor desempenho segundo as métricas de F1 Score, Acurácia, Precisão e Recall. """)
    st.write(""" Adicionalmente, será conduzida uma análise exploratória para evidenciar os impactos gerados pela Passos Mágicos no desempenho dos estudantes. Essa análise levantará indicadores de performance, detalhando a evolução de cada métrica e explorando o comportamento das Pedras, além de ilustrar graficamente os momentos em que o Ponto de Virada ocorre com maior frequência. """)

with tab3:
    col1, col2, col3= st.columns(3)

    with col1:
        st.subheader('**IAN**')
        st.write('Indicador de adequação de nível')
        st.write('Originário de resgistro administrativos')
    with col2:
        st.subheader('**IDA**')
        st.write('Indicador de desempenho acadêmico')
        st.write('Notas de provas e média geral universitária')
    with col3:
        st.subheader('**IEG**')
        st.write('Indicador de engajamento')                
        st.write('Registro de entregas de lições de casa e voluntariado')                
     
    col4, col5, col6 = st.columns(3)

    with col4:
        st.subheader('**IAA**')
        st.write('Indicador de autoavaliação')           
        st.write('Questionário de autoavaliação individual')           

    with col5:
        st.subheader('**IPP**')
        st.write('Indicador psicopedagógico')
        st.write('Questionário de avalidação dos pedagogos e professores')
    with col6:
        st.subheader('**IPV**')
        st.write('Indicador do ponto da virada')            
        st.write('Questionário de avalidação dos pedagogos e professores')