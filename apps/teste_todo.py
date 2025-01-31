import unittest

from playwright.sync_api import sync_playwright


class TestTodoApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.p = sync_playwright().start()
        cls.browser = cls.p.chromium.launch(headless=False, slow_mo=1000)
        cls.context = cls.browser.new_context()
        cls.context.set_default_timeout(5_000)

    def setUp(self) -> None:
        self.page = self.context.new_page()
        self.page.goto("https://vanilton.net/web-test/todos#/")

    def test_criar_todo(self) -> None:
        self.page.get_by_placeholder("What needs to be done?").click()
        self.page.get_by_placeholder("What needs to be done?").fill("Comprar leite")
        self.page.get_by_placeholder("What needs to be done?").press("Enter")

        todo_text = self.page.locator("li").filter(has_text="Comprar leite")
        self.assertTrue(todo_text.is_visible(), "O TODO 'Comprar leite' não foi criado.")

    def test_marcar_todo_como_concluido(self) -> None:
        self.page.get_by_placeholder("What needs to be done?").click()
        self.page.get_by_placeholder("What needs to be done?").fill("Estudar Playwright")
        self.page.get_by_placeholder("What needs to be done?").press("Enter")

        self.page.locator("li").filter(has_text="Estudar Playwright").get_by_role("checkbox").check()

        todo_checkbox = self.page.locator("li").filter(has_text="Estudar Playwright").get_by_role("checkbox")
        self.assertTrue(todo_checkbox.is_checked(), "O TODO 'Estudar Playwright' não foi marcado como concluído.")

    def test_limpar_todos_concluidos(self) -> None:
        self.page.get_by_placeholder("What needs to be done?").click()
        self.page.get_by_placeholder("What needs to be done?").fill("Comprar pão")
        self.page.get_by_placeholder("What needs to be done?").press("Enter")

        self.page.locator("li").filter(has_text="Comprar pão").get_by_role("checkbox").check()

        self.page.get_by_role("button", name="Clear completed").click()

        todo_text = self.page.locator("li").filter(has_text="Comprar pão")
        self.assertFalse(todo_text.is_visible(), "O TODO 'Comprar pão' não foi removido após limpar os concluídos.")

    def tearDown(self) -> None:
        self.page.close()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.context.close()
        cls.browser.close()
        cls.p.stop()


if __name__ == "__main__":
    unittest.main()
