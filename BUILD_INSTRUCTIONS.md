# Installation & Build Instructions for Mobile App

## Quick Setup

### 1. Install Kivy and Buildozer

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install kivy buildozer cython
pip install -r requirements.txt
```

### 2. Prepare for Android Build

#### On Linux:
```bash
sudo apt-get install python3-pip python3-dev
sudo apt-get install default-jdk
sudo apt-get install android-sdk
sudo apt-get install android-ndk

# Set environment variables
export ANDROID_SDK_ROOT=/path/to/android-sdk
export ANDROID_NDK_ROOT=/path/to/android-ndk
```

#### On Mac:
```bash
brew install openjdk
brew install android-sdk
brew install android-ndk
```

#### On Windows:
- Install JDK from Oracle website
- Download Android SDK
- Download Android NDK
- Set environment variables in System Properties

### 3. Build APK for Testing

```bash
cd ~/path/to/math_king_calculator
buildozer android debug
```

Output: `bin/mathkingcalculator-debug.apk`

### 4. Build AAB for Play Store

```bash
buildozer android release
```

Output: `bin/mathkingcalculator-release-unsigned.aab`

### 5. Sign the APK/AAB

```bash
# Create keystore (first time only)
keytool -genkey -v -keystore my-release-key.keystore \
  -keyalg RSA -keysize 2048 -validity 10000 \
  -alias my-key-alias

# Sign APK
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 \
  -keystore my-release-key.keystore \
  bin/mathkingcalculator-release.apk my-key-alias

# Align APK
zipalign -v 4 bin/mathkingcalculator-release.apk \
  bin/mathkingcalculator-release-aligned.apk
```

## Testing

### Install on Android Device

```bash
# Enable USB Debugging on device
# Connect device to computer

adb install -r bin/mathkingcalculator-debug.apk

# View logs
adb logcat
```

### Using Emulator

```bash
# Create emulator
emulator -avd MyDevice

# Install APK
adb install -r bin/mathkingcalculator-debug.apk
```

## Troubleshooting

### Issue: "Java not found"
```bash
export JAVA_HOME=/path/to/jdk
```

### Issue: "Android SDK not found"
```bash
export ANDROID_SDK_ROOT=/path/to/android-sdk
export ANDROID_NDK_ROOT=/path/to/android-ndk
```

### Issue: Build fails
```bash
# Clean and retry
buildozer android clean
buildozer android debug
```

## Next: Submit to Play Store

See MOBILE_APP_GUIDE.md for Play Store submission instructions
