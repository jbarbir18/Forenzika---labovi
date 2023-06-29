import os, sys, optparse
from exif import Image
import webbrowser
from pypdf import PdfReader, PdfWriter

def convertGPScoordinate(coordinate, coordinate_ref):
    decimal_degrees = coordinate[0] + \
                      coordinate[1] / 60 + \
                      coordinate[2] / 3600
    
    if coordinate_ref == "S" or coordinate_ref == "W":
        decimal_degrees = -decimal_degrees
    
    return decimal_degrees

def figMetaData(file_path):
    img_doc = Image(open(file_path, "rb"))

    if not img_doc.has_exif:
        sys.exit(f"Image does not contain EXIF data.")
    else:
        print(f"Image contains EXIF (version {img_doc.exif_version}) data.")
        latitude=convertGPScoordinate(img_doc.gps_latitude,img_doc.gps_latitude_ref)
        longitude=convertGPScoordinate(img_doc.gps_longitude,img_doc.gps_longitude_ref)
        webbrowser.open_new_tab(f"http://www.google.com/maps/place/{latitude},{longitude}")
        print(img_doc.gps_timestamp)
        
    print(f"{dir(img_doc)}\n")


def pdfMetaData(file_path):
    pdf_doc = PdfReader(open(path, "rb"))
    if pdf_doc.is_encrypted:
        pdf_doc.decrypt("banana")

    pdfWriter = PdfWriter()
    for pageNum in pdf_doc.pages:
        pdfWriter.add_page(pageNum)
    with open('decrypted_output.pdf', 'wb') as f:
        pdfWriter.write(f)


if __name__ == "__main__":
    
    
    parser = optparse.OptionParser("Usage: python skriptalab4.py -f hotel.jpeg")
    parser.add_option("-f", dest="file", type="string", help="Enter Path")

    (options, args) = parser.parse_args()

    path = options.file
    if not path:
        print("Enter Path")
        sys.exit(parser.usage)

    if any(path.endswith(ext) for ext in (".jpg", ".bmp", ".jpeg",)):
        figMetaData(path)
    elif path.endswith(".pdf"):
        pdfMetaData(path)
    else:
        print("Error - unsupported extension")