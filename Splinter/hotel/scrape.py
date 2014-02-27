from splinter import Browser
import json

class Comentario(object):


    
    def varrer(self):
        with Browser() as browser: 
            
            url = "http://www.tripadvisor.com.br/Hotel_Review-g303428-d1757286-Reviews-Hardman_Praia_Hotel-Joao_Pessoa_State_of_Paraiba.html" 
            browser.visit(url) 
            autores = browser.find_by_xpath('//*[@class="memberOverlayLink"]/div[2]/span')
             
            aut = []
            for a in autores:
                au = a.text.strip()
                aut.append(au)
                 
            more = browser.find_by_xpath('//*[@class="reviewSelector "]/div/div[2]/div/div/div[3]/p/span/span')
                                            
            for m in more:
                if m.text == "Mais":
                    m.click()
             
            
            descricoes = browser.find_by_xpath('//div[@class="col2of2"]/div')
            k = 0
            descri = []
            for m in descricoes:
                m = m.find_by_xpath('..//div[@class="entry"]/p')
                descricao = m.html.replace("<br>","\n")
                if not descri.count(descricao) == 0:
                    continue
                if not descricao.count('<span class="partnerRvw">') == 0:
                    continue
                descri.append(descricao)
                k +=1
            
            
            listaDeComentarios = []
            
            cont = 0
            while cont < descri.__len__():
                listaDeComentarios.append({'autor': aut[cont], 'descricao' : descri[cont]})
                cont += 1
            
            jsonString = json.JSONEncoder().encode(listaDeComentarios)  
            jsonArquivo = open('Comentarios.json', "w")
            jsonArquivo.write(jsonString)
            jsonArquivo.close()
            print jsonString
            
        