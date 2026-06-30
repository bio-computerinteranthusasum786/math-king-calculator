# buildozer.spec
# Buildozer specification for building Math King Calculator Android App
# This file configures how the app is built for different platforms

[app]
# Application title and package info
title = Math King Calculator
package.name = mathkingcalculator
package.domain = org.mathking

# Source files
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

# Version
version = 1.0.0

# Requirements (what Python packages the app needs)
requirements = python3,kivy,numpy,scipy,android

# Orientation
orientations = portrait,landscape

# Screen settings
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android specific
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Build architecture
android.arch = arm64-v8a
android.release_artifact = aab

# App icon (1024x1024 png)
# icon.filename = %(source.dir)s/data/icon.png

# Presplash (512x512 png)
# presplash.filename = %(source.dir)s/data/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1
