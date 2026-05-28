# Moodul 02: Roboti kirjeldav mudel (URDF / Xacro)

> **Järeleaitamine** — see repo on mõeldud tudengitele, kes teevad ülesande hiljem.
> Täpsem õppematerjal on Moodle'is: **Moodul 02: Roboti kirjeldav mudel**.

---

## Samm 1 — Forki see repo

1. Mine selle repo lehele GitHubis
2. Kliki paremal ülal nuppu **Fork**
3. Vali oma GitHub konto
4. Kliki **Create fork**

Sinu isiklik koopia tekib:
```
https://github.com/SINU-KASUTAJANIMI/TRO013-02-URDF-jarel
```

---

## Samm 2 — Klooni konteinerisse

Ava noVNC terminal (`http://SERVER_IP:33000+N`) ja käivita:

```bash
cd /workspace/ros2_ws/src
git clone https://github.com/SINU-KASUTAJANIMI/TRO013-02-URDF-jarel.git
cd TRO013-02-URDF-jarel
```

> Asenda `SINU-KASUTAJANIMI` oma GitHubi kasutajanimega.

---

## Samm 3 — Tee ülesanne

**Kopeeri yahboom_description oma töökausta:**
```bash
cp -r /opt/mobros_ws/src/yahboom_description /workspace/ros2_ws/src/TRO013-02-URDF-jarel/minu_description
```

**Muuda paketi nimi** `package.xml` ja `CMakeLists.txt` failides:
```
yahboom_description  →  minu_description
```

**Lisa uus andur** (nt ultraheli `sonar_link`) URDF faili lõppu, enne `</robot>` tagi.

**Ehita ja testi:**
```bash
cd /workspace/ros2_ws
colcon build --packages-select minu_description
source install/setup.bash
ros2 launch minu_description display.launch.py
```

**Loo vastuste fail** `vastused_moodul02.md` oma repo juurkausta — vasta Moodle materjalis olevatele küsimustele (vähemalt 100 tähemärki).

---

## Samm 4 — Commit ja push

```bash
cd /workspace/ros2_ws/src/TRO013-02-URDF-jarel
git add .
git commit -m "Moodul 02: minu_description + sonar_link + vastused"
git push
```

> Git küsib parool — kasuta GitHubi **Personal Access Token**:
> GitHub → Settings → Developer settings → Personal access tokens → Generate new token (scopes: `repo`)

---

## Samm 5 — Vaata hindamistulemusi

Pärast push-i käivitub automaatne hindamine (~1-2 min).

**Vaata tulemusi:** oma repo → **Actions** → viimane töö

Hindamine kontrollib:
| Test | Punktid |
|------|---------|
| `minu_description` pakett eksisteerib (package.xml, CMakeLists.txt) | 15 p |
| URDF on korrektne XML | 10 p |
| Sisaldab `base_link`, `base_footprint`, `laser_link`, `camera_link` | 10 p |
| Uus andur lisatud (`sonar_link` vms) | 20 p |
| Launch fail viitab `minu_description` paketile | 5 p |
| `vastused_moodul02.md` olemas ja täidetud | 20 p |

---

## Repo struktuur pärast ülesande tegemist

```
TRO013-02-URDF-jarel/
├── minu_description/
│   ├── urdf/
│   │   └── yahboom_robot.urdf.xacro   ← muudetud (sonar_link lisatud)
│   ├── meshes/
│   ├── launch/
│   │   └── display.launch.py
│   ├── package.xml
│   └── CMakeLists.txt
├── vastused_moodul02.md               ← sinu vastused
└── .github/                           ← hindamine (ära muuda)
```
