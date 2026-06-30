# Mobile App Guide - Publishing to Play Store & App Store

## 🎯 Overview

This guide explains how to convert the Math King Calculator + To-Do List into mobile apps for:
- **Google Play Store** (Android)
- **Apple App Store** (iOS)

---

## 🛠️ Tools & Frameworks

We'll use **Kivy** and **Buildozer** to convert Python to mobile apps.

### Why Kivy?
- ✅ Python-based mobile framework
- ✅ Works on Android & iOS
- ✅ Native performance
- ✅ Large community support
- ✅ Open source & free

---

## 📋 Prerequisites

### For Android (Google Play Store):
- **Windows/Mac/Linux**
- **Java Development Kit (JDK)** - 8 or higher
- **Android SDK** - API level 21+
- **Android NDK**
- **Buildozer**

### For iOS (App Store):
- **Mac OS X** - Required for iOS development
- **Xcode**
- **Python 3.7+**
- **Cython**
- **PyObjC**

---

## 🔧 Setup Instructions

### Step 1: Install Kivy

```bash
# Create virtual environment
python -m venv kivy_env
source kivy_env/bin/activate  # On Windows: kivy_env\Scripts\activate

# Install Kivy
pip install kivy

# Install build tools
pip install buildozer
pip install Cython
pip install java-access-bridge-wrapper
```

### Step 2: Install Android Dependencies (for Android)

**On Linux/Mac:**
```bash
brew install java
brew install android-sdk
brew install android-ndk
```

**On Windows:**
- Download JDK from [Oracle](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)
- Download Android SDK from [Google](https://developer.android.com/studio)
- Download Android NDK from [Google](https://developer.android.com/ndk/downloads)

### Step 3: Install iOS Dependencies (for Mac only)

```bash
# Install Xcode
xcode-select --install

# Install dependencies
pip install pyobjc
pip install pyobjc-framework-Cocoa
```

---

## 📱 Creating Android App

### Step 1: Set Up Kivy Project

```bash
mkdir -p ~/kivy_projects/math_king_calculator
cd ~/kivy_projects/math_king_calculator
```

### Step 2: Create buildozer.spec

Create `buildozer.spec` file:

```ini
[app]

title = Math King Calculator
package.name = mathkingcalculator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0.0

requirements = python3,kivy,numpy,scipy

orientations = portrait,landscape

fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

android.arch = arm64-v8a
android.release_artifact = aab

android.gradle_dependencies = 

android.add_src = 

android.meta_data = 

[buildozer]
log_level = 2
warn_on_root = 1
```

### Step 3: Build APK/AAB

```bash
# Build APK (for testing)
buildozer android debug

# Build AAB (for Play Store)
buildozer android release
```

### Step 4: Sign APK/AAB

```bash
# Create keystore (one time)
keytool -genkey -v -keystore my-release-key.keystore -keyalg RSA -keysize 2048 -validity 10000 -alias my-key-alias

# Sign APK
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore bin/mathkingcalculator-1.0.0-release-unsigned.apk my-key-alias

# Verify APK
jarsigner -verify -verbose -certs bin/mathkingcalculator-1.0.0-release-unsigned.apk
```

### Step 5: Upload to Play Store

1. Go to [Google Play Console](https://play.google.com/console)
2. Create new app
3. Fill app details
4. Add screenshots
5. Add privacy policy
6. Upload signed APK/AAB
7. Submit for review

---

## 🍎 Creating iOS App

### Step 1: Create Xcode Project

```bash
buildozer ios debug
```

### Step 2: Build for iOS

```bash
# Build IPA (iOS app package)
buildozer ios release
```

### Step 3: Sign for App Store

1. Open Xcode project
2. Select team
3. Configure signing
4. Enable automatic code signing

### Step 4: Upload to App Store

1. Go to [App Store Connect](https://appstoreconnect.apple.com/)
2. Create new app
3. Fill app details
4. Add screenshots
5. Add privacy policy
6. Upload IPA using Transporter
7. Submit for review

---

## 📝 App Store Requirements

### Google Play Store:

**Required Files:**
- ✅ App icon (512x512 px)
- ✅ Screenshots (up to 8, 1080x1920 px)
- ✅ Feature graphic (1024x500 px)
- ✅ Privacy policy URL
- ✅ Content rating questionnaire
- ✅ App description (short & long)

**Account Setup:**
- Create Google Play Developer account ($25 one-time)
- Add payment method
- Create app listing
- Upload signed APK/AAB

### Apple App Store:

**Required Files:**
- ✅ App icon (1024x1024 px)
- ✅ Screenshots (5 minimum, 1242x2208 px for iPhone)
- ✅ Preview video (optional)
- ✅ Privacy policy URL
- ✅ Support URL
- ✅ App description

**Account Setup:**
- Apple Developer Program account ($99 per year)
- Enroll in App Store Connect
- Create app identifier
- Create certificates & provisioning profiles
- Upload signed IPA

---

## 🎨 App Store Assets

### Icon Design

**Google Play Store:**
- Size: 512×512 pixels
- Format: PNG, JPG, or GIF
- File size: Max 1 MB

**App Store:**
- Size: 1024×1024 pixels
- Format: JPG or PNG
- File size: Max 1 MB
- No transparency or alpha channels

### Screenshots

**Google Play Store:**
- 5-8 screenshots
- Size: 1080×1920 pixels
- Format: JPG or PNG

**App Store:**
- 5 minimum per device
- iPhone: 1242×2208 pixels
- iPad: 2048×2732 pixels

---

## 📋 Submission Checklist

### Before Submission:

- [ ] App fully functional and tested
- [ ] All features working on mobile
- [ ] Privacy policy ready
- [ ] Support email address
- [ ] App icons created (multiple sizes)
- [ ] Screenshots ready
- [ ] App description written
- [ ] Pricing set
- [ ] No hardcoded credentials
- [ ] Performance optimized
- [ ] Storage permissions handled
- [ ] Network permissions handled

### Google Play Store:

- [ ] Google Play Developer account created
- [ ] Payment method added
- [ ] App signed with keystore
- [ ] Content rating completed
- [ ] Privacy policy URL added
- [ ] Contact email provided
- [ ] AAB/APK uploaded
- [ ] Tested on multiple devices

### Apple App Store:

- [ ] Apple Developer account active
- [ ] App identifier created
- [ ] Certificate generated
- [ ] Provisioning profile created
- [ ] App signed with certificate
- [ ] Privacy policy URL added
- [ ] Support URL added
- [ ] IPA built and tested

---

## 🚀 Build Commands Reference

```bash
# Initialize Kivy project
kivy start myapp

# Build debug APK
buildozer android debug

# Build release AAB
buildozer android release

# Build iOS debug
buildozer ios debug

# Build iOS release
buildozer ios release

# Clean build
buildozer android clean

# Check status
buildozer status

# Run on device
adb install -r bin/mathkingcalculator-debug.apk
```

---

## 📊 Costs

### Google Play Store:
- Developer account: $25 (one-time)
- App listings: Free
- Updates: Free
- In-app purchases: 30% commission

### Apple App Store:
- Developer Program: $99/year
- App listings: Free
- Updates: Free
- In-app purchases: 30% commission

---

## 🔐 App Security

### Before Publishing:

1. **Remove Debug Code**
   ```python
   # Remove print statements for logging
   # Remove test data
   # Remove development URLs
   ```

2. **Secure Storage**
   ```python
   # Use encrypted storage for sensitive data
   # Don't store passwords
   # Use secure APIs
   ```

3. **Permissions**
   - Request only necessary permissions
   - Explain why you need each permission
   - Handle denials gracefully

4. **Privacy**
   - Clear privacy policy
   - No unnecessary data collection
   - Comply with GDPR (EU) & CCPA (US)

---

## 📱 Testing on Devices

### Android:

```bash
# Connect device and enable USB debugging

# Install debug APK
adb install -r bin/mathkingcalculator-debug.apk

# Run app
adb shell am start -n org.example.mathkingcalculator/.MainActivity

# View logs
adb logcat
```

### iOS:

```bash
# Connect device to Mac
# Open Xcode
# Select device
# Run project
# Or use ios-deploy:
ios-deploy --bundle path/to/app.ipa --id DEVICE_ID
```

---

## 🆘 Troubleshooting

### Common Issues:

**Issue: "Java not found"**
```bash
# Set JAVA_HOME
export JAVA_HOME=/path/to/jdk
```

**Issue: "Android SDK not found"**
```bash
# Set ANDROID_SDK_ROOT
export ANDROID_SDK_ROOT=/path/to/android-sdk
export ANDROID_NDK_ROOT=/path/to/android-ndk
```

**Issue: "Build fails with Cython error"**
```bash
pip install --upgrade Cython
```

**Issue: "App crashes on startup"**
```bash
# Check logs:
adb logcat | grep myapp

# Add error handling
# Test with minimal features
```

---

## 📚 Additional Resources

- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Google Play Console](https://play.google.com/console)
- [App Store Connect](https://appstoreconnect.apple.com/)
- [Android Studio Guide](https://developer.android.com/studio)
- [Xcode Guide](https://developer.apple.com/xcode/)

---

## 🎯 Next Steps

1. ✅ Set up development environment
2. ✅ Create Kivy UI for mobile
3. ✅ Test on emulator/device
4. ✅ Create app icons & screenshots
5. ✅ Write privacy policy
6. ✅ Build signed APK/IPA
7. ✅ Submit to stores
8. ✅ Monitor reviews & update

---

**Ready to launch your app?** Start with Android first (faster approval), then move to iOS! 🚀
