# EESTECH CHALLENGE 2022 - ZMANJŠAJMO IZGUBO PITNE VODE S STROJNIM UČENJEM

### 1. KDO SMO?

Ekipo Hallulu predstavljamo študentje tretjega letnika dodiplomskega študija FRI - Haris Kupinić, Luka Brodnik in Luka Markićević. Skupne interese smo se odločili še dodatno nadgraditi in smo se kot navdušenci za ML prijavili na EESTech Challenge 2022.

### 2. IZZIVI

Izbira izziva, s katerim smo se spopadli ni bila najlažja, vendarle je na koncu premagala odločitev za izziv podjetja Medius - ZMANJŠAJMO IZGUBO PITNE VODE S STROJNIM UČENJEM.

### 3. PRISTOP

#### FAZA I

V prvi fazi so se stvari nekoliko zataknile, saj smo že v štartu imeli napačen pristop. Začeli smo z ugotavljanjem outlierjev, ki bi nam pomagali odkriti potencialno izgubo vodo. Po več urnem matranju, smo ugotovili, da pristop ni OK, saj nikjer ne govorimo o odstopanj od normalnih vrednosti. Potem smo začeli tudi z nekoliko enostavnejšimi pristopi - izbira thresholda, ki bi določal ali se izguba zgodila ali ne. Opazovali smo tudi korelacijo med featurji, poskušali z izrisovanjem gruč, vendarle brezuspešno. Končen poskus je bil pretvorba unsupervised learninga v supervised learning z uporabo ročno označenih vrednosti.

#### FAZA II

Faza dva nam je že od začetka bila enostavnejša, saj smo poznali kar nekaj pristopov, ki so se nam zdeli ustrezni. S probavanjem različnih modelov, smo ugotovili, da bi RandomForest bil najboljša izbira. Na koncu smo tudi dobili soliden model, a žal zaradi časovnih omejitev, nam rešitev ni uspelo izpopolniti.

#### 4. KONČEN VTIS

Kljub temu, da na koncu nismo predstavili naše dejansko znanje, saj menimo, da vemo veliko več, bi izpostavili, da je izkušnja, ki smo jo pridobili tukaj zelo koristna in se že vnaprej veselimo ponovnega sodelovanja.