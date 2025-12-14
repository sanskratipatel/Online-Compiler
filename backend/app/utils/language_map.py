LANGUAGES = {
    "python": {
        "image": "python:3.12",
        "file": "main.py",
        "command": ["python", "main.py"]
    },
    "c": {
        "image": "gcc:latest",
        "file": "main.c",
        "command": ["bash", "-c", "gcc main.c -o main && ./main"]
    },
    "cpp": {
        "image": "gcc:latest",
        "file": "main.cpp",
        "command": ["bash", "-c", "g++ main.cpp -o main && ./main"]
    },
    "java": {
        "image": "openjdk:17",
        "file": "Main.java",
        "command": ["bash", "-c", "javac Main.java && java Main"]
    },
    "javascript": {
        "image": "node:20",
        "file": "main.js",
        "command": ["node", "main.js"]
    },
    "go": {
        "image": "golang:1.22",
        "file": "main.go",
        "command": ["go", "run", "main.go"]
    }
}
