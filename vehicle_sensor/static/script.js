$(document).ready(function () {
    const oiltemps_ctx = document.getElementById("oil_temps_chart").getContext("2d");
    const intaketemps_ctx = document.getElementById("intake_temps_chart").getContext("2d");
    const coolanttemps_ctx = document.getElementById("coolant_temps_chart").getContext("2d");
    const rpms_ctx = document.getElementById("rpms_chart").getContext("2d");
    const speeds_ctx = document.getElementById("speeds_chart").getContext("2d");
    const throttlepos_ctx = document.getElementById("throttle_pos_chart").getContext("2d");
  
    const myChart_oiltemps = new Chart(oiltemps_ctx, {
      type: "line",
      data: {
        datasets: [{ label: "Oil Temperature",  }],
      },
      options: {
        borderWidth: 3,
        borderColor: ['rgba(255, 99, 132, 1)',],
      },
    });

    const myChart_intaketemps = new Chart(intaketemps_ctx, {
      type: "line",
      data: {
        datasets: [{ label: "Intake Temperature",  }],
      },
      options: {
        borderWidth: 3,
        borderColor: ['rgba(255, 99, 132, 1)',],
      },
    });

    const myChart_coolanttemps = new Chart(coolanttemps_ctx, {
      type: "line",
      data: {
        datasets: [{ label: "Coolant Temperature",  }],
      },
      options: {
        borderWidth: 3,
        borderColor: ['rgba(255, 99, 132, 1)',],
      },
    });

    const myChart_rpms = new Chart(rpms_ctx, {
      type: "line",
      data: {
        datasets: [{ label: "RPM",  }],
      },
      options: {
        borderWidth: 3,
        borderColor: ['rgba(255, 99, 132, 1)',],
      },
    });

    const myChart_speeds = new Chart(speeds_ctx, {
      type: "line",
      data: {
        datasets: [{ label: "Speeds Measure",  }],
      },
      options: {
        borderWidth: 3,
        borderColor: ['rgba(255, 99, 132, 1)',],
      },
    });

    const myChart_throttlepos = new Chart(throttlepos_ctx, {
      type: "line",
      data: {
        datasets: [{ label: "Throttle Position",  }],
      },
      options: {
        borderWidth: 3,
        borderColor: ['rgba(255, 99, 132, 1)',],
      },
    });
  
    function addData(chart, label, data) {
      chart.data.labels.push(label);
      chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
      });
      chart.update();
    }

    function removeFirstData(chart) {
      chart.data.labels.splice(0, 1);
      chart.data.datasets.forEach((dataset) => {
        dataset.data.shift();
      });
    }
  
      var socket = io.connect("http://127.0.0.1:5000/");
  
    socket.on("updateSensorData", function (msg) {
      console.log("Received Vehicular Data :: Time: " + msg.time + 
      " :: Oil Temperature: " + msg.oil_temps + 
      " :: Intake Temeprature: " + msg.intake_temps +
      " :: Coolant Temperature: " + msg.coolant_temps + 
      " :: RPM: " + msg.rpms +
      " :: Speeds Measure: " + msg.speeds + 
      " :: Throttle Position: " + msg.throttle_pos 
      );
  
      if (myChart_oiltemps.data.labels.length > 10) {
        removeFirstData(myChart_oiltemps);
        removeFirstData(myChart_intaketemps);
        removeFirstData(myChart_coolanttemps);
        removeFirstData(myChart_rpms);
        removeFirstData(myChart_speeds);
        removeFirstData(myChart_throttlepos);
      }

      addData(myChart_oiltemps, msg.time, msg.oil_temps);
      addData(myChart_intaketemps, msg.time, msg.intake_temps);
      addData(myChart_coolanttemps, msg.time, msg.coolant_temps);
      addData(myChart_rpms, msg.time, msg.rpms);
      addData(myChart_speeds, msg.time, msg.speeds);
      addData(myChart_throttlepos, msg.time, msg.throttle_pos);

    });

    window.onbeforeunload = function () {
      socket.emit('client_disconnecting',);
  }
  });