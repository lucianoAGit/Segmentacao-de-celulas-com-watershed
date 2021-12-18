# Segmentação de células com Watershed

  A segmentação de imagem é um processo usado para simplificar a representação de uma imagem em algo que é mais significativo e mais fácil de analisar. Para a realização da segmentação nesse projeto, o algoritmo utilizado foi o Watershed, onde qualquer imagem em tons de cinza pode ser vista como uma superfície topográfica em que a alta intensidade denota picos e colinas, enquanto a baixa intensidade denota vales. Assim, o algoritmo começa a preencher todos os vales isolados, conhecidos como mínimos locais, com água de cores diferentes, os chamados rótulos. Conforme a água sobe, dependendo dos picos próximos, a água de diferentes vales, com diferentes cores, começarão a se fundir. Para evitar isso, são construídas barreiras nos locais onde a água se funde. O processo de preencher com água e construir barreiras continua até que todos os picos estejam debaixo d'água. Então, as barreiras que foram criadas fornecem o resultado da segmentação. 
  O algoritmo gera como resultado uma máscara de segmentação. Após a obtenção da máscara, foi aplicado na máscara um threshold utilizando como valor de limiar de 0 a 255.

# Geração da imagem final
	
  Após a etapa da segmentação, para obter o resultado final da segmentação foi utilizado um operador Bitwise AND para percorrer toda a matriz de pixels da imagem original da base de dados, comparando-a com a máscara resultante do Watershed. A operação Bitwise AND compara dois valores de pixels utilizando suas representações binárias. Desse modo, é retornado um novo valor, para formar esse valor de retorno cada bit é comparado, retornando true quando ambos os bits forem iguais a 1, caso contrário retorna false. 
  
# Banco de Dados

  Para a realização deste projeto, foram utilizadas imagens do conjunto de dados “SN-AM Dataset: White Blood cancer dataset of B-ALL and MM for stain normalization”, do The Cancer Imaging Archive (TCIA). As 29 imagens foram obtidas utilizando-se um microscópio Nikon Eclipse-200 com aumento de 1000x através de câmera digital, resultando em arquivos de formato BMP (Bitmap bruto) de tamanho 2560x1920 pixels.
