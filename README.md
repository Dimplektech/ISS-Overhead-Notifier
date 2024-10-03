# ISS-Overhead-Notifier

This Python project checks if the International Space Station (ISS) is overhead and whether it is currently dark at your location. If both conditions are met, an email will be sent to notify you to look up and see the ISS.

## Features

- Fetches the current position of the ISS using the [Open Notify ISS API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/).
- Determines if the ISS is within ±5 degrees of your location (latitude and longitude).
- Uses [Sunrise-Sunset API](https://sunrise-sunset.org/api) to check if it's dark at your location.
- Sends an email notification if the ISS is overhead and it's dark.

## Requirements

- **Python 3.x**
- **Libraries**:
  - `requests`: To make HTTP requests.
  - `smtplib`: For sending emails.

 ## API References
- ISS Current Location API: Open Notify ISS API
- Sunrise-Sunset API: Sunrise-Sunset API    

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Dimplektech/ISS-Overhead-Notifier.git

2. **Install required libraries**:
   ```bash
   pip install requests

## Configuration
  1. **Latitude and Longitude**
  - By default, the script is set to check for London (Latitude: 51.507351, Longitude: -0.127758).
    If you want to check for another location, update the following variables in the script with your own latitude and longitude:
     ```bash
    MY_LAT = your_latitude
    MY_LONG = your_longitude
  
  2. **Set up Email Credentials**
  - The code uses Gmail to send email notifications.
  - You will need to generate an App Password in your Google Account for enhanced security. Follow these steps:
      1. Go to your Google Account.
      2. Navigate to **Security** and scroll down to **Signing in to Google**.
      3. Enable **2-Step Verification.**
      4.Once 2-Step Verification is enabled, click on **App Passwords**.
      5.Generate an App Password for **Mail** and use the 16-character code generated.
   - Replace the following values in the script with your email credentials and the App Password you generated:
    
       - my_email = "your_email@gmail.com"
       - password = "your_app_password"
  
  3. **Email Setup**
  - Replace the following values in the script:
  
    - my_email: Your Gmail address.
    - password: Your Gmail App Password generated for this application

## How to Run
```bash
  python main.py






   

   

      


  
