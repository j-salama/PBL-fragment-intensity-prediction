import numpy

def spectral_angle(true,predicted):
    #Spectral angle calculation between intensities 
    # Für Formel siehe Malte slides aber hier aufschlüsseling über variablen 
# SA = 1-(2/pi)*arcos(u . v) / (||u|| * ||v||))
# SA = 1-(2/pi)*arcos ( dot_product / (bottom_product) )
# bottom_product = normalized_true * normalized_predicted

    dot_product = numpy.dot(true,predicted)
    bottom_product = numpy.sqrt(numpy.sum(true**2)) * numpy.sqrt(numpy.sum(predicted**2))
    arccos = numpy.arccos(dot_product/bottom_product)

    return 1-((2/numpy.pi)*arccos)

def pearson_correlation(true, predicted):
    return numpy.corrcoef(true, predicted)[0, 1]