import psutil # this package is necessary to get the metrics of CPU and Memory 
from flask import Flask, render_template # this application is built on flask framework

app = Flask(__name__) # creation of application with name flask 

@app.route("/") # as soon as user comes to home directory this program runs 
def index() : # defining a function
    cpu_percent = psutil.cpu_percent() # CPU info 
    mem_percent = psutil.virtual_memory().percent # memory info in percentage 
    Message = None 
    if cpu_percent > 80 or mem_percent > 80: # if condition 
        Message = "High CPU or Memory Utilization detected. Please scale up"
    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=Message)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')