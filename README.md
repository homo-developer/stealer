# Covert Data Exfiltration Calculator Application

This repository contains a Kivy-based Android application that, while appearing as a functional calculator, secretly exfiltrates sensitive data from the device to a Telegram bot.

**WARNING: This code is provided for educational purposes ONLY. Unauthorized use of this application to access or exfiltrate data is illegal and unethical. The developer assumes no responsibility for any misuse. Deploying or distributing this application without explicit consent is strictly prohibited and carries severe legal consequences.**

## Description

The application presents a standard calculator interface built with Kivy. In the background, it scans designated directories for specific file types (images and documents) and transmits them to a pre-configured Telegram bot. This functionality is executed in a separate thread, ensuring the calculator remains responsive.

## Features

* **Functional Calculator:** Implements basic arithmetic operations.
* **Background Data Exfiltration:** Stealthily scans and uploads targeted files.
* **Targeted Directories:** Scans the following directories within the device's storage: `WhatsApp`, `DCIM`, `Camera`, `Download`, and `Telegram`.
* **Targeted File Types:** Exfiltrates files with the following extensions: `.jpg`, `.png`, `.jpeg`, `.gif`, `.html`, `.php`, and `.py`.
* **Telegram Integration:** Leverages the Telegram Bot API for data transmission.
* **Asynchronous Operation:** Uses threading to prevent performance degradation during data exfiltration.

## Requirements

* Python 3.x
* Kivy
* `requests` library

## Installation

1.  **Install Dependencies:**

    ```bash
    pip install kivy requests
    ```

2.  **Configuration:**

    * Replace `"BOT_TOKEN"` with your Telegram bot's API token.
    * Replace `"USER_ID"` with the target Telegram chat ID.

3.  **Execution:**

    ```bash
    python your_script_name.py
    ```

## Code Structure

* **`send_document(file_path)` and `send_photo(file_path)`:** These functions handle the transmission of files to the Telegram bot using the `requests` library.
* **`scan_and_steal_data()`:** This function performs the directory scanning and file exfiltration. It utilizes `os.walk` for directory traversal and `threading` for asynchronous execution.
* **`CalculatorApp` (Kivy Class):** This class defines the calculator application's user interface and initiates the data exfiltration process upon launch.

## Security and Ethical Considerations

**EXTREMELY IMPORTANT:** This application poses a severe security risk. It should only be used in controlled environments for educational purposes. Unauthorized deployment or use is strictly prohibited.

* **Data Privacy:** This application violates user privacy by secretly exfiltrating personal data.
* **Legal Implications:** Unauthorized use of this application can result in severe legal penalties.
* **Security Risks:** This application can be exploited by malicious actors for data theft and other harmful activities.
* **Permission Issues:** The code does not handle Android permissions. This will cause the app to fail on modern android devices without the proper storage permissions.

**Disclaimer:** The developer explicitly disclaims any responsibility for the misuse of this code. Use it responsibly and ethically.
