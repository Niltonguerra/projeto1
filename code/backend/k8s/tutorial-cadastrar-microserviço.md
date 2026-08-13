- esse comandos não precisão ser executados na mão, pois criei um makefile, mas para consulta fica aqui como referência.

## comandos:

Deploy de um serviço no cluster (kind)

1. Build da imagem Docker

```bash
docker build -t banco/<nome do service>:latest .
```
Empacota o serviço numa imagem Docker local.

2. Carregar a imagem no kind

```bash
kind load docker-image banco/<nome do service>:latest --name banco-simplificado
```
O kind roda o cluster dentro de containers Docker — ele não enxerga automaticamente as imagens do seu Docker local. Esse comando copia a imagem pra dentro do nó do cluster.

3. Aplicar o manifest (primeira vez)

```bash
kubectl apply -f k8s/services/<nome do service>.yaml
```
Cria o Deployment e o Service no cluster a partir do arquivo YAML. Só precisa rodar na primeira vez, ou quando mudar o YAML.

4. Atualizar o serviço (após rebuild da imagem)

```bash
kubectl rollout restart deployment/<nome do service> -n services
```
Força o Kubernetes a recriar os pods usando a imagem atualizada. Usar isso após cada kind load com uma nova versão da imagem.

5. Verificar status

```bash
kubectl get pods -n services
```
Lista os pods do namespace services. Status esperado: Running com READY 1/1.



### Ver logs
````bash
kubectl logs -f deployment/<nome do service> -n services
````


### Se o pod travar em CrashLoopBackOff ou ImagePullBackOff
````bash
kubectl describe pod -n services -l app=<nome do service>
````


## rebuildar aplicação:
``` bash
docker build -t banco/<nome do service>:latest .
kind load docker-image banco/<nome do service>:latest --name banco-simplificado
kubectl rollout restart deployment/<nome do service> -n services
```


## expõe o ingress:
```bash
kubectl port-forward service/ingress-nginx-controller 8080:80 -n ingress-nginx --address 0.0.0.0
```