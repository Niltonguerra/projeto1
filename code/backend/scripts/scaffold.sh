#!/bin/bash

SERVICE_NAME=$1
K8S_DIR=$2
PORT=$3
VERSION=${4:-latest}

if [ -z "$SERVICE_NAME" ] || [ -z "$K8S_DIR" ] || [ -z "$PORT" ]; then
  echo "Uso: ./scaffold.sh <service-name> <k8s-dir> <port> [version]"
  exit 1
fi

mkdir -p "$K8S_DIR"

cat > "$K8S_DIR/$SERVICE_NAME.yaml" <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: $SERVICE_NAME
  namespace: services
spec:
  replicas: 1
  selector:
    matchLabels:
      app: $SERVICE_NAME
  template:
    metadata:
      labels:
        app: $SERVICE_NAME
    spec:
      containers:
        - name: $SERVICE_NAME
          image: banco/$SERVICE_NAME:$VERSION
          imagePullPolicy: Never
          ports:
            - containerPort: $PORT
          readinessProbe:
            httpGet:
              path: /health
              port: $PORT
            initialDelaySeconds: 10
            periodSeconds: 5
          livenessProbe:
            httpGet:
              path: /health
              port: $PORT
            initialDelaySeconds: 20
            periodSeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: $SERVICE_NAME
  namespace: services
spec:
  selector:
    app: $SERVICE_NAME
  ports:
    - port: $PORT
      targetPort: $PORT
EOF

echo "Manifesto criado em $K8S_DIR/$SERVICE_NAME.yaml"