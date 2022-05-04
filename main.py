  a      Atsuho c bon mnt?                                              

smmmmmmFAIT PAR ADONIS.PY
hsydyhhhhydysdmdsyhhys+/::-.`  -yhshd+``/o/-`                                                                

`+yddddyshyhysoyyhhsdmdso`           `ohmdhhy`` .+s++/`                 

    `.......`  -ydysdmdys`           `/hdyhhs       -+oo+`              

               `ddhhdmmmd:             /syy+`          ./yy/`           

                ommmmmmmmh`                               .+ho.         

                .dmmmmmmmms                                 `/ys.       

                 /mmmmmmmmms`                                 `/yo`     

                  ommmmmmmmmhyyyhhhhyyysssoo+/::-.`             `oh:    

                  `ommmmmmmmmmmy-...........-::/+ooso+:-`         :h+   

                    /dmmmmmmmmmdho/:----:://++++++++++syys/-`      -ho                                                                                          

                     -mmmmmmmmmmmmmmmmmds+/:------:://++oyhhho:.    -ho 

                    `+mmmmmmmmmmmmmmmmm/                  `.-/sss/.` -d:

                   -smmmmmmmmmmmmmmmmmms`                      `./ss++ds

                 `+dmmmmmmmmmmmmmmmmmmmmh:`                        .:/:`

                `ymmmmmmmmmmmmmmmmmmmmmmmmy:`                           

                `oddmmmmmmmmmmmmmmmmmmmmmmmmy                           

                   -/oydmdmmmmmmmmmmmmmmhyo/.                           

                         ..-::::::::-..                [PLAGUE LOGO]                                                                         

"""[1:]



print(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter(graphics)))

sleep(5)

driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[8]/button').click()

sleep(3)

driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/form/div/div/div[6]').click()

sleep(1)

driver.find_element_by_xpath('/html/body/div/div/div[5]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div/form/div/div/div[3]/div/input').send_keys("lasqurro@gmail.com")

driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div/form/div/div/div[4]/div/input').send_keys('Adonis.nuclear.22')

driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div/form/div/div/div[7]/button').click()

print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter('Vous devez faires le captcha en - de 10s !')))

sleep(10)

chrome_options.headless = True

input(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter('Veuillez pressez "Entrée" quand vous aurez remplis le captcha !')))



sleep(2)







menu = """

Bienvenue sur le premier bot de Trigo !!!

Commands :

[1] Faire rejoindre le bot               [3] Poster dans le "Fil d'actualités" [BETA]              [5] Poll    

[2] Faire un poste dans un groupe        [4] Envoyez un message a un utilisateur                   [6] Paramètre du serveur

Choisissez un nombre(s) :

"""

Anime.Fade(Center.XCenter(banner), Colors.green_to_cyan, Colorate.Vertical, enter=True)



def main():

    os.system('cls')

    print("\n"*5)

    input(n)

    restart = input(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(menu)))

n = input(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(menu)))



if n == '1':

    link = input(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter("Mettez votre lien de groupe ->")))

    driver.get(link)

    sleep(5)

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[3]/div/button').click()

    input(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter('Pressez "Entrée" pour continuer')))

    input(n)

# /html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[3]/div/button





if n == '2':

    os.system('cls') 

    link1 = input(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter("Mettez votre lien de groupe ->")))            #/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/section/div/div/ul/li[1]/div/div/div[1]/span

    driver.get(link1)

    sleep(7)

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/section/div/div/ul/li[1]/div/div/div[1]/button').click()

    text = input(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter("Mettez votre texte ->")))

    sleep(2)

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/section/div/div/ul/li[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div').send_keys(text)

    sleep(2)

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/section/div/div/ul/li[1]/div/div[2]/div/div[2]/div/div[3]/div[2]/button[2]').click()

    input(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter('Pressez "Entrée" pour continuer')))

    input(n)



if n == '3':

    os.system('cls')

    driver.get('https://www.trigo-app.com/')

    sleep(7)

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/button').click()

    text1 = input(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter("Mettez votre titre ->")))

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/textarea').send_keys(text1)

    print(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter('FINIT')))

    text2 = input(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter("Mettez votre texte ->")))

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div[1]/div/div[1]').send_keys(text2)

    input('Pressez "Entrée" Pour continuer ')

    input(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter('Pressez "Entrée" pour continuer')))

    input(n)



if n == '4':

    os.system('cls')

    link2 = input(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter("Mettez le lien du compte a qui vous voulez envoyez un message ->"))) 

    driver.get(link2)

    sleep(7)

    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/button').click()

    sleep(2)

    text3 = input(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter("Mettez votre texte ->")))

    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/textarea').send_keys(text3)

    print(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter("Message bien envoyée !")))

    input(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter('Pressez "Entrée" pour continuer')))

    input(n)



if n == '5':

    os.system('cls')

    link3 = input(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter("Mettez votre lien de groupe ->")))            #/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/section/div/div/ul/li[1]/div/div/div[1]/span

    driver.get(link3)

    sleep(7)

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/section/div/div/ul/li[1]/div/div/div[1]/span').click()

    sleep(2)

    driver.find_element_by_xpath('//*[@id="prefix_z889oa7uo"]/ul/li[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div/div/div[7]/button').click()

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/section/div/div/ul/li[1]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]').click()

    text4 = input(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter("Posez la questions de votre sondage ->")))

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/section/div/div/ul/li[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div/div/figure/div/div[1]/div[2]/div/textarea').send_keys(text4)

    text5 = input(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter("Ecrivez la premiere réponse possible a votre sondage ->")))

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/section/div/div/ul/li[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div/div/figure/div/div[1]/ul/li[1]/div/div/div/textarea').send_keys(text5)

    text5 = input(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter("Ecrivez la deuxieme réponse possible a votre sondage ->")))

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/section/div/div/ul/li[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div/div/figure/div/div[1]/ul/li[2]/div/div/div/textarea').send_keys(text5)

    driver.find_element_by_xpath('/html/body/div/div/div[3]/div/main/div/div/div[2]/div/div/div/div[1]/div/div/div/div/section/div/div/ul/li[1]/div/div[2]/div/div[2]/div/div[3]/div[2]/button[2]').click()

    print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter('Votre sondage a bien été envoyé !')))

    input(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter('Pressez "Entrée" pour continuer')))

    input(n)







if __name__ == '__main__':

    main()
