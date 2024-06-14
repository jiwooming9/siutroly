import win32com.client as win32
import PIL.Image
from wia_scan import *
from reportlab.pdfgen import canvas
import os
import time
import shutil
import tempfile
import win32print



#----------PRINTER----------------
def intailieu(file_path, printer_name=None):
    current_file_path = os.path.abspath(__file__)
    folderpath = os.path.dirname(current_file_path)
    realpath = os.path.join(folderpath, file_path)
    delete_gen_py()
    word = win32.gencache.EnsureDispatch('Word.Application')
    word.Visible = False
    doc = word.Documents.Open(realpath)
    if printer_name:
        word.ActivePrinter = printer_name
    #Thêm Duplex option nếu in đc 2 mặt:
    # - 1 = Simplex (one-sided printing)
    # - 2 = Horizontal duplex (two-sided printing, flip on long edge)
    # - 3 = Vertical duplex (two-sided printing, flip on short edge)
    doc.PrintOut(Copies=1, PrintToFile=False, Collate=True)
    doc.Close(SaveChanges=False)
    word.Quit()

def clear_print_queue(printer_name=None):
    # Get the default printer if no printer name is provided
    if printer_name is None:
        printer_name = win32print.GetDefaultPrinter()
    
    # Open the printer
    printer_handle = win32print.OpenPrinter(printer_name)
    
    # Get the print jobs
    jobs = win32print.EnumJobs(printer_handle, 0, -1, 1)
    
    # Loop through the jobs and delete them
    for job in jobs:
        print(f"Deleting job {job['JobId']} from printer {printer_name}")
        win32print.SetJob(printer_handle, job['JobId'], 0, None, win32print.JOB_CONTROL_DELETE)
    
    # Close the printer handle
    win32print.ClosePrinter(printer_handle)
 

#----Scanner-----

def save_images_as_pdf(images, output_file):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    for image in images:
        pil_image = PIL.Image.open(image)
        pil_image.save(c, format='PDF', resolution=100)
        c.showPage()

    c.save()        
def scanVB_enhanced(tenvb):
    device = prompt_choose_device_and_connect()
    c = canvas.Canvas(tenvb + ".pdf")
    dem = 0
    while True:
        try:
            pillow_image = scan_side(device=device)
            dem +=1
        except Exception as e:  # Xử lý lỗi nếu không còn trang để quét
            print(f"Lỗi quét: {e}")
            if dem == 0:
                continue  # Thoát khỏi vòng lặp nếu có lỗi
            else:
                break

        width_inch, height_inch = 8.27, 11.69
        dpi = 72
        width_pixel, height_pixel = int(width_inch * dpi), int(height_inch * dpi)

        img_path = "temp_img.jpg"
        pillow_image.save(img_path, 'JPEG')

        c.drawImage(img_path, 0, 0, width_pixel, height_pixel)
        c.showPage()
        os.remove(img_path)

    c.save()

def save_images_as_pdf_old(images, output_file):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    for image in images:
        pil_image = PIL.Image.open(image)
        pil_image.save(c, format='PDF', resolution=100)
        c.showPage()

    c.save()        
def scanVB_old(tenvb):
    # images = scan_documents(scanner_name)
    # if images:
    #     save_images_as_pdf(images, tenvb + ".pdf")
    # else:
    #     print("No documents were scanned.")
    device = prompt_choose_device_and_connect()
    pillow_image = scan_side(device=device)
    c = canvas.Canvas(tenvb + ".pdf")
    img_path = "temp_img.jpg"
    pillow_image.save(img_path, 'JPEG')
    c.drawImage(img_path, 0, 0, 595, 842)  # A4 size at 72 DPI
    c.showPage()
    os.remove(img_path)
    c.save()
def scanlientuc(tenvb):
    dem = 0
    while dem < 40:
        try:
            scanVB_old(tenvb)
            return "Đã scan"
        except:
            dem += 1
            time.sleep(3)
    return "Không thấy tài liệu"


def delete_gen_py():
    temp_dir = tempfile.gettempdir()  # Get the path to the %TEMP% directory
    gen_py_path = os.path.join(temp_dir, "gen_py")  # Construct the path to gen_py

    if os.path.exists(gen_py_path):  # Check if gen_py exists
        try:
            shutil.rmtree(gen_py_path)  # Attempt to delete gen_py and its contents
            print("Successfully deleted 'gen_py' folder.")
        except OSError as e:
            print(f"Error deleting 'gen_py': {e}")
    else:
        print("'gen_py' folder not found.")
intailieu("CT01.docx")