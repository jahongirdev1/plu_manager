# plu_manager

`plu_manager` is a universal PLU (Price Look-Up) automation bot that:
- Fetches product data (JSON) from any API or input,
- Saves the data to a `.xls` file in UTF-16 tab-separated format,
- Automatically runs the **PLU Manager** (RTPLU.exe) software and imports the file using screen automation,
- Supports multiple screen resolutions.

---

## 🚀 Features

- Works with `PLU Manager` software (RTPLU.exe)
- Supports JSON input
- Automatically handles different screen resolutions (1024x768, 1920x1080, etc.)
- Windows-only
- Displays message boxes on error/success

---

## 🛠 Installation

Clone the project and install dependencies:

```bash
https://github.com/jahongirdev1/plu_manager
cd plu_manager
pip install -r requirements.txt
