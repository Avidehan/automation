from my_pages.nehutIndex_page import NehutIndexPage


class NehutIndexTest():
    def __init__(self, driver):
        self.driver = driver

    def test_simulator_nehutIndex(self):
        self.page = NehutIndexPage(self.driver)
        self.page.test_simulator_nehutIndex(committee_type="נכות כללית", main_section=2, subsection=1,
                                            description_of_the_defect="", percentage=None,
                                            from_year="2017", from_month="מרץ", until_month="ינואר", until_year="2020")
        self.page.next_button()
        return self.page.simulator_table().text

    def test_simulator_nehutIndex_negtive_insert_big_number_disability_percentage(self):
        self.page = NehutIndexPage(self.driver)
        self.page.insert_disability_percentage("110")
        return self.page.get_disability_percentage_error() == 'אחוז אינו חוקי'
