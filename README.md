# 🔍 Monitoring & Alerting with Prometheus + Grafana

This project demonstrates a complete monitoring and alerting stack using Prometheus, Grafana, and Alertmanager. It monitors both system metrics and custom application metrics.

## 📦 Stack
- Docker + Docker Compose
- Prometheus + Node Exporter
- Grafana (preconfigured dashboard)
- Alertmanager Slack: Incoming Webhooks, alerts channel

## 🖥️ Monitored Metrics
- CPU / Memory / Disk
- HTTP metrics from a sample FastAPI application
- Uptime and error rate

## 📊 Screenshots

![📊 Grafana graph](./assets/grafana-Dashboard-test.png)
![📊 Grafana graph](./assets/grafana-Prometheus_2_0_Stats.png)
![📊 Grafana graph](./assets/grafana-Prometheus.png)
![📊 Grafana graph](./assets/grafana-Prometheus_Stats.png)

![📦 Docker Compose in action](./assets/docker-containers.png)

![🚨 Triggered alert](./assets/alertmanager-HighNetworkTraffic.png)
![🚨 Triggered alert](./assets/alertmanager-NodeExporterDown.png)

![📈 Prometheus metrics](./assets/prometheus-metrics.png)
![📈 Prometheus alert_rules](./assets/prometheus-alert_rules_network.png)
![📈 Prometheus alert_rules](./assets/prometheus-alert_rules.png)

![🔔 Slack notification](.assets/slack-alert.png)


## 🚀 Getting Started
```bash
git clone https://github.com/your_repo.git
cd devops-monitoring

docker-compose build
docker-compose up -d