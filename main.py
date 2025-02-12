from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import tempfile
import subprocess
import shutil

app = FastAPI()

@app.post("/convert")
async def convert_md_to_docx(file: UploadFile = File(...)):
    # Create temporary files
    with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as md_file:
        md_path = md_file.name
        content = await file.read()
        md_file.write(content)

    docx_path = md_path.replace(".md", ".docx")

    try:
        # Run Pandoc command
        subprocess.run(["pandoc", md_path, "-o", docx_path, "--toc"], check=True)

        # Return file as response
        return FileResponse(docx_path, filename=file.filename.replace(".md", ".docx"))

    except subprocess.CalledProcessError as e:
        return {"error": f"Pandoc failed: {e}"}

    finally:
        # Cleanup temp files
        shutil.rmtree(md_path, ignore_errors=True)
        shutil.rmtree(docx_path, ignore_errors=True)
