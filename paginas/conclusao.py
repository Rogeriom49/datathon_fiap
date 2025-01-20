import streamlit as st

st.title('**Conclusão**')

st.write(""" O objetivo do projeto foi desenvolver uma solução em machine learning utilizando o modelo Support Vector Machine (SVM) para identificar de forma objetiva os alunos com risco de reprovação. A análise foi baseada em um conjunto de dados composto por notas acadêmicas e indicadores de desempenho, viabilizando o planejamento de intervenções educacionais mais assertivas e direcionadas. """)
st.write(""" O modelo utilizou técnicas robustas para lidar com dados desbalanceados como a técnica de balanceamento SMOTE (Synthetic Minority Over-sampling Technique), aplicada para lidar com classes desbalanceadas em conjuntos de dados. A quantidade de alunos "em risco" era significativamente menor do que a de alunos "não em risco", o que poderia resultar em um modelo com baixa capacidade de previsão para a classe minoritária. Nesse contexto, o SMOTE foi crucial para gerar novos exemplos sintéticos para a classe minoritária, equilibrando o número de exemplos entre as classes e, assim, melhorando o desempenho do modelo. """)

st.divider()

st.subheader("**Benefícios do Modelo**")
st.write(""" **1. Intervenção Proativa:** Um dos principais benefícios de prever o risco de baixa performance é a capacidade de agir antecipadamente, antes que o aluno alcance um nível crítico de dificuldades acadêmicas. Isso possibilita intervenções mais eficazes e assertivas. """)
st.write("""**2. Apoio Personalizado:** Com base nas previsões fornecidas pelo modelo, é possível oferecer um suporte personalizado, ajustando as intervenções de acordo com as necessidades individuais de cada aluno, garantindo uma abordagem mais direcionada e eficaz. """)
st.write(""" **3. Otimização na Alocação de Recursos:** Ao identificar com precisão os alunos que realmente necessitam de apoio, o modelo permite à Passos Mágicos alocar seus recursos de maneira mais estratégica. Isso assegura que a ajuda seja direcionada especificamente aos estudantes em risco, evitando a distribuição indiscriminada de recursos e garantindo um suporte mais eficiente e focado. """)
st.write(""" **4. Acompanhamento e Monitoramento Contínuo:** O modelo também pode ser utilizado para um acompanhamento constante do desempenho dos alunos ao longo do tempo. À medida que novos dados são coletados, as previsões podem ser atualizadas, ajustando o suporte conforme necessário. Por exemplo, se um aluno inicialmente em risco melhora seu desempenho após a intervenção, o modelo refletirá essa mudança, ajustando a previsão para "não está mais em risco". Esse processo contínuo permite que a instituição acompanhe a eficácia das intervenções e ajuste suas estratégias de forma dinâmica e em tempo real. """)
st.write(""" Em resumo, o modelo de previsão de risco oferece vantagens significativas, como a intervenção precoce, personalização do suporte, eficiência na alocação de recursos, melhoria da retenção de alunos, e monitoramento contínuo do progresso acadêmico. Essas ações não só ajudam os alunos a alcançarem um melhor desempenho, mas também promovem uma gestão acadêmica mais eficaz e uma instituição mais bem-sucedida no apoio a seus estudantes. """)

st.divider()

st.subheader("**Links Relevantes**")
st.write(""" - [Passos Mágicos](https://passosmagicos.org.br)""")
st.write(""" - [Repositório no GitHub](https://github.com/Rogeriom49/datathon_fiap)""")
st.write(""" - [Dashboard](https://app.powerbi.com/view?r=eyJrIjoiMGFmNDAzNTEtMWZkYS00NGFiLWEyN2YtMmRkZjIwNjUyZTA2IiwidCI6IjZkYzg3NGNlLWRkMmItNGFhOS05ZjBkLWFkYjkyNjlhNzU4MCJ9)""")