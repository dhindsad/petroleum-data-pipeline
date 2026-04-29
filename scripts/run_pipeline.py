import subprocess
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]

def run(script_name):
    script_path = BASE_DIR / "scripts" / script_name
    print(f"\n▶ Running {script_name}...")
    result = subprocess.run([sys.executable, str(script_path)])
    if result.returncode != 0:
        print(f"❌ {script_name} failed")
        sys.exit(1)
    print(f"✅ {script_name} completed")

def main():
    print("🚀 Starting Petroleum Data Pipeline...")

    run("extract.py")
    run("transform.py")
    run("validate.py")
    run("load.py")

    print("\n🎉 Pipeline completed successfully!")

if __name__ == "__main__":
    main()