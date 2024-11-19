import wmi

def get_battery_status():
    battery_data = []
    w = wmi.WMI()
    for battery in w.query("SELECT * FROM Win32_Battery"):
        battery_data.append({
            "name": battery.Name,
            "status": battery.BatteryStatus,
            "estimated_charge_remaining": battery.EstimatedChargeRemaining,
            "estimated_run_time": battery.EstimatedRunTime
        })
    return battery_data

if __name__ == "__main__":
    status = get_battery_status()
    print("Battery Status:", status)
