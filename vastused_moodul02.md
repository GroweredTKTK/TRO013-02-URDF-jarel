# Moodul 02: URDF / Xacro — Vastused

## Ülesanne 1: Mudeli analüüs

Ava fail `minu_description/urdf/yahboom_robot.urdf.xacro` ja vasta:

### 1. Mitu link'i on mudelis?

TODO: 10

### 2. Mitu joint'i? Mis tüüpi on ratta joint'id ja miks?

TODO: 9 jointi, ratta jointid on continuous tuupi et ei oleks piiramatud poored.

### 3. Mis vahe on visual ja collision geomeetrial?

TODO: visual - roboti visualiseerimine, nahtav kuju/mudel
collision - kuju mida kasutatakse kokkuporgete ja fuusika arvutamiseks

### 4. Miks on base_footprint eraldi base_link'ist?

TODO: base_footprint on roboti maapinna koordinaatsusteem, kasutatatakse rohkem navigeerimises.
base_link on roboti kere pohine koordinaatsusteem ta on uhendatud base_footprintiga aga asub ratta raadiuse vorra korgemal

---

## Ülesanne 2: Visualiseerimine ja TF puu

### 1. Millised lingid on RViz2-s näha?

TODO: - `base_footprint`
- `base_link`
- `front_left_wheel_link`
- `front_right_wheel_link`
- `rear_left_wheel_link`
- `rear_right_wheel_link`
- `laser_link`
- `camera_link`
- `camera_optical_link`
- `imu_link`

### 2. Kuidas mõjutab laser_link asukoht base_link suhtes /scan andmete tõlgendamist?

TODO: `laser_link` asukoht näitab, kust lidar mõõdab. Kui asukoht on vale, siis `/scan` andmed ja takistuste asukohad tõlgendatakse valesti.

### 3. Lisa ekraanipilt RViz2-st

TODO: /home/student8/github-classroom/Tallinna-Tehnika-korgkool/roboti-kirjeldav-mudel-GroweredTKTK/Screenshots/Screenshot 2026-05-15 115057.png

### 4. Lisa TF puu (frames.pdf)

TODO: kopeeri frames.pdf siia reposse

---

## Ülesanne 3: URDF ja Webots PROTO võrdlus

### 1. Mis on PROTO faili roll Webots simulatsioonis? Miks ei piisa ainult URDF-ist?

TODO: PROTO fail kirjeldab robotit Webots simulatsioonis. Ainult URDF-ist ei piisa, sest Webots vajab ka enda simulatsiooni infot.


### 2. Mis infot annab URDF Webots-kontekstis?

TODO: URDF annab roboti struktuuri: linkid, jointid, sensorite asukohad ja geomeetria.

### 3. Kui tahaksid muuta roboti välimust Webotsis, kas muudaksid URDF-i või PROTO-t? Miks?

TODO: Webotsis muudaksin pigem PROTO faili, sest Webots kasutab seda roboti näitamiseks. URDF-i muudaksin ROS/RViz mudeli jaoks.
