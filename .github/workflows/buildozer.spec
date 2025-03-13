[app]
title = MyApp
package.name = com.example.myapp
version = 1.0
orientation = portrait
fullscreen = False
icon.filename = %(source.dir)s/resources/icon.png
log_level = 2
osx.python_version = 3.8
ios.python_version = 3.8
add_jars = netty-all-4.1.65.Final.jar
android.arch = armeabi-v7a
android.api = 31
android.minapi = 21
requirements = kivymd, requests, python3, hostpython3
android.permissions = INTERNET
android.gradle_dependencies = 'com.android.support:appcompat-v7:26.+,com.android.support:support-compat:28.+'
