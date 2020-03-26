  
from jinja2 import Template
def getHTML():
    with open('images.html') as f:
        s = f.read()
    return s
def main():
    image_list = [
        {"https://www.sciencenews.org/wp-content/uploads/2019/10/100819_JL_groundwater_feat-1028x579.jpg"},
        {"https://cff2.earth.com/uploads/2018/01/08145353/Freshwater-streams-and-rivers-are-being-polluted-with-salt.jpg"},
        { "https://www.worldatlas.com/r/w1200-h701-c1200x701/upload/46/f3/08/waikato-river-new-zealand.jpg"}
    ]
    tmpl = Template(imagesHTML())
    
    print(tmpl.render({'images': image_list }))
main()