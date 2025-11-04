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
- Estudo introdutório sobre Kubernetes, incluindo conceitos de deployments, services, namespaces, configmaps, secrets e ingresses. Conclusão de uma certificação introdutória em Kubernetes, disponível [aqui](assets/certificates/Kubernetes%20for%20the%20Absolute%20Beginners%20-%20Hands-on.pdf).

---

# Semana 2 (23/09/2025 - 30/09/2025)

## Objetivos Principais

- Iniciar a revisão bibliográfica sobre Plataformas Urbanas de Dados e arquiteturas associadas ao contexto de Smart Cities.
- Continuar o aprofundamento de conhecimentos em Kubernetes e gestão de aplicações distribuídas.
- Explorar e otimizar componentes da pipeline de dados, assegurando a estabilidade e escalabilidade do sistema.

## Tarefas Realizadas

- Início da pesquisa e recolha de literatura científica relevante para o enquadramento teórico da dissertação.
- Início de um novo curso sobre Kubernetes, disponível [aqui](https://www.udemy.com/course/certified-kubernetes-application-developer/?couponCode=KEEPLEARNING), com foco em práticas avançadas de deployments e gestão de aplicações.
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
