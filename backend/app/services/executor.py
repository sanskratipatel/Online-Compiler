import subprocess
import tempfile
import os
from app.utils.language_map import LANGUAGES
from app.config import EXECUTION_TIMEOUT, MAX_MEMORY

def execute_code(language: str, code: str):
    lang = LANGUAGES.get(language)

    if not lang:
        return {"error": "Language not supported"}

    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, lang["file"])

        with open(file_path, "w") as f:
            f.write(code)

        cmd = [
            "docker", "run", "--rm",
            "--memory", MAX_MEMORY,
            "--cpus", "0.5",
            "-v", f"{temp_dir}:/code",
            "-w", "/code",
            lang["image"]
        ] + lang["command"]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=EXECUTION_TIMEOUT
            )

            return {
                "output": result.stdout.strip(),
                "error": result.stderr.strip()
            }

        except subprocess.TimeoutExpired:
            return {"error": "Execution timed out"}
