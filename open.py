from selenium import webdriver
import time
import random
from getpass import getpass


class InstaBot():

    def __init__(self, mail, password):

        self.mail = mail
        self.password = password

        self.driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
        self.driver.get("http://www.instagram.com")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name = 'username']").send_keys(mail)
        self.driver.find_element_by_xpath("//input[@name ='password']").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type = 'submit']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),'Nie teraz')]").click()
        time.sleep(1)

    def unfollowers(self):
        self.driver.find_element_by_xpath(f"//a[contains(@href,'/{self.mail}')]").click()
        time.sleep(2)
        # print(following)
        follow_number = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").get_attribute('title')
        follow_number_int = int(follow_number)
        print(follow_number_int)
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]").click()
        followers = self.name(follow_number_int)
        print(followers)
        following_number = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text
        print(following_number)
        following_number_int = int(following_number)
        print(following_number_int)
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]").click()
        following = self.name(following_number_int)
        unfollow = [x for x in following if x not in followers]
        print(unfollow)
        time.sleep(5)

    def name(self, num):
        time.sleep(2)
        try:
            sugs = self.driver.find_element_by_xpath("//h4[contains(text(), 'Propozycje dla Ciebie')]")
            self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
            time.sleep(2)
        except:
            print("NO sug")

        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = self.driver.execute_script("""
                                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                return arguments[0].scrollHeight;
                                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        print(len(links))
        names = []
        i = 0
        for name in links:
            if name.text != '' and i < num:
                names.append(name.text)
                i += 1
            if i == num:
                break

        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names

    def like(self, number=5, hashtag="coding"):
        self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        time.sleep(2)
        i = 0
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a").click()
        time.sleep(5)

        while i < number:
            self.driver.find_element_by_xpath\
                ("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()  # lajk
            button_follow = self.driver.find_element_by_xpath\
                        ("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
            if button_follow.text == "Obserwuj":
                if random.randint(0, 2) == 1 or 2:
                    button_follow.click()  # obserwoanie
            if i+1 == number:  # przerwanie pwtli po i lajkach
                break
            x = random.randint(1, 4)
            for z in range(x):  # następne zdjecie
                time.sleep(random.randint(1, 3))
                self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
                time.sleep(random.random()*4)

            i += 1


# passwordek = getpass()
bot = InstaBot('login', 'password')
bot.like()

