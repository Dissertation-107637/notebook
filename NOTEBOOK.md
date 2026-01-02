# Semana 1 (16/09/2025 - 23/09/2025)

## Objetivos Principais

- Explorar a plataforma atual e compreender, por exemplo, os diferentes fluxos de dados e a camada de segurança.
- Aprendizagem sobre Kubernetes.
- Reunir e organizar documentação relevante (ex.: diagramas) para referência futura.

## Tarefas Realizadas

- Mapeamento inicial da arquitetura da plataforma e dos fluxos de dados existentes.
- Análise do percurso dos dados desde a recolha (IoT/5G e APIs públicas) até ao armazenamento e disponibilização.
- Levantamento dos principais componentes FIWARE em uso (Orion, Cygnus, Keyrock, Wilma, AuthzForce).
- Exploração da configuração do cluster Kubernetes e identificação de como os serviços estão distribuídos.
- Recolha e organização de documentação relevante (diagramas, especificações técnicas e configurações).
- Estudo introdutório sobre Kubernetes, incluindo conceitos de deployments, services, namespaces, configmaps, secrets e ingresses. Conclusão de uma certificação introdutória em Kubernetes, disponível [aqui](assets/certificates/Udemy%20-%20Kubernetes%20for%20the%20Absolute%20Beginners%20-%20Hands-on.pdf).

---

# Semana 2 (23/09/2025 - 30/09/2025)

## Objetivos Principais

- Iniciar a revisão bibliográfica sobre Plataformas Urbanas de Dados e arquiteturas associadas ao contexto de Smart Cities.
- Continuar o aprofundamento de conhecimentos em Kubernetes e gestão de aplicações distribuídas.
- Explorar e otimizar componentes da pipeline de dados, assegurando a estabilidade e escalabilidade do sistema.

## Tarefas Realizadas

- Início da pesquisa e recolha de literatura científica relevante para o enquadramento teórico da dissertação.
- Início de um novo curso sobre Kubernetes, disponível [aqui](https://www.coursera.org/learn/kubernetes-basic-for-devops), com foco em práticas avançadas de deployments e gestão de aplicações.
- Realização de testes para escalar Kafka Connectors utilizando shared subscriptions no MQTT, visando melhorar o processamento paralelo dos fluxos de dados provenientes das câmaras.
- Ajuste e estabilização da pipeline de dados, anteriormente com falhas frequentes, garantindo o processamento contínuo e sem acumulação de mensagens no Kafka.

---

# Semana 3 (30/09/2025 - 07/10/2025)

## Objetivos Principais

- Prosseguir a revisão bibliográfica e consolidar a base teórica da dissertação.
- Iniciar a redação do capítulo de Introdução, com foco na motivação, objetivos e contribuições esperadas.
- Continuar o desenvolvimento de competências em Kubernetes.
- Iniciar a fase experimental relacionada com o novo vertical Smart Crosswalks.

## Tarefas Realizadas

- Continuação da revisão bibliográfica, com organização das principais referências.
- Elaboração de um primeiro draft da Introdução, abordando a motivação do trabalho, os objetivos gerais e específicos e as principais contribuições previstas.
- Continuação do curso sobre Kubernetes, com foco na configuração e orquestração de serviços num cluster.
- Início dos testes e planeamento do desenvolvimento do serviço Smart Crosswalks.

---

# Semana 4 (07/10/2025 - 14/10/2025)

## Objetivos Principais

- Continuar a revisão bibliográfica.
- Dar continuidade ao desenvolvimento de competências em Kubernetes, continuando o curso iniciado nas semanas anteriores.
- Testar e validar o funcionamento inicial do vertical das Smart Crosswalks.
- Avançar na escrita da dissertação, com o draft das secções de Motivação e Objetivos já concluído.

## Tarefas Realizadas

- Continuação da revisão bibliográfica, com identificação de novos artigos e comparação entre diferentes abordagens arquiteturais para plataformas urbanas de dados.
- Continuação do curso sobre Kubernetes.
- Execução de testes práticos no vertical Smart Crosswalks, avaliando o comportamento dos fluxos de recolha e processamento de dados e a integração com os componentes da plataforma.
- Consolidação do texto preliminar da Introdução, incluindo as secções de Motivação e Objetivos, servindo de base para a próxima fase de escrita.

---

# Semana 5 (14/10/2025 - 21/10/2025)

## Objetivos Principais

- Prosseguir a revisão de literatura, consolidando o enquadramento teórico sobre plataformas urbanas de dados e as suas arquiteturas baseadas em FIWARE e Kubernetes.
- Iniciar a fase de implementação prática do vertical Smart Crosswalks.

## Tarefas Realizadas

- Continuação da revisão bibliográfica, orquestração de serviços e mecanismos de interoperabilidade entre verticais.
- Início da implementação do vertical Smart Crosswalks, com a criação do modelo de dados e lógica de processamento.

---

# Semana 6 (21/10/2025 - 28/10/2025)

## Objetivos Principais

- Concluir a implementação do vertical das Smart Crosswalks.
- Prosseguir a revisão bibliográfica, preparando a base para o capítulo do Estado da Arte.
- Preparar o ambiente e o plano de testes para a fase de validação do novo vertical.

## Tarefas Realizadas

- Finalização da implementação completa do vertical, incluindo todos os componentes necessários à recolha, processamento e disponibilização de dados.
- Integração do vertical com os serviços FIWARE existentes, garantindo compatibilidade com os mecanismos de persistência e orquestração.
- Continuação da revisão de literatura, com foco em arquiteturas de dados urbanos, interoperabilidade semântica e plataformas FIWARE aplicadas a Smart Cities.
- Definição do plano de testes e métricas de avaliação para a fase seguinte, destinada à validação funcional e de desempenho do vertical das Smart Crosswalks.

---

# Semana 7 (28/10/2025 - 04/11/2025)

## Objetivos Principais

- Continuar a revisão de literatura.
- Iniciar a redação do Capítulo 2 (Estado da Arte), estruturando as principais secções temáticas.
- Dar início à fase de testes do vertical das Smart Crosswalks, validando o seu funcionamento e desempenho em ambiente real.

## Tarefas Realizadas

- Prosseguimento da revisão bibliográfica, com recolha e análise de novas referências sobre orquestração de serviços, interoperabilidade e gestão de dados em Smart Cities.
- Início da escrita do Capítulo 2 (Estado da Arte), com a elaboração das secções introdutórias e definição da estrutura global do capítulo.
- Início da fase de testes do vertical, avaliando a comunicação entre os componentes FIWARE, a recolha de dados e o processamento dos eventos provenientes dos sensores.
- Registo dos primeiros resultados e observações preliminares, a serem analisados em maior detalhe na fase seguinte.

---

# Semana 8 (04/11/2025 - 11/11/2025)

## Objetivos Principais

- Avançar na escrita do Estado da Arte, com foco na secção Smart Cities and Urban Data Platforms.
- Continuar a fase de implementação e testes do vertical das Smart Crosswalks, garantindo estabilidade e eficiência nos fluxos de dados.
- Explorar formas de otimizar as operações do Orion Context Broker, de modo a melhorar o desempenho global da plataforma.

## Tarefas Realizadas

- Escrita da secção Smart Cities and Urban Data Platforms do Estado da Arte, abordando conceitos fundamentais, desafios e exemplos de plataformas urbanas existentes.
- Continuação da implementação e ajustes do vertical Smart Crosswalks, com foco na fiabilidade dos processos de recolha e publicação de dados, faltando apenas os testes.
- Análise de estratégias para otimizar o desempenho do Orion Context Broker, explorando o uso de memória RAM para armazenamento de entidades transientes, de modo a acelerar as operações de leitura e escrita e reduzir o tempo de resposta do sistema.

---

# Semana 9 (11/11/2025 - 18/11/2025)

## Objetivos Principais

- Expandir a revisão de literatura através da análise de novas plataformas urbanas de dados e soluções relevantes no ecossistema das Smart Cities.
- Testar o vertical Smart Crosswalks, avaliando metodologias para obtenção de localização a partir de câmaras.
- Explorar possíveis novos verticais a integrar na plataforma, identificando casos de uso já implementados noutras cidades inteligentes.

## Tarefas Realizadas

- Pesquisa e análise de várias plataformas urbanas de dados, incluindo Snap4City, City Data Hub, SmartSantander, entre outras, com foco nas suas arquiteturas, camadas funcionais e abordagens de interoperabilidade.
- Testes ao vertical Smart Crosswalks: verificou-se que a utilização de coordenadas GPS inferidas a partir das câmaras resultava em elevada imprecisão. Como alternativa, adotou-se o uso de coordenadas em píxeis da imagem para representar a posição dos utilizadores, garantindo maior fiabilidade no processamento e deteção de eventos.
- Exploração de novos verticais e casos de uso já existentes em Smart Cities, como smart waste management, iluminação pública inteligente, monitorização ambiental e gestão de estacionamento, identificando potenciais candidatos para futura implementação ou integração na plataforma.

---

# Semana 10 (18/11/2025 - 25/11/2025)

## Objetivos Principais

- Validar o novo método de localização baseado em píxeis da imagem utilizado no vertical Smart Crosswalks, garantindo a sua fiabilidade face ao comportamento observado na imagem e avaliar preliminarmente a qualidade dos dados recolhidos, preparando a fase seguinte dedicada à análise estatística.
- Avançar na escrita do Capítulo 2, especificamente nas secções relacionadas com plataformas urbanas de dados existentes e conceitos fundamentais de Smart Cities.

## Tarefas Realizadas

- Testes detalhados ao novo método de localização por coordenadas de píxeis, comparando os resultados obtidos com o comportamento visual observado nas sequências de vídeo. Os testes demonstraram um comportamento positivo e estável, confirmando a adequação desta abordagem.
- Identificação da necessidade de realizar testes adicionais focados na validação estatística dos valores recolhidos (distribuições, precisão, estabilidade), a serem executados na próxima fase.
- Escrita das secções do Estado da Arte relacionadas com Smart Cities e com as principais plataformas urbanas de dados existentes, integrando exemplos como City Data Hub, entre outras.

---

# Semana 11 (25/11/2025 - 02/12/2025)

## Objetivos Principais

- Prosseguir o desenvolvimento do Capítulo 2, consolidando as secções já iniciadas.
- Validar e finalizar a secção dedicada às plataformas urbanas de dados existentes.
- Iniciar e desenvolver a secção relativa aos verticais de Smart Cities descritos na literatura.

## Tarefas Realizadas

- Revisão da secção sobre plataformas urbanas de dados, garantindo clareza, consistência e correta contextualização dos exemplos analisados ao longo das semanas anteriores.
- Escrita da nova secção dedicada aos verticais existentes na literatura, abordando áreas como mobilidade inteligente, gestão de resíduos, monitorização ambiental, smart parking, iluminação inteligente, entre outros.

---

# Semana 12 (02/12/2025 - 09/12/2025)

## Objetivos Principais

- Continuação da escrita do Capítulo 2, com foco em tópicos mais específicos, como modelação de dados (NGSI-LD e NGSIv2), análise de Big Data, escalabilidade, resiliência, observabilidade, segurança, multi-tenancy e controlo de acesso.
- Revisão e aprimoramento das secções já escritas.
- Refinamento dos jobs de processamento de dados, visando melhorar a velocidade e a eficiência das operações de ingestão e processamento.

## Tarefas Realizadas

- Refinamento das secções já escritas, incluindo ajustes no texto e melhorias no alinhamento das ideias.
- Escrita das secções sobre modelação de dados com ênfase nos padrões NGSI-LD e NGSIv2, destacando as vantagens e desafios desses modelos na gestão de dados de Smart Cities.
- Desenvolvimento da secção sobre análise de Big Data, abordando as principais técnicas e ferramentas utilizadas na análise de grandes volumes de dados, com foco na aplicação em plataformas urbanas.

---

# Semana 13 (09/12/2025 - 16/12/2025)

## Objetivos Principais

- Concluir e consolidar a escrita das secções do Capítulo 2 relacionadas com Smart Cities, incluindo o conceito, características e principais desafios.
- Finalizar a análise e descrição das plataformas urbanas de dados atuais, garantindo consistência entre exemplos, arquitetura e objetivos de cada abordagem.
- Completar a secção relativa a vários verticais existentes na literatura, estruturando-os por domínios e extraindo padrões e limitações relevantes para o trabalho.

## Tarefas Realizadas

- Conclusão do tópico sobre o conceito de Smart Cities e desafios associados, integrando aspetos como heterogeneidade de fontes, interoperabilidade, escalabilidade, privacidade/segurança, qualidade de dados e governança.
- Finalização da secção dedicada às plataformas urbanas existentes, consolidando a análise comparativa das soluções estudadas e reforçando a contextualização arquitetural e funcional das mesmas.
- Conclusão da secção sobre vários verticais de Smart Cities descritos na literatura, organizando casos de uso por áreas (e.g., mobilidade, ambiente, resíduos, iluminação, estacionamento) e identificando tendências comuns e limitações observadas nas abordagens existentes.
- Revisão geral das secções concluídas, garantindo coerência interna, melhor ligação entre tópicos e uniformização do estilo de escrita no Capítulo 2.

---

# Semana 14 (16/12/2025 - 23/12/2025)

## Objetivos Principais

- Concluir a formação avançada em Kubernetes iniciada na semana 2.
- Adquirir bases teóricas e práticas sobre bases de dados distribuídas.
- Avançar na escrita do Capítulo 2, desenvolvendo o tópico Context Information Management and Data Models, consolidando conceitos essenciais para a modelação e gestão de contexto em plataformas urbanas de dados.

## Tarefas Realizadas

- Conclusão do curso de Kubernetes iniciado na Semana 2, com revisão e consolidação de conceitos avançados de deployment e operação de aplicações distribuídas em clusters. Certificado disponível [aqui](assets/certificates/KodeKloud%20-%20Kubernetes%20Basics%20for%20DevOps.pdf).
- Conclusão do curso Foundations of Distributed Database Systems, reforçando conceitos relacionados com otimização em ambientes distribuídos e execução eficiente de consultas. Certificado disponível [aqui](assets/certificates/Johns%20Hopkins%20University%20-%20Foundations%20of%20Distributed%20Database%20Systems.pdf).
- Escrita e desenvolvimento do tópico Context Information Management and Data Models no Capítulo 2, abordando a gestão de informação de contexto e a sua relação com modelos de dados e mecanismos de interoperabilidade (incluindo a ligação aos padrões já discutidos anteriormente, como NGSIv2 e NGSI-LD).

# Semana 15 (23/12/2025 - 30/12/2025)

## Objetivos Principais

- Reforçar competências práticas de gestão de aplicações cloud-native em Kubernetes, com foco em operação, manutenção e boas práticas de administração.
- Avançar na escrita do Capítulo 2, concluindo os tópicos transversais relacionados com escalabilidade, Big Data analysis, persistência de dados, segurança, controlo de acessos e multi-tenancy.
- Iniciar e avançar na escrita do Capítulo 3, consolidando a transição do enquadramento teórico para a proposta do trabalho.

## Tarefas Realizadas

- Conclusão do curso Managing Cloud-native Applications with Kubernetes, com certificado disponível [aqui](assets/certificates/Red%20Hat%20-%20Managing%20Cloud-native%20Applications%20with%20Kubernetes.pdf). ￼
- Avanço significativo na redação dos tópicos restantes do Capítulo 2, cobrindo escalabilidade e mecanismos de suporte a crescimento de bases de dados e fluxos de dados, análise de Big Data e implicações para plataformas urbanas, persistência de dados e estratégias associadas, segurança, controlo de acessos e modelo multi-tenant aplicado à plataforma.
- Início e progresso na escrita do Capítulo 3, estruturando o conteúdo inicial e estabelecendo a ligação entre os requisitos e limitações identificados no Estado da Arte e a abordagem proposta no trabalho.
