# Notas - Semana 1

## Resumo

A plataforma opera num cluster Kubernetes e combina várias camadas que vão da ingestão em tempo real de dados à exposição de APIs NGSI/NGSI-LD para consumo interno e externo.

A recolha de dados integra dispositivos IoT distribuídos pela cidade e fluxos provenientes da rede 5G. Todo o tráfego converge num broker MQTT central que disponibiliza os tópicos internamente e, através de Kafka Connectors, encaminha-os para o Kafka para garantir distribuição escalável e consumo paralelo pelos diferentes componentes.

Na camada de **ingestão e messaging**, utiliza Kafka via Strimzi (`01-Strimzi/01-kafka-persistent.yaml`), recebendo dados MQTT e distribuindo-os em tópicos para integração com jobs Orion/NGSI.

Em paralelo, as integrações consomem dados de APIs públicas (ex.: Waze) externas diretamente nos pipelines de processamento usados para criação e atualização de entidades NGSI.

A camada de **persistência e exposição** assenta em MongoDB (histórico) e motores FIWARE: Orion v2 e Orion-LD (gestão de entidades), Cygnus (armazenamento histórico, enviando séries temporais para o MongoDB) e STH-Comet (consultas temporais e estatísticas). Este modelo garante consulta retrospetiva e suporte a análises estatísticas comparativas ao longo do tempo.

Os **jobs de processamento** (`09-jobs/`) consomem tópicos Kafka, processam as mensagens transformando-as em entidades NGSI e alimentam o Orion. No caso do uso de APIs públicas, os jobs processam os dados diretamente para criar/atualizar as entidades NGSI.

---

## Deployment

- **Namespaces chave**: `kafka`, `mongo`, `orionv2`, `orion`, `sth-comet`, `security`, `monitoring`, `public-apis`, `atcll-realtime`, `testmongold`.
- **Segurança no deployment**: stack FIWARE com Keyrock (IAM e gestão de aplicações), AuthZForce (PDP para políticas de autorização) e Wilma (PEP Proxy para validação de tokens). Estes serviços estão integrados no namespace `security` e reforçados com middleware proprietário (`12-security-fiware-stack/`).

### Endpoints expostos

- **`api.new.aveiro-living-lab.it.pt/ngsi-v2/orion`**  
  Serviço: `fiware-orion-service` (namespace `orionv2`).  
  Definido em `14-ingress/orionv2/ingress.yaml` com middleware _strip-prefix_ (`strip-prefix`).

- **`api.new.aveiro-living-lab.it.pt/ngsi-ld/orion`**  
  Serviço: `fiware-orionld-service` (namespace `orion`).  
  Definido em `14-ingress/orion-ld/ingress.yml`.

- **`api.new.aveiro-living-lab.it.pt/ngsi-v2/history`**  
  Serviço: `fiware-sth-service-column` (namespace `sth-comet`).  
  Definido em `14-ingress/sth-comet/ingress.yaml`.

- **`api.new.aveiro-living-lab.it.pt/secure/ngsi-v2`**  
  Serviço: `wilma-orion-service-middleware` (namespace `security`).  
  Definido em `14-ingress/security/proxy-ingress.yaml` com middleware `strip-prefix-fiware-service`.

- **`api.new.aveiro-living-lab.it.pt/route25uw/orion`**  
  Serviço: `wilma-orion-service` (namespace `security`).  
  Ingress definido em `14-ingress/security/ubiwhere-orion-ingress.yaml`.

- **`api.new.aveiro-living-lab.it.pt/route25uw/history`**  
  Serviço: `wilma-sth-comet-service` (namespace `security`).  
  Referência no ingress igual ao anterior, mas o serviço não existe nos manifests.

- **`auth.aveiro-living-lab.it.pt/`**  
  Serviço: `nap-auth-service` (namespace `security`).  
  Definido em `14-ingress/security/auth-ingress.yaml`.

- **`api.new.aveiro-living-lab.it.pt/`**  
  Serviço: `atcll-realtime-backend-service` (namespace `atcll-realtime`).  
  Definido em `14-ingress/atcll-realtime/backend-ingress.yaml`.

- **NodePort `:31662`**  
  Listener externo do Kafka (namespace `kafka`).  
  Configurado em `01-Strimzi/01-kafka-persistent.yaml`.

- **NodePort `:30080`**  
  Kafka UI (namespace `kafka`).  
  Definido em `02-kafkaui/deployment.yaml`. |

---

## Segurança

- **Threat model**: exposição pública via Traefik + TLS; internamente NodePorts sem TLS (Kafka `31662`).
- **Identidade e autenticação**: Keyrock (IAM), Wilma (PEP Proxy para validação de tokens), AuthZForce (PDP para políticas de autorização).
- **Middleware proprietário**: presente em `12-security-fiware-stack/`, reforça fluxos específicos de autenticação e autorização.
- **Configuração adicional**: token básico hardcoded para Nap Auth.
- **Ingress policies**: TLS via Let's Encrypt.
