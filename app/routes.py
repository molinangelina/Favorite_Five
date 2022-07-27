from app import app
from flask import render_template

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/favFive')
def favFive():
    artist = [
        {'name':'Tim Burton',
        'img': 'https://i.pinimg.com/originals/72/8b/4c/728b4c606011f842a41a4de9d8169d2b.gif', 
        'art': 'Coraline'}, 
        {'name':'Eiichiro Oda', 
        'img': 'https://data.whicdn.com/images/227548358/original.gif', 
        'art': 'One Piece'}, 
        {'name':'Junji Ito', 
        'img': 'https://cdn.shopify.com/s/files/1/1882/8385/products/raf_750x1000_075_t_101010_01c5ca27c6_800x.jpg?v=1521830381', 
        'art': 'Uzumaki'},
        {'name':'Hayao Miyazaki', 
        'img': 'https://www.icegif.com/wp-content/uploads/2022/03/icegif-237.gif', 
        'art': 'Spirited Away'},
        {'name':'Salvador Dali', 
        'img': 'https://arthive.net/res/media/img/ox800/work/f38/638647.jpg', 
        'art': 'Le Visage de la Guerre'}]

    return render_template('favFive.html', names = artist)