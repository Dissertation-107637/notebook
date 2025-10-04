# Semana 1

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

# Semana 2

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

# Semana 3

## Objetivos Principais

- Prosseguir a revisão bibliográfica e consolidar a base teórica da dissertação.
- Iniciar a redação do capítulo de Introdução, com foco na motivação, objetivos e contribuições esperadas.
- Continuar o desenvolvimento de competências em Kubernetes.
- Iniciar a fase experimental relacionada com o novo vertical Smart Crosswalks.

## Tarefas Realizadas

- Continuação da revisão bibliográfica, com organização das principais referências.
- Elaboração de um primeiro draft da Introdução, abordando a motivação do trabalho, os objetivos gerais e específicos e as principais contribuições previstas.
- Continuação do curso sobre Kubernetes, com foco em configuração e orquestração de serviços em ambiente de cluster.
- Início dos testes e planeamento do desenvolvimento do serviço Smart Crosswalks.

# Trabalho Futuro

- Continuar a recolha e análise de literatura científica, consolidando o enquadramento teórico sobre Urban Data Platforms, orquestração de serviços e arquiteturas em Smart Cities.
- Refinamento da Introdução e planeamento do Estado da Arte.
- Desenvolvimento do vertical Smart Crosswalks: implementar o fluxo completo de recolha, processamento e exposição de dados, integrando-o na arquitetura existente da plataforma.
