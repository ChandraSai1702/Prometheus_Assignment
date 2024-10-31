## ToDo Application Monitoring with Prometheus and Grafana

This project demonstrates the monitoring of a ToDo application using Prometheus and Grafana. It includes metrics such as requests per second, memory usage, and CPU usage.

## Project Structure

- **ToDo Application**: The core application code.
- **Prometheus**: Configured to scrape metrics from the ToDo application.
- **Grafana**: Used for visualizing the metrics.

## Metrics Export

The ToDo application exports the following metrics:

- **Total HTTP Requests**: Counter for the total number of HTTP requests received.
- **Memory Usage**: Gauge for the memory usage of the application.
- **CPU Usage**: Gauge for the CPU usage of the application.

Metrics are exposed at the `/metrics` endpoint.

## Installation

1. **Create an application**: Here we are using the ToDo application built using Django.
2. **Export Metrics in Your ToDo Application**: Use prometheus_client library to expose the metrics from the ToDo application.
3. **Build the Docker Image and write the kubernetes deployment and service file**
4. **Deploy the ToDo application in minikube**:
   ```bash
     # to deploy the deployment file
     kubectl apply -f todo-deployment.yaml
     # to deploy the service file
     kubectl apply -f todo-service.yaml
5. **Install Prometheus and Grafana**: Use Helm to install both applications in your Kubernetes cluster.

   ```bash
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo add grafana https://grafana.github.io/helm-charts
   helm repo update

   # Install Prometheus
   helm install prometheus prometheus-community/prometheus

   # Install Grafana
   helm install grafana grafana/grafana
6. **Configure Prometheus Scrape Configs**: We can customize the scrape configuration by editing the values.yaml of the Prometheus Helm release or overriding it during installation.
     ```bash
        scrapeConfigs:
          - job_name: 'your_app'
            metrics_path: '/metrics'
            static_configs:
                - targets: ['<minikube ip>:<Nodeport>']
7. **Access the prometheus UI, Grafana UI and ToDo Application UI**: Access the applications with minikube ip and there respective NodePorts.
8. **Add Prometheus as a Data Source in grafana UI**:
      Navigate to Configuration > Data Sources.
      Click Add data source and select Prometheus.
      Set the URL to http://prometheus-server
9. **Create Dashboards**:
      Go to Create > Dashboard.
      Add panels to visualize the metrics, such as:
        * Total HTTP Requests
        * Memory Usage
        * CPU Usage

## Snapshots:

![Screenshot from 2024-10-31 11-44-43](https://github.com/user-attachments/assets/6b1eb164-8769-4b11-9de7-7387289e0742)
![Screenshot from 2024-10-31 11-47-21](https://github.com/user-attachments/assets/d6cd88be-dfb8-4260-b6f0-b0c33d8deb81)
![Screenshot from 2024-10-31 11-47-02](https://github.com/user-attachments/assets/574899b8-90a0-4231-b1b9-1ed6fede066e)
![Screenshot from 2024-10-31 11-44-57](https://github.com/user-attachments/assets/d79e8960-ca2e-4eb1-8cf4-fa3e346a12a2)




     
