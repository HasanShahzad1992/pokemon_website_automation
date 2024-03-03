import selenium.webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

driver_path="C:/Users/Admin/Desktop/pythonpractice/chromedriver.exe"
driver=wd.Chrome(executable_path=driver_path)
driver.get("https://www.tppcrpg.net/login.php")
wait=WebDriverWait(driver,10)

#logging into tppc
trainer_id_access_enter=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/form/p[1]/input")))
trainer_id=446494
trainer_id_access_enter.send_keys(trainer_id)
password_access=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/form/p[2]/input")))
password="hello_12"
password_access.send_keys(password)
login_button_access=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/form/p[3]/input")))
login_button_access.click()

#entering into battle arena
trainer_battle_access=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/ul/li[21]/a")))
trainer_battle_access.click()
opponent_id_access=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/form/p[3]/input[1]")))
opponent_id=446458
opponent_id_access.send_keys(opponent_id)
battle_trainer_button_access=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/form/p[3]/input[2]")))
battle_trainer_button_access.click()

while True:
    last_pokemon_health_access_div=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div[3]/div[2]/ul/li[6]/div/div")))
    last_pokemon_health_access_style=last_pokemon_health_access_div.get_attribute("style")
    last_pokemon_health=int(last_pokemon_health_access_style[7:len(last_pokemon_health_access_style)-2])
    total_pokemon=6
    while last_pokemon_health>0:
        opponent_health_access_div=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div[1]/div[2]/div[3]/fieldset/div")))
        opponent_health_access_title=opponent_health_access_div.get_attribute("title")
        opponent_health=int(opponent_health_access_title[0:len(opponent_health_access_title)-14])
        my_pokemon_health_div=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div[1]/div[1]/div[3]/fieldset/div")))
        my_pokemon_health_title=my_pokemon_health_div.get_attribute("title")
        my_pokemon_health=int(my_pokemon_health_title[0:len(my_pokemon_health_title)-14])
        if opponent_health>0:
            if my_pokemon_health>81:
                cross_chop_move_access=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div[2]/span/select")))
                cross_chop_move_tool=Select(cross_chop_move_access)
                cross_chop_move_tool.select_by_index(0)
                attack_button_access=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div[2]/span/input")))
                attack_button_access.click()
                time.sleep(3)
            elif my_pokemon_health>0 and my_pokemon_health<81:
                recover_move_access=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div[2]/span/select")))
                recover_move_tool=Select(recover_move_access)
                recover_move_tool.select_by_index(1)
                attack_button_access = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[2]/span/input")))
                attack_button_access.click()
                time.sleep(3)
            elif my_pokemon_health==0:
                total_pokemon=total_pokemon-1
                highest_level_pokemon=0
                highest_ith_position=0
                for i in range(1,7):
                    path_of_health="/html/body/div[3]/div/div/div[3]/div[1]/ul/li[" + str(i) + "]/div/div"
                    my_pokemon_small_health_access_div=wait.until(EC.presence_of_element_located((By.XPATH,path_of_health)))
                    my_pokemon_small_health_access_style=my_pokemon_small_health_access_div.get_attribute("style")
                    my_pokemon_small_health_access=int(my_pokemon_small_health_access_style[7:len(my_pokemon_small_health_access_style)-2])
                    if my_pokemon_small_health_access>0:
                        path_of_level="/html/body/div[3]/div/div/div[3]/div[1]/ul/li[" + str(i) + "]/small"
                        my_pokemon_level_access_div=wait.until(EC.presence_of_element_located((By.XPATH,path_of_level)))
                        my_pokemon_level_access=my_pokemon_level_access_div.text.strip()
                        my_pokemon_level=int(my_pokemon_level_access[3:len(my_pokemon_level_access)-1])
                        if my_pokemon_level>=highest_level_pokemon and i>highest_ith_position:
                            highest_level_pokemon=my_pokemon_level
                            highest_ith_position=i
                if total_pokemon>0:
                    pokemon_to_chosen_path="/html/body/div[3]/div/div/div[3]/div[1]/ul/li[" + str(highest_ith_position) + "]/a"
                    pokemon_to_choose=wait.until(EC.element_to_be_clickable((By.XPATH,pokemon_to_chosen_path)))
                    pokemon_to_choose.click()
                    time.sleep(3)
                elif total_pokemon==0:
                    break
        else:
            continue_button_access=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div[2]/span/input")))
            continue_button_access.click()
            time.sleep(3)
        last_pokemon_health_access_div = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[3]/div[2]/ul/li[6]/div/div")))
        last_pokemon_health_access_style = last_pokemon_health_access_div.get_attribute("style")
        last_pokemon_health = int(last_pokemon_health_access_style[7:len(last_pokemon_health_access_style) - 2])
    restart_battle_access=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div[4]/a")))
    restart_battle_access.click()
    choice=int(input("press 6 to end battle"))
    if choice==6:
        break
    else:
        continue
print('hooray')





























