from _sqlite3 import Cache
import json
import time

from scrapy.contrib.linkextractors.sgml import BaseSgmlLinkExtractor
from scrapy.http.request.form import FormRequest
from scrapy.selector import Selector
from scrapy.selector.lxmlsel import HtmlXPathSelector
from scrapy.spider import BaseSpider
from selenium import webdriver


class ComentariosSpider(BaseSpider):
    """Spider"""
    
    name = "hotel"
    allowed_domains = ["www.tripadvisor.com.br"]
    start_urls = ["http://www.tripadvisor.com.br/Hotel_Review-g303428-d1757286-Reviews-Hardman_Praia_Hotel-Joao_Pessoa_State_of_Paraiba.html"]
    
    deals_list_xpath = '//div[@class="reviewSelector"]'
    
    
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def parse(self, response):
        self.driver.get(response.url)
        
        
        
        link = self.driver.find_element_by_xpath('//*[@id="HSCS"]/table/tbody/tr[1]/td[1]/a')
        link.click()
        
        try:
            
            time.sleep(5)
            
            selector = Selector(response)
            
            
            autores = selector.xpath('.//div[@class="username mo"]/span/text()').extract() 
            descricoes = selector.xpath('.//div/div[@class="entry"]/p/text()').extract() 
            """
            descricoes = self.driver.find_elements_by_xpath('//*[@id="UR195186188"]/div[2]/div/div[3]/p/text()')
            autores = selector.xpath('.//div[@class="username mo"]/span/text()').extract() """
          
            
            listaDeComentarios =[]
            print autores.__len__()
            print descricoes.__len__()
            
            cont = 0;
            while cont < descricoes.__len__():
                if descricoes[cont]=="\n":
                    descricoes.remove("\n")
                    continue
                print cont
                print autores[cont]
                print descricoes[cont]
                
                listaDeComentarios.append({'autor': autores[cont], 'descricao' : descricoes[cont]})
                
                cont += 1
        
            """
            jsonString = json.JSONEncoder().encode(listaDeComentarios)  
            jsonArquivo = open('Comentarios.json', "w")
            jsonArquivo.write(jsonString)
            jsonArquivo.close()
            """
        finally:
            print "a"
            