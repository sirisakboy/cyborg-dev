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

# (list) List of exclusions using pattern matching
source.exclude_patterns = license,images/*/*.gz

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests,base64,datetime,pillow

# (str) Custom source folders for requirements
# Sets the source folders for requirements
requirements.source = 

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = 

# (str) Icon of the application
#icon.filename = 

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (str) Permissions
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET

# (list) Permissions
#android.permissions = INTERNET

# (int) Target Android API, should be >= 28
android.api = 33

# (int) Minimum API required
android.minapi = 24

# (int) Android SDK directory
#android.sdk_path = 

# (str) Android NDK directory
#android.ndk_path = 

# (int) Android NDK API
android.ndk_api = 24

# (bool) Use --private data storage (True) or not (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path = 

# (str) Android entry point, default will be ok for most purposes
#android.entrypoint = org.renpy.android.PythonActivity

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not want packaged in your apk!
android.add_jars = 

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
android.add_java_dir = 

# (list) Android AAR archives to add
#android.add_aar = 

# (list) Gradle dependencies to add
android.gradle_dependencies = 

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains 'androidx'
android.enable_androidx = True

# (list) add java compile options - java_options are for javac
#java_options = -source 1.8 -target 1.8

# (list) Java classes to add as activities
#android.add_activites = com.example.ExampleActivity

# (str) OUYA Console category. Can be one of: GAME, APP, or NONE
#ouya.category = GAME

# (str) OUYA icon
#ouya.icon.filename = 

# (str) Compatibility for Android <5
#android.hide_titlebar = 0

# (list) Copy these files to src/main/res/xml/ (used for example with
# the bootstrap)
#android.res_xml = RES_FILE1:RES_FILE2

# (str) Android logcat filter
android.logcat_filters = *:S python:D

# (str) Copy these files to .buildozer/android/app/src/main/assets
#android.assets = 

# (str) Copy these files to .buildozer/android/app/src/main/res
#android.resources = 

# (str) Supported architecture
android.arch = arm64-v8a

# (str) Application icon
#icon.filename = 

# (str) Application icon (for Windows platform)
#icon.filename = 

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage
#build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
#bin_dir = ./bin

[app:android]
# (bool) Copy APK to the "android" directory
#android.copy_and_remove_apk = True

[app:kivy]
# (str) Log level for Kivy
#kivy.log_level = DEBUG

[app:kivysettings]
# (list) Primary dependencies for Kivy
#kivy.deps = 

# (list) Secondary dependencies for Kivy
#kivy.install_internals = 

# (list) Additional libraries to include
#android.library = 

[app:android.permissions]
# (list) Android permissions
#android.permissions = CAMERA,INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE