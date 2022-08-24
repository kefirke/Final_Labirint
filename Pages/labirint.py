import os
from Pages.base import WebPage
from Pages.elements import WebElement, ManyWebElements


class LabirintPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'
        super().__init__(web_driver, url)


# ----------------------------------------= локаторы для строки поиска --------------------------------------------------

    SEARCH_BAR = WebElement(id='search-field')
    SEARCH_BAR_BTN = WebElement(class_name='b-header-b-search-e-btn')


# -------------------------------------- локаторы тестов корзины ------------------------------------------------

    # локатор добавить в отложенное
    add_postponed = WebElement(class_name='fave')
    # локатор счетчика отложено
    counter_postponed = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-putorder.basket-in-dreambox-a')
    # локатор книги
    book1 = WebElement(xpath='//img[@src="https://img4.labirint.ru/rc/8992f19e219e1abe6c8b793f903b554a/363x561q80/'
                             'books76/759814/cover.jpg?1606829575"]')
    # кнопка добавить в корзину
    btn_add_to_cart = WebElement(css_selector='.btn.btn-small.btn-primary.btn-buy')
    # ссылка очистить корзину
    clear_to_cart = WebElement(xpath='//a[@class="b-link-popup"]')
    # ссылка восстановить удаленное
    clear_to_cart_back_up = WebElement(css_selector='.b-link-popup.g-alttext-deepblue')
    # локатор корзины
    btn_cart = WebElement(css_selector='.b-header-b-personal-e-list-item.have-dropdown.last-child')
    # локатор счетчика корзины
    counter_cart = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a')
    # локатор пустой корзины
    empty_cart = WebElement(xpath='//span[@class="g-alttext-small g-alttext-grey g-alttext-head" and '
                                          'contains (text(), "Ваша корзина пуста. Почему?")]')

# ---------------------------------- локаторы панели навигации в шапке сайта ----------------------------------------

    # Лого Лабиринт
    logo_labirirnt = WebElement(class_name='b-header-b-logo-e-logo')
    # верхняя панель навигации
    up_navigation_panel = WebElement(class_name='b-header-b-menu-e-list')
    # ссылка доставка и оплата
    delivery_and_payment = WebElement(xpath='//a[@href="/help/" and @class="b-header-b-sec-menu-e-link"]')
    # Как оформить заказ со страницы Помощь
    help_order = WebElement(xpath='//a[@href="/help/?clause=164"]')
    # Бонусная программа
    bonus = WebElement(xpath='//a[@href="/help/?clause=82"]')
    # ссылка сертификаты
    certificate_linc = WebElement(xpath='//a[@href="/top/certificates/" and '
                                                '@class="b-header-b-sec-menu-e-link"]')
    # ссылка рейтинги
    rating_linc = WebElement(xpath='//a[@href="/rating/?id_genre=-1&nrd=1"]')
    # ссылка новинки
    news_link = WebElement(xpath='//a[@href="/novelty/"and @class="b-header-b-sec-menu-e-link"]')
    # ссылка скидки
    sale_link = WebElement(xpath='//a[@href="/sale/"]')
    # ссылка телефонного номера
    phone_number_linc = WebElement(css_selector='.b-header-b-sec-menu-e-list-'
                                                        'item.have-dropdown.have-dropdown-clickable.analytics-click-js')
    # кнопка вызова по телефону
    phone_number_linc_btn = WebElement(xpath='//*[@id="_support_call_number"]/a')
    # ссылка Контакты
    contakt = WebElement(xpath='//a[@href="/contact/" and @class="b-header-b-sec-menu-e-link"]')
    btn_contakt = WebElement(xpath='//a[@title="Соединить с оператором" and @class="btn btn-small btn-primary"]')
    # ссылка Поддержка
    support = WebElement(xpath='//a[@href="/support/" and @class="b-header-b-sec-menu-e-link"]')
    # иконка Книжные скидки
    icon_books_sale_now = WebElement(css_selector='a.b-header-b-logo-e-discount')
    # иконка Книги
    icon_books = WebElement(xpath='//a[@href="/books/" and @class="b-header-b-menu-e-text"]')
    # главное 2022
    best = WebElement(xpath='//a[@href="/best/" and @class="b-header-b-menu-e-text"]')
    # Скидки сегодня
    best_sale = WebElement(xpath='//a[@href="/best/sale/" and contains(text(), "Скидки сегодня")]')
    # школа
    school = WebElement(xpath='//a[@href="/school/" and @class="b-header-b-menu-e-text"]')
    # Курьер готов доставить
    courier = WebElement(xpath='//a[@class="school-cap-banner__link"and @href="/help/?clause=9"]')
    # игрушки
    games = WebElement(xpath='//a[@href="/games/" and @class="b-header-b-menu-e-text"]')
    # Строка поиска на Игрушки
    btn_search_games = WebElement(css_selector='span.find-button.js-goto-findhere.section-name-genre__find-button')
    search_games = WebElement(xpath='//input[@placeholder="Введите что-нибудь"]')
    # канцтовары
    office = WebElement(xpath='//a[@href="/office/" and @class="b-header-b-menu-e-text"]')
    # клуб
    club = WebElement(xpath='//a[@href="/club/" and @class="b-header-b-menu-e-text"]')
    # ссылка Все книги
    all_books = WebElement(css_selector='li.b-menu-second-item')
    # Ещё
    more = WebElement(xpath='//span[@class="b-header-b-menu-e-link top-link-main have-dropdown-touchlink"]')
    # CD/DVD
    cd_dvd = WebElement(xpath='//a[@href="/multimedia/" and @title="Аудиокниги, музыка, видеофильмы, '
                              'компьютерные программы, игры и др."]')
    # Аудио
    audio = WebElement(xpath='//a[@rel="nofollow" and @href="audio"]')
    # Сувениры
    souvenir = WebElement(xpath='//a[@href="/souvenir/" and @title="Сувениры, альбомы для фотографий, '
                                'фоторамки, календари."]')
    # Журналы
    journals = WebElement(xpath='//a[@href="/journals/" and @title="Литературные журналы: художественные и '
                                'публицистические, поэтические."]')
    # Товары для дома
    household = WebElement(xpath='//a[@href="/household/" and @title="Товары для дома"]')


# ----------------------------------- локаторы иконок справа от строки поиска ---------------------------------------

    # блок иконок
    block_icon = WebElement(css_selector='.b-header-b-personal')
    # иконка сообщения
    icon_messeges = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.'
                                                    'have-dropdown-touchlink.top-link-main_notification')
    # иконка мой лабиринт
    icon_my_lab = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.'
                                                   'top-link-main_cabinet.js-b-autofade-wrap')
    # иконка отложено
    icon_postponed = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.top-link-main_putorder')
    # кнопка сердечко Отложено
    btn_postponed_book = WebElement(xpath='//a[@data-id_book="759814" and @data-hasqtip="0"]')
    # Кнопка В корзину
    btn_in_cart = WebElement(xpath='//a[@id="buy759814"]')
    # локатор всплывающего окна сообщения
    auth_window = WebElement(xpath='//div[@class="js-auth__title new-auth__title" and contains'
                                           ' (text(),"Полный доступ к Лабиринту")]')

# ----------------------------------------- Локаторы блока footer ---------------------------------------------------
    # ссылка поддержка в футере
    support_in_footer = WebElement(xpath='//a[@href="/support/" and @class="b-rfooter-e-item-link '
                                         'analytics-click-js"]')
    # ссылка Как сделать заказ в футере
    help_order1 = WebElement(xpath='//a[@href="/help/order/" and @data-event-content="Как сделать заказ"]')


    # ------------------------------------------------------------------------------------------------------------------

    # локатор всех элементов из поиска
    search_books_title = ManyWebElements(css_selector='.product-title-link')

    # локатор всех элементов из поиска
    certificate_titles = ManyWebElements(css_selector='.product.need-watch.product-rule.watched')

    # локатор всех элементов из поиска
    rating_books_title = ManyWebElements(css_selector='.product.need-watch')

    # локатор всех элементов из поиска
    news_books = ManyWebElements(css_selector='.product.need-watch.watched')

    # локатор всех элементов из поиска
    books_by_title = ManyWebElements(css_selector='.product.need-watch.watched')

    # локатор всех элементов из поиска
    books_by_author = ManyWebElements(css_selector='.product.need-watch.watched')

    # локатор всех элементов из поиска
    audiobooks = ManyWebElements(css_selector='.product.need-watch.watched')

# ------------------------------------------- локаторы номера страниц ----------------------------------------------

    # страница 6
    page_num_6 = WebElement(xpath='//a[@class="pagination-number__text" and @href="?stype=0&page=6"]')






