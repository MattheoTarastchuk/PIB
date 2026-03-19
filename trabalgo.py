arquivo = open("512_yolov4_5000_dados_celulas.txt")

for linha in arquivo:
    if "conf_thresh" in linha:
        print(linha)
