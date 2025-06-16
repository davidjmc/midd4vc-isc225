from multiprocessing import Process, Lock
import uuid
import time
import random
import csv
from collections import defaultdict
from Midd4VCClient import Midd4VCClient

CSV_FILE = "rtt_100_veh4.csv"

class ApplicationClient:
    def __init__(self, client_id, lock, role="client"):
        self.lock = lock
        self.client = Midd4VCClient(role=role, client_id=client_id)
        self.client.set_result_handler(self.on_job_result)

        # Métricas
        self.sent_jobs = {}  # job_id -> timestamp
        self.rtt_values = []  # lista de RTTs
        self.messages_per_vehicle = defaultdict(int)  # vehicle_id -> count
        self.cpu_usage_per_vehicle = defaultdict(list)  # vehicle_id -> list of cpu usages

        self.jobs_sent_count = 0

    def on_job_result(self, data):
        job_id = data.get("job_id")
        vehicle_id = data.get("vehicle_id")
        cpu_usage = data.get("cpu_usage")  # opcional, se veículo enviar isso

        now = time.time()

        # RTT
        if job_id in self.sent_jobs:
            sent_time = self.sent_jobs.pop(job_id) 
            rtt = now - sent_time
            self.rtt_values.append(rtt)
            print(f"[{self.client.client_id}] RTT for {job_id} from {vehicle_id}: {rtt:.3f}s")

        # Contador por veículo
        if vehicle_id:
            self.messages_per_vehicle[vehicle_id] += 1

            # CPU por veículo
            if cpu_usage is not None:
                self.cpu_usage_per_vehicle[vehicle_id].append(cpu_usage)

        print(f"[{self.client.client_id}] Results: {data}")

    def start(self):
        self.client.start()

    def stop(self):
        self.client.stop()
        self.save_rtt_metrics()

        # Mostra métricas ao parar
        print(f"[{self.client.client_id}] MÉTRICAS FINAIS:")
        if self.rtt_values:
            avg_rtt = sum(self.rtt_values) / len(self.rtt_values)
            print(f"→ RTT médio: {avg_rtt:.3f}s")

        print("→ Mensagens por veículo:")
        for v, count in self.messages_per_vehicle.items():
            print(f"  {v}: {count} mensagens")

        print("→ Uso médio de CPU por veículo:")
        for v, cpu_list in self.cpu_usage_per_vehicle.items():
            if cpu_list:
                avg_cpu = sum(cpu_list) / len(cpu_list)
                print(f"  {v}: {avg_cpu:.2f}%")

    def save_rtt_metrics(self):
        if not self.rtt_values:
            return
        avg_rtt = sum(self.rtt_values) / len(self.rtt_values)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        messages_info = "; ".join(
            f"{v}:{c}" for v, c in self.messages_per_vehicle.items()
        ) or "none"

        with self.lock:
            with open(CSV_FILE, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, self.client.client_id, self.jobs_sent_count, f"{avg_rtt:.3f}", messages_info])
            print(f"[{self.client.client_id}] Saved metrics: jobs_sent={self.jobs_sent_count}, avg_rtt={avg_rtt:.3f}s")

    def send_job_periodically(self, min_time=2, max_time=5, save_interval=10):
        try:
            while True:
                job_id = str(uuid.uuid4())
                job = {
                    "job_id": job_id,
                    "function": "math.factorial",
                    "args": [random.randint(1, 10)]
                }

                print(f"[{self.client.client_id}] Submitting job: {job['job_id']} with args: {job['args'][0]}")
                self.sent_jobs[job_id] = time.time()  # start time
                self.client.submit_job(job)
                self.jobs_sent_count += 1

                if self.jobs_sent_count % save_interval == 0:
                    while len(self.rtt_values) < self.jobs_sent_count:
                        time.sleep(0.1)
                    self.save_rtt_metrics()

                # time.sleep(random.uniform(min_time, max_time))
                time.sleep(5)

        except KeyboardInterrupt:
            print(f"[{self.client.client_id}] stopping...")
            self.save_rtt_metrics()

def run_app(client_id, lock):
    app_client = ApplicationClient(client_id=client_id, lock=lock)
    app_client.start()
    app_client.send_job_periodically(min_time=5, max_time=10, save_interval=10)
    app_client.stop()

if __name__ == "__main__":
 
    # Inicializa o arquivo CSV com cabeçalho só uma vez
    with open(CSV_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "client_id", "jobs_sent", "avg_rtt", "messages_per_vehicle"])

    client_ids = [f"Application_{i}" for i in range(1, 101)]  # Mude aqui para a quantidade desejada
    lock = Lock()
    processes = []

    for cid in client_ids:
        p = Process(target=run_app, args=(cid,lock))
        p.start()
        processes.append(p)

    try:
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        print("Stopping all applications...")
        for p in processes:
            p.terminate()


