"""Test: kontrolli kas URDF-ile on lisatud uus link (sonar, bumper vms)."""
import re
import sys

URDF_PATH = "minu_description/urdf/yahboom_robot.urdf.xacro"

# Algsed lingid, mis on juba template-s olemas
ORIGINAL_LINKS = {
    "base_footprint", "base_link",
    "laser_link", "camera_link", "camera_optical_link", "imu_link",
}

with open(URDF_PATH) as f:
    content = f.read()

# Leia koik link nimed (ka makro-pohjased ${name}_link jatame vahele)
links = re.findall(r'<link\s+name="([^"$]+)"', content)

new_links = [l for l in links if l not in ORIGINAL_LINKS and "wheel" not in l]

if not new_links:
    print("FAIL: Uusi linke ei leitud!")
    print(f"  Olemasolevad lingid: {links}")
    print("  Vihje: lisa URDF-i uus link (nt sonar_link) ja ühenda see jointiga base_link külge.")
    sys.exit(1)

# Kontrolli kas uuel lingil on ka joint
for nl in new_links:
    if f'<child link="{nl}"' not in content:
        print(f"FAIL: Link '{nl}' on olemas, aga sellele ei leitud jointigit (<child link=\"{nl}\">).")
        print("  Vihje: lisa joint, mis ühendab uue lingi base_link-iga.")
        sys.exit(1)

# Kontrolli kas uuel lingil on visuaal
for nl in new_links:
    # Leia lingi sisu
    pattern = rf'<link\s+name="{re.escape(nl)}"[^>]*>.*?</link>'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        link_content = match.group()
        if "<visual>" not in link_content:
            print(f"HOIATUS: Link '{nl}' ei sisalda <visual> elementi (robot ei ole nähtav RViz2-s).")

print(f"OK: Uued lingid leitud: {new_links}")
sys.exit(0)
