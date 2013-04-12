# -*- coding: utf-8 -*-

import os
import urllib
import urllib2

from flask import Flask, Response, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/speak")
def speak():
    audio = _text2speech(request.args.get("text"), "pt")
    return (audio, 200, {
        "Content-Type": "audio/mp3",
        "Content-Disposition": "attachment"
        })

def _text2speech(text, language="en"):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
    query_string = urllib.urlencode({"tl": language, "q": text.encode("utf-8")})
    request = urllib2.Request("http://translate.google.com/translate_tts?%s" % query_string, headers=headers)

    f = urllib2.urlopen(request)
    data = f.read()
    f.close()

    return data
