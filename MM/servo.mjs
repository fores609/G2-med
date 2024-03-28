import pigpio from 'pigpio'

const sleep = delayMs => new Promise(resolve => setTimeout(resolve, delayMs))

// SG90 Micro Servo
//const rateHz = 50
const min_angle = -90
const min_usec = 500
const max_angle = 90
const max_usec = 2500

const servo = new pigpio.Gpio(19, { mode: pigpio.Gpio.OUTPUT })

async function setAngle(servo, angle) {
  const duty_usec = Math.floor(((angle - min_angle) / (max_angle - min_angle)) * (max_usec - min_usec) + min_usec)
  console.log(`SERVO: ${angle} ${duty_usec}`)
  servo.servoWrite(duty_usec)
}

async function run() {
  await setAngle(servo, min_angle)
  await sleep(2000)

  await setAngle(servo, 0)
  await sleep(2000)

  await setAngle(servo, max_angle)
  await sleep(2000)
  
  servo.servoWrite(0)
}

run()