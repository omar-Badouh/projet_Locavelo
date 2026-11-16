import os
import time
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
# Ouverture de la page locale index.html
chemin_page = "file://" + os.path.abspath("projet_Locavelo/index.html")
chrome_options .add_argument("--headless=new")
chrome_options .add_argument("--no-sandbox")
chrome_options .add_argument("--disable-dev-shm-usage")
driver =webdriver.Chrome(options=chrome_options)

# Date de demain au format AAAA-MM-JJ (ex: 2026-11-15)
date_demain = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

print("=== EXÉCUTION DES CAS DE TEST AUTOMATISÉS LOCAVÉLO ===\n")

try:
    # ---------------------------------------------------------
    # TC-01 : Nom à la limite basse (2 caractères : "Al"), 1 jour
    # Données exactes du cahier de recette (ligne TC-01)
    # ---------------------------------------------------------
    driver.get(chemin_page)
    driver.find_element(By.ID, "nom").send_keys("Al")
    driver.find_element(By.ID, "email").send_keys("jean.dupont@exemple.fr")
    Select(driver.find_element(By.ID, "velo")).select_by_value("ville")
    driver.find_element(By.ID, "debut").send_keys(date_demain)

    champ_jours = driver.find_element(By.ID, "jours")
    champ_jours.clear()
    champ_jours.send_keys("1")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    prix_tc01 = driver.find_element(By.ID, "r-total").text
    assert prix_tc01 == "12,00 €", f"Attendu '12,00 €', obtenu '{prix_tc01}'"
    print("[SUCCÈS] TC-01 : Nom 'Al' (2 car.), 1 jour -> Réservation confirmée (12,00 €).")

    # ---------------------------------------------------------
    # TC-02 : Nom en dessous de la limite (1 caractère : "A"), 1 jour
    # Données exactes du cahier de recette (ligne TC-02)
    # ---------------------------------------------------------
    driver.get(chemin_page)
    driver.find_element(By.ID, "nom").send_keys("A")
    driver.find_element(By.ID, "email").send_keys("jean.dupont@exemple.fr")
    Select(driver.find_element(By.ID, "velo")).select_by_value("ville")
    driver.find_element(By.ID, "debut").send_keys(date_demain)

    champ_jours = driver.find_element(By.ID, "jours")
    champ_jours.clear()
    champ_jours.send_keys("1")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    erreur_nom = driver.find_element(By.ID, "e-nom").text
    assert "Le nom doit contenir entre 2 et 40 caractères." in erreur_nom
    print(f"[SUCCÈS] TC-02 : Nom 'A' (1 car.) bloqué -> '{erreur_nom}'")

    # ---------------------------------------------------------
    # TC-07 : E-mail valide ("jean.dupont@exemple.fr"), Nom "Jean Dupont", 1 jour
    # Données exactes du cahier de recette (ligne TC-07)
    # ---------------------------------------------------------
    driver.get(chemin_page)
    driver.find_element(By.ID, "nom").send_keys("Jean Dupont")
    driver.find_element(By.ID, "email").send_keys("jean.dupont@exemple.fr")
    Select(driver.find_element(By.ID, "velo")).select_by_value("ville")
    driver.find_element(By.ID, "debut").send_keys(date_demain)

    champ_jours = driver.find_element(By.ID, "jours")
    champ_jours.clear()
    champ_jours.send_keys("1")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    prix_tc07 = driver.find_element(By.ID, "r-total").text
    assert prix_tc07 == "12,00 €", f"Attendu '12,00 €', obtenu '{prix_tc07}'"
    print("[SUCCÈS] TC-07 : E-mail valide -> Réservation confirmée (12,00 €).")

    # ---------------------------------------------------------
    # TC-26 (Bug LOC-3) : Remise de 10 % dès 7 jours de location
    # Données exactes du cahier de recette (ligne TC-26)
    # ---------------------------------------------------------
    driver.get(chemin_page)
    driver.find_element(By.ID, "nom").send_keys("Jean Dupont")
    driver.find_element(By.ID, "email").send_keys("jean.dupont@exemple.fr")
    Select(driver.find_element(By.ID, "velo")).select_by_value("ville")
    driver.find_element(By.ID, "debut").send_keys(date_demain)

    champ_jours = driver.find_element(By.ID, "jours")
    champ_jours.clear()
    champ_jours.send_keys("7")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)

    prix_tc26 = driver.find_element(By.ID, "r-total").text
    if prix_tc26 == "75,60 €":
        print("[SUCCÈS] TC-26 : Remise de 10 % appliquée (75,60 €).")
    else:
        print(f"[ÉCHEC - BUG LOC-3] TC-26 : Attendu '75,60 €', obtenu '{prix_tc26}'.")

finally:
    time.sleep(2)
    driver.quit()
    print("\n=== FIN DE LA CAMPAGNE AUTOMATISÉE ===")
    
