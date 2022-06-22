from selenium.webdriver.common.by import By


class HomePageLocators():
    logo = (By.CLASS_NAME, 'btl-logo')
    search_field = (By.ID, 'TopQuestions')
    search_button = (By.CLASS_NAME, 'SearchBtn')
    search_result = (By.CLASS_NAME, 'rTitle')
    # search_button = (By.XPATH, '//*[@id="results"]/h2/strong')
    braches_button = (By.CLASS_NAME, "snifim")
    payments_button = (By.CLASS_NAME, "payments")
    personal_service_button = (By.CLASS_NAME, "login")


class SimulatorsPageLocators():
    logo = (By.CLASS_NAME, 'btl-logo')

class NehutIndexPageLocators():
    logo = (By.CLASS_NAME, 'btl-logo')
    committee_type = (By.ID,'ctl00_ctl49_g_7d0bf1c8_fd19_413d_ba58_2cfa896f7e91_ctl00_ddl_nosse')
    main_section = (By.ID,'RashiInput')
    subsection = (By.ID,'txtSeif')
    description_of_the_defect = (By.ID,"Description_txt")
    disability_percentage = (By.CLASS_NAME,'checkPercent')
    disability_percentage_error = (By.XPATH,'//*[@id="ctl00_ctl49_g_7d0bf1c8_fd19_413d_ba58_2cfa896f7e91_ctl00_Percent_lbl_error"]')
    datepicker_from = (By.CSS_SELECTOR,'#ctl00_ctl49_g_7d0bf1c8_fd19_413d_ba58_2cfa896f7e91_ctl00_DynDatePicker_From_DateBtn')
    date_from_day = (By.XPATH,'//*[@id="ctl00_ctl49_g_7d0bf1c8_fd19_413d_ba58_2cfa896f7e91_ctl00_DynDatePicker_From_DateBtn_table"]/tbody/tr[4]/td[4]/div')
    date_from_month = (By.XPATH,'//*[@id="ctl00_ctl49_g_7d0bf1c8_fd19_413d_ba58_2cfa896f7e91_ctl00_DynDatePicker_From_DateBtn_root"]/div/div/div/div/div[1]/select[2]')
    date_from_year = (By.XPATH,'//select[@class ="picker__select--year"]')
    datepicker_until= (By.CSS_SELECTOR,'#ctl00_ctl49_g_7d0bf1c8_fd19_413d_ba58_2cfa896f7e91_ctl00_DynDatePicker_To_DateBtn')
    date_until_month = (By.XPATH,
                       '//*[@id="ctl00_ctl49_g_7d0bf1c8_fd19_413d_ba58_2cfa896f7e91_ctl00_DynDatePicker_To_DateBtn_root"]/div/div/div/div/div[1]/select[2]')
    date_until_year = (By.XPATH,
                      '//*[@id="ctl00_ctl49_g_7d0bf1c8_fd19_413d_ba58_2cfa896f7e91_ctl00_DynDatePicker_To_DateBtn_root"]/div/div/div/div/div[1]/select[1]')
    date_until_day = (By.XPATH,'//*[@id="ctl00_ctl49_g_7d0bf1c8_fd19_413d_ba58_2cfa896f7e91_ctl00_DynDatePicker_To_DateBtn_table"]/tbody/tr[3]/td[6]/div')
    eavesdroppin = (By.XPATH,'//*[@id="ctl00_ctl49_g_7d0bf1c8_fd19_413d_ba58_2cfa896f7e91_ctl00_selectSeif"]/div[16]/a/span')
    result_table = (By.XPATH,'//*[@id="ctl00_ctl49_g_7d0bf1c8_fd19_413d_ba58_2cfa896f7e91_ctl00_Gv_Results_ctl02_Label1"]')
    next = (By.XPATH,'//*[@id="ctl00_ctl49_g_7d0bf1c8_fd19_413d_ba58_2cfa896f7e91_ctl00_btn_calc"]')


