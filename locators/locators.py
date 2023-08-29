from selenium.webdriver.common.by import By

class Locators():

    # Home page objects

    search_field_css = '#woocommerce-product-search-field-0'

    myAccount_link_css = '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9'

    product_list_css = '#main > ul > li.product.type-product'

    first_product_title_css = '#main > ul > li.product.type-product.post-348.status-publish.first.instock.product_cat-uncategorized.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > h2'
    third_product_add_to_cart_button_css = '#main > ul > li.product.type-product.post-24.status-publish.instock.product_cat-music.has-post-thumbnail.downloadable.virtual.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart'

    album_listed_price_css = '#main > ul > li.product.type-product.post-24.status-publish.instock.product_cat-music.has-post-thumbnail.downloadable.virtual.purchasable.product-type-simple > a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > span > span > bdi'
    cart_total_amount_css = '#site-header-cart > li:nth-child(1) > a > span.woocommerce-Price-amount.amount'

    product_page_forward_arrow_css = '#main > div:nth-child(2) > nav > ul > li:nth-child(4) > a'
    product_page_back_arrow_css = '#main > div:nth-child(2) > nav > ul > li:nth-child(1) > a'
    product_results_indicator_css = '#main > div:nth-child(2) > p'

    product_page_one_button_css = '#main > div:nth-child(2) > nav > ul > li:nth-child(2) > a'
    product_page_two_button_css = '#main > div:nth-child(2) > nav > ul > li:nth-child(3) > a'
    product_page_three_button_css = '#main > div:nth-child(2) > nav > ul > li:nth-child(4) > span'

    album_css = '#main > ul > li.product.type-product.post-24.status-publish.instock.product_cat-music.has-post-thumbnail.downloadable.virtual.purchasable.product-type-simple > a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > img'



    # Login page objects
    username_textbox_id = 'username'
    password_textbox_id = 'password'

    login_button_css = '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button'
    forgot_password_link_css = '#customer_login > div.u-column1.col-1 > form > p.woocommerce-LostPassword.lost_password > a'

    wrong_password_error_message_css = '#content > div > div.woocommerce > ul > li'
    no_username_error_message_css = '#content > div > div.woocommerce > ul > li'

    # Registration page objects
    username_reg_textbox_id = 'reg_email'
    password_reg_textbox_id = 'reg_password'

    register_button_css = '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button'

    # My Account page objects
    logout_button_css = '#post-9 > div > div > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a'
    home_page_tab_css = '#site-navigation > div:nth-child(2) > ul > li:nth-child(1) > a'

    # Password retrieval objects
    username_lost_password_textbox_id = 'user_login'
    reset_password_button_css = '#post-9 > div > div > form > p:nth-child(4) > button'
    reset_email_sent_confirmation_css = '#post-9 > div > div > div'

    # Product page objects
    quantity_input_css = 'quantity'
    add_to_cart_button_css = '#product-24 > div.summary.entry-summary > form > button'
    added_to_cart_confirmation_message_css = '#content > div > div.woocommerce > div'
    view_cart_button_css = '#content > div > div.woocommerce > div > a'

    # Cart page objects
    remove_item_x_css = '#post-7 > div > div > form > table > tbody > tr.woocommerce-cart-form__cart-item.cart_item > td.product-remove > a'
    product_icon_css = '#post-7 > div > div > form > table > tbody > tr.woocommerce-cart-form__cart-item.cart_item > td.product-thumbnail > a > img'
    product_unit_price_css = '#post-7 > div > div > form > table > tbody > tr.woocommerce-cart-form__cart-item.cart_item > td.product-price > span > bdi'
    item_quantity_input_css = "input[id^='quantity']"
    items_subtotal_css = '#post-7 > div > div > form > table > tbody > tr.woocommerce-cart-form__cart-item.cart_item > td.product-subtotal > span > bdi'
    cart_subtotal_css = '#post-7 > div > div > div.cart-collaterals > div > table > tbody > tr.cart-subtotal > td > span > bdi'
    cart_total_css = '#post-7 > div > div > div.cart-collaterals > div > table > tbody > tr.order-total > td > strong > span > bdi'
    proceed_to_checkout_button_css = '#post-7 > div > div > div.cart-collaterals > div > div > a'

    # Checkout page objects
    # Order total verification
    product_subtotal_css = '#order_review > table > tbody > tr > td.product-total > span > bdi'
    order_subtotal_css = '#order_review > table > tfoot > tr.cart-subtotal > td > span > bdi'
    order_total_css = '#order_review > table > tfoot > tr.order-total > td > strong > span > bdi'

    # Coupon code link, input and button
    coupon_code_link_css = '#post-8 > div > div > div.woocommerce-form-coupon-toggle > div > a'
    coupon_code_textbox_id = 'coupon_code'
    apply_coupon_button_css = '#post-8 > div > div > form.checkout_coupon.woocommerce-form-coupon > p.form-row.form-row-last > button'

    coupon_discount_amount_css = '#order_review > table > tfoot > tr.cart-discount.coupon-ssqa100 > td > span'

    # Billing details
    billing_firstname_textbox_id = 'billing_first_name'
    billing_lastname_textbox_id = 'billing_last_name'
    billing_company_name_textbox_id = 'billing_company'
    billing_country_selector_id = 'select2-billing_country-container'
    billing_street_address_textbox_id = 'billing_address_1'
    billing_apartment_textbox_id = 'billing_address_2'
    billing_city_textbox_id = 'billing_city'
    billing_state_dropdownbox_id = 'billing_state'
    billing_postcode_textbox_id = 'billing_postcode'
    billing_phone_number_textbox_id = 'billing_phone'
    billing_billing_email_textbox_id = 'billing_email'
    billing_notes_textbox_id = 'order_comments'

    # Place order button
    place_order_button_id = 'place_order'

    # Order received confirmation
    order_received_confirmation_xpath = '//*[@id="post-8"]/div/div/div/p'


