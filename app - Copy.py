import os
import subprocess

# Use Linux-style paths for input and output directories
INPUT_DIR = "/data/pdf-input"
OUTPUT_DIR = "/data/pdf-output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def compress_pdf(input_path, output_path):
    """Compress a PDF using Ghostscript."""
    try:
        gs_command = [
            "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS=/ebook",  # Options: /screen, /ebook, /printer, /prepress
            "-dNOPAUSE", "-dQUIET", "-dBATCH",
            f"-sOutputFile={output_path}", input_path
        ]
        subprocess.run(gs_command, check=True)
        print(f"Compressed: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error compressing PDF {input_path}: {e}")

def batch_compress():
    # Get the list of all PDFs in the input directory, limit to 100 files
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.pdf')][:100]
    
    if not files:
        print("No PDF files to process.")
        return

    for file in files:
        input_path = os.path.join(INPUT_DIR, file)
        output_path = os.path.join(OUTPUT_DIR, f"compressed_{file}")

        # Compress and delete the original file
        compress_pdf(input_path, output_path)
        os.remove(input_path)
        print(f"Deleted original file: {input_path}")

if __name__ == "__main__":
    batch_compress()
