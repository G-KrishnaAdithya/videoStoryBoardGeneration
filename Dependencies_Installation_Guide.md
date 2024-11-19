
# Dependencies Installation Guide: ImageMagick and FFmpeg

This document provides instructions for installing **ImageMagick** and **FFmpeg** on macOS, Linux, and Windows.

---

## **1. ImageMagick**

ImageMagick is a tool for image creation, editing, and conversion.

### **macOS**:
1. Install Homebrew (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install ImageMagick via Homebrew:
   ```bash
   brew install imagemagick
   ```

### **Linux**:
1. For Ubuntu/Debian-based systems:
   ```bash
   sudo apt update
   sudo apt install imagemagick -y
   ```
2. For CentOS/RHEL-based systems:
   ```bash
   sudo yum install epel-release -y
   sudo yum install ImageMagick -y
   ```

### **Windows**:
1. Download the Windows installer from the [official website](https://imagemagick.org/script/download.php).
2. Run the installer and follow the instructions.
3. Add ImageMagick to your system's PATH during installation.

---

## **2. FFmpeg**

FFmpeg is a powerful tool for video and audio processing.

### **macOS**:
1. Install FFmpeg via Homebrew:
   ```bash
   brew install ffmpeg
   ```

### **Linux**:
1. For Ubuntu/Debian-based systems:
   ```bash
   sudo apt update
   sudo apt install ffmpeg -y
   ```
2. For CentOS/RHEL-based systems:
   ```bash
   sudo yum install epel-release -y
   sudo yum install ffmpeg -y
   ```

### **Windows**:
1. Download the latest FFmpeg build from the [official site](https://ffmpeg.org/download.html).
2. Extract the archive to a preferred location (e.g., `C:\ffmpeg`).
3. Add FFmpeg to the system PATH:
   - Open **System Properties** -> **Environment Variables**.
   - Add `C:\ffmpeg\bin` to the PATH variable.
4. Verify the installation by running:
   ```cmd
   ffmpeg -version
   ```

---

## **Verification**

To verify the installations:
- **ImageMagick**:
  ```bash
  magick -version
  ```
- **FFmpeg**:
  ```bash
  ffmpeg -version
  ```

Ensure both tools are accessible via the terminal/command prompt.

---

## **Additional Resources**

- [ImageMagick Documentation](https://imagemagick.org/script/index.php)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)

