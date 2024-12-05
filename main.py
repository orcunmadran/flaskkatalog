import os

from flask import Flask, send_file, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/katalog")
def katalog():
    
    tree = ET.parse('katalog.xml')
    root = tree.getroot()

    catalog = []
    for cd in root.findall('CD'):
        cd_dict = {}
        for child in cd:
            cd_dict[child.tag] = child.text
        catalog.append(cd_dict)

    return render_template("katalog.html", data=catalog)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
