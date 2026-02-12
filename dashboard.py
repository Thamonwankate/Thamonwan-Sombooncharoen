from flask import Flask, render_template_string
from flask_socketio import SocketIO
import serial, time

# ---------------- Serial ----------------
SERIAL_PORT = "COM4"   # เปลี่ยนเป็นพอร์ตจริง
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"เปิด Serial port: {SERIAL_PORT} @ {BAUD_RATE}")
except Exception as e:
    print(f"ไม่สามารถเปิด Serial Port: {e}")
    ser = None

# ---------------- Flask + SocketIO ----------------
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# ---------------- HTML Template ----------------
HTML = """  
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<title>Aquarium Dashboard</title>
<script src="https://cdn.socket.io/4.6.1/socket.io.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
body, html { margin:0; padding:0; overflow:hidden; background:#0a1b2a; font-family: Arial, sans-serif;}
canvas#aquarium { position:absolute; top:0; left:0; z-index:0;}
.bubble { position:absolute; background: rgba(135,206,250,0.6); border-radius: 50%; padding: 10px 15px; font-weight: bold; text-align: center; font-size: 14px; box-shadow:0 0 15px rgba(135,206,250,0.8); pointer-events: none; z-index: 5;}
#alerts { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background: #ff4444; color: white; padding: 12px 24px; border-radius: 20px; font-size: 18px; display: none; box-shadow: 0 0 20px rgba(255,0,0,0.8); z-index: 15;}
#charts { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; z-index: 10; background: rgba(0,0,0,0.5); border-radius: 15px; padding: 15px;}
.chart-container { flex: 1 1 300px; height: 240px; background: rgba(255,255,255,0.08); border-radius: 10px; padding: 10px;}
.chart-container canvas { width: 100% !important; height: 100% !important;}
</style>
</head>
<body>
<canvas id="aquarium"></canvas>

<div class="bubble" id="bubbleTemp">Temp: - °C</div>
<div class="bubble" id="bubblePH">pH: -</div>
<div class="bubble" id="bubbleMotion">Motion: -</div>

<div id="alerts"></div>

<div id="charts">
    <div class="chart-container"><canvas id="chartTemp"></canvas></div>
    <div class="chart-container"><canvas id="chartPH"></canvas></div>
    <div class="chart-container"><canvas id="chartMotion"></canvas></div>
</div>

<script>
const socket = io();
const bubbleTemp = document.getElementById("bubbleTemp");
const bubblePH   = document.getElementById("bubblePH");
const bubbleMotion = document.getElementById("bubbleMotion");
const alertBox = document.getElementById("alerts");

// Bubble positions
const bubbles = [
    { el: bubbleTemp, offsetX: 20 },
    { el: bubblePH, offsetX: 180 },
    { el: bubbleMotion, offsetX: 340 }
];
function updateBubblePositions() {
    const top = 20;
    bubbles.forEach(b => { b.el.style.top = top+"px"; b.el.style.left = b.offsetX+"px"; });
}
updateBubblePositions();
window.addEventListener("resize", updateBubblePositions);

// Canvas Aquarium
const canvas = document.getElementById("aquarium");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
window.addEventListener("resize", ()=>{canvas.width=window.innerWidth; canvas.height=window.innerHeight;});

class Fish{
    constructor(){ this.x=Math.random()*canvas.width; this.y=Math.random()*canvas.height*0.7; this.size=30+Math.random()*20; this.speed=1+Math.random()*2; this.dir=Math.random()<0.5?1:-1; this.color=["orange","red","yellow","cyan"][Math.floor(Math.random()*4)]; }
    draw(){
        ctx.beginPath(); ctx.fillStyle=this.color; ctx.ellipse(this.x,this.y,this.size,this.size*0.5,0,0,2*Math.PI); ctx.fill(); ctx.closePath();
        ctx.beginPath(); ctx.moveTo(this.x-this.size*this.dir,this.y); ctx.lineTo(this.x-this.size*this.dir-10,this.y-10); ctx.lineTo(this.x-this.size*this.dir-10,this.y+10); ctx.fill(); ctx.closePath();
        ctx.beginPath(); ctx.fillStyle="white"; ctx.arc(this.x+this.size*0.3*this.dir,this.y-5,4,0,2*Math.PI); ctx.fill();
        ctx.beginPath(); ctx.fillStyle="black"; ctx.arc(this.x+this.size*0.3*this.dir,this.y-5,2,0,2*Math.PI); ctx.fill();
    }
    update(){ this.x+=this.speed*this.dir; if(this.x>canvas.width+50)this.x=-50; if(this.x<-50)this.x=canvas.width+50; this.y+=Math.sin(Date.now()/500+this.x/50)*0.3; this.draw();}
}
const fishes=[]; for(let i=0;i<12;i++) fishes.push(new Fish());
function drawAquarium(){ 
    ctx.clearRect(0,0,canvas.width,canvas.height); 
    const grad=ctx.createLinearGradient(0,0,0,canvas.height); 
    grad.addColorStop(0,"#0a1b2a"); grad.addColorStop(1,"#03396c"); 
    ctx.fillStyle=grad; ctx.fillRect(0,0,canvas.width,canvas.height);
    for(let i=0;i<15;i++){ 
        ctx.fillStyle="green"; ctx.fillRect(i*60,canvas.height-50,10,50+Math.random()*30); 
        ctx.fillStyle="grey"; ctx.beginPath(); ctx.arc(i*60+10,canvas.height-10,10,0,2*Math.PI); ctx.fill(); 
    } 
    fishes.forEach(f=>f.update()); 
    requestAnimationFrame(drawAquarium);
}
drawAquarium();

// Chart.js
function createChart(ctx,label,color,yMin=null,yMax=null){
    return new Chart(ctx,{
        type:'line',
        data:{labels:[], datasets:[{label:"", data:[], borderColor:color, borderWidth:2, pointRadius:0, tension:0.35, fill:false}]},
        options:{
            responsive:true,
            maintainAspectRatio:false,
            animation:false,
            plugins:{legend:{display:false}, title:{display:true, text:label, color:'white', font:{size:16,weight:'bold'}, padding:{bottom:10}}},
            scales:{
                x:{ ticks:{color:'white'}, grid:{color:"rgba(255,255,255,0.1)"} },
                y:{ ticks:{color:'white'}, grid:{color:"rgba(255,255,255,0.1)"}, min:yMin, max:yMax }
            }
        }
    });
}

const chartTemp = createChart(document.getElementById("chartTemp"), "Temperature (°C)", "orange", 0, 40);
const chartPH   = createChart(document.getElementById("chartPH"), "pH Level", "lime", 0, 15);
const chartMotion = createChart(document.getElementById("chartMotion"), "Motion", "cyan");

// SocketIO handler
socket.on("sensor_update", payload=>{
    console.log("Received:", payload); // debug
    const {temp,pir,ph,alerts}=payload;
    bubbleTemp.textContent=`Temp: ${temp.toFixed(2)}°C`;
    bubblePH.textContent=`pH: ${ph.toFixed(2)}`;
    bubbleMotion.textContent=`Motion: ${pir}`;
    if(alerts && alerts.length>0){ 
        alertBox.style.display="block"; 
        alertBox.textContent="⚠ "+alerts.join(" • "); 
        setTimeout(()=>{alertBox.style.display="none";},5000);
    }
    const time=new Date().toLocaleTimeString();
    const charts=[[chartTemp,temp],[chartPH,ph],[chartMotion,pir]];
    charts.forEach(([chart,val])=>{
        chart.data.labels.push(time);
        chart.data.datasets[0].data.push(val);
        if(chart.data.labels.length>30){ chart.data.labels.shift(); chart.data.datasets[0].data.shift(); }
        chart.update();
    });
});
</script>
</body>
</html>
"""

# Flask route
@app.route('/')
def index():
    return render_template_string(HTML)

# ---------------- Serial Reading ----------------
def read_serial():
    if ser is None:
        print("Serial port not opened. Thread exiting.")
        return

    while True:
        try:
            raw = ser.readline().decode('utf-8', errors='ignore').strip()
            if not raw: 
                time.sleep(0.1)
                continue
            if not raw.startswith("Temp:"):  # ข้ามบรรทัดอื่น
                continue

            parts = raw.split(",")
            temp = float(parts[0].split(":")[1])
            pir  = int(parts[1].split(":")[1])
            ph   = float(parts[2].split(":")[1])

            alerts=[]
            if temp>30: alerts.append("Water temperature too high!")
            if not (6.5<=ph<=8.5): alerts.append(f"Water quality abnormal - pH:{ph:.2f}")
            if pir==1: alerts.append("Motion detected!")

            # emit ข้อมูลไปหน้าเว็บ
            socketio.emit("sensor_update", {"temp":temp,"pir":pir,"ph":ph,"alerts":alerts}, namespace="/")

        except Exception as e:
            print("Serial read error:", e)
        time.sleep(0.1)

# start background task using SocketIO async safe
socketio.start_background_task(read_serial)

# ---------------- Run ----------------
if __name__=="__main__":
    print("เปิดเว็บ: http://localhost:5000")
    socketio.run(app, host="0.0.0.0", port=5000, use_reloader=False)
