words = [['Hi'], ['From'], ['Python']]

with open('mypage.html', 'w') as myFile:
        myFile.write('<!DOCTYPE html>')
        myFile.write('<html lang="en">')
        myFile.write('<head>')
        
        myFile.write('<meta charset="UTF-8">')
        myFile.write('<meta http-equiv="X-UA-Compatible" content="IE=edge">')
        myFile.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
        myFile.write('<title>Reporte de datots</title>')
        
        myFile.write('<head>')
        myFile.write('<body>')
        
        myFile.write('<h1>Hola Mundo desde python con html</h1>')
        myFile.write('<table>')
        
        # 2-depth string data to 1-depth 
        words = [word_str for inner in words for word_str in inner] 
    
        # use fstring to build string
        for word in words:
            myFile.write(f'<tr><td>{word}</td></tr>')  
        myFile.write('</table>')
        myFile.write('</body>')
        myFile.write('</html>')