class AirlineCargoExpertSystem:
    def __init__(self):
        print("--- Airline Logistical & Cargo Fleet Scheduling Expert System Initialized ---")

    def schedule_routing(self, cargo_type, weather_status, runway_capacity):
        # Knowledge Base Rules Engine
        if weather_status == 'severe' or runway_capacity == 'critical':
            return "Routing Decision: HOLD ALL FLIGHTS. Trigger automated ground stop. Diversify airborne assets to alternate hubs."
        
        if cargo_type == 'perishable' or cargo_type == 'hazardous':
            if runway_capacity == 'nominal':
                return "Routing Decision: PRIORITY ROUTING STAGE 1. Allocate immediate runway clearance slots, route via primary high-speed corridor."
            else:
                return "Routing Decision: EXPRESS EXPEDITE. Clear secondary logistics paths, issue priority taxi instructions."
        elif cargo_type == 'standard' and weather_status == 'nominal':
            return "Routing Decision: STANDARD FREIGHT ROUTING. Queue behind priority commercial passenger liners within normal intervals."
        else:
            return "Routing Decision: DEFERRED OFF-PEAK ROUTING. Reschedule flights to midnight cargo operation blocks to reduce system load."

# Interactive Interface
cargo = input("Enter primary freight freight classification (perishable / hazardous / standard): ").strip().lower()
weather = input("Enter origin/destination weather conditions vector (nominal / severe): ").strip().lower()
runway = input("Enter live airside runway capacity index status (nominal / full / critical): ").strip().lower()

flight_plan = AirlineCargoExpertSystem().schedule_routing(cargo, weather, runway)
print(f"\n[ATC Dispatch Directive]\n{flight_plan}")
