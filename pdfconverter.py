import pdfcrowd
import sys
from datetime import datetime
from GrabzIt import GrabzItImageOptions, GrabzItPDFOptions
from GrabzIt import GrabzItClient




def convert_url_img(url):
    filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = 'tmp\img\{}.png'.format(filename1)
    try:
        grabzIt = GrabzItClient.GrabzItClient("YmI5YzRiY2U1NzI3NDNkMTk5OGJjNDRkNjNkNmUxNGE=","RT8/Pz8/egY/Pz8/Vz8/OD8/Cz8RRj8/Pz8/PyEOMz8=")
        options = GrabzItImageOptions.GrabzItImageOptions()
        options.format = "png"
        options.browserHeight = -1
        options.height = -1
        options.width = -1
        grabzIt.URLToImage(url, options)
        grabzIt.SaveTo(path)
    except Error as why:
        print('grabzIt Error: {}\n'.format(why))
        raise
    return path

def convert_url_pdf(url):
    filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = "tmp\pdf\{}.pdf".format(filename1)
    try:
        grabzIt = GrabzItClient.GrabzItClient("YmI5YzRiY2U1NzI3NDNkMTk5OGJjNDRkNjNkNmUxNGE=",
                                              "RT8/Pz8/egY/Pz8/Vz8/OD8/Cz8RRj8/Pz8/PyEOMz8=")

        options = GrabzItPDFOptions.GrabzItPDFOptions()
        grabzIt.URLToPDF(url, options)
        grabzIt.SaveTo(path)
        grabzIt.SaveTo(path)
    except pdfcrowd.Error as why:
        # report the error
        sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

        # rethrow or handle the exception
        raise
    return path

if __name__ == "__main__":
    filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
    test = convert_url_pdf('https://www.wikipedia.org/')
    print(test)
