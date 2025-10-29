import os
from pathlib import Path

BASE = Path(__file__).resolve().parent

for settings_path in BASE.rglob("settings.py"):
    project_dir = settings_path.parent.parent
    env_path = project_dir / ".env"

    print(f"🛠️ Fixing {settings_path}")

    # Read existing settings.py
    with open(settings_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Remove old email credentials
    new_lines = []
    for line in lines:
        if "EMAIL_HOST_USER" in line or "EMAIL_HOST_PASSWORD" in line:
            continue
        new_lines.append(line)

    # Add secure env-based email settings at the end
    new_lines.append("\n")
    new_lines.append("# Secure email settings\n")
    new_lines.append("import os\n")
    new_lines.append("from dotenv import load_dotenv\n")
    new_lines.append("from pathlib import Path\n")
    new_lines.append("BASE_DIR = Path(__file__).resolve().parent.parent\n")
    new_lines.append("load_dotenv(BASE_DIR / '.env')\n")
    new_lines.append("EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'\n")
    new_lines.append("EMAIL_HOST = 'smtp.gmail.com'\n")
    new_lines.append("EMAIL_PORT = 587\n")
    new_lines.append("EMAIL_USE_TLS = True\n")
    new_lines.append("EMAIL_HOST_USER = os.getenv('EMAIL_USER')\n")
    new_lines.append("EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASS')\n")

    # Save new settings.py
    with open(settings_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    # Create .env file (if not exists)
    if not env_path.exists():
        with open(env_path, "w", encoding="utf-8") as env:
            env.write("EMAIL_USER=\nEMAIL_PASS=\n")
        print(f"✅ Created {env_path}")

print("\n🎯 All done! Now add .env entries for each project manually.")
