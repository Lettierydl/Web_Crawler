#!/bin/sh

#  Script.sh
#  
#
#  Created by Leo on 25/02/14.
#
cd hotel/
scrapy crawl hotel
echo Arquivo Comentarios.json Criado
open Comentarios.json