from flask import *
import mlab
from mongoengine import *

mlab.connect()
app = Flask(__name__)
class Places(Document):
    name = StringField()
    description = StringField()
    image = StringField()


@app.route('/')
def index():
    return render_template('index.html', places=Places.objects())

@app.route('/admin')
def admin():
    return render_template('admin.html', places=Places.objects())

@app.route('/delete_place/<place_id>')
def delete_place(place_id):
    place = PLaces.objects().with_id(place_id)
    if place is not None:
        place.delete()
    return redirect('/admin')

if __name__ == '__main__':
    app.run(debug=True)
