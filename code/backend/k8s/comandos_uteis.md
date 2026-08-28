## comando para criar um banco no postgres:
```bash
kubectl exec -it postgres-0 -n infra -- \
  psql -U banco_user -d banco_simplificado -c "CREATE DATABASE airflow;"
```