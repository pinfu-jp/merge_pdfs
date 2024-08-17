
from merge_pdf import merge_pdfs_in_folder, open_pdf, select_pdf_folder_and_out_file


if __name__ == "__main__":

    pdf_folder, output_pdf = select_pdf_folder_and_out_file()

    merge_pdfs_in_folder(pdf_folder, output_pdf)

    open_pdf(output_pdf)
