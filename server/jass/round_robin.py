import json
import time

def assign_jobs_round_robin(engine):
    engine.check_job_timeouts()

    busy_vehicles = set(engine.jobs_in_progress.values())
    total_vehicles = len(engine.vehicle_order)

    if total_vehicles == 0:
        print("[Midd4VCServer] No vehicles registered.")
        return

    assigned_count = 0

    while engine.jobs_queue and assigned_count < total_vehicles:
        job = engine.jobs_queue.pop(0)
        job_id = job["job_id"]

        # Tenta encontrar o próximo veículo livre
        tries = 0
        assigned = False

        while tries < total_vehicles:
            vehicle_id = engine.vehicle_order[engine.next_vehicle_index]
            engine.next_vehicle_index = (engine.next_vehicle_index + 1) % total_vehicles

            if vehicle_id not in busy_vehicles:
                # Veículo disponível encontrado
                engine.jobs_in_progress[job_id] = vehicle_id
                engine.job_assignments[job_id] = {
                    "vehicle_id": vehicle_id,
                    "assigned_at": time.time(),
                    "job_data": job
                }

                print(f"[Midd4VCServer] Assigning job {job_id} to vehicle {vehicle_id} (Round-Robin)")
                if engine.mqtt_client:
                    engine.mqtt_client.publish(f"vc/vehicle/{vehicle_id}/job/assign", json.dumps(job), qos=1)
                else:
                    print(f"[Midd4VCServer] MQTT client not set. Cannot assign job {job_id}.")
                assigned = True
                assigned_count += 1
                break

            tries += 1

        if not assigned:
            # Nenhum veículo disponível no ciclo atual
            engine.jobs_queue.insert(0, job)
            break
