from scrapy.selector import Selector
from scrapy.spider import BaseSpider

import json


class ComentariosSpider(BaseSpider):
    """Spider"""
    
    name = "hotel"
    allowed_domains = ["www.tripadvisor.com.br"]
    start_urls = ["http://www.tripadvisor.com.br/Hotel_Review-g303428-d1757286-Reviews-Hardman_Praia_Hotel-Joao_Pessoa_State_of_Paraiba.html"]
    
    deals_list_xpath = '//div[@class="reviewSelector"]'
    
    def parse(self, response):
        selector = Selector(response)
        autores = selector.xpath('.//div[@class="username mo"]/span/text()').extract()
        descricoes = selector.xpath('.//div[@class="entry"]/p[@class="partial_entry"]/text()').extract()
        
        listaDeComentarios =[]
        
        cont = 0;
        while cont < descricoes.__len__():
            if descricoes[cont]=="\n":
                descricoes.remove("\n")
                continue
            cont += 1
            
            listaDeComentarios.append({'autor': autores[cont], 'descricao' : descricoes[cont]})
            
            cont += 1
        
        jsonString = json.JSONEncoder().encode(listaDeComentarios)  
        jsonArquivo = open('Comentarios.json', "w")
        jsonArquivo.write(jsonString)
        jsonArquivo.close()
            
            
            