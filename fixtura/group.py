from model.group import Group

class GroupHelper:
    def __init__(self,app):
        self.app=app

    def open_groups_page(self):
        wb = self.app.wb
        if not (wb.current_url.endswith("/group.php") and len(wb.find_elements_by_name("new")) > 0):
            wb.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("group page").click()

    def create(self, group):
        wb = self.app.wb
        self.open_groups_page()
        # init group creations
        wb.find_element_by_name("new").click()
        self.fill_group_form(group)
        #submit group creation
        wb.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wb = self.app.wb
        self.open_groups_page()
        # select first group
        wb.find_element_by_name("selected[]").click()
        # submit deletion
        wb.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def modify(self, new_data):
        wb = self.app.wb
        self.open_groups_page()
        # select first group
        wb.find_element_by_name("selected[]").click()
        # submit editing
        wb.find_element_by_name("edit").click()
        self.fill_group_form(new_data)
        # submit update
        wb.find_element_by_name("update").click()
        self.return_to_groups_page()


    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wb = self.app.wb
        if text is not None:
            wb.find_element_by_name(field_name).click()
            wb.find_element_by_name(field_name).clear()
            wb.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wb = self.app.wb
        self.open_groups_page()
        return len(wb.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wb = self.app.wb
        self.open_groups_page()
        list_gpoups=[]
        for element in wb.find_elements_by_css_selector("span.group"):
            text=element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            list_gpoups.append(Group(name=text, id=id))
        return list_gpoups



