import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog


def merge_pdfs_in_folder(folder_path, output_path):
    # フォルダ内のファイルを取得し、名前順にソート
    pdf_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.pdf')])

    # PDFファイルのリストを表示（デバッグ用）
    print(f"統合するPDFファイル: {pdf_files}")

    # PDFを結合するためのPdfMergerオブジェクトを作成
    merger = PyPDF2.PdfMerger()

    # フォルダ内のPDFを結合
    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        with open(pdf_path, 'rb') as file:
            merger.append(file)
    
    # 結合したPDFを新しいファイルとして保存
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

    print("PDFファイルが正常に統合されました！")



# tkinterを使ってユーザーにフォルダとファイルパスを選択させる
def select_pdf_folder_and_out_file():
    # GUIウィンドウを隠す
    root = tk.Tk()
    root.withdraw()

    # フォルダを選択させる
    folder_path = filedialog.askdirectory(title="PDFが保存されているフォルダを選択してください")

    if not folder_path:
        print("フォルダが選択されませんでした。")
        return

    # 保存先のファイルを選択させる
    output_path = filedialog.asksaveasfilename(
        title="結合後のPDFファイルの保存場所を指定してください",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not output_path:
        print("保存先のファイルが選択されませんでした。")
        return

    return (folder_path, output_path)


def open_pdf(file_path):
    # Windowsの場合、デフォルトのPDFビューアで開く
    if os.name == 'nt':
        os.startfile(file_path)
    else:
        # 他のOS（LinuxやmacOS）の場合は subprocess を使用
        try:
            subprocess.run(['open', file_path])  # macOS
        except FileNotFoundError:
            subprocess.run(['xdg-open', file_path])  # Linux
