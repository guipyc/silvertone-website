import pyrebase

config = {"apiKey": "AIzaSyDKRTugV9mU0QJHrEhAT_yBYU6HcrASlxg",
  "authDomain": "silvertone-batch1011.firebaseapp.com",
  "projectId": "silvertone-batch1011",
  "storageBucket": "silvertone-batch1011.appspot.com",
  "messagingSenderId": "909112813098",
  "appId": "1:909112813098:web:21b613c427ae95667a4553",
  "measurementId": "G-RZHFZL7BRF"}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
#path_on_cloud =
#path_local =
