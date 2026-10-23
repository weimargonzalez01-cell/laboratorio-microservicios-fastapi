from locust import HttpUser, task, between


class Cliente(HttpUser):
    wait_time = between(0.5, 1.5)

    @task
    def usuarios(self):
        self.client.get("/usuarios")

    @task
    def productos(self):
        self.client.get("/productos")

    @task
    def pedidos(self):
        self.client.get("/pedidos")