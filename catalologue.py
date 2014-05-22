import sys,json
import bottle
from bson import json_util
from bottle import route, run, debug, request, response, HTTPResponse, get, template, static_file
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import datetime, json

@route('/')
def staticFile():
    return static_file("index.html",root="")
    
@route('/css/bootstrap.min.css')
def loadbootstrapcss():
    return static_file("bootstrap.min.css",root="css")
    
@route('/css/starter-template.css')
def loadbootstrapcss():
    return static_file("starter-template.css",root="css")
    
@route('/js/bootstrap.min.js')
def loadbootstrapcss():
    return static_file("bootstrap.min.js",root="js")
    
@route('/js/catalogue.js')
def loadbootstrapcss():
    return static_file("catalogue.js",root="js")

@route('/insert', method='POST')
def put_incatalogue():
    client = MongoClient()
    db = client.mycatalogue
    apparels = json.loads('[{"category":"Apparel","desc":"new bottom","name":"jeans","review":"fits perfectly","imageLink":"http://img.ehowcdn.com/article-new-thumbnail/ehow/images/a04/kj/k6/make-dark-jeans-fade-800x800.jpg"},{"category":"Apparel","desc":"new top","name":"tee","review":"fits alright","imageLink":"http://hudsonautoparts.com/wp-content/uploads/2013/07/th_NIS010046.jpg"},{"category":"Apparel","desc":"new top","name":"tshirt","review":"fits alright","imageLink":"http://www.customize-tshirt.com/images/heat_transfet_print_tshirt.png"},{"category":"Apparel","desc":"new bottom","name":"trouser","review":"fits perfectly","imageLink":"http://i.ebayimg.com/t/HEAVYWEIGHT-MOLESKIN-TROUSERS-NEW-SHOOTING-WALK-OLIVE-/00/$(KGrHqIOKkIE3rv9YtI5BN+JITWqEg~~0_35.JPG"},{"category":"Apparel","desc":"new top","name":"blouse","review":"fits alright","imageLink":"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTr8TA-ie0SxQBfACbmzf8cJ2pBz3ISdxwCxyQT0miaurxkrrgB9A"},{"category":"Apparel","desc":"new top","name":"tank top","review":"fits alright","imageLink":"http://images.cdn.bigcartel.com/bigcartel/product_images/122655384/max_h-300+max_w-300/DREAMERTANK_HEATHERGREY2.jpg"},{"category":"Apparel","desc":"new bottom","name":"shorts","review":"fits perfectly","imageLink":"http://blogs.babycenter.com/wp-content/uploads/2013/06/mossimo1-300x200.jpg"},{"category":"Apparel","desc":"new top","name":"shirt","review":"fits alright","imageLink":"http://www.thereferencecouncil.com/wordpress/wp-content/uploads/2011/11/shirt.jpg"},{"category":"Apparel","desc":"new top","name":"jacket","review":"fits alright","imageLink":"http://images.motorcycleparts2u.com/xmoto-pics/xf094912-river-road-sedona-mesh-jacket.jpg"},{"category":"Apparel","desc":"new bottom","name":"skirt","review":"fits perfectly","imageLink":"http://www3.images.coolspotters.com/photos/962903/h-and-m-heart-skirt-profile.jpg"},{"category":"Apparel","desc":"new top","name":"vest","review":"fits alright","imageLink":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbSc7RPXHlj7YUEvcBhThkkj6ZkTnUV_2CNJr_UbICgiTiG078"},{"category":"Apparel","desc":"new top","name":"cardigan","review":"fits alright","imageLink":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7MsT2FUutviOqgURl_cIcwEY2RXenrgVr4xWZ7b4VwJs9PEGwUw"}]')
    itemid2 = db.items.insert(apparels)
    healthitems = json.loads('[{"category":"Health","desc":"medicine","name":"tylenol","imageLink":"http://timewellness.files.wordpress.com/2010/01/tylenol.jpg"},{"category":"Health","desc":"beauty","name":"nail polish","color":"red","imageLink":" http://wirawiri.net/wp-content/uploads/2012/10/red-nail-polish.jpg"},{"category":"Health","desc":"medicine","name":"nyquil","imageLink":"http://ecx.images-amazon.com/images/I/410V209xbtL._SX300_.jpg"},{"category":"Health","desc":"beauty","name":"shampoo","imageLink":"http://www.scform.com/wp-content/themes/lifestyle-parent/thumb.php?src=http://www.scform.com/wp-content/uploads/2012/10/34fbcpx.png&h=200&w=300&zc=1&q=100"},{"category":"Health","desc":"medicine","name":"ZzzQuil","imageLink":"http://www.minaslater.com/wp-content/uploads/2013/05/ZzzQuil-300x200.jpg"},{"category":"Health","desc":"beauty","name":"nail polish","color":"pink","imageLink":"http://www.brodiecosmetics.com.au/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/R/E/REVLON-NAIL-POLISH-285-OH-MY-MAGENTA-FULL-SIZED-BRIGHT-PINK.jpg"},{"category":"Health","desc":"medicine","name":"neosporin","imageLink":"http://i.ebayimg.com/00/s/NDI3WDY0MA==/z/QVYAAOxysstSZDdS/$(KGrHqV,!rEFJh5VGfp(BSZDdR6rE!~~60_35.JPG"},{"category":"Health","desc":"beauty","name":"conditioner","imageLink":"http://seejencut.files.wordpress.com/2011/07/pureology-platinum-shampoo-hair-conditioner-shampoo.jpg?w=490"},{"category":"Health","desc":"medicine","name":"benadryl","imageLink":"http://chachingonashoestring.com/wp-content/uploads/2014/03/Screen-Shot-2014-03-20-at-10.32.23-AM1.png"},{"category":"Health","desc":"beauty","name":"mascara","imageLink":"http://rsi.rs/wp-content/uploads/2014/01/Joko-volumen-maskara-300x200.png"}]')
    itemid2 += db.items.insert(healthitems)
    homeitems = json.loads('[{"category":"Home","desc":"decor","name":"chair","type":"lounge","imageLink":"http://famousfurniture.eu/images/T/Lounge%20Chair%20%26%20Ottoman.gif"},{"category":"Home","desc":"appliance","name":"blender","imageLink":"http://img.diytrade.com/cdimg/1061791/11379249/0/1260406518/blender_food_processor_food_mixer.jpg"},{"category":"Home","desc":"decor","name":"table","type":"Fusball","imageLink":"http://www.foosballsoccer.com/uploads/2/4/7/3/24731873/5370370_orig.jpg"},{"category":"Home","desc":"appliance","name":"oven","imageLink":"http://www.hiwtc.com/photo/products/21/06/22/62203.jpg"},{"category":"Home","desc":"decor","name":"chair","type":"patio","imageLink":"http://www.patiocover.us/wp-content/themes/Patio/images/Summer-01.jpg"},{"category":"Home","desc":"appliance","name":"microwave","imageLink":"http://labface.com/blog/wp-content/uploads/2012/07/MICROWAVE-OVEN.jpg"},{"category":"Home","desc":"decor","name":"bed","type":"queen","imageLink":"http://blog.designgallerie.com/wp-content/uploads/2009/11/Queen-Bed-with-Side-Rail-Slat-Cappuccino.jpg"},{"category":"Home","desc":"appliance","name":"fridge","imageLink":"http://i00.i.aliimg.com/photo/v0/10943592/Electroiux_Icon_Refrigerator_In_Stainless_Steel.jpg"},{"category":"Home","desc":"decor","name":"table","type":"dining","imageLink":"http://st.houzz.com/simgs/bf2103a5034432ad_4-8350/contemporary-dining-tables.jpg"},{"category":"Home","desc":"appliance","name":"TV","imageLink":"http://smartblogs.com/wp-content/uploads/2010/07/television.jpg"}]')
    itemid2 += db.items.insert(homeitems)
    if itemid2 == '':
        db.disconnect
        return HTTPResponse(status=500)
    returnbody = json.dumps({"itemId":str(itemid2)})
    db.disconnect
    return HTTPResponse(status=200, body=returnbody)
        
@route('/getAll/:category', method='GET')
def getallcatalogue(category):
    client = MongoClient()
    db = client.mycatalogue
    if(category=="All"):
        itemlist = "["
        for item in db.items.find():
            itemlist+= JSONEncoder().encode(item)+","
        itemlist = itemlist+"]"    
        print(itemlist)
    else:
        itemlist = "["
        for item in db.items.find({"category": category}):
            itemlist+= JSONEncoder().encode(item)+","
        itemlist = itemlist+"]"    
        print(itemlist)
    topicsjson = json.dumps(itemlist)
    db.disconnect
    response.content_type = 'application/json'
    return HTTPResponse(status=200, body=topicsjson)
    
@route('/search/:searchTerm', method='GET')
def search(searchTerm):
    client = MongoClient()
    db = client.mycatalogue
    itemlist = "["
    for item in db.items.find({"$or":[
    {"name": searchTerm},
    {"desc": searchTerm},
    {"category": searchTerm},
    {"color": searchTerm},
    {"review": searchTerm},
    {"type": searchTerm}
    ]}):
        itemlist+= JSONEncoder().encode(item)+","
    itemlist = itemlist+"]"    
    print(itemlist)
    topicsjson = json.dumps(itemlist)
    db.disconnect
    response.content_type = 'application/json'
    return HTTPResponse(status=200, body=topicsjson)
    
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
        
run(host='localhost', port=1234)