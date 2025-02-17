INITIAL_URL = "https://www.mercadolivre.com.br/"
SEARCH_TEXT = "playstation 5"
N_PAGES = 10
SELECTORS = {
    "search_input": "#cb1-edit",
    "search_button": "body > header > div > div.nav-area.nav-top-area.nav-center-area > form > button > div",
    "item_card": "li.ui-search-layout__item",
    "next_button": "#root-app > div > div.ui-search-main.ui-search-main--only-products.ui-search-main--with-topkeywords > section > nav > ul > li.andes-pagination__button.andes-pagination__button--next",
}
