from icrawler.builtin import BingImageCrawler

# Carpeta donde se guardarán las imágenes
output_dir = 'datasets/mi_dataset/images/train'

# Palabras clave para buscar peluches
palabras = ["peluche", "teddy bear", "cute plush", "stuffed toy", "plush animal"]

# Descargar 40 imágenes por palabra
for palabra in palabras:
    crawler = BingImageCrawler(storage={'root_dir': output_dir + '/' + palabra.replace(' ', '_')})
    crawler.crawl(keyword=palabra, max_num=40)