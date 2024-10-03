
import smtplib
import  requests
from datetime import datetime
import time
MY_LAT = 51.507351
MY_LONG = -0.127758


# ---Location of the ISS
# check whether ISS is nearer to us

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_long = data["iss_position"]["longitude"]
    iss_lati = data["iss_position"]["latitude"]

    iss_position = (iss_long, iss_lati )
    print(iss_position)
    # Your position is within +5 or -5 degrees of the ISS position
    if MY_LAT - 5 <= float(iss_lati) <= MY_LAT + 5 and MY_LONG - 5 <= float(iss_long) >= MY_LONG + 5:
        return True

def is_dark():
    #---get sunrise and sunset time of your location
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0
    }
    response= requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()

    # In API json file time is in 2024-10-03T06:03:47+00:00 format
    # and we need just time in hr in 24 hr clock format,so split
    # original time by T first then ":"
    sunrise = (data["results"]["sunrise"]).split("T")[1].split(":")[0]
    sunset = (data["results"]["sunset"]).split("T")[1].split(":")[0]
    print(sunrise)
    print(sunset)
    # Check whether it is  currently dark?
    time_now = datetime.now()
    curr_hr = time_now.hour

    if curr_hr > int(sunset) or curr_hr <= int(sunrise):
       return True


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    # Keep checking in 1 min
    time.sleep(60)
    if is_dark() and  is_iss_overhead():
        # ---Create Connection to send email
        my_email = "dimple.temp27@gmail.com"
        password = "ijtp nazs bupm prmt"  # App password not email password
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="dimple.temp27@yahoo.com",
                            msg="Subject:Look up!! \n\n International Space Ship(ISS) is above in the Sky")
        connection.close()
        print("LOOK UP IN THE SKY ,U might see Iss!!")
    else:
        print("Not yet")














