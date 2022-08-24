# python -m pytest -v --driver chrome --driver-path chromedriver.exe test_labirint.py


from Pages.labirint import LabirintPage
from config import Config
import time
import pytest

@pytest.mark.xfail
def test_load_page(web_browser):
    """Проверка загрузки страницы."""
    page = LabirintPage(web_browser)
    page.wait_page_loaded()
    assert page.check_js_errors()

def test_go_to_main_page(web_browser):
    """ Проверка перехода на главную страницу """
    page = LabirintPage(web_browser)
    page.sale_link.click()
    page.logo_labirirnt.click()
    assert page.get_current_url() == Config.base_url

def test_visible_up_navigation_panel(web_browser):
    """ Панель навигации видна на сайте """
    page = LabirintPage(web_browser)
    assert page.up_navigation_panel.is_visible()

def test_visible_block_icons(web_browser):
    """ Блок иконок виден на странице """
    page = LabirintPage(web_browser)
    assert page.block_icon.is_visible()


def test_scroll_page(web_browser):
    """ Проверка скроллинга страницы """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.title_book_adventure)
    page.SEARCH_BAR_BTN.click()
    page.page_num_6.scroll_to_element()
    assert page.page_num_6.is_clickable()
    page.page_num_6.highlight_and_make_screenshot('scrolling.png')

def test_clic_icon_messages(web_browser):
    """ Название всплывающего окна 'Сообщения' соответствует параметрам """
    page = LabirintPage(web_browser)
    page.icon_messeges.click()
    text = page.auth_window.get_text()
    assert text == Config.text_auth_window


def test_clic_icon_my_lab(web_browser):
    """ Название всплывающего окна 'Мой лабиринт' соответствует параметрам """
    page = LabirintPage(web_browser)
    page.icon_my_lab.click()
    text = page.auth_window.get_text()
    assert text == Config.text_auth_window


def test_clic_icon_postponed(web_browser):
    """ Переход по кнопке Отложенное ведет на страницу Отложенное"""
    page = LabirintPage(web_browser)
    page.icon_postponed.click()
    assert page.get_current_url() == Config.postponed_url

def test_clic_icon_support(web_browser):
    """ Переход по кнопке Поддержка ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.support.click()
    assert page.get_current_url() == Config.support_url

def test_clic_icon_contakt(web_browser):
    """ Переход по кнопке Контакты ведет на страницу с контактами"""
    page = LabirintPage(web_browser)
    page.contakt.click()
    assert page.get_current_url() == Config.contakt_url

def test_btn_contakt_text(web_browser):
    """ Проверяем, что на кнопке на странице Контакты есть надпись."""
    page = LabirintPage(web_browser)
    page.contakt.click()
    # проверим, что текст есть
    assert page.btn_contakt.get_text() == Config.text_btn_contakt

def test_clic_icon_books_sale_now(web_browser):
    """ Переход по иконке Книжные скидки ведет на соответствующую страницу."""
    page = LabirintPage(web_browser)
    page.icon_books_sale_now.click()
    assert page.get_current_url() == Config.books_sale_now

def test_clic_icon_books(web_browser):
    """ Переход на иконке Книги на ссылку Все книги"""
    page = LabirintPage(web_browser)
    page.icon_books.click()
    assert page.get_current_url() == Config.all_books_url

def test_clic_icon_best(web_browser):
    """ Переход на иконке Главное 2022 на ссылку Главные книги 2022"""
    page = LabirintPage(web_browser)
    page.best.click()
    assert page.get_current_url() == Config.best_url

def test_clic_best_sale(web_browser):
    """ Переход со страницы Главное 2022 на ссылку Скидки сегодня"""
    page = LabirintPage(web_browser)
    page.best.click()
    page.best_sale.wait_to_be_clickable()
    page.best_sale.click()
    assert page.get_current_url() == Config.best_sale_url

def test_clic_school(web_browser):
    """ Переход на иконке Школа на ссылку Школа"""
    page = LabirintPage(web_browser)
    page.school.click()
    assert page.get_current_url() == Config.school_url

def test_clic_school_courier(web_browser):
    """ Переход со страницы Школа на ссылку Курьер готов доставить."""
    page = LabirintPage(web_browser)
    page.school.click()
    page.courier.wait_to_be_clickable()
    page.courier.click()
    assert page.get_current_url() == Config.courier_url

def test_clic_games(web_browser):
    """ Переход на иконке Игрушки на ссылку Игрушки."""
    page = LabirintPage(web_browser)
    page.games.click()
    assert page.get_current_url() == Config.games_url

def test_clic_search_games(web_browser):
    """ На странице Игрушки есть  свое поле поиска."""
    page = LabirintPage(web_browser)
    page.games.click()
    page.btn_search_games.wait_to_be_clickable()
    page.btn_search_games.click()
    page.search_games.scroll_to_element()
    assert page.search_games.is_presented()
    page.search_games.highlight_and_make_screenshot('search.png')

def test_clic_office(web_browser):
    """ Переход на иконке Канцтовары на ссылку Канцтовары."""
    page = LabirintPage(web_browser)
    page.office.click()
    assert page.get_current_url() == Config.office_url

def test_clic_club(web_browser):
    """ Переход на иконке Клуб на ссылку Клуб."""
    page = LabirintPage(web_browser)
    page.club.click()
    assert page.get_current_url() == Config.club_url


def test_clic_more_cd_dvd(web_browser):
    """ Переход по списку Ещё на ссылку Мультимедиа и соответствующую страницу."""
    page = LabirintPage(web_browser)
    page.more.click()
    page.cd_dvd.scroll_to_element()
    page.cd_dvd.click()
    assert page.get_current_url() == Config.cd_dvd_url

def test_clic_more_cd_dvd_audio(web_browser):
    """ Переход со страницы Мультимедиа по ссылке Аудио на соответствующую страницу."""
    page = LabirintPage(web_browser)
    page.more.click()
    page.cd_dvd.scroll_to_element()
    page.cd_dvd.click()
    page.audio.wait_to_be_clickable()
    page.audio.click()
    assert page.get_current_url() == Config.audio_url

def test_clic_more_souvenir(web_browser):
    """ Переход по списку Ещё на ссылку Сувениры и соответствующую страницу."""
    page = LabirintPage(web_browser)
    page.more.click()
    page.souvenir.scroll_to_element()
    page.souvenir.click()
    assert page.get_current_url() == Config.souvenir_url

def test_clic_more_journals(web_browser):
    """ Переход по списку Ещё на ссылку Журналы и соответствующую страницу."""
    page = LabirintPage(web_browser)
    page.more.click()
    page.journals.scroll_to_element()
    page.journals.click()
    assert page.get_current_url() == Config.journals_url

def test_clic_more_household(web_browser):
    """ Переход по списку Ещё на ссылку Товары для дома и соответствующую страницу."""
    page = LabirintPage(web_browser)
    page.more.click()
    page.household.scroll_to_element()
    page.household.click()
    assert page.get_current_url() == Config.household_url


def test_delivery_and_payment_linc(web_browser):
    """ Переход по ссылке Доставка и оплата ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.delivery_and_payment.click()
    assert page.get_current_url() == Config.delivery_and_payment_url

def test_help_order(web_browser):
    """ Переход по ссылке Как оформить заказ со страницы Помощь ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.delivery_and_payment.click()
    page.help_order.scroll_to_element()
    page.help_order.click()
    assert page.get_current_url() == Config.help_order_url

def test_bonus(web_browser):
    """ Переход по ссылке Бонусная программа со страницы Помощь ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.delivery_and_payment.click()
    page.bonus.scroll_to_element()
    page.bonus.click()
    assert page.get_current_url() == Config.bonus_url


def test_certificate_linc(web_browser):
    """ Переход по ссылке Сертификаты ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.certificate_linc.click()
    assert page.get_current_url() == Config.certificate_url


def test_certificate_availability(web_browser):
    """ Проверяем, что на странице сертификаты есть сертификаты """
    page = LabirintPage(web_browser)
    page.certificate_linc.click()
    page.certificate_titles.scroll_to_element()
    # проверим что количество сертификатов равно 8
    assert page.certificate_titles.count() == 8


def test_rating_linc(web_browser):
    """ Переход по ссылке Рейтинг ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.rating_linc.click()
    assert page.get_current_url() == Config.rating_url


def test_rating_book(web_browser):
    """ Проверяем, что на странице Рейтинги есть книги """
    page = LabirintPage(web_browser)
    page.rating_linc.click()
    assert page.rating_books_title.count() == 60


def test_news_linc(web_browser):
    """ Переход по ссылке Новинки ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.news_link.click()
    assert page.get_current_url() == Config.news_url

def test_news_books(web_browser):
    """ Проверяем, что на странице Новинки есть книги """
    page = LabirintPage(web_browser)
    page.news_link.click()
    assert page.news_books.count() == 60


def test_sale_linc(web_browser):
    """ Переход по ссылке Скидки ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.sale_link.click()
    assert page.get_current_url() == Config.sale_url


def test_phone_number_linc(web_browser):
    """ Переход по ссылке 8 800 600-95-25 """
    page = LabirintPage(web_browser)
    page.phone_number_linc.click()
    text = page.phone_number_linc_btn.get_text()
    assert text == Config.text_phone_number


def test_search_product_adventure(web_browser):
    """ Проверяем, что поиск по запросу "Приключения" выдает результаты """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.title_book_adventure)
    page.SEARCH_BAR_BTN.click()
    # проверим что на странице 60 карточек книг
    assert page.search_books_title.count() == 60

def test_photo_product(web_browser):
    """ Проверяем, что карточки в результатах поиска "Приключения" имеют фото """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.title_book_adventure)
    page.SEARCH_BAR_BTN.click()
    # проверим что атрибут src не пустой
    assert page.search_books_title.get_attribute('src') != ''


def test_search_product_adventure_error(web_browser):
    """ Проверяем, что если перепутана раскладка, по запросу "Приключения", выдача правильная """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.title_book_adventure_error)
    page.SEARCH_BAR_BTN.click()
    # проверим что в названии книг содержатся искомые слова
    for title in page.search_books_title.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'Приключения' or 'приключения' in title(), msg

def test_search_books_by_title(web_browser):
    """ Проверяем, что поиск по названию книги выдает результаты """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.title_book2)
    page.SEARCH_BAR_BTN.click()
    # проверим что на странице 49 карточек книг
    assert page.books_by_title.count() == 49

def test_books_by_title_attribute_title(web_browser):
    """ Проверяем, что карточки в результате поиска  по названию имеют заполненный атрибут title. """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.title_book2)
    page.SEARCH_BAR_BTN.click()
    # проверим что атрибут title не пустой
    assert page.books_by_title.get_attribute('title') != ''

def test_search_books_by_author(web_browser):
    """ Проверяем, что поиск по автору выдает результаты """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.author)
    page.SEARCH_BAR_BTN.click()
    # проверим что на странице 60 карточек книг
    assert page.books_by_author.count() == 60

def test_search_books_by_author_photo(web_browser):
    """ Проверяем, что карточки в результатах поиска по автору имеют фото """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.author)
    page.SEARCH_BAR_BTN.click()
    # проверим что атрибут src не пустой
    assert page.books_by_author.get_attribute('src') != ''

def test_search_audiobooks(web_browser):
    """ Проверяем, что поиск по запросу "Аудиокниги" выдает результаты """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.title_book3)
    page.SEARCH_BAR_BTN.click()
    # проверим что на странице 60 карточек книг
    assert page.audiobooks.count() == 60


def test_add_book_in_cart(web_browser):
    """ Проверка добавления книги в корзину """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.title_book1)
    page.SEARCH_BAR_BTN.click()
    page.book1.click()
    page.btn_add_to_cart.click()
    page.btn_cart.click()
    # проверим что локатор книги виден в корзине
    assert page.book1.is_visible()
    # проверим что счетчик корзины изменился
    assert page.counter_cart.get_text() == '1'

@pytest.mark.xfail
def test_delete_from_cart(web_browser):
    """ Проверка удаления книги из корзины """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.title_book1)
    page.SEARCH_BAR_BTN.click()
    page.book1.click()
    page.btn_add_to_cart.click()
    page.btn_cart.click()
    assert page.counter_cart.get_text() == '1'
    page.clear_to_cart.scroll_to_element()
    page.clear_to_cart.is_clickable()
    page.clear_to_cart.click()
    page.wait_page_loaded()
    page.empty_cart.scroll_to_element()
    page.empty_cart.is_visible()
    # проверим, что корзина пуста
    assert page.empty_cart.get_text() == Config.text_empty_cart
    page.empty_cart.highlight_and_make_screenshot('empty_cart.png')

@pytest.mark.xfail
def test_restore_from_remote_cart(web_browser):
    """ Проверка восстановления в корзину после удаления книги """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.title_book1)
    page.SEARCH_BAR_BTN.click()
    page.book1.click()
    page.btn_add_to_cart.click()
    page.btn_cart.click()
    page.clear_to_cart.scroll_to_element()
    page.clear_to_cart.click()
    page.refresh()
    page.clear_to_cart_back_up.scroll_to_element()
    page.clear_to_cart_back_up.click()
    page.wait_page_loaded()
    # проверим что счетчик корзины изменился
    assert page.counter_cart.get_text() == '1'


@pytest.mark.xfail
def test_add_book_in_postponed(web_browser):
    """ Проверка добавления книги в отложенное """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.title_book1)
    page.SEARCH_BAR_BTN.click()
    page.btn_postponed_book.scroll_to_element()
    page.btn_postponed_book.click()
    page.wait_page_loaded()
    page.icon_postponed.scroll_to_element()
    assert page.counter_postponed.get_text() == '1'

@pytest.mark.xfail
def test_add_book_from_postponed_in_cart(web_browser):
    """ Проверка добавления книги из отложенного в корзину """
    page = LabirintPage(web_browser)
    page.SEARCH_BAR.send_keys(Config.title_book1)
    page.SEARCH_BAR_BTN.click()
    page.btn_postponed_book.scroll_to_element()
    page.btn_postponed_book.click()
    page.wait_page_loaded()
    page.icon_postponed.scroll_to_element()
    assert page.counter_postponed.get_text() == '1'
    page.icon_postponed.click()
    page.wait_page_loaded()
    page.btn_in_cart.scroll_to_element()
    page.btn_in_cart.click()
    page.wait_page_loaded()
    assert page.counter_cart.get_text() == '1'