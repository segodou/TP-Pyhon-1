from fpdf import FPDF
import requests, urllib, json
import sys
from operator import itemgetter, attrgetter
import urllib.request, urllib.error
import urllib, json
import logging
import io
from zipfile import ZipFile
from tempfile import mktemp

# On vérifie le nombre d'argument passé au programme
if len(sys.argv) !=	5:
		sys.exit("ERROR: I need	exactly	four argument.")
with open(sys.argv[4], 'w') as pyearbook:                 # Ouverture du fichier pdf pour écriture
    
    # Téléchargement du fichier zip
    filename = mktemp('.zip')
    theurl = sys.argv[2]
    name, hdrs =  urllib.request.urlretrieve(theurl, filename)
    thefile=ZipFile(filename)
    thefile.extractall("./zipFolder")
    thefile.close()
    
    # On crée un objet Fpdf
    yearbook = FPDF('L', 'mm', 'A4')                      
    class PDF(FPDF):
        # Page header                                       
        def header(self):                                 
            # Logo
            self.image('./zipFolder/logo.png', 10, 10, 25)
            # Arial bold 15
            self.set_font('Arial', 'B', 15)
            self.set_text_color(0, 0, 0)  

            self.cell(1)
            # Title
            self.cell(0, 10, 'Pokemon Yearbook - Gr.1', 1, 0, 'C')
            # Line break
            self.ln(16.5)

        # Page footer
        def footer(self):                                       
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            # Arial italic 8
            self.set_font('Arial', 'I', 8)
            self.set_text_color(0, 0, 0)  
            # Page number
            self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
     
    # Récupération des données du fichiers Json       
    url = sys.argv[1]
    response = urllib.request.urlopen(url);
    response.info().get('content-type')
    response.info().get_content_charset()
    encoding = response.info().get_content_charset('utf8')
    data1 = json.loads(response.read().decode(encoding))

    # Instantiation of inherited class
    yearbook = PDF()
    yearbook.alias_nb_pages()
    yearbook.add_page('L')
    
    # Tri des pokémons par ordre alphabétique de leur nom
    data = list(sorted(data1['pokemon'], key=itemgetter("name")))
    
    # Initialisation du log journal
    #logging.basicConfig(filename = sys.argv[3], format = '%(message)s', filemode = 'w')
    #logger = logging.getLogger()
    #logger.setLevel(logging.DEBUG)
    logFile = open(sys.argv[3], 'w',  encoding='utf-8')
    # Affiche le nombre total de pokemon
    logFile.write("We have {} pokemons.\n".format(len(data)))
    
    # Fonction pour vérifier si le lien de l'image est valide ou pas
    def checkURL(url1):
        try:
            f = urllib.request.urlopen(url1)
            yearbook.image(pokemon['img'], w=30, h=30)
            logFile.write('Treating Pokemon : {}\n'.format(pokemon['name']))
        except:
            yearbook.image('./zipFolder/placeholder.png', w=30, h=30)
            logFile.write('!!! The image file {} does not exist. It was replaced with the placeholder...!!! Treating Pokemon : {}\n'.format(pokemon['img'],pokemon['name']))

    
    # Création de la grille 4*3
    nbreCell = 0
    i = 0
    y1 = 27
    y2 = 25
    for pokemon in data[:50]:
        # remplissage ligne1, colonne1
        pokemon = data[i]
        yearbook.cell(93, 40, border=1)
        yearbook.set_xy(12, y1)
        if __name__ == '__main__':
            url1 = pokemon['img']
        checkURL(url1)
        yearbook.set_xy(0, y1)
        yearbook.set_text_color(0, 0, 0)        
        yearbook.set_font('Arial', 'B', 8)
        yearbook.cell(50.5, 4.28, 'Type:', 0, 1, 'R')
        yearbook.set_xy(41, y1+3.5)        
        yearbook.set_font('Arial', '', 8)
        yearbook.cell(42.5, 4.28, ",".join(pokemon['type']), 0, 1)  
        yearbook.set_font('Arial', 'B', 8)
        yearbook.cell(42.5, 4.28, 'Height:', 0, 1, 'R')
        yearbook.set_font('Arial', '', 8)
        yearbook.cell(41.5, 4.28, pokemon['height'], 0, 1, 'R')
        yearbook.set_font('Arial', 'B', 8)
        yearbook.cell(43, 4.28, 'Weight:', 0, 1, 'R')
        yearbook.set_font('Arial', '', 8)
        yearbook.set_xy(41, y1+20)  
        yearbook.cell(41, 4.28, pokemon['weight'], 0, 1)
        yearbook.set_font('Arial', 'B', 8)
        yearbook.cell(50.5, 4.28, 'Weaknesses:', 0, 1, 'R')
        yearbook.set_xy(41, y1+29)
        yearbook.set_font('Arial', '', 8)
        yearbook.cell(50.5, 4.28, ",".join(pokemon['weaknesses']), 0, 1)   
        yearbook.add_font('DejaVuB', '', './zipFolder/DejaVuSansCondensed-Bold.ttf', uni=True)
        yearbook.set_font('DejaVuB', '', 11)
        yearbook.set_text_color(255, 0, 0)  
        yearbook.cell(28.5, 0, 'Name:', 0, 1, 'L')
        yearbook.ln(1)
        yearbook.add_font('DejaVu', '', './zipFolder/DejaVuSansCondensed.ttf', uni=True)
        yearbook.set_font('DejaVu', '', 11)
        try:
            yearbook.cell(28.5, 5.28, txt='{:s}'.format(pokemon['name']), border=0, ln=0, align='L')
        except:
            continue
        nbreCell = nbreCell + 1
        i = i + 1
        
        # remplissage ligne1 colonne2
        pokemon = data[i]
        yearbook.set_xy(103, y2+1.5)
        yearbook.cell(93, 40, border=1)
        yearbook.set_xy(105, y1)
        if __name__ == '__main__':
            url1 = pokemon['img']
        checkURL(url1)
        yearbook.set_xy(90, y1)
        yearbook.set_text_color(0, 0, 0)        
        yearbook.set_font('Arial', 'B', 8)
        yearbook.cell(53.5, 4.28, 'Type:', 0, 1, 'R')
        yearbook.set_xy(134.5, y1+3.5)        
        yearbook.set_font('Arial', '', 8)
        yearbook.cell(146, 4.28, ",".join(pokemon['type']), 0, 1)  
        yearbook.set_font('Arial', 'B', 8)
        yearbook.cell(136.5, 4.28, 'Height:', 0, 1, 'R')
        yearbook.set_font('Arial', '', 8)
        yearbook.cell(136, 4.28, pokemon['height'], 0, 1, 'R')
        yearbook.set_font('Arial', 'B', 8)
        yearbook.cell(137, 4.28, 'Weight:', 0, 1, 'R')
        yearbook.set_font('Arial', '', 8)
        yearbook.set_xy(135, y1+20)  
        yearbook.cell(135, 4.28, pokemon['weight'], 0, 1)
        yearbook.set_font('Arial', 'B', 8)
        yearbook.cell(145, 4.28, 'Weaknesses:', 0, 1, 'R')
        yearbook.set_xy(135, y1+29)
        yearbook.set_font('Arial', '', 8)
        yearbook.cell(145, 4.28, ",".join(pokemon['weaknesses']), 0, 1)   
        yearbook.add_font('DejaVuB', '', './zipFolder/DejaVuSansCondensed-Bold.ttf', uni=True)
        yearbook.set_font('DejaVuB', '', 11)
        yearbook.set_text_color(255 , 0, 0)  
        yearbook.cell(108, 0, 'Name:', 0, 1, 'R')
        yearbook.set_xy(103.5, y1+34)
        yearbook.add_font('DejaVu', '', './zipFolder/DejaVuSansCondensed.ttf', uni=True)
        yearbook.set_font('DejaVu', '', 11)
        try:
            yearbook.cell(116, 5.28, txt='{:s}'.format(pokemon['name']), border=0, ln=0)
        except:
            continue
        nbreCell = nbreCell + 1
        i = i + 1
        
        # remplissage ligne1 colonne 3
        pokemon = data[i]
        yearbook.set_xy(196, y2+1.5)
        yearbook.cell(93, 40, border = 1)
        yearbook.set_xy(198, y1)
        if __name__ == '__main__':
            url1 = pokemon['img']
        checkURL(url1)
        yearbook.set_xy(183, y1)
        yearbook.set_text_color(0, 0, 0)        
        yearbook.set_font('Arial', 'B', 8)
        yearbook.cell(53.5, 4.28, 'Type:', 0, 1, 'R')
        yearbook.set_xy(227.5, y1+3.5)        
        yearbook.set_font('Arial', '', 8)
        yearbook.cell(239, 4.28, ",".join(pokemon['type']), 0, 1)  
        yearbook.set_font('Arial', 'B', 8)
        yearbook.cell(229.5, 4.28, 'Height:', 0, 1, 'R')
        yearbook.set_font('Arial', '', 8)
        yearbook.cell(229, 4.28, pokemon['height'], 0, 1, 'R')
        yearbook.set_font('Arial', 'B', 8)
        yearbook.cell(230, 4.28, 'Weight:', 0, 1, 'R')
        yearbook.set_font('Arial', '', 8)
        yearbook.set_xy(228, y1+20)  
        yearbook.cell(228, 4.28, pokemon['weight'], 0, 1)
        yearbook.set_font('Arial', 'B', 8)
        yearbook.cell(238, 4.28, 'Weaknesses:', 0, 1, 'R')
        yearbook.set_xy(228, y1+29)
        yearbook.set_font('Arial', '', 8)
        yearbook.cell(238, 4.28, ",".join(pokemon['weaknesses']), 0, 1)   
        yearbook.add_font('DejaVuB', '', './zipFolder/DejaVuSansCondensed-Bold.ttf', uni=True)
        yearbook.set_font('DejaVuB', '', 11)
        yearbook.set_text_color(255 , 0, 0)  
        yearbook.cell(200.5, 0, 'Name:', 0, 1, 'R')
        yearbook.set_xy(196, y1+34)
        yearbook.add_font('DejaVu', '', './zipFolder/DejaVuSansCondensed.ttf', uni=True)
        yearbook.set_font('DejaVu','',11)
        try:
            yearbook.cell(209, 5.28, txt='{:s}'.format(pokemon['name']), border=0, ln=0)
        except:
            continue
        nbreCell = nbreCell + 1
        yearbook.ln(5.5)
        
        if nbreCell <= 11:
            i = i + 1
            y1 = y1 + 40
            y2 = y2 + 40
        else:
            i = i + 1 
            nbreCell = 0
            y1 = 27
            y2 = 25
    logFile.write('All done.')   
    yearbook.output("pyearbook.pdf")
