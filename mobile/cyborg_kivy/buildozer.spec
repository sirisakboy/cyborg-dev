[app]

# (str) Title of your application
title = CYBORG NEXUS Mobile

# (str) Package name
package.name = cyborgnexus

# (str) Package domain (needed for android/ios packaging)
package.domain = com.sirisakboy

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, dist, build

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests,pillow

# (str) Garden requirements
#garden_requirements =

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (str) Permissions
android.permissions = CAMERA,INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android NDK API
android.ndk_api = 21

# (str) Supported architecture
android.arch = arm64-v8a

# (str) Application icon
#icon.filename = 

[buildozer]
log_level = 2
warn_on_root = 1

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) Android SDK directory
#android.sdk_path =

# (str) Android NDK directory
#android.ndk_path =

# (str) Bootstrap for Android
android.bootstrap = sdl2

# (str) Android SDK command to use
android.sdk = 20

# (str) Android NDK command to use
android.ndk = 25b

# (bool) Use fullscreen
fullscreen = 1