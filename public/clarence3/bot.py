COMPONENTS = [
    {
        "name": "Base",
        "port": "A",
        "min": 0,
        "max": 360
    },
    {
        "name": "Secondary Arm",
        "port": "D",
        "min": 204,
        "max": 311
    },{
        "name": "Primary Arm",
        "port": "E",
        "min": 8,
        "max": 149
    },{
        "name": "Gripper",
        "port": "C",
        "min": 136,
        "max": 238
    }
]

def from_percent(min, max, percentage):
    return min + ((max - min) * percentage)

def run_component(index, percentage, leverage = 5):
    component = COMPONENTS[index]
    port = component["port"]
    min = component["min"] + leverage
    max = component["max"] - leverage
    
    true_percent = percentage / 100
    
    degree = int(from_percent(min, max, true_percent))
    print(component["name"], degree)
    
data = [50, 50, 50, 50]
for i in range(len(data)):
    run_component(i, data[i])